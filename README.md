# Ai_Home_Automation
Learning resources for a Home Automation project using the Raspberry Pi.

## Wireless

How to get on the wireless network using the command-line.

1. `$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`
1. Add the following network to the bottom, save, and exit.
````
network={
	ssid="AcroboticGuest"
	psk="***look at the whiteboard***"
	proto=RSN
	key_mgmt=WPA-PSK
	pairwise=CCMP
	auth_alg=OPEN
}
````
1. `$ sudo nano /etc/network/interfaces`
1. Replace the contents with the following, save, and exit.
````
auto lo
auto wlan0

iface lo inet loopback
iface eth0 inet dhcp

allow-hotplug wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp
````
