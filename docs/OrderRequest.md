# OrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session** | [**Session**](Session.md) |  | [optional] 
**duration** | [**Duration**](Duration.md) |  | [optional] 
**order_type** | [**OrderTypeRequest**](OrderTypeRequest.md) |  | [optional] 
**cancel_time** | **datetime** |  | [optional] 
**complex_order_strategy_type** | [**ComplexOrderStrategyType**](ComplexOrderStrategyType.md) |  | [optional] 
**quantity** | **float** |  | [optional] 
**filled_quantity** | **float** |  | [optional] 
**remaining_quantity** | **float** |  | [optional] 
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
**account_number** | **int** |  | [optional] 
**order_activity_collection** | [**List[OrderActivity]**](OrderActivity.md) |  | [optional] 
**replacing_order_collection** | [**List[OrderRequest]**](OrderRequest.md) |  | [optional] 
**child_order_strategies** | [**List[OrderRequest]**](OrderRequest.md) |  | [optional] 
**status_description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.order_request import OrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderRequest from a JSON string
order_request_instance = OrderRequest.from_json(json)
# print the JSON string representation of the object
print(OrderRequest.to_json())

# convert the object into a dict
order_request_dict = order_request_instance.to_dict()
# create an instance of OrderRequest from a dict
order_request_from_dict = OrderRequest.from_dict(order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


