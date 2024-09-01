# FeeValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**type** | [**FeeType**](FeeType.md) |  | [optional] 

## Example

```python
from openapi_client.models.fee_value import FeeValue

# TODO update the JSON string below
json = "{}"
# create an instance of FeeValue from a JSON string
fee_value_instance = FeeValue.from_json(json)
# print the JSON string representation of the object
print(FeeValue.to_json())

# convert the object into a dict
fee_value_dict = fee_value_instance.to_dict()
# create an instance of FeeValue from a dict
fee_value_from_dict = FeeValue.from_dict(fee_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


