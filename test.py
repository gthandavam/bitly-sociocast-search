
if __name__ == '__main__':
	b = {u'url': u'http://techcrunch.com/', u'classification': {u'f20f': 0.9352}}
	print b.keys
	print b['url']
	
	cat_dict = b['classification']	

	for b in cat_dict:
		print b


