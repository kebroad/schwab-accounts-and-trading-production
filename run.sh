#!/bin/bash

# Define variables
PYTHON_VERSIONS=("3.7" "3.8" "3.9" "3.10" "3.11")
INPUT="path/to/your/openapi.yaml"
CONFIG="config.json"
OUTPUT_DIR="generated-client"
SWAGGER_FILE="$OUTPUT_DIR/swagger.json"
UPDATED_SWAGGER_FILE="$OUTPUT_DIR/updated_swagger.json"

# Function to run commands for a specific Python version
run_for_python_version() {
  local python_version=$1

  echo "Setting up Python $python_version..."
  pyenv install -s $python_version
  pyenv local $python_version

  echo "Installing dependencies..."
  python -m pip install --upgrade pip
  pip install flake8 pytest jq
  if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
  if [ -f test-requirements.txt ]; then pip install -r test-requirements.txt; fi

  echo "Generating Python client from $INPUT with $CONFIG..."
  openapi-generator-cli generate -i $INPUT -g python -c $CONFIG -o $OUTPUT_DIR

  if [ -f "$SWAGGER_FILE" ]; then
    echo "Removing all 'oneOf' references from $SWAGGER_FILE..."
    jq 'walk(if type == "object" then del(.oneOf) else . end)' $SWAGGER_FILE > $UPDATED_SWAGGER_FILE
    echo "Updated swagger file saved to $UPDATED_SWAGGER_FILE"
  else
    echo "Error: $SWAGGER_FILE not found."
    exit 1
  fi

  echo "Linting with flake8..."
  flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
  flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

  echo "Testing with pytest..."
  pytest
}

# Loop through each Python version and run the commands
for python_version in "${PYTHON_VERSIONS[@]}"; do
  run_for_python_version $python_version
done