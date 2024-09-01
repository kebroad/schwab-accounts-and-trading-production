# Fees


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_legs** | [**List[FeeLeg]**](FeeLeg.md) |  | [optional] 

## Example

```python
from openapi_client.models.fees import Fees

# TODO update the JSON string below
json = "{}"
# create an instance of Fees from a JSON string
fees_instance = Fees.from_json(json)
# print the JSON string representation of the object
print(Fees.to_json())

# convert the object into a dict
fees_dict = fees_instance.to_dict()
# create an instance of Fees from a dict
fees_from_dict = Fees.from_dict(fees_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


