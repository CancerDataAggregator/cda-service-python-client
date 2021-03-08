# cda_client.QueryApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**boolean_query**](QueryApi.md#boolean_query) | **POST** /api/v1/boolean-query/{version} | Execute boolean query
[**bulk_data**](QueryApi.md#bulk_data) | **GET** /api/v1/bulk-data/{version} | Return all data in CDA
[**sql_query**](QueryApi.md#sql_query) | **POST** /api/v1/sql-query/{version} | Execute SQL directly on a version of the dataset


# **boolean_query**
> QueryResponseData boolean_query(version, query, offset=offset, limit=limit, dry_run=dry_run)

Execute boolean query

Execute a query composed of conditions on columns combined with boolean operators  

### Example

```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cda_client.QueryApi(api_client)
    version = 'version_example' # str | Dataset version
query = cda_client.Query() # Query | The boolean query
offset = 56 # int | The number of entries to skip (optional)
limit = 56 # int | The numbers of entries to return (optional)
dry_run = False # bool | If true, don't run the query, only generate and return it. (optional) (default to False)

    try:
        # Execute boolean query
        api_response = api_instance.boolean_query(version, query, offset=offset, limit=limit, dry_run=dry_run)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueryApi->boolean_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Dataset version | 
 **query** | [**Query**](Query.md)| The boolean query | 
 **offset** | **int**| The number of entries to skip | [optional] 
 **limit** | **int**| The numbers of entries to return | [optional] 
 **dry_run** | **bool**| If true, don&#39;t run the query, only generate and return it. | [optional] [default to False]

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
**200** | common query response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_data**
> QueryResponseData bulk_data(version, offset=offset, limit=limit)

Return all data in CDA

Return all data in CDA

### Example

```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cda_client.QueryApi(api_client)
    version = 'version_example' # str | Dataset version
offset = 56 # int | The number of entries to skip (optional)
limit = 56 # int | The numbers of entries to return (optional)

    try:
        # Return all data in CDA
        api_response = api_instance.bulk_data(version, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueryApi->bulk_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Dataset version | 
 **offset** | **int**| The number of entries to skip | [optional] 
 **limit** | **int**| The numbers of entries to return | [optional] 

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
**200** | common query response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sql_query**
> QueryResponseData sql_query(version, body, offset=offset, limit=limit)

Execute SQL directly on a version of the dataset

### Example

```python
from __future__ import print_function
import time
import cda_client
from cda_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cda_client.QueryApi(api_client)
    version = 'version_example' # str | Dataset version
body = 'body_example' # str | BigQuery SQL to run on data table
offset = 56 # int | The number of entries to skip (optional)
limit = 56 # int | The numbers of entries to return (optional)

    try:
        # Execute SQL directly on a version of the dataset
        api_response = api_instance.sql_query(version, body, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueryApi->sql_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Dataset version | 
 **body** | **str**| BigQuery SQL to run on data table | 
 **offset** | **int**| The number of entries to skip | [optional] 
 **limit** | **int**| The numbers of entries to return | [optional] 

### Return type

[**QueryResponseData**](QueryResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | common query response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

