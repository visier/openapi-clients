# DataProviderAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adp_auth_params** | [**AdpAuthParamsDTO**](AdpAuthParamsDTO.md) |  | [optional] 
**auth_context** | **str** |  | [optional] 
**bamboo_auth_params** | [**BambooAuthParamsDTO**](BambooAuthParamsDTO.md) |  | [optional] 
**big_query_auth_params** | [**BigQueryAuthParamsDTO**](BigQueryAuthParamsDTO.md) |  | [optional] 
**copy_s3_auth_params** | [**CopyS3AuthParamsDTO**](CopyS3AuthParamsDTO.md) |  | [optional] 
**dayforce_v2_auth_params** | [**DayforceV2AuthParamsDTO**](DayforceV2AuthParamsDTO.md) |  | [optional] 
**dimensions_auth_params** | [**DimensionsAuthParamsDTO**](DimensionsAuthParamsDTO.md) |  | [optional] 
**empty_auth_params** | **object** |  | [optional] 
**fusion_auth_params** | [**FusionAuthParamsDTO**](FusionAuthParamsDTO.md) |  | [optional] 
**gong_auth_params** | [**GongAuthParamsDTO**](GongAuthParamsDTO.md) |  | [optional] 
**google_sheets_auth_params** | [**GoogleSheetsAuthParamsDTO**](GoogleSheetsAuthParamsDTO.md) |  | [optional] 
**google_workspace_auth_params** | [**GoogleWorkspaceAuthParamsDTO**](GoogleWorkspaceAuthParamsDTO.md) |  | [optional] 
**greenhouse_auth_params** | [**GreenhouseAuthParamsDTO**](GreenhouseAuthParamsDTO.md) |  | [optional] 
**has_updates** | **bool** |  | [optional] 
**icims_auth_params** | [**IcimsAuthParamsDTO**](IcimsAuthParamsDTO.md) |  | [optional] 
**internal_s3_auth_params** | [**InternalS3AuthParamsDTO**](InternalS3AuthParamsDTO.md) |  | [optional] 
**jdbc_auth_params** | [**JdbcAuthParamsDTO**](JdbcAuthParamsDTO.md) |  | [optional] 
**jira_auth_params** | [**JiraAuthParamsDTO**](JiraAuthParamsDTO.md) |  | [optional] 
**lever_auth_params** | [**LeverAuthParamsDTO**](LeverAuthParamsDTO.md) |  | [optional] 
**medallia_auth_params** | [**MedalliaAuthParamsDTO**](MedalliaAuthParamsDTO.md) |  | [optional] 
**ms365_auth_params** | [**Microsoft365AuthParamsDTO**](Microsoft365AuthParamsDTO.md) |  | [optional] 
**my_sql_auth_params** | [**MySqlAuthParamsDTO**](MySqlAuthParamsDTO.md) |  | [optional] 
**namely_auth_params** | [**NamelyAuthParamsDTO**](NamelyAuthParamsDTO.md) |  | [optional] 
**oracle_db_auth_params** | [**OracleDbAuthParamsDTO**](OracleDbAuthParamsDTO.md) |  | [optional] 
**provider** | **str** | The data provider associated with the credential.  - Valid values: UKG, Dimensions, Workday, Redshift, BasicS3, CopyS3, SqlServer, Snowflake | [optional] 
**qualtrics_auth_params** | [**QualtricsAuthParamsDTO**](QualtricsAuthParamsDTO.md) |  | [optional] 
**redshift_auth_params** | [**RedshiftAuthParamsDTO**](RedshiftAuthParamsDTO.md) |  | [optional] 
**s3_auth_params** | [**BasicS3AuthParamsDTO**](BasicS3AuthParamsDTO.md) |  | [optional] 
**salesforce_auth_params** | [**SalesforceAuthParamsDTO**](SalesforceAuthParamsDTO.md) |  | [optional] 
**salesforce_v2_auth_params** | [**SalesforceV2AuthParamsDTO**](SalesforceV2AuthParamsDTO.md) |  | [optional] 
**service_now_auth_params** | [**ServiceNowAuthParamsDTO**](ServiceNowAuthParamsDTO.md) |  | [optional] 
**slack_auth_params** | [**SlackAuthParamsDTO**](SlackAuthParamsDTO.md) |  | [optional] 
**snowflake_auth_params** | [**SnowflakeAuthParamsDTO**](SnowflakeAuthParamsDTO.md) |  | [optional] 
**sql_server_auth_params** | [**SqlServerAuthParamsDTO**](SqlServerAuthParamsDTO.md) |  | [optional] 
**success_factors_auth_params** | [**SuccessFactorsAuthParamsDTO**](SuccessFactorsAuthParamsDTO.md) |  | [optional] 
**tenant_domain_name** | **str** |  | [optional] 
**ultimate_auth_params** | [**UltimateAuthParamsDTO**](UltimateAuthParamsDTO.md) |  | [optional] 
**willow_auth_params** | [**WillowAuthParamsDTO**](WillowAuthParamsDTO.md) |  | [optional] 
**workday_auth_params** | [**WorkdayAuthParamsDTO**](WorkdayAuthParamsDTO.md) |  | [optional] 
**workday_raas_auth_params** | [**WorkdayRaasAuthParamsDTO**](WorkdayRaasAuthParamsDTO.md) |  | [optional] 
**zoom_auth_params** | [**ZoomAuthParamsDTO**](ZoomAuthParamsDTO.md) |  | [optional] 

## Example

```python
from visier.api.data_handling.models.data_provider_auth_params_dto import DataProviderAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataProviderAuthParamsDTO from a JSON string
data_provider_auth_params_dto_instance = DataProviderAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(DataProviderAuthParamsDTO.to_json())

# convert the object into a dict
data_provider_auth_params_dto_dict = data_provider_auth_params_dto_instance.to_dict()
# create an instance of DataProviderAuthParamsDTO from a dict
data_provider_auth_params_dto_from_dict = DataProviderAuthParamsDTO.from_dict(data_provider_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


