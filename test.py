#test.py

import json
import urllib2
import httplib
import time

# Data from keyboard
'''
print 'please input the data [time(sentat=543), node, inputs]'

print 'ex: [[535, 10, 150, 250],[530,17,1437,3164]]'

data_string = raw_input()
'''

# Construct post_url (without apikey)
post_url = 'http://emoncms.org'+'/input/bulk'+'.json?apikey='

# Add apikey to post_url
post_url = post_url + 'fa068db077aa9580f393c308cd730270'

# Data automatic

n = 0
value1 = 100
value2 = 2000
value3 = 1567
value4 = 500

for n in range(11):
	value1 = value1 + 100
	value2 = value2 - 110
	value3 = value3 - 13
	value4 = value4 + 60
	
	databuffer = [[535,10,value1,value2],[530,17,value3,value4]]
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
    
	time.sleep(6)


print 'end'
