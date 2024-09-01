# OrderValidationDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_rule_name** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**activity_message** | **str** |  | [optional] 
**original_severity** | [**APIRuleAction**](APIRuleAction.md) |  | [optional] 
**override_name** | **str** |  | [optional] 
**override_severity** | [**APIRuleAction**](APIRuleAction.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_validation_detail import OrderValidationDetail

# TODO update the JSON string below
json = "{}"
# create an instance of OrderValidationDetail from a JSON string
order_validation_detail_instance = OrderValidationDetail.from_json(json)
# print the JSON string representation of the object
print(OrderValidationDetail.to_json())

# convert the object into a dict
order_validation_detail_dict = order_validation_detail_instance.to_dict()
# create an instance of OrderValidationDetail from a dict
order_validation_detail_from_dict = OrderValidationDetail.from_dict(order_validation_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


