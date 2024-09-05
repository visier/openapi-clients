#!/bin/bash

# Check if the search path argument is provided
if [ -z "$1" ]; then
  echo "Error: Search path argument is required."
  echo "Provided argument: search_path=${1:-<not provided>}"
  exit 1
fi

# Set error flag to 0
error_flag=0

# Path to search for directories
SEARCH_PATH=$1

# Find directories matching the pattern and run tox tests
while IFS= read -r dir; do
  cd "$dir"
  if ! tox -p 2; then
    error_flag=1
  fi
  cd - > /dev/null
done < <(find "$SEARCH_PATH" -type d -name "visier.sdk.api*" -print)

# Exit with the error flag status
exit $error_flag