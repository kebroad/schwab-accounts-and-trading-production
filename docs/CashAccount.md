# CashAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_balances** | [**CashInitialBalance**](CashInitialBalance.md) |  | [optional] 
**current_balances** | [**CashBalance**](CashBalance.md) |  | [optional] 
**projected_balances** | [**CashBalance**](CashBalance.md) |  | [optional] 

## Example

```python
from openapi_client.models.cash_account import CashAccount

# TODO update the JSON string below
json = "{}"
# create an instance of CashAccount from a JSON string
cash_account_instance = CashAccount.from_json(json)
# print the JSON string representation of the object
print(CashAccount.to_json())

# convert the object into a dict
cash_account_dict = cash_account_instance.to_dict()
# create an instance of CashAccount from a dict
cash_account_from_dict = CashAccount.from_dict(cash_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


