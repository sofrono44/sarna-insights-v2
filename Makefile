.PHONY: up down logs proto test clean help

# Default target
help:
	@echo "Sarna Insights v2 - Available Commands:"
	@echo "  make up          - Start all services"
	@echo "  make down        - Stop all services"
	@echo "  make logs        - View logs (ctrl+c to exit)"
	@echo "  make proto       - Compile protobuf files"
	@echo "  make test        - Run all tests"
	@echo "  make clean       - Remove all data and generated files"

up:
	docker-compose up -d
	@echo "Services starting..."
	@echo "Frontend: http://localhost"
	@echo "API: http://localhost:8000"
	@echo "API Docs: http://localhost:8000/docs"

down:
	docker-compose down

logs:
	docker-compose logs -f

proto:
	@echo "WARNING: Proto files are committed to git. Only regenerate if you've updated .proto files"
	@echo "Building proto compiler..."
	docker build -f docker/proto/Dockerfile -t sarna-proto-compiler .
	@echo "Generating proto files..."
	docker run --rm -v "$(CURDIR)/protos:/protos" -v "$(CURDIR)/backend/generated:/output" sarna-proto-compiler
	@echo "Fixing imports..."
	docker-compose exec backend python scripts/fix_proto_imports.py
	@echo "Fixing grpc imports..."
	docker-compose exec backend python -c "import re; from pathlib import Path; [open(f,'w').write(re.sub(r'^from \. import grpc$$','import grpc',open(f).read(),flags=re.MULTILINE)) for f in Path('/app/generated').rglob('*_pb2_grpc.py')]"
	@echo "Fixing api_hub_enums imports..."
	docker-compose exec backend python -c "import re; from pathlib import Path; [open(f,'w').write(re.sub(r'from \. import api_hub_enums_pb2','from .api_hub import api_hub_enums_pb2',open(f).read())) for f in Path('/app/generated').glob('*.py') if f.name != '__init__.py']"
	@echo "Proto generation complete. Remember to commit the changes!"

test-integration:
	docker-compose run --rm backend pytest tests/integration

test-e2e:
	docker-compose run --rm backend pytest tests/e2e

test: test-integration test-e2e

clean:
	docker-compose down -v
	rm -rf backend/generated/*
	@echo "Cleaned up volumes and generated files"
