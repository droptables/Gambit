import pymongo,re


def sanity_check():

	for record in boxscores.find():
		try:
			awaytotals.append(record['away_totals']['points'])
		except:
			if record['eventkey'].startswith("2011"):
				print record['eventkey']
			failedids.write(record['eventkey']+"\n")


def get_matches(teama, teamb):
	teamaawaypoints = []
	teamahomepoints = []
	teambawaypionts = []
	teambhomepoints = []

	for record in boxscores.find():
		if record['eventkey'].startswith("2015"):
			pass
		else:
			if record['eventkey'][9:].startswith(teama) or record['eventkey'][9:].endswith(teama):
				if record['eventkey'][9:].startswith(teamb) or record['eventkey'][9:].endswith(teamb):
					if record['away_team']['team_id']==teama:
						teamaawaypoints.append(record['away_totals']['points'])
					else:
						teambhomepoints.append(record['home_totals']['points'])

					if record['away_team']['team_id']==teamb:
						teambawaypionts.append(record['away_totals']['points'])
					else:
						teamahomepoints.append(record['home_totals']['points'])


	for item in teamaawaypoints:
		print item

	for item in teambhomepoints:
		print item


def mongo_query():
	#for record in boxscores.find({"eventkey": "20120415-toronto-raptors-at-atlanta-hawks"}, {"away_totals"}):
		#print record
	#for item in boxscores.find({"away_totals.points": 100}):
	#	print item
	#print boxscores.distinct('away_totals.points')
	
	#for item in boxscores.find({"eventkey": "20120415-toronto-raptors-at-atlanta-hawks"},{'away_team.team_id':1}):
	#	print item

	# for record in boxscores.find(
	# 	{'eventkey': {'$in': [ re.compile('.*toronto-raptors.*atlanta-hawks'), 
	# 	re.compile('.*atlanta-hawks.*toronto-raptors')]}},{"$and":[ {"away_team.team_id":"atlanta-hawks"}]}):

	# 	print record
	#.find({"$or":[ {"vals":1700}, {"vals":100}]})
	for record in boxscores.find({"$and":[ {"away_team.team_id":"washington-wizards"}, {"home_team.team_id":"atlanta-hawks"}]}):

		print record['eventkey']
		print str(record['away_totals']['points']) +" VS "+ str(record['home_totals']['points'])


		


	#[x for x in c.things.find( {'$or' : [{'name':'1'}, {'name':'2'}] } )]
	





if __name__ == '__main__':
	global boxscores

	client = pymongo.MongoClient('localhost',27017)
	db = client.nba
	seasonresults= db.seasonresults
	boxscores= db.boxscores

	failedids=open('failedids.txt', 'w')
	mongo_query()
	#get_matches("cleveland-cavaliers", "sacramento-kings")

