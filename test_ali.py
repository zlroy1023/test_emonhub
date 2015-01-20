#test.py

import json
import urllib2
import httplib
import time
import random

# Data from keyboard
'''
print 'please input the data [time(sentat=543), node, inputs]'

print 'ex: [[535, 10, 150, 250],[530,17,1437,3164]]'

data_string = raw_input()
'''

# Construct post_url (without apikey)
post_url = 'http://192.168.137.1/emoncms-master'+'/input/bulk'+'.json?apikey='

# Add apikey to post_url
post_url = post_url + 'f53ee983b447c8352e44f40f4982164e'

# Data automatic

n = 1
while (n != 0):
	value1 = random.uniform(0, 40)
	value2 = random.uniform(200, 2500)
	
	databuffer = [[535,5,value1],[530,8,value2]]
	data_string = json.dumps(databuffer, separators=(',', ':'))
	post_body = "data="+data_string+"&sentat=543"

	reply = ""
	request = urllib2.Request(post_url, post_body)
	try:
		response = urllib2.urlopen(request, timeout=60)
	except urllib2.HTTPError as e:
		self._log.warning("Couldn't send to server, HTTPError: " +
                          str(e.code))
	except urllib2.URLError as e:
	        self._log.warning("Couldn't send to server, URLError: " +
	                  str(e.reason))
	except httplib.HTTPException:
	        self._log.warning("Couldn't send to server, HTTPException")
	except Exception:
	        import traceback
	        self._log.warning("Couldn't send to server, Exception: " +
	                  traceback.format_exc())
	else:
	        reply = response.read()


	print post_url
	print post_body

	print reply
    
	time.sleep(10)


print 'end'
