# UserPreference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[UserPreferenceAccount]**](UserPreferenceAccount.md) |  | [optional] 
**streamer_info** | [**List[StreamerInfo]**](StreamerInfo.md) |  | [optional] 
**offers** | [**List[Offer]**](Offer.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_preference import UserPreference

# TODO update the JSON string below
json = "{}"
# create an instance of UserPreference from a JSON string
user_preference_instance = UserPreference.from_json(json)
# print the JSON string representation of the object
print(UserPreference.to_json())

# convert the object into a dict
user_preference_dict = user_preference_instance.to_dict()
# create an instance of UserPreference from a dict
user_preference_from_dict = UserPreference.from_dict(user_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


