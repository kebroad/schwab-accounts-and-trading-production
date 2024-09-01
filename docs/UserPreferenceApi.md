# openapi_client.UserPreferenceApi

All URIs are relative to *https://api.schwabapi.com/trader/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_preference**](UserPreferenceApi.md#get_user_preference) | **GET** /userPreference | Get user preference information for the logged in user.


# **get_user_preference**
> List[UserPreference] get_user_preference()

Get user preference information for the logged in user.

Get user preference information for the logged in user.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.user_preference import UserPreference
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.schwabapi.com/trader/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.schwabapi.com/trader/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserPreferenceApi(api_client)

    try:
        # Get user preference information for the logged in user.
        api_response = api_instance.get_user_preference()
        print("The response of UserPreferenceApi->get_user_preference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserPreferenceApi->get_user_preference: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UserPreference]**](UserPreference.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of user preference values. |  -  |
**400** | An error message indicating the validation problem with the request. |  * Schwab-Client-CorrelID -  <br>  |
**401** | An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application |  * Schwab-Client-CorrelID -  <br>  |
**403** | An error message indicating the caller is forbidden from accessing this service |  * Schwab-Client-CorrelID -  <br>  |
**404** | An error message indicating the resource is not found |  * Schwab-Client-CorrelID -  <br>  |
**500** | An error message indicating there was an unexpected server error |  * Schwab-Client-CorrelID -  <br>  |
**503** | An error message indicating server has a temporary problem responding |  * Schwab-Client-CorrelID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

