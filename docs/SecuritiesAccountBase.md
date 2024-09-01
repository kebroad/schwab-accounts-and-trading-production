# SecuritiesAccountBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**round_trips** | **int** |  | [optional] 
**is_day_trader** | **bool** |  | [optional] [default to False]
**is_closing_only_restricted** | **bool** |  | [optional] [default to False]
**pfcb_flag** | **bool** |  | [optional] [default to False]
**positions** | [**List[Position]**](Position.md) |  | [optional] 

## Example

```python
from openapi_client.models.securities_account_base import SecuritiesAccountBase

# TODO update the JSON string below
json = "{}"
# create an instance of SecuritiesAccountBase from a JSON string
securities_account_base_instance = SecuritiesAccountBase.from_json(json)
# print the JSON string representation of the object
print(SecuritiesAccountBase.to_json())

# convert the object into a dict
securities_account_base_dict = securities_account_base_instance.to_dict()
# create an instance of SecuritiesAccountBase from a dict
securities_account_base_from_dict = SecuritiesAccountBase.from_dict(securities_account_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


