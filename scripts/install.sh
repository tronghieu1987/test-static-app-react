#!/bin/bash

SCRIPT_DIR=$(cd $(dirname "$0") && pwd)
cd "$SCRIPT_DIR/../"

npm install -g @azure/static-web-apps-cli