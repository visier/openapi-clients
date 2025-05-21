#!/bin/bash

# Check if the search path argument is provided
if [ -z "$1" ]; then
  echo "Error: Search path argument is required."
  echo "Provided argument: search_path=${1:-<not provided>}"
  exit 1
fi

# Set error code to 0
error_code=0

# Path to search for directories
SEARCH_PATH=$1

dir="$SEARCH_PATH/visier_platform_sdk"
# Check if the visier_platform_sdk directory exists
if [ -d "$dir" ]; then
  cd "$dir" || exit 10
  if ! tox -p 2; then
    error_code=20
  fi
  cd - > /dev/null || exit 30
else
  echo "Error: Directory visier_platform_sdk not found in $SEARCH_PATH"
  error_code=40
fi

# Exit with the error code
echo "Error code: $error_code"
exit $error_code