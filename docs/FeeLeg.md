# FeeLeg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_values** | [**List[FeeValue]**](FeeValue.md) |  | [optional] 

## Example

```python
from openapi_client.models.fee_leg import FeeLeg

# TODO update the JSON string below
json = "{}"
# create an instance of FeeLeg from a JSON string
fee_leg_instance = FeeLeg.from_json(json)
# print the JSON string representation of the object
print(FeeLeg.to_json())

# convert the object into a dict
fee_leg_dict = fee_leg_instance.to_dict()
# create an instance of FeeLeg from a dict
fee_leg_from_dict = FeeLeg.from_dict(fee_leg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


