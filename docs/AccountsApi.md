# openapi_client.AccountsApi

All URIs are relative to *https://api.schwabapi.com/trader/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account**](AccountsApi.md#get_account) | **GET** /accounts/{accountNumber} | Get a specific account balance and positions for the logged in user.
[**get_account_numbers**](AccountsApi.md#get_account_numbers) | **GET** /accounts/accountNumbers | Get list of account numbers and their encrypted values
[**get_accounts**](AccountsApi.md#get_accounts) | **GET** /accounts | Get linked account(s) balances and positions for the logged in user.


# **get_account**
> Account get_account(account_number, fields=fields)

Get a specific account balance and positions for the logged in user.

Specific account information with balances and positions.\\nThe balance information on these accounts is displayed by default but\\nPositions will be returned based on the \\\"positions\\\" flag.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.account import Account
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
    api_instance = openapi_client.AccountsApi(api_client)
    account_number = 'account_number_example' # str | The encrypted ID of the account
    fields = 'fields_example' # str | This allows one to determine\\nwhich fields they want returned. Possible values in this String can be:\\n<br><code>positions</code><br> Example:<br><code>fields=positions</code> (optional)

    try:
        # Get a specific account balance and positions for the logged in user.
        api_response = api_instance.get_account(account_number, fields=fields)
        print("The response of AccountsApi->get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The encrypted ID of the account | 
 **fields** | **str**| This allows one to determine\\nwhich fields they want returned. Possible values in this String can be:\\n&lt;br&gt;&lt;code&gt;positions&lt;/code&gt;&lt;br&gt; Example:&lt;br&gt;&lt;code&gt;fields&#x3D;positions&lt;/code&gt; | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A valid account, matching the provided input parameters |  * Schwab-Client-CorrelId -  <br>  |
**400** | An error message indicating the validation problem with the request. |  * Schwab-Client-CorrelID -  <br>  |
**401** | An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application |  * Schwab-Client-CorrelID -  <br>  |
**403** | An error message indicating the caller is forbidden from accessing this service |  * Schwab-Client-CorrelID -  <br>  |
**404** | An error message indicating the resource is not found |  * Schwab-Client-CorrelID -  <br>  |
**500** | An error message indicating there was an unexpected server error |  * Schwab-Client-CorrelID -  <br>  |
**503** | An error message indicating server has a temporary problem responding |  * Schwab-Client-CorrelID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_numbers**
> List[AccountNumberHash] get_account_numbers()

Get list of account numbers and their encrypted values

Account numbers in plain text cannot be used outside of headers or request/response bodies. As the first step consumers must invoke this service to retrieve the list of plain text/encrypted value pairs, and use encrypted account values for all subsequent calls for any accountNumber request.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.account_number_hash import AccountNumberHash
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
    api_instance = openapi_client.AccountsApi(api_client)

    try:
        # Get list of account numbers and their encrypted values
        api_response = api_instance.get_account_numbers()
        print("The response of AccountsApi->get_account_numbers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_numbers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AccountNumberHash]**](AccountNumberHash.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of valid \\\&quot;accounts\\\&quot;, matching the provided input parameters. |  * Schwab-Client-CorrelId -  <br>  |
**400** | An error message indicating the validation problem with the request. |  * Schwab-Client-CorrelID -  <br>  |
**401** | An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application |  * Schwab-Client-CorrelID -  <br>  |
**403** | An error message indicating the caller is forbidden from accessing this service |  * Schwab-Client-CorrelID -  <br>  |
**404** | An error message indicating the resource is not found |  * Schwab-Client-CorrelID -  <br>  |
**500** | An error message indicating there was an unexpected server error |  * Schwab-Client-CorrelID -  <br>  |
**503** | An error message indicating server has a temporary problem responding |  * Schwab-Client-CorrelID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> List[Account] get_accounts(fields=fields)

Get linked account(s) balances and positions for the logged in user.

All the linked account information for the user logged in. The\\nbalances on these accounts are displayed by default however the positions\\non these accounts will be displayed based on the \\\"positions\\\" flag.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.account import Account
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
    api_instance = openapi_client.AccountsApi(api_client)
    fields = 'fields_example' # str | This allows one to determine which fields they want returned. Possible value in this String can be:\\n<br><code>positions</code><br> Example:<br><code>fields=positions</code> (optional)

    try:
        # Get linked account(s) balances and positions for the logged in user.
        api_response = api_instance.get_accounts(fields=fields)
        print("The response of AccountsApi->get_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| This allows one to determine which fields they want returned. Possible value in this String can be:\\n&lt;br&gt;&lt;code&gt;positions&lt;/code&gt;&lt;br&gt; Example:&lt;br&gt;&lt;code&gt;fields&#x3D;positions&lt;/code&gt; | [optional] 

### Return type

[**List[Account]**](Account.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of valid \\\&quot;accounts\\\&quot;, matching the provided input parameters. |  * Schwab-Client-CorrelId -  <br>  |
**400** | An error message indicating the validation problem with the request. |  * Schwab-Client-CorrelID -  <br>  |
**401** | An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application |  * Schwab-Client-CorrelID -  <br>  |
**403** | An error message indicating the caller is forbidden from accessing this service |  * Schwab-Client-CorrelID -  <br>  |
**404** | An error message indicating the resource is not found |  * Schwab-Client-CorrelID -  <br>  |
**500** | An error message indicating there was an unexpected server error |  * Schwab-Client-CorrelID -  <br>  |
**503** | An error message indicating server has a temporary problem responding |  * Schwab-Client-CorrelID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

