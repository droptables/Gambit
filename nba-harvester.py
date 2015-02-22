import json,os, urllib2, uncurl, requests, pymongo, time
from clint.textui import colored

def get_season_results(team):
	seasons = ['2012','2013','2014', '2015']

	for year in seasons:
		seasonsquery="https://erikberg.com/nba/results/"+team+".json?season="+year
		print colored.yellow("[*] Getting "+seasonsquery)
		r = requests.get(seasonsquery,
    	headers={
        	"Authorization": "Bearer 90448d9e-2eab-4b41-8b73-a919824bc36f",
        	'User-Agent': 'python test',
    		'From': 'endersavage@gmail.com'
    	},
    	cookies={},
		)
		for item in r.json():
			seasonresults.insert(item)
		print colored.green("[+] "+team+year+" complete")


def get_team_stats(team):

	teamquery = "https://erikberg.com/nba/team-stats.json?team_id="+team
	print colored.yellow("[*] Getting "+teamquery)
	r = requests.get(teamquery,
    headers={
        	"Authorization": "Bearer 90448d9e-2eab-4b41-8b73-a919824bc36f",
        	'User-Agent': 'python test',
    		'From': 'zimbabwhemahn@gmail.com'
    },
    	cookies={},
	)
	
	teamstats.insert(r.json())

	print colored.green("[+] " + teamquery+" complete")


def get_box_score(eventid):
	print colored.yellow("[*] Fetching "+ eventid)
	boxquery="https://erikberg.com/nba/boxscore/"+eventid+".json"

	r = requests.get(boxquery,
    headers={
        	"Authorization": "Bearer 90448d9e-2eab-4b41-8b73-a919824bc36f",
        	'User-Agent': 'Box Score Harvest Bot, endersavage@gmail.com',
    		'From': 'endersavage@gmail.com @endersavage'
    },
    	cookies={},
	)
	print r.headers
	boxresult = r.json()
	boxresult['eventkey']=eventid
	boxscores.insert(boxresult)
	print colored.green("[+] "+eventid+" complete.")


if __name__ == '__main__':
	client = pymongo.MongoClient('localhost',27017)
	db = client.nba
	seasonresults = db.seasonresults
	teamstats = db.teamstats
	boxscores= db.boxscores
	teamlist = ["atlanta-hawks", "boston-celtics", "brooklyn-nets", "charlotte-hornets", "chicago-bulls", "cleveland-cavaliers", "dallas-mavericks", "denver-nuggets", "detroit-pistons", "golden-state-warriors", "houston-rockets", "indiana-pacers", "los-angeles-clippers", "los-angeles-lakers", "memphis-grizzlies", "miami-heat", "milwaukee-bucks", "minnesota-twins", "new-orleans-pelicans", "new-york-knicks", "oklahoma-city-thunder", "orlando-magic", "philadelphia-76ers", "phoenix-suns", "portland-trail-blazers", "sacramento-kings", "san-antonio-spurs", "toronto-raptors", "utah-jazz", "washington-wizards"]

	#for team in teamlist:
		#get_season_results(team)
		#get_team_stats(team)
	#	time.sleep(20)
	#for eventid in seasonresults.distinct("event_id"):
	for eventid in open('schedule-ids.txt').readlines():
		get_box_score(eventid.rstrip())
		time.sleep(12)
		
	print colored.green("[+] Fetching complete.")