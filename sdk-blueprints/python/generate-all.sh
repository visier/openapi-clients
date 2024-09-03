#!/bin/bash
# This script generates all packages for SDK
set -e

# Get the directory of the current script
script_dir=$(dirname "$0")

pip uninstall -y visier.sdk.api.core
pip uninstall -y visier.sdk.api.analytic_model

"$script_dir"/generate-package.sh visier.sdk.api.core res/authentication-apis.yaml sdk-blueprints/python/core &
"$script_dir"/generate-package.sh visier.sdk.api.analytic_model res/analytic-model-apis.yaml sdk-blueprints/python/api
#&
#"$script_dir"/generate-package.sh visier.sdk.api.administration res/administration-apis.yaml sdk-blueprints/python/api &
#"$script_dir"/generate-package.sh visier.sdk.api.data_in res/data-in-apis.yaml sdk-blueprints/python/api &
#"$script_dir"/generate-package.sh visier.sdk.api.data_out res/data-out-apis.yaml sdk-blueprints/python/api &

# Wait for all background processes to complete
wait

pip install sdk-generation-test/visier.sdk.api.core/.
pip install sdk-generation-test/visier.sdk.api.analytic_model/.