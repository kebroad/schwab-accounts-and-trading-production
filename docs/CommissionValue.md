# CommissionValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**type** | [**FeeType**](FeeType.md) |  | [optional] 

## Example

```python
from openapi_client.models.commission_value import CommissionValue

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionValue from a JSON string
commission_value_instance = CommissionValue.from_json(json)
# print the JSON string representation of the object
print(CommissionValue.to_json())

# convert the object into a dict
commission_value_dict = commission_value_instance.to_dict()
# create an instance of CommissionValue from a dict
commission_value_from_dict = CommissionValue.from_dict(commission_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


