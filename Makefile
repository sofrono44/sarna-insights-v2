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
	docker-compose run --rm proto-compiler

test-integration:
	docker-compose run --rm backend pytest tests/integration

test-e2e:
	docker-compose run --rm backend pytest tests/e2e

test: test-integration test-e2e

clean:
	docker-compose down -v
	rm -rf backend/generated/*
	@echo "Cleaned up volumes and generated files"
