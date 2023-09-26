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
* ![image_2](images/azure_subscriptions/2.png)

## how to change the directory for any subscription
* ![image_3](images/azure_subscriptions/3.png)

## create a  new user in azure active directory
* ![image_5](images/azure_subscriptions/5.png)
* ![image_6](images/azure_subscriptions/6.png)
* ![image_7](images/azure_subscriptions/7.png)
* ![image_8](images/azure_subscriptions/8.png)
* ![image_](images/azure_subscriptions/9.png)
* ![image_](images/azure_subscriptions/10.png)
* ![image_](images/azure_subscriptions/11.png)
* ![image_](images/azure_subscriptions/12.png)
* ![image_](images/azure_subscriptions/13.png)
* ![image_](images/azure_subscriptions/14.png)
* ![image_](images/azure_subscriptions/15.png)
* ![image_](images/azure_subscriptions/16.png)

## create storage account by Main User <ashish> and give Reader Access to UserA

### create Storage Account
![image_](images/azure_subscriptions/17.png)
![image_](images/azure_subscriptions/18.png)
![image_](images/azure_subscriptions/19.png)
![image_](images/azure_subscriptions/20.png)
![image_](images/azure_subscriptions/21.png)
![image_](images/azure_subscriptions/22.png)
![image_](images/azure_subscriptions/23.png)
![image_](images/azure_subscriptions/24.png)
![image_](images/azure_subscriptions/25.png)
![image_](images/azure_subscriptions/26.png)
![image_](images/azure_subscriptions/27.png)
![image_](images/azure_subscriptions/28.png)
![image_](images/azure_subscriptions/29.png)
![image_](images/azure_subscriptions/30.png)
![image_](images/azure_subscriptions/31.png)
![image_](images/azure_subscriptions/32.png)
![image_](images/azure_subscriptions/33.png)
![image_](images/azure_subscriptions/34.png)
![image_](images/azure_subscriptions/35.png)
![image_](images/azure_subscriptions/36.png)

### check if the userA have access, it should not be able to access
![image_](images/azure_subscriptions/37.png)

### grant access at storage level (reader access only)
![image_](images/azure_subscriptions/38.png)
![image_](images/azure_subscriptions/39.png)
![image_](images/azure_subscriptions/40.png)
![image_](images/azure_subscriptions/41.png)
![image_](images/azure_subscriptions/42.png)
![image_](images/azure_subscriptions/43.png)
![image_](images/azure_subscriptions/44.png)
![image_](images/azure_subscriptions/45.png)
![image_](images/azure_subscriptions/46.png)

### check if the userA have access, it should have access
![image_](images/azure_subscriptions/47.png)
![image_](images/azure_subscriptions/48.png)

## provide acces at Resource Group Level

### create a vm in Resource Group and create VM
![image_](images/azure_subscriptions/49.png)
![image_](images/azure_subscriptions/50.png)
![image_](images/azure_subscriptions/51.png)
![image_](images/azure_subscriptions/52.png)
![image_](images/azure_subscriptions/53.png)
![image_](images/azure_subscriptions/54.png)
![image_](images/azure_subscriptions/55.png)

### give Reader access to VM only
![image_](images/azure_subscriptions/57.png)
![image_](images/azure_subscriptions/58.png)
![image_](images/azure_subscriptions/59.png)
![image_](images/azure_subscriptions/60.png)
![image_](images/azure_subscriptions/61.png)
![image_](images/azure_subscriptions/62.png)
![image_](images/azure_subscriptions/63.png)
![image_](images/azure_subscriptions/64.png)
![image_](images/azure_subscriptions/65.png)

### check if user can see all components related to VM
![image_](images/azure_subscriptions/66.png)
![image_](images/azure_subscriptions/67.png)
![image_](images/azure_subscriptions/68.png)
![image_](images/azure_subscriptions/69.png)

### give Reader access at Resource Group Level
![image_](images/azure_subscriptions/70.png)
![image_](images/azure_subscriptions/71.png)
![image_](images/azure_subscriptions/72.png)
![image_](images/azure_subscriptions/73.png)
![image_](images/azure_subscriptions/74.png)
![image_](images/azure_subscriptions/75.png)
![image_](images/azure_subscriptions/76.png)
![image_](images/azure_subscriptions/77.png)

### check if user have access and  what type
![image_](images/azure_subscriptions/78.png)
![image_](images/azure_subscriptions/79.png)
![image_](images/azure_subscriptions/80.png)
![image_](images/azure_subscriptions/81.png)
![image_](images/azure_subscriptions/82.png)


## Difference
* Reader
  * only read access. cant perform actions
* Contributor
  * Read + start stop and perform action. can't provider access to others
* User Access Administrator
  * Read + start stop and perform action + can provider access to others
* Owner
  * have complete access to start, stop, create, provide access to others


## create custom role
![image_](images/azure_subscriptions/83.png)
![image_](images/azure_subscriptions/84.png)
![image_](images/azure_subscriptions/85.png)
![image_](images/azure_subscriptions/86.png)
![image_](images/azure_subscriptions/87.png)
![image_](images/azure_subscriptions/88.png)
![image_](images/azure_subscriptions/89.png)
![image_](images/azure_subscriptions/90.png)
![image_](images/azure_subscriptions/91.png)
![image_](images/azure_subscriptions/92.png)
![image_](images/azure_subscriptions/93.png)
![image_](images/azure_subscriptions/94.png)
![image_](images/azure_subscriptions/95.png)
![image_](images/azure_subscriptions/96.png)
![image_](images/azure_subscriptions/97.png)
![image_](images/azure_subscriptions/98.png)
![image_](images/azure_subscriptions/99.png)