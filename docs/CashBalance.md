# CashBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_available_for_trading** | **float** |  | [optional] 
**cash_available_for_withdrawal** | **float** |  | [optional] 
**cash_call** | **float** |  | [optional] 
**long_non_marginable_market_value** | **float** |  | [optional] 
**total_cash** | **float** |  | [optional] 
**cash_debit_call_value** | **float** |  | [optional] 
**unsettled_cash** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.cash_balance import CashBalance

# TODO update the JSON string below
json = "{}"
# create an instance of CashBalance from a JSON string
cash_balance_instance = CashBalance.from_json(json)
# print the JSON string representation of the object
print(CashBalance.to_json())

# convert the object into a dict
cash_balance_dict = cash_balance_instance.to_dict()
# create an instance of CashBalance from a dict
cash_balance_from_dict = CashBalance.from_dict(cash_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


