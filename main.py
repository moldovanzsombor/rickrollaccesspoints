#!/usr/bin/env python3

from scapy.all import Dot11, Dot11Beacon, Dot11Elt, RadioTap, sendp
from threading import Thread
from sys import argv, exit
from os import getuid
from randmac import RandMac as random_mac
from banner import banner

class fake_accesspoint:
	def __init__(self, mac_addr, ssid):
		self.mac_addr = mac_addr
		self.ssid = ssid

	def __repr__(self):
		return self.mac_addr, self.ssid

def send_beacon(mac, ssid, verbose = False):
	dot11 = Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=mac, addr3=mac, type=0, subtype=8)
	beacon = Dot11Beacon(cap="ESS+privacy")
	essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))

	frame = RadioTap() / dot11 / beacon / essid

	if verbose:
		print(f"Sending beacon: {ssid}")

	sendp(frame, inter=0.1, loop=1, iface=interface, verbose=0)

def extend_lyrics(lyrics, count):
	original = lyrics[:]

	i = j = 0
	while count > len(lyrics):
		lyrics.append(original[i] + f" {j}")

		if i >= len(original) - 1:
			i = 0
			j += 1
		else:
			i += 1
	return lyrics

lyrics = [
	"0) We're no strangers to love",
	"1) You know the rules",
	"2) and so do I",
	"3) A full commitment's",
	"4) what I'm thinking of",
	"5) You wouldn't get this",
	"6) from any other guy",
	"7) I just wanna tell you",
	"8) how I'm feeling",
	"9) Gotta make you understand",
	"a) Never gonna give you up",
	"b) Never gonna let you down",
	"c) Never gonna run around",
	"d) and desert you",
	"e) Never gonna make you cry",
	"f) Never gonna say goodbye",
	"g) Never gonna tell a lie",
	"h) and hurt you",
	"i) We've known each other",
	"j) for so long",
	"k) Your heart's been",
	"l) aching but",
	"m) You're too shy to say it",
	"n) Inside we both know",
	"o) what’s been going on",
	"p) We know the game and",
	"q) we’re gonna play it",
	"r) Annnnnd if you ask me",
	"s) how I’m feeling",
	"t) Don’t tell me you’re",
	"u) too blind to see",
	"v) Never gonna give you up",
	"w) Never gonna let you down",
	"x) Never gonna run around",
	"y) and desert you",
]

if __name__ == "__main__":
	if '-h' in argv or '--help' in argv:
		print(banner)
		exit()

	if getuid() != 0:
		print('Must run as root!\n')
		exit()

	threads = []
	accesspoints = []
	interface = "wlan0mon"
	accesspoint_count = len(lyrics)

	for i in range(1, len(argv)):
		if argv[i] == '-n':
			try:
				accesspoint_count = int(argv[i + 1])
				i += 1
			except:
				print(banner)
				exit()

		elif argv[i] == '-i' or argv[i] == '--interface':
			try:
				interface = argv[i + 1]
				i += 1
			except:
				print(banner)
				exit()

	verbose = '-v' in argv or '--verbose' in argv

	if accesspoint_count > len(lyrics):
		lyrics = extend_lyrics(lyrics, accesspoint_count)

	for i in range(0, accesspoint_count):
		accesspoints.append(fake_accesspoint(str(random_mac()), lyrics[i]))

	if verbose:
		for i in range(0, len(accesspoints)):
			print(accesspoints[i].__repr__())

	for i in range(0, len(accesspoints)):
		Thread(target=send_beacon, args=(accesspoints[i].__repr__()[0], accesspoints[i].__repr__()[1], verbose)).start()

