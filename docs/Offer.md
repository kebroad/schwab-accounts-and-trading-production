# Offer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level2_permissions** | **bool** |  | [optional] [default to False]
**mkt_data_permission** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.offer import Offer

# TODO update the JSON string below
json = "{}"
# create an instance of Offer from a JSON string
offer_instance = Offer.from_json(json)
# print the JSON string representation of the object
print(Offer.to_json())

# convert the object into a dict
offer_dict = offer_instance.to_dict()
# create an instance of Offer from a dict
offer_from_dict = Offer.from_dict(offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


