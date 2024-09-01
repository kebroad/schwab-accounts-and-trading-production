# openapi_client.TransactionsApi

All URIs are relative to *https://api.schwabapi.com/trader/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transactions_by_id**](TransactionsApi.md#get_transactions_by_id) | **GET** /accounts/{accountNumber}/transactions/{transactionId} | Get specific transaction information for a specific account
[**get_transactions_by_path_param**](TransactionsApi.md#get_transactions_by_path_param) | **GET** /accounts/{accountNumber}/transactions | Get all transactions information for a specific account.


# **get_transactions_by_id**
> List[Transaction] get_transactions_by_id(account_number, transaction_id)

Get specific transaction information for a specific account

Get specific transaction information for a specific account

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.transaction import Transaction
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
    api_instance = openapi_client.TransactionsApi(api_client)
    account_number = 'account_number_example' # str | The encrypted ID of the account
    transaction_id = 56 # int | The ID of the transaction being retrieved.

    try:
        # Get specific transaction information for a specific account
        api_response = api_instance.get_transactions_by_id(account_number, transaction_id)
        print("The response of TransactionsApi->get_transactions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transactions_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The encrypted ID of the account | 
 **transaction_id** | **int**| The ID of the transaction being retrieved. | 

### Return type

[**List[Transaction]**](Transaction.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A List of orders for the account, matching the provided input parameters |  * Schwab-Client-CorrelId -  <br>  |
**400** | An error message indicating the validation problem with the request. |  * Schwab-Client-CorrelID -  <br>  |
**401** | An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application |  * Schwab-Client-CorrelID -  <br>  |
**403** | An error message indicating the caller is forbidden from accessing this service |  * Schwab-Client-CorrelID -  <br>  |
**404** | An error message indicating the resource is not found |  * Schwab-Client-CorrelID -  <br>  |
**500** | An error message indicating there was an unexpected server error |  * Schwab-Client-CorrelID -  <br>  |
**503** | An error message indicating server has a temporary problem responding |  * Schwab-Client-CorrelID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_path_param**
> List[Transaction] get_transactions_by_path_param(account_number, start_date, end_date, types, symbol=symbol)

Get all transactions information for a specific account.

All transactions for a specific account. Maximum number of transactions in response is 3000. Maximum date range is 1 year.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.transaction import Transaction
from openapi_client.models.transaction_type import TransactionType
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
    api_instance = openapi_client.TransactionsApi(api_client)
    account_number = 'account_number_example' # str | The encrypted ID of the account
    start_date = 'start_date_example' # str | Specifies that no transactions entered before this time should be returned.\\nValid ISO-8601 formats are :<br> <code>yyyy-MM-dd'T'HH:mm:ss.SSSZ</code> .  Example start date is '2024-03-28T21:10:42.000Z'. The 'endDate' must also be set.
    end_date = 'end_date_example' # str | Specifies that no transactions entered after this time should be returned.Valid\\nISO-8601 formats are :<br> <code>yyyy-MM-dd'T'HH:mm:ss.SSSZ</code>. Example start date is '2024-05-10T21:10:42.000Z'.\\nThe 'startDate' must also be set.
    types = openapi_client.TransactionType() # TransactionType | Specifies that only transactions of this status should be returned.
    symbol = 'symbol_example' # str | It filters all the transaction activities based on the symbol specified. <u>NOTE:</u> If there is any special character in the symbol, please send th encoded value. (optional)

    try:
        # Get all transactions information for a specific account.
        api_response = api_instance.get_transactions_by_path_param(account_number, start_date, end_date, types, symbol=symbol)
        print("The response of TransactionsApi->get_transactions_by_path_param:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transactions_by_path_param: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The encrypted ID of the account | 
 **start_date** | **str**| Specifies that no transactions entered before this time should be returned.\\nValid ISO-8601 formats are :&lt;br&gt; &lt;code&gt;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&lt;/code&gt; .  Example start date is &#39;2024-03-28T21:10:42.000Z&#39;. The &#39;endDate&#39; must also be set. | 
 **end_date** | **str**| Specifies that no transactions entered after this time should be returned.Valid\\nISO-8601 formats are :&lt;br&gt; &lt;code&gt;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&lt;/code&gt;. Example start date is &#39;2024-05-10T21:10:42.000Z&#39;.\\nThe &#39;startDate&#39; must also be set. | 
 **types** | [**TransactionType**](.md)| Specifies that only transactions of this status should be returned. | 
 **symbol** | **str**| It filters all the transaction activities based on the symbol specified. &lt;u&gt;NOTE:&lt;/u&gt; If there is any special character in the symbol, please send th encoded value. | [optional] 

### Return type

[**List[Transaction]**](Transaction.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A List of orders for the account, matching the provided input\\nparameters |  * Schwab-Client-CorrelId -  <br>  |
**400** | An error message indicating the validation problem with the request. |  * Schwab-Client-CorrelID -  <br>  |
**401** | An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application |  * Schwab-Client-CorrelID -  <br>  |
**403** | An error message indicating the caller is forbidden from accessing this service |  * Schwab-Client-CorrelID -  <br>  |
**404** | An error message indicating the resource is not found |  * Schwab-Client-CorrelID -  <br>  |
**500** | An error message indicating there was an unexpected server error |  * Schwab-Client-CorrelID -  <br>  |
**503** | An error message indicating server has a temporary problem responding |  * Schwab-Client-CorrelID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

