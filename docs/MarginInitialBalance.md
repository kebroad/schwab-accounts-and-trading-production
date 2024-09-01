# MarginInitialBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accrued_interest** | **float** |  | [optional] 
**available_funds_non_marginable_trade** | **float** |  | [optional] 
**bond_value** | **float** |  | [optional] 
**buying_power** | **float** |  | [optional] 
**cash_balance** | **float** |  | [optional] 
**cash_available_for_trading** | **float** |  | [optional] 
**cash_receipts** | **float** |  | [optional] 
**day_trading_buying_power** | **float** |  | [optional] 
**day_trading_buying_power_call** | **float** |  | [optional] 
**day_trading_equity_call** | **float** |  | [optional] 
**equity** | **float** |  | [optional] 
**equity_percentage** | **float** |  | [optional] 
**liquidation_value** | **float** |  | [optional] 
**long_margin_value** | **float** |  | [optional] 
**long_option_market_value** | **float** |  | [optional] 
**long_stock_value** | **float** |  | [optional] 
**maintenance_call** | **float** |  | [optional] 
**maintenance_requirement** | **float** |  | [optional] 
**margin** | **float** |  | [optional] 
**margin_equity** | **float** |  | [optional] 
**money_market_fund** | **float** |  | [optional] 
**mutual_fund_value** | **float** |  | [optional] 
**reg_t_call** | **float** |  | [optional] 
**short_margin_value** | **float** |  | [optional] 
**short_option_market_value** | **float** |  | [optional] 
**short_stock_value** | **float** |  | [optional] 
**total_cash** | **float** |  | [optional] 
**is_in_call** | **float** |  | [optional] 
**unsettled_cash** | **float** |  | [optional] 
**pending_deposits** | **float** |  | [optional] 
**margin_balance** | **float** |  | [optional] 
**short_balance** | **float** |  | [optional] 
**account_value** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.margin_initial_balance import MarginInitialBalance

# TODO update the JSON string below
json = "{}"
# create an instance of MarginInitialBalance from a JSON string
margin_initial_balance_instance = MarginInitialBalance.from_json(json)
# print the JSON string representation of the object
print(MarginInitialBalance.to_json())

# convert the object into a dict
margin_initial_balance_dict = margin_initial_balance_instance.to_dict()
# create an instance of MarginInitialBalance from a dict
margin_initial_balance_from_dict = MarginInitialBalance.from_dict(margin_initial_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


