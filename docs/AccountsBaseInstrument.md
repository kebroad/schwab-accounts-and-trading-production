# AccountsBaseInstrument


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
from openapi_client.models.accounts_base_instrument import AccountsBaseInstrument

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsBaseInstrument from a JSON string
accounts_base_instrument_instance = AccountsBaseInstrument.from_json(json)
# print the JSON string representation of the object
print(AccountsBaseInstrument.to_json())

# convert the object into a dict
accounts_base_instrument_dict = accounts_base_instrument_instance.to_dict()
# create an instance of AccountsBaseInstrument from a dict
accounts_base_instrument_from_dict = AccountsBaseInstrument.from_dict(accounts_base_instrument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


