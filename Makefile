OPENAPI_GEN := npx @openapitools/openapi-generator-cli
INPUT := swagger.json

# Check if npm is installed
check-npm:
	@npm -v >/dev/null 2>&1 || { echo >&2 "npm is not installed. Please install npm and try again."; exit 1; }

# Install openapi-generator-cli globally if not installed
install-openapi-gen: check-npm
	@if npm list -g @openapitools/openapi-generator-cli &> /dev/null; then \
		echo "$(OPENAPI_GEN) is already installed."; \
	else \
		echo "Installing $(OPENAPI_GEN) globally..."; \
		npm install -g @openapitools/openapi-generator-cli@v6.5.0; \
	fi

# Generate code using openapi-generator-cli
generate: install-openapi-gen
	@echo "Generating Python client from $(INPUT) with config.json..."
	$(OPENAPI_GEN) generate -i $(INPUT) -g python

# Clean target to remove everything except Makefile, config.json, and swagger.json
clean:
	find . -type f ! -name 'Makefile' ! -name 'config.yaml' ! -name 'swagger.json' -delete
	find . -type d ! -name '.' ! -name '..' ! -name '.git' -exec rm -rf {} \;

all: generate