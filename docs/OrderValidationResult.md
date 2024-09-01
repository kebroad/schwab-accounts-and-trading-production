# OrderValidationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**List[OrderValidationDetail]**](OrderValidationDetail.md) |  | [optional] 
**accepts** | [**List[OrderValidationDetail]**](OrderValidationDetail.md) |  | [optional] 
**rejects** | [**List[OrderValidationDetail]**](OrderValidationDetail.md) |  | [optional] 
**reviews** | [**List[OrderValidationDetail]**](OrderValidationDetail.md) |  | [optional] 
**warns** | [**List[OrderValidationDetail]**](OrderValidationDetail.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_validation_result import OrderValidationResult

# TODO update the JSON string below
json = "{}"
# create an instance of OrderValidationResult from a JSON string
order_validation_result_instance = OrderValidationResult.from_json(json)
# print the JSON string representation of the object
print(OrderValidationResult.to_json())

# convert the object into a dict
order_validation_result_dict = order_validation_result_instance.to_dict()
# create an instance of OrderValidationResult from a dict
order_validation_result_from_dict = OrderValidationResult.from_dict(order_validation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


