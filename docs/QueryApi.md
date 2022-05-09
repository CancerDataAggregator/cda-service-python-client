# cda_client.QueryApi

All URIs are relative to *https://cancerdata.dsde-dev.broadinstitute.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**boolean_query**](QueryApi.md#boolean_query) | **POST** /api/v1/boolean-query/{version} | Execute boolean query
[**bulk_data**](QueryApi.md#bulk_data) | **GET** /api/v1/bulk-data/{version} | Return all data in CDA
[**columns**](QueryApi.md#columns) | **GET** /api/v1/columns/{version} | Returns all column names
[**diagnosis_query**](QueryApi.md#diagnosis_query) | **POST** /api/v1/diagnosis/{version} | Execute Diagnosis query
[**files**](QueryApi.md#files) | **POST** /api/v1/files/{version} | Returns a list of files given a boolean query
[**global_counts**](QueryApi.md#global_counts) | **POST** /api/v1/global-counts/{version} | Returns counts of the DCS
[**job_status**](QueryApi.md#job_status) | **GET** /api/v1/job-status/{id} | Return the running status of long running queries.
[**query**](QueryApi.md#query) | **GET** /api/v1/query/{id} | Given a query ID, return the a page of data from the query result.
[**research_subject_files_query**](QueryApi.md#research_subject_files_query) | **POST** /api/v1/researchsubjects/files/{version} | Execute ResearchSubject Files query
[**research_subject_query**](QueryApi.md#research_subject_query) | **POST** /api/v1/researchsubjects/{version} | Execute Research Subject query
[**specimen_files_query**](QueryApi.md#specimen_files_query) | **POST** /api/v1/specimen/files/{version} | Execute Specimen Files query
[**specimen_query**](QueryApi.md#specimen_query) | **POST** /api/v1/specimens/{version} | Execute Specimens query
[**sql_query**](QueryApi.md#sql_query) | **POST** /api/v1/sql-query | Execute SQL directly on a version of the dataset
[**subject_files_query**](QueryApi.md#subject_files_query) | **POST** /api/v1/subjects/files/{version} | Execute Subject Files query
[**subject_query**](QueryApi.md#subject_query) | **POST** /api/v1/subjects/{version} | Execute Subject query
[**treatments_query**](QueryApi.md#treatments_query) | **POST** /api/v1/treatments/{version} | Execute Treatments query
[**unique_values**](QueryApi.md#unique_values) | **POST** /api/v1/unique-values/{version} | Returns all unique values


# **boolean_query**
> QueryCreatedData boolean_query(query)

Execute boolean query

Execute a query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example

```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_created_data import QueryCreatedData
from pprint import pprint
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    query = Query(
        node_type="column",
        value="value_example",
        l=Query(),
        r=Query(),
    ) # Query | The boolean query
    dry_run = False # bool | If true, don't run the query, only generate and return it. (optional) if omitted the server will use the default value of False
    table = "broad-dsde-dev.cda_dev" # str | tablename (optional) if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

    # example passing only required values which don't have defaults set
    try:
        # Execute boolean query
        api_response = api_instance.boolean_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->boolean_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute boolean query
        api_response = api_instance.boolean_query(query, dry_run=dry_run, table=table)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->boolean_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The boolean query |
 **version** | **str**| Dataset version | defaults to "all_v3_0_subjects_meta"
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it. | [optional] if omitted the server will use the default value of False
 **table** | **str**| tablename | [optional] if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

### Return type

[**QueryCreatedData**](QueryCreatedData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query created response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_data**
> QueryCreatedData bulk_data()

Return all data in CDA

Return all data in CDA

### Example

```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query_created_data import QueryCreatedData
from pprint import pprint
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    table = "broad-dsde-dev.cda_dev" # str | tablename (optional) if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

    # example passing only required values which don't have defaults set
    try:
        # Return all data in CDA
        api_response = api_instance.bulk_data()
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->bulk_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return all data in CDA
        api_response = api_instance.bulk_data(table=table)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->bulk_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Dataset version | defaults to "all_v3_0_subjects_meta"
 **table** | **str**| tablename | [optional] if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

### Return type

[**QueryCreatedData**](QueryCreatedData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query created response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **columns**
> QueryCreatedData columns()

Returns all column names

Return columnNames for schema

### Example

```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query_created_data import QueryCreatedData
from pprint import pprint
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    table = "broad-dsde-dev.cda_dev" # str | tablename (optional) if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

    # example passing only required values which don't have defaults set
    try:
        # Returns all column names
        api_response = api_instance.columns()
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->columns: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all column names
        api_response = api_instance.columns(table=table)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->columns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Dataset version | defaults to "all_v3_0_subjects_meta"
 **table** | **str**| tablename | [optional] if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

### Return type

[**QueryCreatedData**](QueryCreatedData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query created response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diagnosis_query**
> QueryCreatedData diagnosis_query(query)

Execute Diagnosis query

Execute a query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example

```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_created_data import QueryCreatedData
from pprint import pprint
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    query = Query(
        node_type="column",
        value="value_example",
        l=Query(),
        r=Query(),
    ) # Query | The diagnosis query
    dry_run = False # bool | If true, don't run the query, only generate and return it. (optional) if omitted the server will use the default value of False
    table = "broad-dsde-dev.cda_dev" # str | tablename (optional) if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

    # example passing only required values which don't have defaults set
    try:
        # Execute Diagnosis query
        api_response = api_instance.diagnosis_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->diagnosis_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute Diagnosis query
        api_response = api_instance.diagnosis_query(query, dry_run=dry_run, table=table)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->diagnosis_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The diagnosis query |
 **version** | **str**| Dataset version | defaults to "all_v3_0_subjects_meta"
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it. | [optional] if omitted the server will use the default value of False
 **table** | **str**| tablename | [optional] if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

### Return type

[**QueryCreatedData**](QueryCreatedData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query created response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files**
> QueryCreatedData files(query)

Returns a list of files given a boolean query

Return list of files for given query

### Example

```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_created_data import QueryCreatedData
from pprint import pprint
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    query = Query(
        node_type="column",
        value="value_example",
        l=Query(),
        r=Query(),
    ) # Query | The boolean query
    dry_run = False # bool | If true, don't run the query, only generate and return it. (optional) if omitted the server will use the default value of False
    table = "broad-dsde-dev.cda_dev" # str | tablename (optional) if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of files given a boolean query
        api_response = api_instance.files(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->files: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of files given a boolean query
        api_response = api_instance.files(query, dry_run=dry_run, table=table)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The boolean query |
 **version** | **str**| Dataset version | defaults to "all_v3_0_Files"
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it. | [optional] if omitted the server will use the default value of False
 **table** | **str**| tablename | [optional] if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

### Return type

[**QueryCreatedData**](QueryCreatedData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query created response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **global_counts**
> QueryCreatedData global_counts(query)

Returns counts of the DCS

Return GlobalCounts for schema

### Example

```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_created_data import QueryCreatedData
from pprint import pprint
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    query = Query(
        node_type="column",
        value="value_example",
        l=Query(),
        r=Query(),
    ) # Query | counts
    dry_run = False # bool | If true, don't run the query, only generate and return it. (optional) if omitted the server will use the default value of False
    table = "broad-dsde-dev.cda_dev" # str | tablename (optional) if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

    # example passing only required values which don't have defaults set
    try:
        # Returns counts of the DCS
        api_response = api_instance.global_counts(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->global_counts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns counts of the DCS
        api_response = api_instance.global_counts(query, dry_run=dry_run, table=table)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->global_counts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| counts |
 **version** | **str**| Dataset version | defaults to "all_v3_0_Files"
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it. | [optional] if omitted the server will use the default value of False
 **table** | **str**| tablename | [optional] if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

### Return type

[**QueryCreatedData**](QueryCreatedData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query created response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_status**
> JobStatusData job_status(id)

Return the running status of long running queries.

For long running queries we may need to determine if the query is PENDING RUNNING, DONE or FAILURE. Pass the Job ID to this endpoint and get the running status back. 

### Example

```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.job_status_data import JobStatusData
from pprint import pprint
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    id = "id_example" # str | Query ID

    # example passing only required values which don't have defaults set
    try:
        # Return the running status of long running queries.
        api_response = api_instance.job_status(id)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->job_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Query ID |

### Return type

[**JobStatusData**](JobStatusData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get&#39;s Bigquery job id status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query**
> QueryResponseData query(id)

Given a query ID, return the a page of data from the query result.

Use this API to get the data back from a query. If there is more data present, next_url will contain the link to use to get the rest of the data. If the current page of data is not yet ready, the result will be empty, but next_url will be set. 

### Example

```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query_response_data import QueryResponseData
from pprint import pprint
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    id = "id_example" # str | Query ID
    offset = 0 # int | The number of entries to skip (optional) if omitted the server will use the default value of 0
    limit = 100 # int | The numbers of entries to return per page of data (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    try:
        # Given a query ID, return the a page of data from the query result.
        api_response = api_instance.query(id)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Given a query ID, return the a page of data from the query result.
        api_response = api_instance.query(id, offset=offset, limit=limit)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Query ID |
 **offset** | **int**| The number of entries to skip | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of entries to return per page of data | [optional] if omitted the server will use the default value of 100

### Return type

[**QueryResponseData**](QueryResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **research_subject_files_query**
> QueryCreatedData research_subject_files_query(query)

Execute ResearchSubject Files query

Execute a ResearchSubject Files query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example

```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_created_data import QueryCreatedData
from pprint import pprint
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    query = Query(
        node_type="column",
        value="value_example",
        l=Query(),
        r=Query(),
    ) # Query | The research subject query
    dry_run = False # bool | If true, don't run the query, only generate and return it. (optional) if omitted the server will use the default value of False
    table = "broad-dsde-dev.cda_dev" # str | tablename (optional) if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

    # example passing only required values which don't have defaults set
    try:
        # Execute ResearchSubject Files query
        api_response = api_instance.research_subject_files_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->research_subject_files_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute ResearchSubject Files query
        api_response = api_instance.research_subject_files_query(query, dry_run=dry_run, table=table)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->research_subject_files_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The research subject query |
 **version** | **str**| Dataset version | defaults to "all_v3_0_subjects_meta"
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it. | [optional] if omitted the server will use the default value of False
 **table** | **str**| tablename | [optional] if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

### Return type

[**QueryCreatedData**](QueryCreatedData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query created response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **research_subject_query**
> QueryCreatedData research_subject_query(query)

Execute Research Subject query

Execute a query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example

```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_created_data import QueryCreatedData
from pprint import pprint
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    query = Query(
        node_type="column",
        value="value_example",
        l=Query(),
        r=Query(),
    ) # Query | The Research Subject query
    dry_run = False # bool | If true, don't run the query, only generate and return it. (optional) if omitted the server will use the default value of False
    table = "broad-dsde-dev.cda_dev" # str | tablename (optional) if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

    # example passing only required values which don't have defaults set
    try:
        # Execute Research Subject query
        api_response = api_instance.research_subject_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->research_subject_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute Research Subject query
        api_response = api_instance.research_subject_query(query, dry_run=dry_run, table=table)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->research_subject_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The Research Subject query |
 **version** | **str**| Dataset version | defaults to "all_v3_0_subjects_meta"
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it. | [optional] if omitted the server will use the default value of False
 **table** | **str**| tablename | [optional] if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

### Return type

[**QueryCreatedData**](QueryCreatedData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query created response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specimen_files_query**
> QueryCreatedData specimen_files_query(query)

Execute Specimen Files query

Execute a Specimen Files query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example

```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_created_data import QueryCreatedData
from pprint import pprint
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    query = Query(
        node_type="column",
        value="value_example",
        l=Query(),
        r=Query(),
    ) # Query | The specimen query
    dry_run = False # bool | If true, don't run the query, only generate and return it. (optional) if omitted the server will use the default value of False
    table = "broad-dsde-dev.cda_dev" # str | tablename (optional) if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

    # example passing only required values which don't have defaults set
    try:
        # Execute Specimen Files query
        api_response = api_instance.specimen_files_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->specimen_files_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute Specimen Files query
        api_response = api_instance.specimen_files_query(query, dry_run=dry_run, table=table)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->specimen_files_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The specimen query |
 **version** | **str**| Dataset version | defaults to "all_v3_0_subjects_meta"
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it. | [optional] if omitted the server will use the default value of False
 **table** | **str**| tablename | [optional] if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

### Return type

[**QueryCreatedData**](QueryCreatedData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query created response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specimen_query**
> QueryCreatedData specimen_query(query)

Execute Specimens query

Execute a query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example

```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_created_data import QueryCreatedData
from pprint import pprint
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    query = Query(
        node_type="column",
        value="value_example",
        l=Query(),
        r=Query(),
    ) # Query | The specimen query
    dry_run = False # bool | If true, don't run the query, only generate and return it. (optional) if omitted the server will use the default value of False
    table = "broad-dsde-dev.cda_dev" # str | tablename (optional) if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

    # example passing only required values which don't have defaults set
    try:
        # Execute Specimens query
        api_response = api_instance.specimen_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->specimen_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute Specimens query
        api_response = api_instance.specimen_query(query, dry_run=dry_run, table=table)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->specimen_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The specimen query |
 **version** | **str**| Dataset version | defaults to "all_v3_0_subjects_meta"
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it. | [optional] if omitted the server will use the default value of False
 **table** | **str**| tablename | [optional] if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

### Return type

[**QueryCreatedData**](QueryCreatedData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query created response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sql_query**
> QueryCreatedData sql_query(body)

Execute SQL directly on a version of the dataset

### Example

```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query_created_data import QueryCreatedData
from pprint import pprint
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    body = "body_example" # str | BigQuery SQL to run on data table

    # example passing only required values which don't have defaults set
    try:
        # Execute SQL directly on a version of the dataset
        api_response = api_instance.sql_query(body)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->sql_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| BigQuery SQL to run on data table |

### Return type

[**QueryCreatedData**](QueryCreatedData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query created response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subject_files_query**
> QueryCreatedData subject_files_query(query)

Execute Subject Files query

Execute a Subject Files query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example

```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_created_data import QueryCreatedData
from pprint import pprint
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    query = Query(
        node_type="column",
        value="value_example",
        l=Query(),
        r=Query(),
    ) # Query | The subject query
    dry_run = False # bool | If true, don't run the query, only generate and return it. (optional) if omitted the server will use the default value of False
    table = "broad-dsde-dev.cda_dev" # str | tablename (optional) if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

    # example passing only required values which don't have defaults set
    try:
        # Execute Subject Files query
        api_response = api_instance.subject_files_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->subject_files_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute Subject Files query
        api_response = api_instance.subject_files_query(query, dry_run=dry_run, table=table)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->subject_files_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The subject query |
 **version** | **str**| Dataset version | defaults to "all_v3_0_subjects_meta"
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it. | [optional] if omitted the server will use the default value of False
 **table** | **str**| tablename | [optional] if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

### Return type

[**QueryCreatedData**](QueryCreatedData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query created response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subject_query**
> QueryCreatedData subject_query(query)

Execute Subject query

Execute a Subject query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example

```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_created_data import QueryCreatedData
from pprint import pprint
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    query = Query(
        node_type="column",
        value="value_example",
        l=Query(),
        r=Query(),
    ) # Query | The subject query
    dry_run = False # bool | If true, don't run the query, only generate and return it. (optional) if omitted the server will use the default value of False
    table = "broad-dsde-dev.cda_dev" # str | tablename (optional) if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

    # example passing only required values which don't have defaults set
    try:
        # Execute Subject query
        api_response = api_instance.subject_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->subject_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute Subject query
        api_response = api_instance.subject_query(query, dry_run=dry_run, table=table)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->subject_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The subject query |
 **version** | **str**| Dataset version | defaults to "all_v3_0_subjects_meta"
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it. | [optional] if omitted the server will use the default value of False
 **table** | **str**| tablename | [optional] if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

### Return type

[**QueryCreatedData**](QueryCreatedData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query created response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **treatments_query**
> QueryCreatedData treatments_query(query)

Execute Treatments query

Execute a query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example

```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_created_data import QueryCreatedData
from pprint import pprint
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    query = Query(
        node_type="column",
        value="value_example",
        l=Query(),
        r=Query(),
    ) # Query | The treatments query
    dry_run = False # bool | If true, don't run the query, only generate and return it. (optional) if omitted the server will use the default value of False
    table = "broad-dsde-dev.cda_dev" # str | tablename (optional) if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

    # example passing only required values which don't have defaults set
    try:
        # Execute Treatments query
        api_response = api_instance.treatments_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->treatments_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute Treatments query
        api_response = api_instance.treatments_query(query, dry_run=dry_run, table=table)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->treatments_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The treatments query |
 **version** | **str**| Dataset version | defaults to "all_v3_0_subjects_meta"
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it. | [optional] if omitted the server will use the default value of False
 **table** | **str**| tablename | [optional] if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

### Return type

[**QueryCreatedData**](QueryCreatedData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query created response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unique_values**
> QueryCreatedData unique_values(body)

Returns all unique values

Return unique values given a qualified columnName

### Example

```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query_created_data import QueryCreatedData
from pprint import pprint
# Defining the host is optional and defaults to https://cancerdata.dsde-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cancerdata.dsde-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    body = "body_example" # str | column_name of table value being requested
    system = "system_example" # str | Filter on system for results (optional)
    table = "broad-dsde-dev.cda_dev" # str | tablename (optional) if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

    # example passing only required values which don't have defaults set
    try:
        # Returns all unique values
        api_response = api_instance.unique_values(body)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->unique_values: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all unique values
        api_response = api_instance.unique_values(body, system=system, table=table)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->unique_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| column_name of table value being requested |
 **version** | **str**| Dataset version | defaults to "all_v3_0_subjects_meta"
 **system** | **str**| Filter on system for results | [optional]
 **table** | **str**| tablename | [optional] if omitted the server will use the default value of "broad-dsde-dev.cda_dev"

### Return type

[**QueryCreatedData**](QueryCreatedData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query created response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

