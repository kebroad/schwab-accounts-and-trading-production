# OrderLegCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_leg_type** | **str** |  | [optional] 
**leg_id** | **int** |  | [optional] 
**instrument** | **object** |  | [optional] 
**instruction** | [**Instruction**](Instruction.md) |  | [optional] 
**position_effect** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 
**quantity_type** | **str** |  | [optional] 
**div_cap_gains** | **str** |  | [optional] 
**to_symbol** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.order_leg_collection import OrderLegCollection

# TODO update the JSON string below
json = "{}"
# create an instance of OrderLegCollection from a JSON string
order_leg_collection_instance = OrderLegCollection.from_json(json)
# print the JSON string representation of the object
print(OrderLegCollection.to_json())

# convert the object into a dict
order_leg_collection_dict = order_leg_collection_instance.to_dict()
# create an instance of OrderLegCollection from a dict
order_leg_collection_from_dict = OrderLegCollection.from_dict(order_leg_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


