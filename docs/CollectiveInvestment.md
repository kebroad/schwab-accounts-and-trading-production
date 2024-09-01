# CollectiveInvestment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**asset_type** | **str** |  | 
**cusip** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**instrument_id** | **int** |  | [optional] 
**net_change** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.collective_investment import CollectiveInvestment

# TODO update the JSON string below
json = "{}"
# create an instance of CollectiveInvestment from a JSON string
collective_investment_instance = CollectiveInvestment.from_json(json)
# print the JSON string representation of the object
print(CollectiveInvestment.to_json())

# convert the object into a dict
collective_investment_dict = collective_investment_instance.to_dict()
# create an instance of CollectiveInvestment from a dict
collective_investment_from_dict = CollectiveInvestment.from_dict(collective_investment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


