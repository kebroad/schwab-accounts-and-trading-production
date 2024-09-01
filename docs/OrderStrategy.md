# OrderStrategy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**advanced_order_type** | **str** |  | [optional] 
**close_time** | **datetime** |  | [optional] 
**entered_time** | **datetime** |  | [optional] 
**order_balance** | [**OrderBalance**](OrderBalance.md) |  | [optional] 
**order_strategy_type** | [**OrderStrategyType**](OrderStrategyType.md) |  | [optional] 
**order_version** | **float** |  | [optional] 
**session** | [**Session**](Session.md) |  | [optional] 
**status** | [**ApiOrderStatus**](ApiOrderStatus.md) |  | [optional] 
**all_or_none** | **bool** |  | [optional] 
**discretionary** | **bool** |  | [optional] 
**duration** | [**Duration**](Duration.md) |  | [optional] 
**filled_quantity** | **float** |  | [optional] 
**order_type** | [**OrderType**](OrderType.md) |  | [optional] 
**order_value** | **float** |  | [optional] 
**price** | **float** |  | [optional] 
**quantity** | **float** |  | [optional] 
**remaining_quantity** | **float** |  | [optional] 
**sell_non_marginable_first** | **bool** |  | [optional] 
**settlement_instruction** | [**SettlementInstruction**](SettlementInstruction.md) |  | [optional] 
**strategy** | [**ComplexOrderStrategyType**](ComplexOrderStrategyType.md) |  | [optional] 
**amount_indicator** | [**AmountIndicator**](AmountIndicator.md) |  | [optional] 
**order_legs** | [**List[OrderLeg]**](OrderLeg.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_strategy import OrderStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of OrderStrategy from a JSON string
order_strategy_instance = OrderStrategy.from_json(json)
# print the JSON string representation of the object
print(OrderStrategy.to_json())

# convert the object into a dict
order_strategy_dict = order_strategy_instance.to_dict()
# create an instance of OrderStrategy from a dict
order_strategy_from_dict = OrderStrategy.from_dict(order_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


