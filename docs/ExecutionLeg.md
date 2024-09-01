# ExecutionLeg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leg_id** | **int** |  | [optional] 
**price** | **float** |  | [optional] 
**quantity** | **float** |  | [optional] 
**mismarked_quantity** | **float** |  | [optional] 
**instrument_id** | **int** |  | [optional] 
**time** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.execution_leg import ExecutionLeg

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionLeg from a JSON string
execution_leg_instance = ExecutionLeg.from_json(json)
# print the JSON string representation of the object
print(ExecutionLeg.to_json())

# convert the object into a dict
execution_leg_dict = execution_leg_instance.to_dict()
# create an instance of ExecutionLeg from a dict
execution_leg_from_dict = ExecutionLeg.from_dict(execution_leg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


