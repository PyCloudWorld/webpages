# Azure Subscription
when you create azure account you get 2 things
* Azure Subscription 
* Azure Active Directory

## Azure Subscription 
Azure Subscriptions is for billing 
    

## Azure Active Directory
* Azure Active Directory is where you handle users and their identities. 
* also the identities of your applications

## mapping between Subscription and AD 
* one Azure Subscription can only be mapped to one AD Account.
* one Azure Active Directory can be mapped to more than one Azure Subscription account
* ![image_1](images/azure_subscriptions/1.png)
* ![image_2](images/azure_subscriptions/2.PNG)

## how to change the directory for any subscription
* ![image_3](images/azure_subscriptions/3.PNG)

## create a  new user in azure active directory
* ![image_5](images/azure_subscriptions/5.PNG)
* ![image_6](images/azure_subscriptions/6.PNG)
* ![image_7](images/azure_subscriptions/7.PNG)
* ![image_8](images/azure_subscriptions/8.PNG)
* ![image_](images/azure_subscriptions/9.PNG)
* ![image_](images/azure_subscriptions/10.PNG)
* ![image_](images/azure_subscriptions/11.PNG)
* ![image_](images/azure_subscriptions/12.PNG)
* ![image_](images/azure_subscriptions/13.PNG)
* ![image_](images/azure_subscriptions/14.PNG)
* ![image_](images/azure_subscriptions/15.PNG)
* ![image_](images/azure_subscriptions/16.PNG)

## create storage account by Main User <ashish> and give Reader Access to UserA

### create Storage Account
![image_](images/azure_subscriptions/17.PNG)
![image_](images/azure_subscriptions/18.PNG)
![image_](images/azure_subscriptions/19.PNG)
![image_](images/azure_subscriptions/20.PNG)
![image_](images/azure_subscriptions/21.PNG)
![image_](images/azure_subscriptions/22.PNG)
![image_](images/azure_subscriptions/23.PNG)
![image_](images/azure_subscriptions/24.PNG)
![image_](images/azure_subscriptions/25.PNG)
![image_](images/azure_subscriptions/26.PNG)
![image_](images/azure_subscriptions/27.PNG)
![image_](images/azure_subscriptions/28.PNG)
![image_](images/azure_subscriptions/29.PNG)
![image_](images/azure_subscriptions/30.PNG)
![image_](images/azure_subscriptions/31.PNG)
![image_](images/azure_subscriptions/32.PNG)
![image_](images/azure_subscriptions/33.PNG)
![image_](images/azure_subscriptions/34.PNG)
![image_](images/azure_subscriptions/35.PNG)
![image_](images/azure_subscriptions/36.PNG)

### check if the userA have access, it should not be able to access
![image_](images/azure_subscriptions/37.PNG)

### grant access at storage level (reader access only)
![image_](images/azure_subscriptions/38.PNG)
![image_](images/azure_subscriptions/39.PNG)
![image_](images/azure_subscriptions/40.PNG)
![image_](images/azure_subscriptions/41.PNG)
![image_](images/azure_subscriptions/42.PNG)
![image_](images/azure_subscriptions/43.PNG)
![image_](images/azure_subscriptions/44.PNG)
![image_](images/azure_subscriptions/45.PNG)
![image_](images/azure_subscriptions/46.PNG)

### check if the userA have access, it should have access
![image_](images/azure_subscriptions/47.PNG)
![image_](images/azure_subscriptions/48.PNG)

## provide acces at Resource Group Level

### create a vm in Resource Group and create VM
![image_](images/azure_subscriptions/49.PNG)
![image_](images/azure_subscriptions/50.PNG)
![image_](images/azure_subscriptions/51.PNG)
![image_](images/azure_subscriptions/52.PNG)
![image_](images/azure_subscriptions/53.PNG)
![image_](images/azure_subscriptions/54.PNG)
![image_](images/azure_subscriptions/55.PNG)

### give Reader access to VM only
![image_](images/azure_subscriptions/57.PNG)
![image_](images/azure_subscriptions/58.PNG)
![image_](images/azure_subscriptions/59.PNG)
![image_](images/azure_subscriptions/60.PNG)
![image_](images/azure_subscriptions/61.PNG)
![image_](images/azure_subscriptions/62.PNG)
![image_](images/azure_subscriptions/63.PNG)
![image_](images/azure_subscriptions/64.PNG)
![image_](images/azure_subscriptions/65.PNG)

### check if user can see all components related to VM
![image_](images/azure_subscriptions/66.PNG)
![image_](images/azure_subscriptions/67.PNG)
![image_](images/azure_subscriptions/68.PNG)
![image_](images/azure_subscriptions/69.PNG)

### give Reader access at Resource Group Level
![image_](images/azure_subscriptions/70.PNG)
![image_](images/azure_subscriptions/71.PNG)
![image_](images/azure_subscriptions/72.PNG)
![image_](images/azure_subscriptions/73.PNG)
![image_](images/azure_subscriptions/74.PNG)
![image_](images/azure_subscriptions/75.PNG)
![image_](images/azure_subscriptions/76.PNG)
![image_](images/azure_subscriptions/77.PNG)

### check if user have access and  what type
![image_](images/azure_subscriptions/78.PNG)
![image_](images/azure_subscriptions/79.PNG)
![image_](images/azure_subscriptions/80.PNG)
![image_](images/azure_subscriptions/81.PNG)
![image_](images/azure_subscriptions/82.PNG)


## Difference
* Reader
  * only read access. cant perform actions
* Contributor
  * Read + start stop and perform action. can't provider access to others
* User Access Administrator
  * Read + start stop and perform action + can provider access to others
* Owner
  * have complete access to start, stop, create, provide access to others
