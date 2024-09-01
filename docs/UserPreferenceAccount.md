# UserPreferenceAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**primary_account** | **bool** |  | [optional] [default to False]
**type** | **str** |  | [optional] 
**nick_name** | **str** |  | [optional] 
**account_color** | **str** | Green | Blue | [optional] 
**display_acct_id** | **str** |  | [optional] 
**auto_position_effect** | **bool** |  | [optional] [default to False]

## Example

```python
from openapi_client.models.user_preference_account import UserPreferenceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of UserPreferenceAccount from a JSON string
user_preference_account_instance = UserPreferenceAccount.from_json(json)
# print the JSON string representation of the object
print(UserPreferenceAccount.to_json())

# convert the object into a dict
user_preference_account_dict = user_preference_account_instance.to_dict()
# create an instance of UserPreferenceAccount from a dict
user_preference_account_from_dict = UserPreferenceAccount.from_dict(user_preference_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


