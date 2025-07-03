FROM python:3.11-slim

# Install protobuf compiler and gRPC tools
RUN apt-get update && apt-get install -y \
    protobuf-compiler \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir grpcio-tools==1.60.0

WORKDIR /protos

# Copy compilation script
COPY scripts/generate-protos.sh /compile.sh
RUN chmod +x /compile.sh

CMD ["/compile.sh"]
