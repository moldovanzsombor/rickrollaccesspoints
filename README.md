# rickrollaccesspoints

## Requirements
* scapy
* randmac

## Monitor mode.
For this to work you must first put your wireless device into monitor mode. One way doing it is demonstrated below using airmon-ng.
$ sudo airmon-ng start wlan0

Not every wireless adapter supports monitor mode.

Your wireless adapter will then be displayed as "wlan0mon"

After you are finished turn off montitor mode by entering the following command:
$ sudo airmon-ng stop wlan0mon
