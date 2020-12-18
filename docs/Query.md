# Query

Queries are built up of operators flanked by columns, values or further queries.  For example, the query \"age < 50\" (where age is a column name and not a value) is expressed as:    ```   node_type: \"<\",   l:     node_type: column     value: age   r:     node_type: value     value: 50   ``` 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**l** | [**Query**](Query.md) |  | [optional] 
**r** | [**Query**](Query.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


