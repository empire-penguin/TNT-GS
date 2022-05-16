#!/bin/bash -x

echo "Creating virtual environment..."
if [[ "$OSTYPE" == "linux-gnu" ]]; then
    virtualenv --python=/Library/Frameworks/Python.framework/Versions/3.9/bin/python3 ./venv
    source ./venv/bin/activate
elif [[ "$OSTYPE" == "darwin"* ]]; then
    virtualenv --python=/Library/Frameworks/Python.framework/Versions/3.9/bin/python3 ./venv
    source ./venv/bin/activate
else
    echo "ERROR: $OSTYPE is not currently supported."
    exit 1
fi

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Installation completed successfully"
bash ./scripts/run.sh