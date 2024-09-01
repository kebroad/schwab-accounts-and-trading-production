# MarginAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_balances** | [**MarginInitialBalance**](MarginInitialBalance.md) |  | [optional] 
**current_balances** | [**MarginBalance**](MarginBalance.md) |  | [optional] 
**projected_balances** | [**MarginBalance**](MarginBalance.md) |  | [optional] 

## Example

```python
from openapi_client.models.margin_account import MarginAccount

# TODO update the JSON string below
json = "{}"
# create an instance of MarginAccount from a JSON string
margin_account_instance = MarginAccount.from_json(json)
# print the JSON string representation of the object
print(MarginAccount.to_json())

# convert the object into a dict
margin_account_dict = margin_account_instance.to_dict()
# create an instance of MarginAccount from a dict
margin_account_from_dict = MarginAccount.from_dict(margin_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


