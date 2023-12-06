# Query

A Query consists of a node type, a value and l and r Query objects. A Query must have a node type, but other fields are optional depending on the node type. See the description of `node_type`for more information.  For example, the query \"age < 50\" is expressed as:  ``` {   \"node_type\": \"<\",   \"l\": {     \"node_type\": \"column\",     \"value\": \"age\"   },   \"r\": {     \"node_type\": \"unquoted\",     \"value\": 50   } } ``` 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_type** | **str** | Query contents and behavior depends on &#x60;node_type&#x60;:  * &#x60;column&#x60; - column name is in &#x60;value&#x60;  * &#x60;quoted&#x60; - value that needs quotes is in &#x60;value&#x60;  * &#x60;unquoted&#x60; - value that doesn&#39;t need quotes is in &#x60;value&#x60;  * &#x60;&gt;&#x3D;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;AND&#x60;, &#x60;OR&#x60; - &#x60;l&#x60; and &#x60;r&#x60; are used to create the expression &#x60;l&#x60; op &#x60;r&#x60;  * &#x60;SUBQUERY&#x60; - &#x60;l&#x60; is run as a query on the results of query &#x60;r&#x60;  * &#x60;NOT&#x60; - &#x60;l&#x60; is used to create the expression &#x60;NOT l&#x60;  | [optional] 
**value** | **str** |  | [optional] 
**l** | [**Query**](Query.md) |  | [optional] 
**r** | [**Query**](Query.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


