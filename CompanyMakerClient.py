#Requirments for a company:
#	Energy:
#		Power Plant:Connected to
#			Wind Turbines $10000
#			River Turbines $50000
#			Coal Mine $500000/yr init:$100000
#			Oil Mine $500000/yr init:$50000
#	Supplies:
#		Mining:For each it is: $500000/yr init:$100000
#			Gold
#			Copper
#			Silver
#			Iron
#			Silicon
#	Company Partnership:Unpriced
#		Trading
#		Buying
#		Selling
#	Industries:
#		Airplanes:580mi/hr
#			Airport $1000000
#			Airplain Creator $750000
#		Ships:55mi/hr
#			Harbor $750000
#			Ship Builder $50000
#		Trucks:23mi/hr
#			Truck Deployer $50000
#			Truck Factory $25000
#		Shipper:Unpriced or $1000000+
#		Flyer:Unpriced or $1500000+
#		Trucker:Unpriced or $50000+
#	Utilities:
#		Robot maker $2000000
#		Robot that builds robots maker (Gold:Quickest/Copper:Slowest/Silver:Medium): 1000 nuggets, Iron: 10000 nuggets, Silicon: 500 nuggets
#		Robot (Gold:Quickest/Copper:Slowest/Silver:Medium): 100 nuggets, Iron: 1000 nuggets, Silicon: 50 nuggets
#	Communicatiion Services:
#		Low quality $50000
#		OK quality $100000
#		Great quality $150000

#Initializing
import pygame, sys, sqlite3, os
from pygame.locals import *
from TCPmodClient import *
pygame.init()
pygame.display.set_mode((423, 440))
#423, 440
Power = pygame.image.load("Power.png")
Industries = pygame.image.load("Industries.png")
Utilities = pygame.image.load("Utilities.png")
Communications = pygame.image.load("Communications.png")
Supplies = pygame.image.load("Supplies.png")
Store = pygame.image.load("Store.png")
def connect():
	create = not os.path.exists("Companies.sql")
	db = sqlite3.connect("Companies.sql")
	if create:
		cursor = db.cursor()
		cursor.execute("""CREATE TABLE companies
			{id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL}""")
def Home():
	pass
def Play():
	while True:
		canvas.blit(Power, (0, 0))
		canvas.blit(Industries, (143, 0))
		canvas.blit(Utilities, (286, 0))
		canvas.blit(Communications, (0, 220))
		canvas.blit(Supplies, (143, 220))
		canvas.blit(Store, (286, 220))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
while True:
	pass
