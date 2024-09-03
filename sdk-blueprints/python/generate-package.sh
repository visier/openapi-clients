#!/bin/bash
# This script is used for debugging purposes to generate Python SDK packages locally using openapi-generator-cli.
set -e

# Define variables
package_name=$1
spec_file=$2
blueprints_dir=$3

output_dir="sdk-generation-test/$package_name"
templates_dir="$blueprints_dir/templates"

# Extract the specification version
spec_version=$(awk '/version:/ {gsub(/"| /, "", $2); print $2}' "$spec_file")

echo "Generating Visier API $package_name $spec_version $spec_file"

# Prepare directories
mkdir -p "$output_dir"
cp -f "$blueprints_dir/.openapi-generator-ignore" "$output_dir/.openapi-generator-ignore"

# Generate the SDK
openapi-generator-cli generate \
  -i "$spec_file" \
  -g python \
  -t "$templates_dir" \
  --package-name "$package_name" \
  -o "$output_dir" \
  --skip-validate-spec \
  --additional-properties=packageVersion="$spec_version",corePackageName="visier.sdk.api.core"