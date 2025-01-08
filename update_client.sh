source .venv/bin/activate
cd ../
openapi-python-client generate --url http://127.0.0.1:8000/openapi.json --config cda-service-python-client/openapi_config.yml --overwrite
cd cda-service-python-client/
deactivate