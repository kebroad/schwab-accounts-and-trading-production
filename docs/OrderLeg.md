# OrderLeg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ask_price** | **float** |  | [optional] 
**bid_price** | **float** |  | [optional] 
**last_price** | **float** |  | [optional] 
**mark_price** | **float** |  | [optional] 
**projected_commission** | **float** |  | [optional] 
**quantity** | **float** |  | [optional] 
**final_symbol** | **str** |  | [optional] 
**leg_id** | **float** |  | [optional] 
**asset_type** | [**AssetType**](AssetType.md) |  | [optional] 
**instruction** | [**Instruction**](Instruction.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_leg import OrderLeg

# TODO update the JSON string below
json = "{}"
# create an instance of OrderLeg from a JSON string
order_leg_instance = OrderLeg.from_json(json)
# print the JSON string representation of the object
print(OrderLeg.to_json())

# convert the object into a dict
order_leg_dict = order_leg_instance.to_dict()
# create an instance of OrderLeg from a dict
order_leg_from_dict = OrderLeg.from_dict(order_leg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


