# TransactionAPIOptionDeliverable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_symbol** | **str** |  | [optional] 
**strike_percent** | **int** |  | [optional] 
**deliverable_number** | **int** |  | [optional] 
**deliverable_units** | **float** |  | [optional] 
**deliverable** | **object** |  | [optional] 
**asset_type** | [**AssetType**](AssetType.md) |  | [optional] 

## Example

```python
from openapi_client.models.transaction_api_option_deliverable import TransactionAPIOptionDeliverable

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionAPIOptionDeliverable from a JSON string
transaction_api_option_deliverable_instance = TransactionAPIOptionDeliverable.from_json(json)
# print the JSON string representation of the object
print(TransactionAPIOptionDeliverable.to_json())

# convert the object into a dict
transaction_api_option_deliverable_dict = transaction_api_option_deliverable_instance.to_dict()
# create an instance of TransactionAPIOptionDeliverable from a dict
transaction_api_option_deliverable_from_dict = TransactionAPIOptionDeliverable.from_dict(transaction_api_option_deliverable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


