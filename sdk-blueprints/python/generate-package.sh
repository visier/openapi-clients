#!/bin/bash
# This script is used for debugging purposes to generate Python SDK packages locally using openapi-generator-cli.
set -e

# Define variables
package_name=$1
spec_file=$2
blueprints_dir=$3
output_dir=$4

# Check if all required arguments are provided
if [ -z "$package_name" ] || [ -z "$spec_file" ] || [ -z "$blueprints_dir" ] || [ -z "$output_dir" ]; then
  echo "Error: Missing required arguments."
  echo "Usage: $0 <package_name> <spec_file> <blueprints_dir> <output_dir>"
  echo "Provided arguments: package_name=${package_name:-<not provided>}, spec_file=${spec_file:-<not provided>}, blueprints_dir=${blueprints_dir:-<not provided>}, output_dir=${output_dir:-<not provided>}"
  exit 1
fi

output_api_dir="$4/$package_name"
templates_dir="$blueprints_dir/templates"

# Extract the specification version
spec_version=$(awk '/version:/ {gsub(/"| /, "", $2); print $2}' "$spec_file")

echo "Generating Visier API $package_name $spec_version $spec_file"

# Prepare directories
if [ -d "$output_api_dir" ]; then
    echo "Cleaning existing output directory: $output_api_dir"
    rm -rf "$output_api_dir"/*
else
    echo "Creating output directory: $output_api_dir"
    mkdir -p "$output_api_dir"
fi

cp -f "$blueprints_dir/.openapi-generator-ignore" "$output_api_dir/.openapi-generator-ignore"

# Generate the SDK
openapi-generator-cli generate \
  -i "$spec_file" \
  -g python \
  -t "$templates_dir" \
  --package-name "$package_name" \
  -o "$output_api_dir" \
  --skip-validate-spec \
  --additional-properties=packageVersion="$spec_version",corePackageName="visier.sdk.api.core"