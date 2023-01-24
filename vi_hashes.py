import json
import jsonlines
import requests
import time
import csv

# Reads a Kenna VI+ Snapshot file and creates a csv file of CVE malware hash associations.

# Path to exported snapshot.jsonl file
snapshot = 'Snapshot_Download-1667925118040.jsonl' 
# Kenna api token
token = 'API TOKEN GOES HERE'
# Kenna API host
api_host = 'https://api.eu.kennasecurity.com'




headers = {'content-type': 'application/json', 'X-Risk-Token': token}
csv_header = ('CVE','MD5','SHA1','SHA256')

with open('kenna_malware_hashes.csv', 'w', encoding='UTF8') as r:
	writer = csv.writer(r)
	writer.writerow(csv_header)
	with jsonlines.open(snapshot) as f:

	    for line in f.iter():
	    	cve = (line['cve_id'])
	    	malware_exploitable = (line['malware_exploitable'])

	    	if malware_exploitable == True:
		    	url = f'{api_host}/vulnerability_definitions/{cve}/malware'
		    	search = requests.request("GET", url, headers=headers)
		    	results = search.json()

		    	for i in (results['malware']):
		    		md5 = i['md5']
		    		sha1 = i['sha1']
		    		sha256 = i['sha256']
		    		row = (cve,md5,sha1,sha256)
		    		writer.writerow(row)

		    	time.sleep(.3)




