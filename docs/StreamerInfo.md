# StreamerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**streamer_socket_url** | **str** |  | [optional] 
**schwab_client_customer_id** | **str** |  | [optional] 
**schwab_client_correl_id** | **str** |  | [optional] 
**schwab_client_channel** | **str** |  | [optional] 
**schwab_client_function_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.streamer_info import StreamerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StreamerInfo from a JSON string
streamer_info_instance = StreamerInfo.from_json(json)
# print the JSON string representation of the object
print(StreamerInfo.to_json())

# convert the object into a dict
streamer_info_dict = streamer_info_instance.to_dict()
# create an instance of StreamerInfo from a dict
streamer_info_from_dict = StreamerInfo.from_dict(streamer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


