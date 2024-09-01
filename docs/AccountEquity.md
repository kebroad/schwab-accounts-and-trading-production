# AccountEquity


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
from openapi_client.models.account_equity import AccountEquity

# TODO update the JSON string below
json = "{}"
# create an instance of AccountEquity from a JSON string
account_equity_instance = AccountEquity.from_json(json)
# print the JSON string representation of the object
print(AccountEquity.to_json())

# convert the object into a dict
account_equity_dict = account_equity_instance.to_dict()
# create an instance of AccountEquity from a dict
account_equity_from_dict = AccountEquity.from_dict(account_equity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


