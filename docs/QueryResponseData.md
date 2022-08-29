# QueryResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**query_sql** | **str, none_type** | the generated BigQuery SQL | [optional] 
**total_row_count** | **int, none_type** | the total number of rows in the query. can be null if the query is not complete | [optional] 
**next_url** | **str, none_type** | a URL to use to fetch the next page of data in the query. can be null if the query is not complete | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


