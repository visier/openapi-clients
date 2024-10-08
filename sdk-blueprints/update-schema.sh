# Internal script for debugging SDK generation locally.
# Run from the root of the openapi-clients repository.

# Define directory where projects are stored
projects_dir="$HOME/projects"

vserver_dir="$projects_dir/com.visier.vserver"
python_sdk_repository_dir="$projects_dir/python-sdk/src"

version="22222222.99201.1494"

# Before running this script docker image should be build from repository com.visier.containers.openapi
docker container run -u $UID --rm -v "$vserver_dir":/vserver -e VERSION=$version -e OPENAPI_OUTPUT_ROOT="/vserver/target/openapi" -e GENERATE_API_DESCRIPTIONS=true visier-openapi:latest

# Copy openapi specifications to res directory
cp "$vserver_dir/target/openapi"/*.yaml res/

# Run preprocessing openapi specs script
python3 "sdk-blueprints/preprocessing/preprocessing.py" res "sdk-generation-test/specs"

# Run python SDK generation script
./sdk-blueprints/python/generate-all.sh "$python_sdk_repository_dir" "sdk-generation-test/specs"
