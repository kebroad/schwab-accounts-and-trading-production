# CommissionLeg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commission_values** | [**List[CommissionValue]**](CommissionValue.md) |  | [optional] 

## Example

```python
from openapi_client.models.commission_leg import CommissionLeg

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionLeg from a JSON string
commission_leg_instance = CommissionLeg.from_json(json)
# print the JSON string representation of the object
print(CommissionLeg.to_json())

# convert the object into a dict
commission_leg_dict = commission_leg_instance.to_dict()
# create an instance of CommissionLeg from a dict
commission_leg_from_dict = CommissionLeg.from_dict(commission_leg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


