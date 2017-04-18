import json
import requests
from random import randint

key = "AIzaSyDzqT1_izlreFmVssHu_vB7c6FxyCBQH8U"
def get_all(place , state):
	id = search_id(place , state)
	photo_url = []
	title = []
	for i in range(len(id)):
		
		y = get_name(id[i])
		title.append(y)
		print y
		x = get_photos(y)
		photo_url.append(x)
	
	return photo_url , title


def search_id(place , state):
	if state == 'happy':
		stateArray = ['National Park' , 'Beaches' ,'Waterfalls']
		setState = stateArray[randint(0,len(stateArray)-1)]
	elif state == 'party':
		stateArray = ['Nightclubs' , 'Cruise' , 'Beaches']
		setState = stateArray[randint(0,len(stateArray)-1)]
	elif state == 'gloomy':
		stateArray = ['Hill Station' , 'National Park']
		setState = stateArray[randint(0,len(stateArray)-1)]
	elif state == 'shopping':
		setState = 'Shopping'
	else:
		setState = 'Places of Interest'
	print(place)
	print(state)
	print("Getting Results...")
	page = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json?query="+setState+"around"+place+"&key="+key)
	page = json.loads(page.content)
	results = []
	resultsPage = page['results']
	dataset = []
	for i in range(len(resultsPage)):
		dataset.append(resultsPage[i]['place_id'])
	return dataset[:10]

def get_photos(place):
	page = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json?query="+place+"&key="+key)
	page = json.loads(page.content)
	resultsPage = page['results']
	try:
		results = resultsPage[0]['photos'][0]['photo_reference']
		ref_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference="+results+"&key="+key
	except KeyError:
		ref_url = ''
	return(ref_url)

def get_name(id):
	page = requests.get("https://maps.googleapis.com/maps/api/place/details/json?placeid="+id+"&key="+key)
	page = json.loads(page.content)
	resultsPage = page['result']
	try:
		results = (resultsPage['name'])
	except KeyError:
		result = ''
	return(results)

def get_location(id):
	page = requests.get("https://maps.googleapis.com/maps/api/place/details/json?placeid="+id+"&key="+key)
	page = json.loads(page.content)
	results = []
	resultsPage = page['result']
	try:
		results.append(resultsPage['geometry']['location'])
	except KeyError:
		result = ''
	return(results)

def get_addr(id):
	page = requests.get("https://maps.googleapis.com/maps/api/place/details/json?placeid="+id+"&key="+key)
	page = json.loads(page.content)
	results = []
	resultsPage = page['results']
	try:
		results.append(resultsPage['formatted_address'])
	except KeyError:
		result = ''
	return(results)

def distance(place , state):

	origin = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json?query="+place+"&key="+key)
	origin = json.loads(page.content)
	originLoc = origin['result']['location']
	originLoc_lat = originLoc['lat']
	originLoc_lng = originLoc['lng']

	target = search_id(place,state)
	targetLoc = get_location(target)
	targetLoc_lat = [] 
	targetLoc_lng = []

	#for i in range(targetLoc):
	#	page = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="++","+""+&destinations="+ +","+ +&key="+key)
