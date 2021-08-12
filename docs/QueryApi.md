# cda_client.QueryApi

All URIs are relative to *https://cda.cda-dev.broadinstitute.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**boolean_query**](QueryApi.md#boolean_query) | **POST** /api/v1/boolean-query/{version} | Execute boolean query
[**boolean_query2**](QueryApi.md#boolean_query2) | **POST** /api/v1/boolean-query2/{version} | Execute boolean query
[**bulk_data**](QueryApi.md#bulk_data) | **GET** /api/v1/bulk-data/{version} | Return all data in CDA
[**query**](QueryApi.md#query) | **GET** /api/v1/query/{id} | Given a query ID, return the a page of data from the query result.
[**sql_query**](QueryApi.md#sql_query) | **POST** /api/v1/sql-query | Execute SQL directly on a version of the dataset
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
# Defining the host is optional and defaults to https://cda.cda-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cda.cda-dev.broadinstitute.org"
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
        api_response = api_instance.boolean_query(query, dry_run=dry_run)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->boolean_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The boolean query |
 **version** | **str**| Dataset version | defaults to "v3"
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it. | [optional] if omitted the server will use the default value of False

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

# **boolean_query2**
> QueryCreatedData boolean_query2(query)

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
# Defining the host is optional and defaults to https://cda.cda-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cda.cda-dev.broadinstitute.org"
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

    # example passing only required values which don't have defaults set
    try:
        # Execute boolean query
        api_response = api_instance.boolean_query2(query)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->boolean_query2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute boolean query
        api_response = api_instance.boolean_query2(query, dry_run=dry_run)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->boolean_query2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)| The boolean query |
 **version** | **str**| Dataset version | defaults to "v3"
 **table** | **str**| table name | defaults to "gdc-bq-sample.cda_mvp"
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it. | [optional] if omitted the server will use the default value of False

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
# Defining the host is optional and defaults to https://cda.cda-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cda.cda-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Return all data in CDA
        api_response = api_instance.bulk_data()
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->bulk_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Dataset version | defaults to "v3"

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
# Defining the host is optional and defaults to https://cda.cda-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cda.cda-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    id = "id_example" # str | Query ID
    offset = 0 # int | The number of entries to skip (optional) if omitted the server will use the default value of 0
    limit = 1000 # int | The numbers of entries to return per page of data (optional) if omitted the server will use the default value of 1000

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
 **limit** | **int**| The numbers of entries to return per page of data | [optional] if omitted the server will use the default value of 1000

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
# Defining the host is optional and defaults to https://cda.cda-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cda.cda-dev.broadinstitute.org"
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
# Defining the host is optional and defaults to https://cda.cda-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cda.cda-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    body = "body_example" # str | column_name of table value being requested
    system = "system_example" # str | Filter on system for results (optional)

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
        api_response = api_instance.unique_values(body, system=system)
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling QueryApi->unique_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| column_name of table value being requested |
 **version** | **str**| Dataset version | defaults to "v3"
 **system** | **str**| Filter on system for results | [optional]

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

