# TransactionBaseInstrument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_type** | **str** |  | 
**cusip** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**instrument_id** | **int** |  | [optional] 
**net_change** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.transaction_base_instrument import TransactionBaseInstrument

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionBaseInstrument from a JSON string
transaction_base_instrument_instance = TransactionBaseInstrument.from_json(json)
# print the JSON string representation of the object
print(TransactionBaseInstrument.to_json())

# convert the object into a dict
transaction_base_instrument_dict = transaction_base_instrument_instance.to_dict()
# create an instance of TransactionBaseInstrument from a dict
transaction_base_instrument_from_dict = TransactionBaseInstrument.from_dict(transaction_base_instrument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


