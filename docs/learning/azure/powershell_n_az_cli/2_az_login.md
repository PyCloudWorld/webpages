# Run Azure powershell


* first check the version of your powershell
```cmd
    $PSVersionTable.PSVersionc
```
* ![image_1](images/2_az_login/1.png)



* commands to install Azure Powershell module
```cmd
    Install-Module -Name Az -Repository PSGallery -Force
    Update-Module -Name Az -Force
```

* ![image_1](images/2_az_login/2.png)



### Sign in
* commands to install Azure Powershell module
```cmd
    Connect-AzAccount
```
* ![image_1](images/2_az_login/3.png)


