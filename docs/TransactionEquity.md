# TransactionEquity


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
from openapi_client.models.transaction_equity import TransactionEquity

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionEquity from a JSON string
transaction_equity_instance = TransactionEquity.from_json(json)
# print the JSON string representation of the object
print(TransactionEquity.to_json())

# convert the object into a dict
transaction_equity_dict = transaction_equity_instance.to_dict()
# create an instance of TransactionEquity from a dict
transaction_equity_from_dict = TransactionEquity.from_dict(transaction_equity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


