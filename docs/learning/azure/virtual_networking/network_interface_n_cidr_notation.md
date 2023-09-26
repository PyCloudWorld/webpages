# Network Interface & CIDR Notation

## <hr/> CIDR fullform
* `C` - Classless
* `ID` - Inter-Domain
* `R` - Routing

## <hr/>Network Interface
![basic_concept](images/network_interface_n_cidr_notation/basic_concept.png)

## <hr/>IP basic concept
![basic_concept](images/network_interface_n_cidr_notation/ip_1.png)

## <hr/>IP basic concept
![basic_concept](images/network_interface_n_cidr_notation/ip_2.png)

## convert IP number to 8 bit 
example:
192.0.2.0</br>
<pre>
`192 is less than 256 and greater than 128`
    :   256   128  64    32    16    8     4    2
    :   0     1    0     0     0     0     0    0
</pre>
`192- 128 = 64`
<pre>
    :   256   128  64    32    16    8     4    2
    :   0     1    0     0     0     0     0    0  
    :   0     1    1     0     0     0     0    0
</pre>    
so 192 is 01100000
    
## <hr/>IP & Masking
![basic_concept](images/network_interface_n_cidr_notation/ip_3.png)

## <hr/>IP Number of host available
![basic_concept](images/network_interface_n_cidr_notation/ip_4.png)

## <hr/>IP masking shorthand
![basic_concept](images/network_interface_n_cidr_notation/ip_5.png)

## <hr/>IP host count
![basic_concept](images/network_interface_n_cidr_notation/ip_6.png)


## <hr/>IP having multiple Subnet 
![basic_concept](images/network_interface_n_cidr_notation/ip_7.png)

## <hr/>Multiple interface on same VM or Server 
![basic_concept](images/network_interface_n_cidr_notation/ip_8.png)