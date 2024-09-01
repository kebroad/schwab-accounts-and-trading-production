# OrderActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | **str** |  | [optional] 
**execution_type** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 
**order_remaining_quantity** | **float** |  | [optional] 
**execution_legs** | [**List[ExecutionLeg]**](ExecutionLeg.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_activity import OrderActivity

# TODO update the JSON string below
json = "{}"
# create an instance of OrderActivity from a JSON string
order_activity_instance = OrderActivity.from_json(json)
# print the JSON string representation of the object
print(OrderActivity.to_json())

# convert the object into a dict
order_activity_dict = order_activity_instance.to_dict()
# create an instance of OrderActivity from a dict
order_activity_from_dict = OrderActivity.from_dict(order_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


