# MarginBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_funds** | **float** |  | [optional] 
**available_funds_non_marginable_trade** | **float** |  | [optional] 
**buying_power** | **float** |  | [optional] 
**buying_power_non_marginable_trade** | **float** |  | [optional] 
**day_trading_buying_power** | **float** |  | [optional] 
**day_trading_buying_power_call** | **float** |  | [optional] 
**equity** | **float** |  | [optional] 
**equity_percentage** | **float** |  | [optional] 
**long_margin_value** | **float** |  | [optional] 
**maintenance_call** | **float** |  | [optional] 
**maintenance_requirement** | **float** |  | [optional] 
**margin_balance** | **float** |  | [optional] 
**reg_t_call** | **float** |  | [optional] 
**short_balance** | **float** |  | [optional] 
**short_margin_value** | **float** |  | [optional] 
**sma** | **float** |  | [optional] 
**is_in_call** | **float** |  | [optional] 
**stock_buying_power** | **float** |  | [optional] 
**option_buying_power** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.margin_balance import MarginBalance

# TODO update the JSON string below
json = "{}"
# create an instance of MarginBalance from a JSON string
margin_balance_instance = MarginBalance.from_json(json)
# print the JSON string representation of the object
print(MarginBalance.to_json())

# convert the object into a dict
margin_balance_dict = margin_balance_instance.to_dict()
# create an instance of MarginBalance from a dict
margin_balance_from_dict = MarginBalance.from_dict(margin_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


