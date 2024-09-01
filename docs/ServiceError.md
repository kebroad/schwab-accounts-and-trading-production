# ServiceError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.service_error import ServiceError

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceError from a JSON string
service_error_instance = ServiceError.from_json(json)
# print the JSON string representation of the object
print(ServiceError.to_json())

# convert the object into a dict
service_error_dict = service_error_instance.to_dict()
# create an instance of ServiceError from a dict
service_error_from_dict = ServiceError.from_dict(service_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


