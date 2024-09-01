# Transaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **int** |  | [optional] 
**time** | **datetime** |  | [optional] 
**user** | [**UserDetails**](UserDetails.md) |  | [optional] 
**description** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**type** | [**TransactionType**](TransactionType.md) |  | [optional] 
**status** | **str** |  | [optional] 
**sub_account** | **str** |  | [optional] 
**trade_date** | **datetime** |  | [optional] 
**settlement_date** | **datetime** |  | [optional] 
**position_id** | **int** |  | [optional] 
**order_id** | **int** |  | [optional] 
**net_amount** | **float** |  | [optional] 
**activity_type** | **str** |  | [optional] 
**transfer_items** | [**List[TransferItem]**](TransferItem.md) |  | [optional] 

## Example

```python
from openapi_client.models.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print(Transaction.to_json())

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_from_dict = Transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


