# AccountMutualFund


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_type** | **str** |  | 
**cusip** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**instrument_id** | **int** |  | [optional] 
**net_change** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.account_mutual_fund import AccountMutualFund

# TODO update the JSON string below
json = "{}"
# create an instance of AccountMutualFund from a JSON string
account_mutual_fund_instance = AccountMutualFund.from_json(json)
# print the JSON string representation of the object
print(AccountMutualFund.to_json())

# convert the object into a dict
account_mutual_fund_dict = account_mutual_fund_instance.to_dict()
# create an instance of AccountMutualFund from a dict
account_mutual_fund_from_dict = AccountMutualFund.from_dict(account_mutual_fund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


