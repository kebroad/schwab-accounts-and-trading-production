# AccountOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option_deliverables** | [**List[AccountAPIOptionDeliverable]**](AccountAPIOptionDeliverable.md) |  | [optional] 
**put_call** | **str** |  | [optional] 
**option_multiplier** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**underlying_symbol** | **str** |  | [optional] 
**asset_type** | **str** |  | 
**cusip** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**instrument_id** | **int** |  | [optional] 
**net_change** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.account_option import AccountOption

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOption from a JSON string
account_option_instance = AccountOption.from_json(json)
# print the JSON string representation of the object
print(AccountOption.to_json())

# convert the object into a dict
account_option_dict = account_option_instance.to_dict()
# create an instance of AccountOption from a dict
account_option_from_dict = AccountOption.from_dict(account_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


