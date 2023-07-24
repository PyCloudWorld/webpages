# Virtual Network

## <hr/>Virtual Network can have many Address Space and Subnets
![vnet_1](images/virtual_network/vnet_1.PNG)

<br/>

![vnet_2](images/virtual_network/vnet_2.PNG)

<br/>

![vnet_3](images/virtual_network/vnet_3.PNG)

<br/>

![vnet_4](images/virtual_network/vnet_4.PNG)

## <hr/>Cost of IP Addresses
https://azure.microsoft.com/en-us/pricing/details/ip-addresses/

![vnet_5](images/virtual_network/vnet_5.PNG)


## <hr/>Create public IP address

![vnet_6](images/virtual_network/vnet_6.PNG)


## <hr/> attaching the public IP address to the VM
- ip address cannot be directly attached to VM.
- its attached it Network interface which is attached to VM
![vnet_7](images/virtual_network/vnet_7.PNG)

- 
- steps
![vnet_8](images/virtual_network/vnet_8.PNG)


## <hr/>Attaching addition Network Interface to the VM
- first you need to create new Network Interface.
-  you need to create this Network Interface in the same Virtual Network and Subnet where the VM exist.
- then you need to stop the VM. else it won't allow the attaching of the Network Interface

![vnet_9](images/virtual_network/vnet_9.PNG)

![vnet_10](images/virtual_network/vnet_10.PNG)

![vnet_11](images/virtual_network/vnet_11.PNG)

![vnet_12](images/virtual_network/vnet_12.PNG)

![vnet_13](images/virtual_network/vnet_13.PNG)