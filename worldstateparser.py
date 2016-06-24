import io
import re
import os
import sys
import time
import datetime
import urllib2

# == Sortie Data ==
bossIndex = [
	"", # 0
	"Vay Hek", # 1
	"", # 2
	"", # 3
	"Sargus Ruk", # 4
	"", # 5
	"The Jackal", # 6
	"", # 7
	"", # 8
	"", # 9
	""  #10
]

regionIndex = [
	"Derelict", # 0
	"Mercury", # 1
	"Venus",   # 2
	"Earth",   # 3
	"Mars",    # 4
	"Jupiter", # 5
	"Saturn",  # 6
	"Uranus",  # 7
	"Neptune", # 8
	"Pluto",   # 9
	"Ceres", #10
	"Eris", #11
	"Sedna", #12
	"Europa", #13
	"Dojo", #14
	"Void",  #15
	"Phobos"
]

missionIndex = [
	"Exterminate", # 0
	"", # 1
	"Rescue", # 2
	"", # 3
	"Spy", # 4
	"", # 5
	"", # 6
	"Interception", # 7
	"", # 8
	"Assassination", # 9
	""  #10
]

modifierIndex = [
	"", # 0
	"Radiation Hazard ", # 1
	"", # 2
	"Energy Reduction ", # 3
	"Eximus Stronghold ", # 4
	"Weapon Restriction ", # 5
	"", # 6
	"", # 7
	"", # 8
	"", # 9
	""  #10
]

numberIndex = [
	"1, Level 50-60",
	"2, Level 65-80",
	"3, Level 80-100"	
]

if __name__ == "__main__" :

	text = urllib2.urlopen("http://content.warframe.com/dynamic/worldState.php").read()
	trash,alerts = text.split("\"Alerts\":")
	alerts,sorties = alerts.split("\"Sorties\":")
	sorties,globalupgrades = sorties.split("\"GlobalUpgrades\":")
	darvo,trash = globalupgrades.split("\"LibraryInfo\":")
	trash,darvo = darvo.split("\"DailyDeals\":")

	if (str(sys.argv[1]).lower() == "~alerts"):
		print alerts
# 		[
# {
# 	"_id":{"$id":"575588ebe03747fbf8c411ee"},
# 	"Activation":{"sec":1466626605,"usec":567000},
# 	"Expiry":{"sec":1466629890,"usec":172000},
# 	"MissionInfo":{
# 		"descText":"/Lotus/Language/Alerts/ExterminationDesc4",
# 		"location":"SolNode227",
# 		"missionType":"MT_EXTERMINATION",
# 		"faction":"FC_GRINEER",
# 		"seed":78075,
# 		"difficulty":0.9770710749086,
# 		"missionReward":{"credits":3200},
# 		"levelOverride":"/Lotus/Levels/Proc/Grineer/GrineerAsteroidExterminate",
# 		"enemySpec":"/Lotus/Types/Game/GrineerSquadOne",
# 		"minEnemyLevel":7,
# 		"maxEnemyLevel":10
# 	}
# },


# {
# 	"_id":{"$id":"575588ebe03747fbf8c411ef"},
# 	"Activation":{"sec":1466628518,"usec":848000},
# 	"Expiry":{"sec":1466630895,"usec":266000},
# 	"MissionInfo":{
# 		"descText":"/Lotus/Language/Alerts/SabotageDesc6",
# 		"location":"SolNode170",
# 		"missionType":"MT_HIVE",
# 		"faction":"FC_INFESTATION",
# 		"seed":72076,
# 		"difficulty":0.90293475186918,
# 		"missionReward":{"credits":11000},
# 		"levelOverride":"/Lotus/Levels/Proc/Infestation/InfestedCorpusShipSabotage",
# 		"enemySpec":"/Lotus/Types/Game/InfestedSquadC",
# 		"minEnemyLevel":35,
# 		"maxEnemyLevel":38
# 	}
# }

# ],
	elif (str(sys.argv[1]).lower() == "~sortie"):
		trash,sorties = sorties.split("\"Variants\":[")
		sorties,trash = sorties.split("]}]")
		sorties = sorties.replace("{","")
		sorties = sorties.replace("},","#")
		sorties = sorties.replace("}","")
		sorties = sorties.replace("\"bossIndex\":","")
		sorties = sorties.replace("\"regionIndex\":","")
		sorties = sorties.replace("\"missionIndex\":","")
		sorties = sorties.replace("\"modifierIndex\":","")

		sorties = sorties.split("#")

		out = ""

		for i in range(3):
			boss,planet,mission,modifier = sorties[i].split(",")
			if i == 0:
				out = "```python\n**Defeat " + bossIndex[int(boss)] + "'s forces!**\n"
			out += "Mission " + numberIndex[i] + ": " + modifierIndex[int(modifier)] + missionIndex[int(mission)] + " on " + regionIndex[int(planet)] + "\n"
		out += "```"
		print out

	elif (str(sys.argv[1]).lower() == "~darvo"):
		do == "nothing"
	else:
		do == "nothing"


	# print alerts + "\n"
	# print sorties + "\n"
	# print darvo + "\n"