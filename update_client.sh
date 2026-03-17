python3 -m venv .venv
source .venv/bin/activate
pip3 install openapi-python-client
cd ../
openapi-python-client generate --url http://127.0.0.1:8000/openapi.json --config cda-client/openapi_config.yml --overwrite
cd cda_client/
deactivate