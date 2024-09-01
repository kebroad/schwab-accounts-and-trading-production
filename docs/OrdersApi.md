# openapi_client.OrdersApi

All URIs are relative to *https://api.schwabapi.com/trader/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](OrdersApi.md#cancel_order) | **DELETE** /accounts/{accountNumber}/orders/{orderId} | Cancel an order for a specific account
[**get_order**](OrdersApi.md#get_order) | **GET** /accounts/{accountNumber}/orders/{orderId} | Get a specific order by its ID, for a specific account
[**get_orders_by_path_param**](OrdersApi.md#get_orders_by_path_param) | **GET** /accounts/{accountNumber}/orders | Get all orders for a specific account.
[**get_orders_by_query_param**](OrdersApi.md#get_orders_by_query_param) | **GET** /orders | Get all orders for all accounts
[**place_order**](OrdersApi.md#place_order) | **POST** /accounts/{accountNumber}/orders | Place order for a specific account.
[**preview_order**](OrdersApi.md#preview_order) | **POST** /accounts/{accountNumber}/previewOrder | Preview order for a specific account. **Coming Soon**.
[**replace_order**](OrdersApi.md#replace_order) | **PUT** /accounts/{accountNumber}/orders/{orderId} | Replace order for a specific account


# **cancel_order**
> cancel_order(account_number, order_id)

Cancel an order for a specific account

Cancel a specific order for a specific account<br>

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
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
    api_instance = openapi_client.OrdersApi(api_client)
    account_number = 'account_number_example' # str | The encrypted ID of the account
    order_id = 56 # int | The ID of the order being cancelled

    try:
        # Cancel an order for a specific account
        api_instance.cancel_order(account_number, order_id)
    except Exception as e:
        print("Exception when calling OrdersApi->cancel_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The encrypted ID of the account | 
 **order_id** | **int**| The ID of the order being cancelled | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty response body if an order was successfully canceled. |  * Schwab-Client-CorrelId -  <br>  |
**400** | An error message indicating the validation problem with the request. |  * Schwab-Client-CorrelID -  <br>  |
**401** | An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application |  * Schwab-Client-CorrelID -  <br>  |
**403** | An error message indicating the caller is forbidden from accessing this service |  * Schwab-Client-CorrelID -  <br>  |
**404** | An error message indicating the resource is not found |  * Schwab-Client-CorrelID -  <br>  |
**500** | An error message indicating there was an unexpected server error |  * Schwab-Client-CorrelID -  <br>  |
**503** | An error message indicating server has a temporary problem responding |  * Schwab-Client-CorrelID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> Order get_order(account_number, order_id)

Get a specific order by its ID, for a specific account

Get a specific order by its ID, for a specific account

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.order import Order
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
    api_instance = openapi_client.OrdersApi(api_client)
    account_number = 'account_number_example' # str | The encrypted ID of the account
    order_id = 56 # int | The ID of the order being retrieved.

    try:
        # Get a specific order by its ID, for a specific account
        api_response = api_instance.get_order(account_number, order_id)
        print("The response of OrdersApi->get_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The encrypted ID of the account | 
 **order_id** | **int**| The ID of the order being retrieved. | 

### Return type

[**Order**](Order.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An order object, matching the input parameters |  * Schwab-Client-CorrelId -  <br>  |
**400** | An error message indicating the validation problem with the request. |  * Schwab-Client-CorrelID -  <br>  |
**401** | An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application |  * Schwab-Client-CorrelID -  <br>  |
**403** | An error message indicating the caller is forbidden from accessing this service |  * Schwab-Client-CorrelID -  <br>  |
**404** | An error message indicating the resource is not found |  * Schwab-Client-CorrelID -  <br>  |
**500** | An error message indicating there was an unexpected server error |  * Schwab-Client-CorrelID -  <br>  |
**503** | An error message indicating server has a temporary problem responding |  * Schwab-Client-CorrelID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders_by_path_param**
> List[Order] get_orders_by_path_param(account_number, from_entered_time, to_entered_time, max_results=max_results, status=status)

Get all orders for a specific account.

All orders for a specific account. Orders retrieved can be filtered based on input parameters below. Maximum date range is 1 year.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.api_order_status import ApiOrderStatus
from openapi_client.models.order import Order
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
    api_instance = openapi_client.OrdersApi(api_client)
    account_number = 'account_number_example' # str | The encrypted ID of the account
    from_entered_time = 'from_entered_time_example' # str | Specifies that no orders entered before this time should be returned.\\nValid ISO-8601 formats are :<br> <code>yyyy-MM-dd'T'HH:mm:ss.SSSZ</code>  Example fromEnteredTime is '2024-03-29T00:00:00.000Z'.\\n'toEnteredTime' must also be set.
    to_entered_time = 'to_entered_time_example' # str | Specifies that no orders entered after this time should be returned.Valid\\nISO-8601 formats are :<br> <code>yyyy-MM-dd'T'HH:mm:ss.SSSZ</code>.  Example toEnteredTime is '2024-04-28T23:59:59.000Z'.\\n'fromEnteredTime' must also be set.
    max_results = 56 # int | The max number of orders to retrieve. Default is 3000. (optional)
    status = openapi_client.ApiOrderStatus() # ApiOrderStatus | Specifies that only orders of this status should be returned. (optional)

    try:
        # Get all orders for a specific account.
        api_response = api_instance.get_orders_by_path_param(account_number, from_entered_time, to_entered_time, max_results=max_results, status=status)
        print("The response of OrdersApi->get_orders_by_path_param:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_orders_by_path_param: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The encrypted ID of the account | 
 **from_entered_time** | **str**| Specifies that no orders entered before this time should be returned.\\nValid ISO-8601 formats are :&lt;br&gt; &lt;code&gt;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&lt;/code&gt;  Example fromEnteredTime is &#39;2024-03-29T00:00:00.000Z&#39;.\\n&#39;toEnteredTime&#39; must also be set. | 
 **to_entered_time** | **str**| Specifies that no orders entered after this time should be returned.Valid\\nISO-8601 formats are :&lt;br&gt; &lt;code&gt;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&lt;/code&gt;.  Example toEnteredTime is &#39;2024-04-28T23:59:59.000Z&#39;.\\n&#39;fromEnteredTime&#39; must also be set. | 
 **max_results** | **int**| The max number of orders to retrieve. Default is 3000. | [optional] 
 **status** | [**ApiOrderStatus**](.md)| Specifies that only orders of this status should be returned. | [optional] 

### Return type

[**List[Order]**](Order.md)

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

# **get_orders_by_query_param**
> List[Order] get_orders_by_query_param(from_entered_time, to_entered_time, max_results=max_results, status=status)

Get all orders for all accounts

Get all orders for all accounts<br>

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.api_order_status import ApiOrderStatus
from openapi_client.models.order import Order
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
    api_instance = openapi_client.OrdersApi(api_client)
    from_entered_time = 'from_entered_time_example' # str | Specifies that no orders entered before this time should be returned. Valid ISO-8601 formats are-\\nyyyy-MM-dd'T'HH:mm:ss.SSSZ Date must be within 60 days from today's date.\\n'toEnteredTime' must also be set.
    to_entered_time = 'to_entered_time_example' # str | Specifies that no orders entered after this time should be returned.Valid ISO-8601 formats are -\\nyyyy-MM-dd'T'HH:mm:ss.SSSZ. 'fromEnteredTime' must also be set.
    max_results = 56 # int | The max number of orders to retrieve. Default is 3000. (optional)
    status = openapi_client.ApiOrderStatus() # ApiOrderStatus | Specifies that only orders of this status should be returned. (optional)

    try:
        # Get all orders for all accounts
        api_response = api_instance.get_orders_by_query_param(from_entered_time, to_entered_time, max_results=max_results, status=status)
        print("The response of OrdersApi->get_orders_by_query_param:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_orders_by_query_param: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_entered_time** | **str**| Specifies that no orders entered before this time should be returned. Valid ISO-8601 formats are-\\nyyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ Date must be within 60 days from today&#39;s date.\\n&#39;toEnteredTime&#39; must also be set. | 
 **to_entered_time** | **str**| Specifies that no orders entered after this time should be returned.Valid ISO-8601 formats are -\\nyyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ. &#39;fromEnteredTime&#39; must also be set. | 
 **max_results** | **int**| The max number of orders to retrieve. Default is 3000. | [optional] 
 **status** | [**ApiOrderStatus**](.md)| Specifies that only orders of this status should be returned. | [optional] 

### Return type

[**List[Order]**](Order.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A List of orders for the specified account or if its not mentioned,\\nfor all the linked accounts, matching the provided input parameters. |  * Schwab-Client-CorrelId -  <br>  |
**400** | An error message indicating the validation problem with the request. |  * Schwab-Client-CorrelID -  <br>  |
**401** | An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application |  * Schwab-Client-CorrelID -  <br>  |
**403** | An error message indicating the caller is forbidden from accessing this service |  * Schwab-Client-CorrelID -  <br>  |
**404** | An error message indicating the resource is not found |  * Schwab-Client-CorrelID -  <br>  |
**500** | An error message indicating there was an unexpected server error |  * Schwab-Client-CorrelID -  <br>  |
**503** | An error message indicating server has a temporary problem responding |  * Schwab-Client-CorrelID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_order**
> place_order(account_number, body)

Place order for a specific account.

Place an order for a specific account.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.order_request import OrderRequest
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
    api_instance = openapi_client.OrdersApi(api_client)
    account_number = 'account_number_example' # str | The encrypted ID of the account
    body = openapi_client.OrderRequest() # OrderRequest | The new Order Object.

    try:
        # Place order for a specific account.
        api_instance.place_order(account_number, body)
    except Exception as e:
        print("Exception when calling OrdersApi->place_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The encrypted ID of the account | 
 **body** | [**OrderRequest**](OrderRequest.md)| The new Order Object. | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Empty response body if an order was successfully placed/created. |  * Schwab-Client-CorrelId -  <br>  * Location - Link to the newly created order if order was successfully\\ncreated. <br>  |
**400** | An error message indicating the validation problem with the request. |  * Schwab-Client-CorrelID -  <br>  |
**401** | An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application |  * Schwab-Client-CorrelID -  <br>  |
**403** | An error message indicating the caller is forbidden from accessing this service |  * Schwab-Client-CorrelID -  <br>  |
**404** | An error message indicating the resource is not found |  * Schwab-Client-CorrelID -  <br>  |
**500** | An error message indicating there was an unexpected server error |  * Schwab-Client-CorrelID -  <br>  |
**503** | An error message indicating server has a temporary problem responding |  * Schwab-Client-CorrelID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_order**
> PreviewOrder preview_order(account_number, preview_order)

Preview order for a specific account. **Coming Soon**.

Preview an order for a specific account.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.preview_order import PreviewOrder
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
    api_instance = openapi_client.OrdersApi(api_client)
    account_number = 'account_number_example' # str | The encrypted ID of the account
    preview_order = openapi_client.PreviewOrder() # PreviewOrder | The Order Object.

    try:
        # Preview order for a specific account. **Coming Soon**.
        api_response = api_instance.preview_order(account_number, preview_order)
        print("The response of OrdersApi->preview_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->preview_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The encrypted ID of the account | 
 **preview_order** | [**PreviewOrder**](PreviewOrder.md)| The Order Object. | 

### Return type

[**PreviewOrder**](PreviewOrder.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An order object, matching the input parameters |  * Schwab-Client-CorrelId -  <br>  |
**400** | An error message indicating the validation problem with the request. |  * Schwab-Client-CorrelID -  <br>  |
**401** | An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application |  * Schwab-Client-CorrelID -  <br>  |
**403** | An error message indicating the caller is forbidden from accessing this service |  * Schwab-Client-CorrelID -  <br>  |
**404** | An error message indicating the resource is not found |  * Schwab-Client-CorrelID -  <br>  |
**500** | An error message indicating there was an unexpected server error |  * Schwab-Client-CorrelID -  <br>  |
**503** | An error message indicating server has a temporary problem responding |  * Schwab-Client-CorrelID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_order**
> replace_order(account_number, order_id, body)

Replace order for a specific account

Replace an existing order for an account. The existing order will be replaced by the new               order. Once replaced, the old order will be canceled and a new order will be created.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.order_request import OrderRequest
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
    api_instance = openapi_client.OrdersApi(api_client)
    account_number = 'account_number_example' # str | The encrypted ID of the account
    order_id = 56 # int | The ID of the order being retrieved.
    body = openapi_client.OrderRequest() # OrderRequest | The Order Object.

    try:
        # Replace order for a specific account
        api_instance.replace_order(account_number, order_id, body)
    except Exception as e:
        print("Exception when calling OrdersApi->replace_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The encrypted ID of the account | 
 **order_id** | **int**| The ID of the order being retrieved. | 
 **body** | [**OrderRequest**](OrderRequest.md)| The Order Object. | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Empty response body if an order was successfully replaced/created. |  * Schwab-Client-CorrelId -  <br>  * Location - Link to the newly created order if order was successfully\\ncreated. <br>  |
**400** | An error message indicating the validation problem with the request. |  * Schwab-Client-CorrelID -  <br>  |
**401** | An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application |  * Schwab-Client-CorrelID -  <br>  |
**403** | An error message indicating the caller is forbidden from accessing this service |  * Schwab-Client-CorrelID -  <br>  |
**404** | An error message indicating the resource is not found |  * Schwab-Client-CorrelID -  <br>  |
**500** | An error message indicating there was an unexpected server error |  * Schwab-Client-CorrelID -  <br>  |
**503** | An error message indicating server has a temporary problem responding |  * Schwab-Client-CorrelID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

