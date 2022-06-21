# cda-client
API definition for the CDA

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 3.0.0_RC
- Package version: 6.21.2022
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cda_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cda_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import cda_client
from pprint import pprint
from cda_client.api import meta_api
from cda_client.model.dataset_description import DatasetDescription
from cda_client.model.system_status import SystemStatus
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)



# Enter a context with an instance of the API client
with cda_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_api.MetaApi(api_client)
    
    try:
        # List descriptions of all available datasets
        api_response = api_instance.all_release_notes()
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling MetaApi->all_release_notes: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://cancerdata.dsde-dev.broadinstitute.org*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*MetaApi* | [**all_release_notes**](docs/MetaApi.md#all_release_notes) | **GET** /api/v1/dataset-description/all | List descriptions of all available datasets
*MetaApi* | [**latest_release_notes**](docs/MetaApi.md#latest_release_notes) | **GET** /api/v1/dataset-description/latest | Description of latest dataset
*MetaApi* | [**service_status**](docs/MetaApi.md#service_status) | **GET** /status | CDA status
*QueryApi* | [**boolean_query**](docs/QueryApi.md#boolean_query) | **POST** /api/v1/boolean-query/{version} | Execute boolean query
*QueryApi* | [**bulk_data**](docs/QueryApi.md#bulk_data) | **GET** /api/v1/bulk-data/{version} | Return all data in CDA
*QueryApi* | [**columns**](docs/QueryApi.md#columns) | **GET** /api/v1/columns/{version} | Returns all column names
*QueryApi* | [**diagnosis_counts_query**](docs/QueryApi.md#diagnosis_counts_query) | **POST** /api/v1/diagnosis/counts/{version} | Execute Diagnosis Counts query
*QueryApi* | [**diagnosis_query**](docs/QueryApi.md#diagnosis_query) | **POST** /api/v1/diagnosis/{version} | Execute Diagnosis query
*QueryApi* | [**file_counts_query**](docs/QueryApi.md#file_counts_query) | **POST** /api/v1/files/counts/{version} | Execute File Counts query
*QueryApi* | [**files**](docs/QueryApi.md#files) | **POST** /api/v1/files/{version} | Returns a list of files given a boolean query
*QueryApi* | [**global_counts**](docs/QueryApi.md#global_counts) | **POST** /api/v1/global-counts/{version} | Returns counts of the DCS
*QueryApi* | [**job_status**](docs/QueryApi.md#job_status) | **GET** /api/v1/job-status/{id} | Return the running status of long running queries.
*QueryApi* | [**query**](docs/QueryApi.md#query) | **GET** /api/v1/query/{id} | Given a query ID, return the a page of data from the query result.
*QueryApi* | [**research_subject_counts_query**](docs/QueryApi.md#research_subject_counts_query) | **POST** /api/v1/researchsubjects/counts/{version} | Execute ResearchSubjects Counts query
*QueryApi* | [**research_subject_file_counts_query**](docs/QueryApi.md#research_subject_file_counts_query) | **POST** /api/v1/researchsubjects/files/counts/{version} | Execute ResearchSubjects File Counts query
*QueryApi* | [**research_subject_files_query**](docs/QueryApi.md#research_subject_files_query) | **POST** /api/v1/researchsubjects/files/{version} | Execute ResearchSubject Files query
*QueryApi* | [**research_subject_query**](docs/QueryApi.md#research_subject_query) | **POST** /api/v1/researchsubjects/{version} | Execute Research Subject query
*QueryApi* | [**specimen_counts_query**](docs/QueryApi.md#specimen_counts_query) | **POST** /api/v1/specimen/counts/{version} | Execute Specimen Counts query
*QueryApi* | [**specimen_file_counts_query**](docs/QueryApi.md#specimen_file_counts_query) | **POST** /api/v1/specimen/files/counts/{version} | Execute Specimen File Counts query
*QueryApi* | [**specimen_files_query**](docs/QueryApi.md#specimen_files_query) | **POST** /api/v1/specimen/files/{version} | Execute Specimen Files query
*QueryApi* | [**specimen_query**](docs/QueryApi.md#specimen_query) | **POST** /api/v1/specimens/{version} | Execute Specimens query
*QueryApi* | [**sql_query**](docs/QueryApi.md#sql_query) | **POST** /api/v1/sql-query | Execute SQL directly on a version of the dataset
*QueryApi* | [**subject_counts_query**](docs/QueryApi.md#subject_counts_query) | **POST** /api/v1/subjects/counts/{version} | Execute Subjects Counts query
*QueryApi* | [**subject_file_counts_query**](docs/QueryApi.md#subject_file_counts_query) | **POST** /api/v1/subjects/files/counts/{version} | Execute Subjects File Counts query
*QueryApi* | [**subject_files_query**](docs/QueryApi.md#subject_files_query) | **POST** /api/v1/subjects/files/{version} | Execute Subject Files query
*QueryApi* | [**subject_query**](docs/QueryApi.md#subject_query) | **POST** /api/v1/subjects/{version} | Execute Subject query
*QueryApi* | [**treatment_counts_query**](docs/QueryApi.md#treatment_counts_query) | **POST** /api/v1/treatments/counts/{version} | Execute Treatments Counts query
*QueryApi* | [**treatments_query**](docs/QueryApi.md#treatments_query) | **POST** /api/v1/treatments/{version} | Execute Treatments query
*QueryApi* | [**unique_values**](docs/QueryApi.md#unique_values) | **POST** /api/v1/unique-values/{version} | Returns all unique values


## Documentation For Models

 - [DatasetDescription](docs/DatasetDescription.md)
 - [DatasetInfo](docs/DatasetInfo.md)
 - [ErrorReport](docs/ErrorReport.md)
 - [JobStatusData](docs/JobStatusData.md)
 - [Model](docs/Model.md)
 - [Query](docs/Query.md)
 - [QueryCreatedData](docs/QueryCreatedData.md)
 - [QueryResponseData](docs/QueryResponseData.md)
 - [SystemStatus](docs/SystemStatus.md)
 - [SystemStatusSystems](docs/SystemStatusSystems.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in cda_client.apis and cda_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from cda_client.api.default_api import DefaultApi`
- `from cda_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import cda_client
from cda_client.apis import *
from cda_client.models import *
```

