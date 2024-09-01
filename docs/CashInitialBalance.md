# CashInitialBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accrued_interest** | **float** |  | [optional] 
**cash_available_for_trading** | **float** |  | [optional] 
**cash_available_for_withdrawal** | **float** |  | [optional] 
**cash_balance** | **float** |  | [optional] 
**bond_value** | **float** |  | [optional] 
**cash_receipts** | **float** |  | [optional] 
**liquidation_value** | **float** |  | [optional] 
**long_option_market_value** | **float** |  | [optional] 
**long_stock_value** | **float** |  | [optional] 
**money_market_fund** | **float** |  | [optional] 
**mutual_fund_value** | **float** |  | [optional] 
**short_option_market_value** | **float** |  | [optional] 
**short_stock_value** | **float** |  | [optional] 
**is_in_call** | **float** |  | [optional] 
**unsettled_cash** | **float** |  | [optional] 
**cash_debit_call_value** | **float** |  | [optional] 
**pending_deposits** | **float** |  | [optional] 
**account_value** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.cash_initial_balance import CashInitialBalance

# TODO update the JSON string below
json = "{}"
# create an instance of CashInitialBalance from a JSON string
cash_initial_balance_instance = CashInitialBalance.from_json(json)
# print the JSON string representation of the object
print(CashInitialBalance.to_json())

# convert the object into a dict
cash_initial_balance_dict = cash_initial_balance_instance.to_dict()
# create an instance of CashInitialBalance from a dict
cash_initial_balance_from_dict = CashInitialBalance.from_dict(cash_initial_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


