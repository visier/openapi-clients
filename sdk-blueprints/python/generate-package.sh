#!/bin/bash
# This script is used to generate Python SDK packages using openapi-generator-cli.
set -e

# Define variables
package_name=$1
spec_file=$2
blueprints_dir=$3
output_dir=$4
post_version=$5

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
spec_version=$(awk '/version:/ {
    gsub(/"| /, "", $2);
    sub(/[0-9]+\./, "0.", $2);
    print $2
}' "$spec_file")

if [ -n "$post_version" ]; then
    spec_version="${spec_version}.${post_version}"
fi

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

# Update the config file with the provided variables
script_dir=$(dirname "$0")
config_file="$script_dir/config.yaml"
config_expanded="$script_dir/config_expanded.yaml"
export spec_file=$spec_file output_api_dir=$output_api_dir templates_dir=$templates_dir package_name=$package_name spec_version=$spec_version
envsubst < "$config_file" > "$config_expanded"

openapi-generator-cli generate -c "$config_expanded" --skip-validate-spec