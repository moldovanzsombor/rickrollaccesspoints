# rickrollaccesspoints

### Requirements
* scapy
* randmac

### For this to work you must first put your wireless device into monitor mode. One way doing it is demonstrated below.
$ sudo airmon-ng start wlan0
#### Your wireless adapter will then be called "wlan0mon"

### After you are finished turn off montitor mode by entering the following command:
$ sudo airmon-ng stop wlan0mon
