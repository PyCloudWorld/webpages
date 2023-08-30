# User Defined Routes
![image](images/user_defined_routes/0.png)

## <hr/>Virtual WAN
### </hr> Step 1: Create Virtual Network with 3 subnets 
![image](images/user_defined_routes/1.png)
![image](images/user_defined_routes/2.png)
![image](images/user_defined_routes/3.png)
![image](images/user_defined_routes/4.png)


### </hr> Step 2: Create VM's in each Subnet
* subnetA and SubnetB virtual machines should not have the public IP Address

![image](images/user_defined_routes/5.png)
![image](images/user_defined_routes/6.png)
![image](images/user_defined_routes/7.png)
![image](images/user_defined_routes/8.png)
![image](images/user_defined_routes/9.png)
![image](images/user_defined_routes/10.png)
![image](images/user_defined_routes/11.png)
![image](images/user_defined_routes/12.png)
![image](images/user_defined_routes/13.png)

### </hr> Step 3: Create Route Table in Azure.

* Route all the traffic of the Virtual Network to the windowsCentral

![image](images/user_defined_routes/16.png)
![image](images/user_defined_routes/17.png)
![image](images/user_defined_routes/18.png)
![image](images/user_defined_routes/19.png)

### </hr> Step 4: Associate the Route Table to the subnet
* Associate the Route Table to the subnetA and SubnetB
* now any traffic starting from SubnetA and SubnetB will first go the windowsCentral


![image](images/user_defined_routes/20.png)
![image](images/user_defined_routes/21.png)
![image](images/user_defined_routes/22.png)
![image](images/user_defined_routes/23.png)

# Step 5: Enable IP Forwarding at azure level
![image](images/user_defined_routes/31.png)
![image](images/user_defined_routes/32.png)

### </hr> Step 6: Login to WindowsCentral and enable Windows Routing at OS level
![image](images/user_defined_routes/24.png)
![image](images/user_defined_routes/25.png)
![image](images/user_defined_routes/26.png)
![image](images/user_defined_routes/27.png)
![image](images/user_defined_routes/28.png)
![image](images/user_defined_routes/29.png)
![image](images/user_defined_routes/30.png)
![image](images/user_defined_routes/33.png)
![image](images/user_defined_routes/34.png)
![image](images/user_defined_routes/35.png)
![image](images/user_defined_routes/36.png)
![image](images/user_defined_routes/37.png)
![image](images/user_defined_routes/38.png)
