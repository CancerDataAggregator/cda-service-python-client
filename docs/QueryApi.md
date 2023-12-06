# cda_client.QueryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**boolean_query**](QueryApi.md#boolean_query) | **POST** /api/v1/boolean-query | Execute boolean query
[**bulk_data**](QueryApi.md#bulk_data) | **GET** /api/v1/bulk-data | Return all data in CDA
[**columns**](QueryApi.md#columns) | **GET** /api/v1/columns | Returns all column names and definitions for schema
[**diagnosis_counts_query**](QueryApi.md#diagnosis_counts_query) | **POST** /api/v1/diagnosis/counts | Execute Diagnosis Counts query
[**diagnosis_query**](QueryApi.md#diagnosis_query) | **POST** /api/v1/diagnosis | Execute Diagnosis query
[**file_counts_query**](QueryApi.md#file_counts_query) | **POST** /api/v1/files/counts | Execute File Counts query
[**files**](QueryApi.md#files) | **POST** /api/v1/files | Returns a list of files given a boolean query
[**global_counts**](QueryApi.md#global_counts) | **POST** /api/v1/global-counts | Returns counts of the DCS
[**mutation_counts_query**](QueryApi.md#mutation_counts_query) | **POST** /api/v1/mutations/counts | Execute Mutation Counts query
[**mutation_query**](QueryApi.md#mutation_query) | **POST** /api/v1/mutations | Execute Mutation query
[**research_subject_counts_query**](QueryApi.md#research_subject_counts_query) | **POST** /api/v1/researchsubjects/counts | Execute ResearchSubjects Counts query
[**research_subject_file_counts_query**](QueryApi.md#research_subject_file_counts_query) | **POST** /api/v1/researchsubjects/files/counts | Execute ResearchSubjects File Counts query
[**research_subject_files_query**](QueryApi.md#research_subject_files_query) | **POST** /api/v1/researchsubjects/files | Execute ResearchSubject Files query
[**research_subject_query**](QueryApi.md#research_subject_query) | **POST** /api/v1/researchsubjects | Execute Research Subject query
[**specimen_counts_query**](QueryApi.md#specimen_counts_query) | **POST** /api/v1/specimen/counts | Execute Specimen Counts query
[**specimen_file_counts_query**](QueryApi.md#specimen_file_counts_query) | **POST** /api/v1/specimen/files/counts | Execute Specimen File Counts query
[**specimen_files_query**](QueryApi.md#specimen_files_query) | **POST** /api/v1/specimen/files | Execute Specimen Files query
[**specimen_query**](QueryApi.md#specimen_query) | **POST** /api/v1/specimens | Execute Specimens query
[**subject_counts_query**](QueryApi.md#subject_counts_query) | **POST** /api/v1/subjects/counts | Execute Subjects Counts query
[**subject_file_counts_query**](QueryApi.md#subject_file_counts_query) | **POST** /api/v1/subjects/files/counts | Execute Subjects File Counts query
[**subject_files_query**](QueryApi.md#subject_files_query) | **POST** /api/v1/subjects/files | Execute Subject Files query
[**subject_query**](QueryApi.md#subject_query) | **POST** /api/v1/subjects | Execute Subject query
[**treatment_counts_query**](QueryApi.md#treatment_counts_query) | **POST** /api/v1/treatments/counts | Execute Treatments Counts query
[**treatments_query**](QueryApi.md#treatments_query) | **POST** /api/v1/treatments | Execute Treatments query
[**unique_values**](QueryApi.md#unique_values) | **POST** /api/v1/unique-values | Returns all unique values


# **boolean_query**
> PagedResponseData boolean_query(query)

Execute boolean query

Execute a query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.paged_response_data import PagedResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False
    include_count = False # bool | Show the number of results available for the query (optional) if omitted the server will use the default value of False
    offset = 0 # int | The number of entries to skip (optional) if omitted the server will use the default value of 0
    limit = 100 # int | The numbers of entries to return per page of data (optional) if omitted the server will use the default value of 100

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
        api_response = api_instance.boolean_query(query, dry_run=dry_run, include_count=include_count, offset=offset, limit=limit)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->boolean_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The boolean query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False
 **include_count** | **bool**| Show the number of results available for the query | [optional] if omitted the server will use the default value of False
 **offset** | **int**| The number of entries to skip | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of entries to return per page of data | [optional] if omitted the server will use the default value of 100

### Return type

[**PagedResponseData**](PagedResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_data**
> PagedResponseData bulk_data()

Return all data in CDA

Return all data in CDA

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.paged_response_data import PagedResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    table = "table_example" # str | tablename (optional)
    include_count = False # bool | Show the number of results available for the query (optional) if omitted the server will use the default value of False
    offset = 0 # int | The number of entries to skip (optional) if omitted the server will use the default value of 0
    limit = 100 # int | The numbers of entries to return per page of data (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return all data in CDA
        api_response = api_instance.bulk_data(table=table, include_count=include_count, offset=offset, limit=limit)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->bulk_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **str**| tablename | [optional]
 **include_count** | **bool**| Show the number of results available for the query | [optional] if omitted the server will use the default value of False
 **offset** | **int**| The number of entries to skip | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of entries to return per page of data | [optional] if omitted the server will use the default value of 100

### Return type

[**PagedResponseData**](PagedResponseData.md)

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

# **columns**
> ColumnsResponseData columns()

Returns all column names and definitions for schema

Return columnNames for schema along with their descriptions

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.columns_response_data import ColumnsResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns all column names and definitions for schema
        api_response = api_instance.columns()
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->columns: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ColumnsResponseData**](ColumnsResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | columns response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diagnosis_counts_query**
> QueryResponseData diagnosis_counts_query(query)

Execute Diagnosis Counts query

Execute a Diagnosis Counts query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_response_data import QueryResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Execute Diagnosis Counts query
        api_response = api_instance.diagnosis_counts_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->diagnosis_counts_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute Diagnosis Counts query
        api_response = api_instance.diagnosis_counts_query(query, dry_run=dry_run)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->diagnosis_counts_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The diagnosis query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False

### Return type

[**QueryResponseData**](QueryResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | counts data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diagnosis_query**
> PagedResponseData diagnosis_query(query)

Execute Diagnosis query

Execute a query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.paged_response_data import PagedResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False
    include_count = False # bool | Show the number of results available for the query (optional) if omitted the server will use the default value of False
    offset = 0 # int | The number of entries to skip (optional) if omitted the server will use the default value of 0
    limit = 100 # int | The numbers of entries to return per page of data (optional) if omitted the server will use the default value of 100

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
        api_response = api_instance.diagnosis_query(query, dry_run=dry_run, include_count=include_count, offset=offset, limit=limit)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->diagnosis_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The diagnosis query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False
 **include_count** | **bool**| Show the number of results available for the query | [optional] if omitted the server will use the default value of False
 **offset** | **int**| The number of entries to skip | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of entries to return per page of data | [optional] if omitted the server will use the default value of 100

### Return type

[**PagedResponseData**](PagedResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_counts_query**
> QueryResponseData file_counts_query(query)

Execute File Counts query

Execute a File Counts query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_response_data import QueryResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    ) # Query | The files query
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Execute File Counts query
        api_response = api_instance.file_counts_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->file_counts_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute File Counts query
        api_response = api_instance.file_counts_query(query, dry_run=dry_run)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->file_counts_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The files query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False

### Return type

[**QueryResponseData**](QueryResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | counts data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files**
> PagedResponseData files(query)

Returns a list of files given a boolean query

Return list of files for given query

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.paged_response_data import PagedResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False
    include_count = False # bool | Show the number of results available for the query (optional) if omitted the server will use the default value of False
    offset = 0 # int | The number of entries to skip (optional) if omitted the server will use the default value of 0
    limit = 100 # int | The numbers of entries to return per page of data (optional) if omitted the server will use the default value of 100

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
        api_response = api_instance.files(query, dry_run=dry_run, include_count=include_count, offset=offset, limit=limit)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The boolean query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False
 **include_count** | **bool**| Show the number of results available for the query | [optional] if omitted the server will use the default value of False
 **offset** | **int**| The number of entries to skip | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of entries to return per page of data | [optional] if omitted the server will use the default value of 100

### Return type

[**PagedResponseData**](PagedResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **global_counts**
> QueryResponseData global_counts(query)

Returns counts of the DCS

Return GlobalCounts for schema

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_response_data import QueryResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False

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
        api_response = api_instance.global_counts(query, dry_run=dry_run)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->global_counts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| counts |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False

### Return type

[**QueryResponseData**](QueryResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | counts data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mutation_counts_query**
> QueryResponseData mutation_counts_query(query)

Execute Mutation Counts query

Execute a Mutation Counts query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_response_data import QueryResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    ) # Query | The mutation query
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Execute Mutation Counts query
        api_response = api_instance.mutation_counts_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->mutation_counts_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute Mutation Counts query
        api_response = api_instance.mutation_counts_query(query, dry_run=dry_run)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->mutation_counts_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The mutation query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False

### Return type

[**QueryResponseData**](QueryResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | counts data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mutation_query**
> PagedResponseData mutation_query(query)

Execute Mutation query

Execute a query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.paged_response_data import PagedResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    ) # Query | The mutation query
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False
    include_count = False # bool | Show the number of results available for the query (optional) if omitted the server will use the default value of False
    offset = 0 # int | The number of entries to skip (optional) if omitted the server will use the default value of 0
    limit = 100 # int | The numbers of entries to return per page of data (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    try:
        # Execute Mutation query
        api_response = api_instance.mutation_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->mutation_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute Mutation query
        api_response = api_instance.mutation_query(query, dry_run=dry_run, include_count=include_count, offset=offset, limit=limit)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->mutation_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The mutation query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False
 **include_count** | **bool**| Show the number of results available for the query | [optional] if omitted the server will use the default value of False
 **offset** | **int**| The number of entries to skip | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of entries to return per page of data | [optional] if omitted the server will use the default value of 100

### Return type

[**PagedResponseData**](PagedResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **research_subject_counts_query**
> QueryResponseData research_subject_counts_query(query)

Execute ResearchSubjects Counts query

Execute a ResearchSubjects Counts query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_response_data import QueryResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    ) # Query | The research subjects query
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Execute ResearchSubjects Counts query
        api_response = api_instance.research_subject_counts_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->research_subject_counts_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute ResearchSubjects Counts query
        api_response = api_instance.research_subject_counts_query(query, dry_run=dry_run)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->research_subject_counts_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The research subjects query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False

### Return type

[**QueryResponseData**](QueryResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | counts data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **research_subject_file_counts_query**
> QueryResponseData research_subject_file_counts_query(query)

Execute ResearchSubjects File Counts query

Execute a ResearchSubjects File Counts query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_response_data import QueryResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    ) # Query | The research subjects query
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Execute ResearchSubjects File Counts query
        api_response = api_instance.research_subject_file_counts_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->research_subject_file_counts_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute ResearchSubjects File Counts query
        api_response = api_instance.research_subject_file_counts_query(query, dry_run=dry_run)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->research_subject_file_counts_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The research subjects query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False

### Return type

[**QueryResponseData**](QueryResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | counts data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **research_subject_files_query**
> PagedResponseData research_subject_files_query(query)

Execute ResearchSubject Files query

Execute a ResearchSubject Files query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.paged_response_data import PagedResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False
    include_count = False # bool | Show the number of results available for the query (optional) if omitted the server will use the default value of False
    offset = 0 # int | The number of entries to skip (optional) if omitted the server will use the default value of 0
    limit = 100 # int | The numbers of entries to return per page of data (optional) if omitted the server will use the default value of 100

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
        api_response = api_instance.research_subject_files_query(query, dry_run=dry_run, include_count=include_count, offset=offset, limit=limit)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->research_subject_files_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The research subject query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False
 **include_count** | **bool**| Show the number of results available for the query | [optional] if omitted the server will use the default value of False
 **offset** | **int**| The number of entries to skip | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of entries to return per page of data | [optional] if omitted the server will use the default value of 100

### Return type

[**PagedResponseData**](PagedResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **research_subject_query**
> PagedResponseData research_subject_query(query)

Execute Research Subject query

Execute a query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.paged_response_data import PagedResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False
    include_count = False # bool | Show the number of results available for the query (optional) if omitted the server will use the default value of False
    offset = 0 # int | The number of entries to skip (optional) if omitted the server will use the default value of 0
    limit = 100 # int | The numbers of entries to return per page of data (optional) if omitted the server will use the default value of 100

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
        api_response = api_instance.research_subject_query(query, dry_run=dry_run, include_count=include_count, offset=offset, limit=limit)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->research_subject_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The Research Subject query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False
 **include_count** | **bool**| Show the number of results available for the query | [optional] if omitted the server will use the default value of False
 **offset** | **int**| The number of entries to skip | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of entries to return per page of data | [optional] if omitted the server will use the default value of 100

### Return type

[**PagedResponseData**](PagedResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specimen_counts_query**
> QueryResponseData specimen_counts_query(query)

Execute Specimen Counts query

Execute a Specimen Counts query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_response_data import QueryResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Execute Specimen Counts query
        api_response = api_instance.specimen_counts_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->specimen_counts_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute Specimen Counts query
        api_response = api_instance.specimen_counts_query(query, dry_run=dry_run)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->specimen_counts_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The specimen query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False

### Return type

[**QueryResponseData**](QueryResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | counts data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specimen_file_counts_query**
> QueryResponseData specimen_file_counts_query(query)

Execute Specimen File Counts query

Execute a Specimen File Counts query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_response_data import QueryResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Execute Specimen File Counts query
        api_response = api_instance.specimen_file_counts_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->specimen_file_counts_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute Specimen File Counts query
        api_response = api_instance.specimen_file_counts_query(query, dry_run=dry_run)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->specimen_file_counts_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The specimen query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False

### Return type

[**QueryResponseData**](QueryResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | counts data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specimen_files_query**
> PagedResponseData specimen_files_query(query)

Execute Specimen Files query

Execute a Specimen Files query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.paged_response_data import PagedResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False
    include_count = False # bool | Show the number of results available for the query (optional) if omitted the server will use the default value of False
    offset = 0 # int | The number of entries to skip (optional) if omitted the server will use the default value of 0
    limit = 100 # int | The numbers of entries to return per page of data (optional) if omitted the server will use the default value of 100

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
        api_response = api_instance.specimen_files_query(query, dry_run=dry_run, include_count=include_count, offset=offset, limit=limit)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->specimen_files_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The specimen query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False
 **include_count** | **bool**| Show the number of results available for the query | [optional] if omitted the server will use the default value of False
 **offset** | **int**| The number of entries to skip | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of entries to return per page of data | [optional] if omitted the server will use the default value of 100

### Return type

[**PagedResponseData**](PagedResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specimen_query**
> PagedResponseData specimen_query(query)

Execute Specimens query

Execute a query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.paged_response_data import PagedResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False
    include_count = False # bool | Show the number of results available for the query (optional) if omitted the server will use the default value of False
    offset = 0 # int | The number of entries to skip (optional) if omitted the server will use the default value of 0
    limit = 100 # int | The numbers of entries to return per page of data (optional) if omitted the server will use the default value of 100

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
        api_response = api_instance.specimen_query(query, dry_run=dry_run, include_count=include_count, offset=offset, limit=limit)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->specimen_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The specimen query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False
 **include_count** | **bool**| Show the number of results available for the query | [optional] if omitted the server will use the default value of False
 **offset** | **int**| The number of entries to skip | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of entries to return per page of data | [optional] if omitted the server will use the default value of 100

### Return type

[**PagedResponseData**](PagedResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subject_counts_query**
> QueryResponseData subject_counts_query(query)

Execute Subjects Counts query

Execute a Subjects Counts query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_response_data import QueryResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    ) # Query | The subjects query
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Execute Subjects Counts query
        api_response = api_instance.subject_counts_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->subject_counts_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute Subjects Counts query
        api_response = api_instance.subject_counts_query(query, dry_run=dry_run)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->subject_counts_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The subjects query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False

### Return type

[**QueryResponseData**](QueryResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | counts data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subject_file_counts_query**
> QueryResponseData subject_file_counts_query(query)

Execute Subjects File Counts query

Execute a Subjects File Counts query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_response_data import QueryResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    ) # Query | The subjects query
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Execute Subjects File Counts query
        api_response = api_instance.subject_file_counts_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->subject_file_counts_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute Subjects File Counts query
        api_response = api_instance.subject_file_counts_query(query, dry_run=dry_run)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->subject_file_counts_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The subjects query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False

### Return type

[**QueryResponseData**](QueryResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | counts data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subject_files_query**
> PagedResponseData subject_files_query(query)

Execute Subject Files query

Execute a Subject Files query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.paged_response_data import PagedResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False
    include_count = False # bool | Show the number of results available for the query (optional) if omitted the server will use the default value of False
    offset = 0 # int | The number of entries to skip (optional) if omitted the server will use the default value of 0
    limit = 100 # int | The numbers of entries to return per page of data (optional) if omitted the server will use the default value of 100

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
        api_response = api_instance.subject_files_query(query, dry_run=dry_run, include_count=include_count, offset=offset, limit=limit)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->subject_files_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The subject query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False
 **include_count** | **bool**| Show the number of results available for the query | [optional] if omitted the server will use the default value of False
 **offset** | **int**| The number of entries to skip | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of entries to return per page of data | [optional] if omitted the server will use the default value of 100

### Return type

[**PagedResponseData**](PagedResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subject_query**
> PagedResponseData subject_query(query)

Execute Subject query

Execute a Subject query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.paged_response_data import PagedResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False
    include_count = False # bool | Show the number of results available for the query (optional) if omitted the server will use the default value of False
    offset = 0 # int | The number of entries to skip (optional) if omitted the server will use the default value of 0
    limit = 100 # int | The numbers of entries to return per page of data (optional) if omitted the server will use the default value of 100

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
        api_response = api_instance.subject_query(query, dry_run=dry_run, include_count=include_count, offset=offset, limit=limit)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->subject_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The subject query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False
 **include_count** | **bool**| Show the number of results available for the query | [optional] if omitted the server will use the default value of False
 **offset** | **int**| The number of entries to skip | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of entries to return per page of data | [optional] if omitted the server will use the default value of 100

### Return type

[**PagedResponseData**](PagedResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **treatment_counts_query**
> QueryResponseData treatment_counts_query(query)

Execute Treatments Counts query

Execute a Treatments Counts query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.query_response_data import QueryResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    ) # Query | The treatment query
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Execute Treatments Counts query
        api_response = api_instance.treatment_counts_query(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->treatment_counts_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute Treatments Counts query
        api_response = api_instance.treatment_counts_query(query, dry_run=dry_run)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->treatment_counts_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The treatment query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False

### Return type

[**QueryResponseData**](QueryResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | counts data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **treatments_query**
> PagedResponseData treatments_query(query)

Execute Treatments query

Execute a query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response. 

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.query import Query
from cda_client.model.paged_response_data import PagedResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
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
    dry_run = False # bool | If true, don't run the query, only generate and return it (optional) if omitted the server will use the default value of False
    include_count = False # bool | Show the number of results available for the query (optional) if omitted the server will use the default value of False
    offset = 0 # int | The number of entries to skip (optional) if omitted the server will use the default value of 0
    limit = 100 # int | The numbers of entries to return per page of data (optional) if omitted the server will use the default value of 100

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
        api_response = api_instance.treatments_query(query, dry_run=dry_run, include_count=include_count, offset=offset, limit=limit)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->treatments_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The treatments query |
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it | [optional] if omitted the server will use the default value of False
 **include_count** | **bool**| Show the number of results available for the query | [optional] if omitted the server will use the default value of False
 **offset** | **int**| The number of entries to skip | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of entries to return per page of data | [optional] if omitted the server will use the default value of 100

### Return type

[**PagedResponseData**](PagedResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unique_values**
> PagedResponseData unique_values(body)

Returns all unique values

Return unique values given a qualified columnName

### Example


```python
import time
import cda_client
from cda_client.api import query_api
from cda_client.model.paged_response_data import PagedResponseData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    body = "body_example" # str | column_name being requested
    system = "system_example" # str | Filter on system for results (optional)
    count = True # bool | Show the number of occurances for each value (optional)
    include_count = False # bool | Show the number of results available for the query (optional) if omitted the server will use the default value of False
    offset = 0 # int | The number of entries to skip (optional) if omitted the server will use the default value of 0
    limit = 100 # int | The numbers of entries to return per page of data (optional) if omitted the server will use the default value of 100

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
        api_response = api_instance.unique_values(body, system=system, count=count, include_count=include_count, offset=offset, limit=limit)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->unique_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| column_name being requested |
 **system** | **str**| Filter on system for results | [optional]
 **count** | **bool**| Show the number of occurances for each value | [optional]
 **include_count** | **bool**| Show the number of results available for the query | [optional] if omitted the server will use the default value of False
 **offset** | **int**| The number of entries to skip | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of entries to return per page of data | [optional] if omitted the server will use the default value of 100

### Return type

[**PagedResponseData**](PagedResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

