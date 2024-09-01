# OrderBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_value** | **float** |  | [optional] 
**projected_available_fund** | **float** |  | [optional] 
**projected_buying_power** | **float** |  | [optional] 
**projected_commission** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.order_balance import OrderBalance

# TODO update the JSON string below
json = "{}"
# create an instance of OrderBalance from a JSON string
order_balance_instance = OrderBalance.from_json(json)
# print the JSON string representation of the object
print(OrderBalance.to_json())

# convert the object into a dict
order_balance_dict = order_balance_instance.to_dict()
# create an instance of OrderBalance from a dict
order_balance_from_dict = OrderBalance.from_dict(order_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


