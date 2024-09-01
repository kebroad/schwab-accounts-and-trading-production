# AccountCashEquivalent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**asset_type** | **str** |  | 
**cusip** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**instrument_id** | **int** |  | [optional] 
**net_change** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.account_cash_equivalent import AccountCashEquivalent

# TODO update the JSON string below
json = "{}"
# create an instance of AccountCashEquivalent from a JSON string
account_cash_equivalent_instance = AccountCashEquivalent.from_json(json)
# print the JSON string representation of the object
print(AccountCashEquivalent.to_json())

# convert the object into a dict
account_cash_equivalent_dict = account_cash_equivalent_instance.to_dict()
# create an instance of AccountCashEquivalent from a dict
account_cash_equivalent_from_dict = AccountCashEquivalent.from_dict(account_cash_equivalent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


