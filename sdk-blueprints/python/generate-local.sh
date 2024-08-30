spec_file=$1
output_dir=$2
package_name=$3
spec_version=$4

PYTHON_DIR=sdk-blueprints/python

mkdir -p "$output_dir"
cp ./sdk-blueprints/python/core.openapi-generator-ignore "$output_dir/.openapi-generator-ignore"


openapi-generator-cli generate \
  -i "$spec_file" \
  -g python \
  -t $PYTHON_DIR/templates \
  --package-name "$package_name" \
  -o "$output_dir" \
  --skip-validate-spec \
  --additional-properties=packageVersion="$spec_version",corePackageName="visier.sdk.api.core"