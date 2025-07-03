#!/bin/bash
set -euo pipefail

PROTO_SRC=$(dirname "$(pwd)")
PROTO_GEN=$(dirname $(dirname "$(pwd)"))/UX/lib/models/protos/generated

echo "$PROTO_SRC -> $PROTO_GEN"

echo "Remove old Dart code"
mkdir -p ${PROTO_GEN}
if [[ -d "${PROTO_GEN}" ]]; then
  rm -rf ${PROTO_GEN}/*
fi

echo "Generate Dart"
protoc --dart_out=grpc:${PROTO_GEN} -I ${PROTO_SRC} ${PROTO_SRC}/*.proto
protoc --dart_out=grpc:${PROTO_GEN} -I ${PROTO_SRC} ${PROTO_SRC}/google/protobuf/*.proto
protoc --dart_out=grpc:${PROTO_GEN} -I ${PROTO_SRC} ${PROTO_SRC}/admin/*.proto

echo "Cleanup"
# find all enum proto files
find ${PROTO_SRC} -name "*_enums.proto" -print0 | grep -v -z google |
    while IFS= read -r -d '' PROTO_FILE; do
      if [[ ! $(grep -q -E "^\s*enum " "${PROTO_FILE}") ]]; then
        echo "${PROTO_FILE}"
        # find all enums in proto file
        ENUM_NAMES=$(grep -E "^\s*enum " "${PROTO_FILE}" | sed -E "s/\s*enum\s+([a-z0-9]+).*/\1/ig" )
        for ENUM_NAME in $ENUM_NAMES; do
            echo "  - ${ENUM_NAME}"

            # find all enum fields
            ENUM_FIELDS=$(grep -E "^\s*${ENUM_NAME}_" "${PROTO_FILE}" | grep "=" | sed -E "s/^\s*(${ENUM_NAME})_([a-z0-9_]+).*$/\1_\2/ig")
            for ENUM_FIELD in $ENUM_FIELDS; do
                ENUM_FIELD_REPLACEMENT=$(echo ${ENUM_FIELD} | sed "s/${ENUM_NAME}_//g;s/_//g")
                echo "     - ${ENUM_FIELD} -> ${ENUM_FIELD_REPLACEMENT}"
                if [[ $(grep -rl "${ENUM_FIELD}" "${PROTO_GEN}" | wc -l) -gt 0 ]]; then
                  DART_FILES_WITH_ENUM_FIELD=$(grep -rl "${ENUM_FIELD}" "${PROTO_GEN}")
                  for DART_FILE in $DART_FILES_WITH_ENUM_FIELD; do
                    #echo "        - ${DART_FILE}"
                    sed -i "s/${ENUM_FIELD}/${ENUM_FIELD_REPLACEMENT}/g" "${DART_FILE}"
                  done
                fi
            done
        done
      fi
  done

echo "Format"
dart format ${PROTO_GEN}

echo "Analyze"
flutter analyze --no-fatal-infos ${PROTO_GEN} | grep -v info
