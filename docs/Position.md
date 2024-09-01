# Position


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_quantity** | **float** |  | [optional] 
**average_price** | **float** |  | [optional] 
**current_day_profit_loss** | **float** |  | [optional] 
**current_day_profit_loss_percentage** | **float** |  | [optional] 
**long_quantity** | **float** |  | [optional] 
**settled_long_quantity** | **float** |  | [optional] 
**settled_short_quantity** | **float** |  | [optional] 
**aged_quantity** | **float** |  | [optional] 
**instrument** | **object** |  | [optional] 
**market_value** | **float** |  | [optional] 
**maintenance_requirement** | **float** |  | [optional] 
**average_long_price** | **float** |  | [optional] 
**average_short_price** | **float** |  | [optional] 
**tax_lot_average_long_price** | **float** |  | [optional] 
**tax_lot_average_short_price** | **float** |  | [optional] 
**long_open_profit_loss** | **float** |  | [optional] 
**short_open_profit_loss** | **float** |  | [optional] 
**previous_session_long_quantity** | **float** |  | [optional] 
**previous_session_short_quantity** | **float** |  | [optional] 
**current_day_cost** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.position import Position

# TODO update the JSON string below
json = "{}"
# create an instance of Position from a JSON string
position_instance = Position.from_json(json)
# print the JSON string representation of the object
print(Position.to_json())

# convert the object into a dict
position_dict = position_instance.to_dict()
# create an instance of Position from a dict
position_from_dict = Position.from_dict(position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


