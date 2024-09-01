# AccountNumberHash


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**hash_value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.account_number_hash import AccountNumberHash

# TODO update the JSON string below
json = "{}"
# create an instance of AccountNumberHash from a JSON string
account_number_hash_instance = AccountNumberHash.from_json(json)
# print the JSON string representation of the object
print(AccountNumberHash.to_json())

# convert the object into a dict
account_number_hash_dict = account_number_hash_instance.to_dict()
# create an instance of AccountNumberHash from a dict
account_number_hash_from_dict = AccountNumberHash.from_dict(account_number_hash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


