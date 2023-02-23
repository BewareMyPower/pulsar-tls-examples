#!/bin/bash
set -ex
cd `dirname $0`

if [[ $# -lt 1 ]]; then
    echo "Usage: $0 <wheel-url>"
    exit 1
fi

FILENAME=$(basename $1)
if [[ -f $FILENAME ]]; then
    echo "$FILENAME already exists!"
else
    curl -O -L $1
fi

if [[ $USER != "root" ]]; then
    SUDO=sudo
fi
$SUDO python3 -m pip install ./pulsar_client-*.whl --force-reinstall
