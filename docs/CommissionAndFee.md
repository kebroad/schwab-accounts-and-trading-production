# CommissionAndFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commission** | [**Commission**](Commission.md) |  | [optional] 
**fee** | [**Fees**](Fees.md) |  | [optional] 
**true_commission** | [**Commission**](Commission.md) |  | [optional] 

## Example

```python
from openapi_client.models.commission_and_fee import CommissionAndFee

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionAndFee from a JSON string
commission_and_fee_instance = CommissionAndFee.from_json(json)
# print the JSON string representation of the object
print(CommissionAndFee.to_json())

# convert the object into a dict
commission_and_fee_dict = commission_and_fee_instance.to_dict()
# create an instance of CommissionAndFee from a dict
commission_and_fee_from_dict = CommissionAndFee.from_dict(commission_and_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


