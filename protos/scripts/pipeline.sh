#!/bin/bash
set -euox pipefail

if [ -z "$1" ]; then
    echo "Please provide source directory."
    exit 1
fi
BASE_FOLDER=$1

echo "== Setup flutter/dart"
flutter config --no-analytics > /dev/null
sudo apt-get install -y protobuf-compiler > /dev/null
dart pub global activate protoc_plugin > /dev/null
echo "== Versions"
dart --version
flutter --version
protoc --version

echo "== Setup destination UX branch: ${BRANCH_NAME}"
cd ${BASE_FOLDER}/UX
set +e
git ls-remote --exit-code --heads origin ${BRANCH_NAME} >/dev/null 2>&1
BRANCH_CHECK_CODE=$?
set -e

if [[ ${BRANCH_CHECK_CODE} == '0' ]]; then
  echo "Git branch '${BRANCH_NAME}' exists in the remote repository"
  git fetch origin ${BRANCH_NAME}
  git switch ${BRANCH_NAME}
else
  echo "Git branch '${BRANCH_NAME}' does not exist in the remote repository"
  git checkout -B ${BRANCH_NAME}
fi

echo "== Generate code"
cd ${BASE_FOLDER}/protos/scripts
./sync-protos.sh

echo "== Commit changes"
cd ${BASE_FOLDER}/UX
git config --global user.email "${DTS_USER_EMAIL:-DevOps@sarna.io}"
git config --global user.name "${DTS_USER_NAME}"
if [[ ${BRANCH_CHECK_CODE} == '0' ]]; then
  git pull
fi
if [[ `git status --porcelain` ]]; then
  git status
  git add .
  git commit -m "Generate code from protos"

  if [[ ${BRANCH_CHECK_CODE} == '0' ]]; then
    git push
  else
    git push --set-upstream origin ${BRANCH_NAME}
  fi
else
  echo No changes
fi
