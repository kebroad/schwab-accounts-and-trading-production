# TransactionOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration_date** | **datetime** |  | [optional] 
**option_deliverables** | [**List[TransactionAPIOptionDeliverable]**](TransactionAPIOptionDeliverable.md) |  | [optional] 
**option_premium_multiplier** | **int** |  | [optional] 
**put_call** | **str** |  | [optional] 
**strike_price** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**underlying_symbol** | **str** |  | [optional] 
**underlying_cusip** | **str** |  | [optional] 
**deliverable** | **object** |  | [optional] 
**asset_type** | **str** |  | 
**cusip** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**instrument_id** | **int** |  | [optional] 
**net_change** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.transaction_option import TransactionOption

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionOption from a JSON string
transaction_option_instance = TransactionOption.from_json(json)
# print the JSON string representation of the object
print(TransactionOption.to_json())

# convert the object into a dict
transaction_option_dict = transaction_option_instance.to_dict()
# create an instance of TransactionOption from a dict
transaction_option_from_dict = TransactionOption.from_dict(transaction_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


