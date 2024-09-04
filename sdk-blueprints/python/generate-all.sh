#!/bin/bash
# This script generates all packages for SDK
set -e

output_dir=$1

# Check if the required argument is provided
if [ -z "$output_dir" ]; then
  echo "Error: Missing required argument."
  echo "Usage: $0 <output_dir>"
  echo "Provided argument: output_dir=${output_dir:-<not provided>}"
  exit 1
fi

# Get the directory of the current script
script_dir=$(dirname "$0")

"$script_dir"/generate-package.sh visier.sdk.api.core res/authentication-apis.yaml sdk-blueprints/python/core "$output_dir"
"$script_dir"/generate-package.sh visier.sdk.api.analytic_model res/analytic-model-apis.yaml sdk-blueprints/python/api "$output_dir"
"$script_dir"/generate-package.sh visier.sdk.api.administration res/administration-apis.yaml sdk-blueprints/python/api "$output_dir"
"$script_dir"/generate-package.sh visier.sdk.api.data_in res/data-in-apis.yaml sdk-blueprints/python/api "$output_dir"
"$script_dir"/generate-package.sh visier.sdk.api.data_out res/data-out-apis.yaml sdk-blueprints/python/api "$output_dir"