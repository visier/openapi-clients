#!/bin/bash
# This script generates all packages for SDK
set -e

output_dir=$1
spec_dir=$2
version_postfix=$3

# Check if the required arguments are provided
if [ -z "$output_dir" ] || [ -z "$spec_dir" ]; then
  echo "Error: Missing required arguments."
  echo "Usage: $0 <output_dir> <spec_dir>"
  echo "Provided arguments: output_dir=${output_dir:-<not provided>}, spec_dir=${spec_dir:-<not provided>}"
  exit 1
fi

# Get the directory of the current script
script_dir=$(dirname "$0")

# Script for py post processing.
export PYTHON_POST_PROCESS_FILE="python3 $script_dir/post_process.py"

"$script_dir"/generate-package.sh visier_api_core "$spec_dir/authentication-apis.yaml" sdk-blueprints/python/core "$output_dir" "$version_postfix"
"$script_dir"/generate-package.sh visier_api_analytic_model "$spec_dir/analytic-model-apis.yaml" sdk-blueprints/python/api "$output_dir" "$version_postfix"
"$script_dir"/generate-package.sh visier_api_administration "$spec_dir/administration-apis.yaml" sdk-blueprints/python/api "$output_dir" "$version_postfix"
"$script_dir"/generate-package.sh visier_api_data_in "$spec_dir/data-in-apis.yaml" sdk-blueprints/python/api "$output_dir" "$version_postfix"
"$script_dir"/generate-package.sh visier_api_data_out "$spec_dir/data-out-apis.yaml" sdk-blueprints/python/api "$output_dir" "$version_postfix"