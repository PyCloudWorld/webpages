# Azure Firewall Service

## <hr/>Features
* built-in high availability
* can deploy the azure firewall instance across two or more availability zones
* filter traffic based on filly qualified domain names
* can create network filtering rules , based on :
  * source IP
  * destination IP address
  * port
  * protocol
* stateful in nature, so it understands what packets of to allow
* built-in threat intelligence


## <hr/> Main concept
![image](images/azure_firewall_service/main.png)
## <hr/> step 1: create Virtual Networks
![image](images/azure_firewall_service/0.png)
![image](images/azure_firewall_service/1.png)
![image](images/azure_firewall_service/2.png)
![image](images/azure_firewall_service/3.png)
![image](images/azure_firewall_service/4.png)
![image](images/azure_firewall_service/5.png)
![image](images/azure_firewall_service/6.png)
## <hr/> step 2: create Virtual Machines
![image](images/azure_firewall_service/7.png)
![image](images/azure_firewall_service/8.png)
![image](images/azure_firewall_service/9.png)
![image](images/azure_firewall_service/10.png)
![image](images/azure_firewall_service/11.png)
![image](images/azure_firewall_service/12.png)
![image](images/azure_firewall_service/13.png)
![image](images/azure_firewall_service/14.png)
![image](images/azure_firewall_service/15.png)
## <hr/> step 3: create subnet for Azure Firewall
![image](images/azure_firewall_service/16.png)
![image](images/azure_firewall_service/17.png)
![image](images/azure_firewall_service/18.png)
## <hr/> step 4: create Azure Firewall
![image](images/azure_firewall_service/19.png)
![image](images/azure_firewall_service/20.png)
![image](images/azure_firewall_service/21.png)
![image](images/azure_firewall_service/22.png)
![image](images/azure_firewall_service/23.png)
## <hr/> step 5: create Rule in Azure Firewall Policy 
![image](images/azure_firewall_service/24.png)
![image](images/azure_firewall_service/25.png)
![image](images/azure_firewall_service/26.png)
![image](images/azure_firewall_service/27.png)
## <hr/> step 6: try connecting
![image](images/azure_firewall_service/28.png)
![image](images/azure_firewall_service/29.png)
![image](images/azure_firewall_service/30.png)
