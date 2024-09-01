# Order


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session** | [**Session**](Session.md) |  | [optional] 
**duration** | [**Duration**](Duration.md) |  | [optional] 
**order_type** | [**OrderType**](OrderType.md) |  | [optional] 
**cancel_time** | **datetime** |  | [optional] 
**complex_order_strategy_type** | [**ComplexOrderStrategyType**](ComplexOrderStrategyType.md) |  | [optional] 
**quantity** | **float** |  | [optional] 
**filled_quantity** | **float** |  | [optional] 
**remaining_quantity** | **float** |  | [optional] 
**requested_destination** | [**RequestedDestination**](RequestedDestination.md) |  | [optional] 
**destination_link_name** | **str** |  | [optional] 
**release_time** | **datetime** |  | [optional] 
**stop_price** | **float** |  | [optional] 
**stop_price_link_basis** | [**StopPriceLinkBasis**](StopPriceLinkBasis.md) |  | [optional] 
**stop_price_link_type** | [**StopPriceLinkType**](StopPriceLinkType.md) |  | [optional] 
**stop_price_offset** | **float** |  | [optional] 
**stop_type** | [**StopType**](StopType.md) |  | [optional] 
**price_link_basis** | [**PriceLinkBasis**](PriceLinkBasis.md) |  | [optional] 
**price_link_type** | [**PriceLinkType**](PriceLinkType.md) |  | [optional] 
**price** | **float** |  | [optional] 
**tax_lot_method** | [**TaxLotMethod**](TaxLotMethod.md) |  | [optional] 
**order_leg_collection** | [**List[OrderLegCollection]**](OrderLegCollection.md) |  | [optional] 
**activation_price** | **float** |  | [optional] 
**special_instruction** | [**SpecialInstruction**](SpecialInstruction.md) |  | [optional] 
**order_strategy_type** | [**OrderStrategyType**](OrderStrategyType.md) |  | [optional] 
**order_id** | **int** |  | [optional] 
**cancelable** | **bool** |  | [optional] [default to False]
**editable** | **bool** |  | [optional] [default to False]
**status** | [**Status**](Status.md) |  | [optional] 
**entered_time** | **datetime** |  | [optional] 
**close_time** | **datetime** |  | [optional] 
**tag** | **str** |  | [optional] 
**account_number** | **int** |  | [optional] 
**order_activity_collection** | [**List[OrderActivity]**](OrderActivity.md) |  | [optional] 
**replacing_order_collection** | [**List[Order]**](Order.md) |  | [optional] 
**child_order_strategies** | [**List[Order]**](Order.md) |  | [optional] 
**status_description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


