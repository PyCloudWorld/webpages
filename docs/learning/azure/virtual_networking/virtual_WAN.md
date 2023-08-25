# Virtual WAN

## <hr/>Virtual WAN
![image](images/virtual_wan/1.png)
![image](images/virtual_wan/2.png)
![image](images/virtual_wan/3.png)
![image](images/virtual_wan/28.png)

## <hr/>Steps to install
* install virtual WAN
* create the Hub inside VirtualWAN
* map it with the VNets and on- premise

## <hr/> Types of VirtualWAN
* There are 2 types of VirtualWAN
  * Standard 
  * Basic
![image](images/virtual_wan/28.png)



  
### </hr> Step 1: lets create 2 VNet's and one one VM in it
* the public IP would be off in both the cases
1. VNET: <vnet1>
   * VM : <windows11> 
   * IP range : <10.1.0.0/16>
2. VNET: <vnet2>
   * VM : <windows22> 
   * IP range : <10.2.0.0/16>
![image](images/virtual_wan/31.png)
![image](images/virtual_wan/4.png)
![image](images/virtual_wan/5.png)
![image](images/virtual_wan/6.png)
![image](images/virtual_wan/7.png)
![image](images/virtual_wan/8.png)
![image](images/virtual_wan/9.png)
![image](images/virtual_wan/10.png)
![image](images/virtual_wan/11.png)
![image](images/virtual_wan/12.png)
![image](images/virtual_wan/13.png)
![image](images/virtual_wan/14.png)
![image](images/virtual_wan/15.png)
![image](images/virtual_wan/16.png)
![image](images/virtual_wan/17.png)
![image](images/virtual_wan/19.png)
![image](images/virtual_wan/20.png)
![image](images/virtual_wan/21.png)
![image](images/virtual_wan/22.png)
![image](images/virtual_wan/23.png)
![image](images/virtual_wan/24.png)

### <hr/> Step 2: create VirtualWAN
* Name : pyVirtualWAN
* Type: Standard
![image](images/virtual_wan/32.png)
![image](images/virtual_wan/25.png)
![image](images/virtual_wan/26.png)
![image](images/virtual_wan/27.png)
![image](images/virtual_wan/28.png)
 
### <hr/> Step 3 : create HUB
* Name : pyHub
* Hub private address space : <10.3.0.0/16>
  * is The hub's address range in CIDR notation.
  * its like a VNET so we need to provide an IP range for it, which has to be unique
* Virtual Hub Capacity : 
  * means how many VMS in total the hub can handle
* Hub Routing Prference:
  * its VPN or
  * ExpressRoute

![image](images/virtual_wan/33.png)
![image](images/virtual_wan/29.png)
![image](images/virtual_wan/30.png)

### <hr/> step 4 : create Virtual Network Connection
* Name : PyWAN-VNET1
* Name : PyWAN-VNET2
![image](images/virtual_wan/34.png)
![image](images/virtual_wan/35.png)
![image](images/virtual_wan/36.png)
![image](images/virtual_wan/37.png)
![image](images/virtual_wan/38.png)

### </hr> step 5 : User VPN Configuration
* first create root and child Certificate
* generate certificate : https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-certificates-point-to-site
![image](images/virtual_wan/76.png)
![image](images/virtual_wan/41.png)
![image](images/virtual_wan/42.png)
![image](images/virtual_wan/43.png)
![image](images/virtual_wan/44.png)
![image](images/virtual_wan/45.png)
![image](images/virtual_wan/46.png)
![image](images/virtual_wan/47.png)
![image](images/virtual_wan/48.png)
![image](images/virtual_wan/49.png)
![image](images/virtual_wan/50.png)
![image](images/virtual_wan/51.png)
![image](images/virtual_wan/52.png)
![image](images/virtual_wan/53.png)
![image](images/virtual_wan/54.png)
![image](images/virtual_wan/55.png)
![image](images/virtual_wan/56.png)
![image](images/virtual_wan/57.png)
![image](images/virtual_wan/58.png)
![image](images/virtual_wan/59.png)
![image](images/virtual_wan/60.png)
![image](images/virtual_wan/61.png)
![image](images/virtual_wan/62.png)
![image](images/virtual_wan/63.png)
![image](images/virtual_wan/64.png)
![image](images/virtual_wan/65.png)
![image](images/virtual_wan/66.png)
![image](images/virtual_wan/67.png)
![image](images/virtual_wan/68.png)
![image](images/virtual_wan/69.png)
![image](images/virtual_wan/70.png)

### <hr/> Step 6 : User VPN configuration will only work once we have Gateway created
* go to Virtual WAN => Hub => User VPN (Point to Site) => Create User VPN Gateway
* you need to mention client address pool : <172.16.0.0/16>
![image](images/virtual_wan/77.png)
![image](images/virtual_wan/71.png)
![image](images/virtual_wan/73.png)
![image](images/virtual_wan/74.png)
![image](images/virtual_wan/75.png)

### <hr/> step 7 : Download virtual WAN user VPN profile
![image](images/virtual_wan/78.png)
![image](images/virtual_wan/79.png)

###<hr/> completed
![image](images/virtual_wan/77.png)