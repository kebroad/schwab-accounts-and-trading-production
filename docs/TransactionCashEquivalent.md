# TransactionCashEquivalent


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
from openapi_client.models.transaction_cash_equivalent import TransactionCashEquivalent

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCashEquivalent from a JSON string
transaction_cash_equivalent_instance = TransactionCashEquivalent.from_json(json)
# print the JSON string representation of the object
print(TransactionCashEquivalent.to_json())

# convert the object into a dict
transaction_cash_equivalent_dict = transaction_cash_equivalent_instance.to_dict()
# create an instance of TransactionCashEquivalent from a dict
transaction_cash_equivalent_from_dict = TransactionCashEquivalent.from_dict(transaction_cash_equivalent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


