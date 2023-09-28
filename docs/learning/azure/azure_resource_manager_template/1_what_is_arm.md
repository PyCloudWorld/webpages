# BASIC OF POWERSHELL
Template format
```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "languageVersion": "",
  "contentVersion": "",
  "apiProfile": "",
  "definitions": { },
  "parameters": { },
  "variables": { },
  "functions": [ ],
  "resources": [ ], /* or "resources": { } with languageVersion 2.0 */
  "outputs": { }
}
```

| Element name    | Required | Description                                                                                          |
|-----------------|----------|------------------------------------------------------------------------------------------------------|
| $schema         | 	Yes     | 	Location of the JavaScript Object Notation                                                          |
| languageVersion | 	No      | 	Language version of the template.                                                                   | 
| contentVersion  | 	Yes     | 	Version of the template (such as 1.0.0.0).                                                          |  
| apiProfile      | 	No      | 	An API version that serves as a collection of API versions for resource types.                      |  
| definitions     | 	No      | 	Schemas that are used to validate array and object values.                                          | 
| parameters      | 	No      | 	Values that are provided when deployment is executed to customize resource deployment.              | 
| variables       | 	No      | 	Values that are used as JSON fragments in the template to simplify template language expressions.   | 
| functions       | 	No      | 	User-defined functions that are available within the template.                                      | 
| resources       | 	Yes     | 	Resource types that are deployed or updated in a resource group or subscription.                    | 
| outputs         | 	No      | 	Values that are returned after deployment.                                                          | 