# TransactionFixedIncome


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**maturity_date** | **datetime** |  | [optional] 
**factor** | **float** |  | [optional] 
**multiplier** | **float** |  | [optional] 
**variable_rate** | **float** |  | [optional] 
**asset_type** | **str** |  | 
**cusip** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**instrument_id** | **int** |  | [optional] 
**net_change** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.transaction_fixed_income import TransactionFixedIncome

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionFixedIncome from a JSON string
transaction_fixed_income_instance = TransactionFixedIncome.from_json(json)
# print the JSON string representation of the object
print(TransactionFixedIncome.to_json())

# convert the object into a dict
transaction_fixed_income_dict = transaction_fixed_income_instance.to_dict()
# create an instance of TransactionFixedIncome from a dict
transaction_fixed_income_from_dict = TransactionFixedIncome.from_dict(transaction_fixed_income_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


