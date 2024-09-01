# PreviewOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** |  | [optional] 
**order_strategy** | [**OrderStrategy**](OrderStrategy.md) |  | [optional] 
**order_validation_result** | [**OrderValidationResult**](OrderValidationResult.md) |  | [optional] 
**commission_and_fee** | [**CommissionAndFee**](CommissionAndFee.md) |  | [optional] 

## Example

```python
from openapi_client.models.preview_order import PreviewOrder

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewOrder from a JSON string
preview_order_instance = PreviewOrder.from_json(json)
# print the JSON string representation of the object
print(PreviewOrder.to_json())

# convert the object into a dict
preview_order_dict = preview_order_instance.to_dict()
# create an instance of PreviewOrder from a dict
preview_order_from_dict = PreviewOrder.from_dict(preview_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


