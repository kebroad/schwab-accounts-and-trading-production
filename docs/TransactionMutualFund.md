# TransactionMutualFund


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_family_name** | **str** |  | [optional] 
**fund_family_symbol** | **str** |  | [optional] 
**fund_group** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**exchange_cutoff_time** | **datetime** |  | [optional] 
**purchase_cutoff_time** | **datetime** |  | [optional] 
**redemption_cutoff_time** | **datetime** |  | [optional] 
**asset_type** | **str** |  | 
**cusip** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**instrument_id** | **int** |  | [optional] 
**net_change** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.transaction_mutual_fund import TransactionMutualFund

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMutualFund from a JSON string
transaction_mutual_fund_instance = TransactionMutualFund.from_json(json)
# print the JSON string representation of the object
print(TransactionMutualFund.to_json())

# convert the object into a dict
transaction_mutual_fund_dict = transaction_mutual_fund_instance.to_dict()
# create an instance of TransactionMutualFund from a dict
transaction_mutual_fund_from_dict = TransactionMutualFund.from_dict(transaction_mutual_fund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


