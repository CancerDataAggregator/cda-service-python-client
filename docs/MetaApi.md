# cda_client.MetaApi

All URIs are relative to *https://cda.cda-dev.broadinstitute.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_release_notes**](MetaApi.md#all_release_notes) | **GET** /api/v1/dataset-description/all | List descriptions of all available datasets
[**latest_release_notes**](MetaApi.md#latest_release_notes) | **GET** /api/v1/dataset-description/latest | Description of latest dataset
[**service_status**](MetaApi.md#service_status) | **GET** /status | CDA status


# **all_release_notes**
> [DatasetDescription] all_release_notes()

List descriptions of all available datasets

Return data model and release notes of all releases.

### Example

```python
import time
import cda_client
from cda_client.api import meta_api
from cda_client.model.dataset_description import DatasetDescription
from pprint import pprint
# Defining the host is optional and defaults to https://cda.cda-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cda.cda-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = meta_api.MetaApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List descriptions of all available datasets
        api_response = api_instance.all_release_notes()
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling MetaApi->all_release_notes: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[DatasetDescription]**](DatasetDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of dataset descriptions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **latest_release_notes**
> DatasetDescription latest_release_notes()

Description of latest dataset

Return data model and release notes for latest release.

### Example

```python
import time
import cda_client
from cda_client.api import meta_api
from cda_client.model.dataset_description import DatasetDescription
from pprint import pprint
# Defining the host is optional and defaults to https://cda.cda-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cda.cda-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = meta_api.MetaApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Description of latest dataset
        api_response = api_instance.latest_release_notes()
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling MetaApi->latest_release_notes: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DatasetDescription**](DatasetDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Latest dataset description |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_status**
> SystemStatus service_status()

CDA status

Returns the operational status of the service

### Example

```python
import time
import cda_client
from cda_client.api import meta_api
from cda_client.model.system_status import SystemStatus
from pprint import pprint
# Defining the host is optional and defaults to https://cda.cda-dev.broadinstitute.org
# See configuration.py for a list of all supported configuration parameters.
configuration = cda_client.Configuration(
    host = "https://cda.cda-dev.broadinstitute.org"
)


# Enter a context with an instance of the API client
with cda_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = meta_api.MetaApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # CDA status
        api_response = api_instance.service_status()
        pprint(api_response)
    except cda_client.ApiException as e:
        print("Exception when calling MetaApi->service_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemStatus**](SystemStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | common status response |  -  |
**500** | common status response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

