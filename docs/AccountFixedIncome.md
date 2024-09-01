# AccountFixedIncome


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maturity_date** | **datetime** |  | [optional] 
**factor** | **float** |  | [optional] 
**variable_rate** | **float** |  | [optional] 
**asset_type** | **str** |  | 
**cusip** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**instrument_id** | **int** |  | [optional] 
**net_change** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.account_fixed_income import AccountFixedIncome

# TODO update the JSON string below
json = "{}"
# create an instance of AccountFixedIncome from a JSON string
account_fixed_income_instance = AccountFixedIncome.from_json(json)
# print the JSON string representation of the object
print(AccountFixedIncome.to_json())

# convert the object into a dict
account_fixed_income_dict = account_fixed_income_instance.to_dict()
# create an instance of AccountFixedIncome from a dict
account_fixed_income_from_dict = AccountFixedIncome.from_dict(account_fixed_income_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


