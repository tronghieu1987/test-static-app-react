#!/bin/bash

SCRIPT_DIR=$(cd $(dirname "$0") && pwd)
cd "$SCRIPT_DIR/../"

# install new web app dependencies
if [[ "$1" == "--install" ]]; then
    echo "Installing web app dependencies"
    npm install
fi

# clean up
"$SCRIPT_DIR/cleanup-ports.sh"

# build app and serve
npm run build
swa start build --api-location api
