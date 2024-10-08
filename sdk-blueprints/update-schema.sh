# Internal script for debugging SDK generation locally.
# Run from the root of the openapi-clients repository.

# Exit immediately if any command exits with a non-zero status
set -e

# Define the version of the openapi specification
version="${1:-0.0.001}"

# Define directory where projects are stored
projects_dir="${2:-$HOME/projects}"

vserver_dir="$projects_dir/com.visier.vserver"
python_sdk_repository_dir="$projects_dir/python-sdk/src"

# Before running this script docker image should be build from repository com.visier.containers.openapi
docker container run -u $UID --rm -v "$vserver_dir":/vserver -e VERSION=$version -e OPENAPI_OUTPUT_ROOT="/vserver/target/openapi" -e GENERATE_API_DESCRIPTIONS=false visier-openapi:latest

# Copy openapi specifications to res directory
cp "$vserver_dir/target/openapi"/*.yaml res/

# Run preprocessing openapi specs script
python3 "sdk-blueprints/preprocessing/preprocessing.py" res "sdk-generation-test/specs"

# Run python SDK generation script
./sdk-blueprints/python/generate-all.sh "$python_sdk_repository_dir" "sdk-generation-test/specs"
