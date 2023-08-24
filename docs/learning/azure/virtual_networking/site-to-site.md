# Site to Site Configuration
- a secure connection between an on-premise network and an Azure network via the Internet.

- On the on-premise side, you need to have a VPN device that can route traffic via the Internet onto the VPN gateway in Azure. 
  - The VPN device can be a hardware device like a Cisco router or a software device ( e.g Windows Server 2016 running Routing and Remote services). 
  - The VPN device needs to have a publically routable IP address.

- The subnets in your on-premise network must not overlap with the subnets in your Azure virtual network

- The Site-to-Site VPN connection uses an IPSec tunnel to encrypt the traffic.

- The VPN gateway resource you create in Azure is used to route encrypted traffic between your on-premise data center and your Azure virtual network.

- There are different SKU's for the Azure VPN gateway service. Each SKU has a different pricing and attributes associated with it 

## <hr/>Virtual Network can have many Address Space and Subnets
![1](images/site-to-site/1.png)

### <hr/><hr/>high level
![image](images/site-to-site/72.png)
![image](images/site-to-site/73.png)
![image](images/site-to-site/74.png)
![image](images/site-to-site/75.png)
![image](images/site-to-site/76.png)
![image](images/site-to-site/77.png)
![image](images/site-to-site/78.png)
![image](images/site-to-site/79.png)
![image](images/site-to-site/83.png)
![image](images/site-to-site/84.png)
![image](images/site-to-site/85.png)

## <hr/><hr/>lets start the installation



## <hr/>step 1 : make the azure main_office_vnet, ip range as 10.0.0.0/16 and add create a vm 

![image](images/site-to-site/3.png)
![image](images/site-to-site/4.png)
![image](images/site-to-site/5.png)
## <hr/>step 2: create a GatewaySubnet
![image](images/site-to-site/6.png)
![image](images/site-to-site/7.png)

## <hr/>step 3: create VM with no public IP in the main_office_vnet and in subnetA
![image](images/site-to-site/8.png)
![image](images/site-to-site/9.png)


## <hr/>step 4 : create VPN Gateway to main_office_vnet to GatewaySubnet


![image](images/site-to-site/16.png)
![image](images/site-to-site/17.png)
![image](images/site-to-site/18.png)
![image](images/site-to-site/19.png)

## <hr/>step 5: create on_premise_vnet with IP range 10.1.0.0/16 
![image](images/site-to-site/10.png)
![image](images/site-to-site/11.png)

## <hr/>step 6: create 1 VM's. one for client machine and other as Routing VM
![image](images/site-to-site/14.png)
![image](images/site-to-site/15.png)


## <hr/>step 7 : enable the Routing Service on the windows machine
![image](images/site-to-site/20.png)
![image](images/site-to-site/21.png)
![image](images/site-to-site/22.png)
![image](images/site-to-site/24.png)
![image](images/site-to-site/25.png)
![image](images/site-to-site/32.png)
![image](images/site-to-site/34.png)
![image](images/site-to-site/35.png)
![image](images/site-to-site/36.png)
![image](images/site-to-site/37.png)
## <hr/>step 8: create Local Network Gateway in the main_office_network and give it details from the on_premise_vnet 
![image](images/site-to-site/26.png)
![image](images/site-to-site/27.png)
![image](images/site-to-site/28.png)
![image](images/site-to-site/29.png)
![image](images/site-to-site/30.png)

## <hr/>step 10:  create a new connection in the VPN Gateway and connect the VPN with the local Network gateway
![image](images/site-to-site/40.png)
![image](images/site-to-site/41.png)

## <hr/>step 11: on routermachice you need to tell the main_office_vnet vpn details to Demand-dial Interface.
![image](images/site-to-site/42.png)
![image](images/site-to-site/43.png)
![image](images/site-to-site/44.png)
![image](images/site-to-site/45.png)
![image](images/site-to-site/46.png)
![image](images/site-to-site/47.png)
![image](images/site-to-site/48.png)
![image](images/site-to-site/49.png)
![image](images/site-to-site/50.png)
![image](images/site-to-site/51.png)
![image](images/site-to-site/52.png)
![image](images/site-to-site/52.png)
![image](images/site-to-site/53.png)
![image](images/site-to-site/54.png)
![image](images/site-to-site/55.png)
![image](images/site-to-site/56.png)
![image](images/site-to-site/57.png)
![image](images/site-to-site/58.png)
![image](images/site-to-site/59.png)


## <hr/>Completed. Connect to machine


### <hr/>step 13: lets add another vnt network and add a vm 
![image](images/site-to-site/60.png)
![image](images/site-to-site/61.png)
![image](images/site-to-site/62.png)
![image](images/site-to-site/63.png)

### <hr/>step 14: add vnet peering between main to on-premise2
![image](images/site-to-site/71.png)

### <hr/>step 15: add the details of the new vnet to static Routes in the RoutingServer
![image](images/site-to-site/66.png)
![image](images/site-to-site/67.png)
![image](images/site-to-site/68.png)
![image](images/site-to-site/80.png)
![image](images/site-to-site/82.png)



