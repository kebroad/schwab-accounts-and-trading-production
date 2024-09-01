# TransferItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument** | **object** |  | [optional] 
**amount** | **float** |  | [optional] 
**cost** | **float** |  | [optional] 
**price** | **float** |  | [optional] 
**fee_type** | **str** |  | [optional] 
**position_effect** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.transfer_item import TransferItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransferItem from a JSON string
transfer_item_instance = TransferItem.from_json(json)
# print the JSON string representation of the object
print(TransferItem.to_json())

# convert the object into a dict
transfer_item_dict = transfer_item_instance.to_dict()
# create an instance of TransferItem from a dict
transfer_item_from_dict = TransferItem.from_dict(transfer_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


