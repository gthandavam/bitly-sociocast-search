import requests, datetime

access_token = "500752aa74ab91846753fc86c53f8e7cb27f5c81"
base_url = "https://api-ssl.bitly.com/v3/"

# A story is a group of related links that are about the same thing.
# This is based on shared topics and phrases extracted from the content of each link.

def get_story_info_link(link="http://bit.ly/14eLfvJ", endpoint="story_api/story_info"):
	'''
	The above prints out a JSON response containing the story id,
	which brings you to the corresponding story page when added to the end of this url:
	http://rt.ly/story?story_id=
	'''
	params = {
		'access_token': access_token,
		'link': link
	}
	return requests.get(base_url + endpoint, params=params).json()

def get_story_from_phrases(phrases=("istanbul", "gezi park", "turkey"), endpoint="story_api/story_from_phrases"):
	params = {
		'access_token' : access_token,
		'phrases': phrases
	}
	return requests.get(base_url + endpoint, params=params).json()

def get_story_title(story_id, endpoint="story_api/title"):
	params = {
		'access_token': access_token,
		'story_id': story_id
	}
	return requests.get(base_url + endpoint, params=params).json()

def get_story_metadata(story_id, endpoint="story_api/metadata"):
	params = {
		'access_token': access_token,
		'story_id': story_id,
		'field': ("rates", "titles", "images", "clicks")
	}
	return requests.get(base_url + endpoint, params=params).json()

'''
Here, given a story id, we `limit` the results to 10 for each `field` and get back the top 10 cities from which the story is receiving clicks, domains on which links in the story appear, and link referrers. You can also return a more general distribution across `regions` and `countries` as well as get back associated `phrases` and `topics`. 
'''
def get_story_distribution(story_id, endpoint="story_api/distribution"):
	params = {
		'access_token': access_token,
		'story_id': story_id,
		'limit': 10,
		'field': ("cities", "domains", "referrers", "phrases", "topics", "regions", "countries")
	}
	return requests.get(base_url + endpoint, params=params).json()

def get_story_history(story_id, endpoint="story_api/history"):
	params = {
		'access_token': access_token,
		'story_id': story_id,
		'filters': ("top10_by_current_rate"),
		'start_time': datetime.timedelta(minutes=10),
		'end_time': datetime.datetime.now()
	}
	return requests.get(base_url + endpoint, params=params).json()

def f(phrases = ("snowden", "NSA") ):
	d = get_story_from_phrases( phrases )
	story_id = d['data']['story_id']
	return story_id

if __name__ == '__main__':
	pass