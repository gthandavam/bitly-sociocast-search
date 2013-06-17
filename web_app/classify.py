import json
import requests
import time
import hashlib
import urllib2

api_key="Gm0JmWyvo4FVldPEImUfak9y" 
api_secret="AXa0PgIsxJ1gef0KBtlOtyIo9VPTUgUQjJjXkAdP"

def get_sig(ts): 
	signer = hashlib.sha256()
        msg = "apikey=Gm0JmWyvo4FVldPEImUfak9y&apisecret=AXa0PgIsxJ1gef0KBtlOtyIo9VPTUgUQjJjXkAdP&ts="
	signer.update(msg+ts)
	return signer.hexdigest()	

def make_content_profile_url(url):
        ts = str(int(time.time()))
	api_sig = get_sig(ts) 
	ret_url = "http://api-sandbox.sociocast.com/1.0/content/profile?url="+url+"&apikey="+api_key+"&sig="+api_sig+"&ts="+ts
	return ret_url 

def get_content_profile(url): 
	rest_url = make_content_profile_url(url)
 	r = requests.get(rest_url+"&humread=true")
	return r

def get_categories(url_list):
	ret = {}
	for url in url_list:
		res = get_content_profile(url)
		res = res.json()	
		ret[url] = res
	return ret

'''
if __name__=="__main__":
	response = get_content_profile("http://techcrunch.com/")
	temp =	response.json()
	print temp
	
	list = ["http://techcrunch.com/"]
	print get_categories(list)
'''
