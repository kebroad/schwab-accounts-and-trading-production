# AccountAPIOptionDeliverable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | [optional] 
**deliverable_units** | **float** |  | [optional] 
**api_currency_type** | **str** |  | [optional] 
**asset_type** | [**AssetType**](AssetType.md) |  | [optional] 

## Example

```python
from openapi_client.models.account_api_option_deliverable import AccountAPIOptionDeliverable

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAPIOptionDeliverable from a JSON string
account_api_option_deliverable_instance = AccountAPIOptionDeliverable.from_json(json)
# print the JSON string representation of the object
print(AccountAPIOptionDeliverable.to_json())

# convert the object into a dict
account_api_option_deliverable_dict = account_api_option_deliverable_instance.to_dict()
# create an instance of AccountAPIOptionDeliverable from a dict
account_api_option_deliverable_from_dict = AccountAPIOptionDeliverable.from_dict(account_api_option_deliverable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


