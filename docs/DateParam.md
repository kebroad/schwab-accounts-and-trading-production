# DateParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Valid ISO-8601 format is :&lt;br&gt; &lt;code&gt;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&lt;/code&gt; | [optional] 

## Example

```python
from openapi_client.models.date_param import DateParam

# TODO update the JSON string below
json = "{}"
# create an instance of DateParam from a JSON string
date_param_instance = DateParam.from_json(json)
# print the JSON string representation of the object
print(DateParam.to_json())

# convert the object into a dict
date_param_dict = date_param_instance.to_dict()
# create an instance of DateParam from a dict
date_param_from_dict = DateParam.from_dict(date_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


