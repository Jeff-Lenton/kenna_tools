import json
import jsonlines
import requests
import time
import csv
import argparse

parser = argparse.ArgumentParser( 
    description="Reads a Kenna VI+ Snapshot file and creates a csv file of CVE to malware hash associations.")

parser.add_argument('-t', action='store', dest='token', required=True, help='Kenna API token - place in single quotes to escape special chars')
parser.add_argument('-f', action='store', dest='snapshot', required=True, help='File path to Snapshot file')
parser.add_argument('-a', action='store', default='api.eu.kennasecurity.com', dest='api_host', required=False, help='Kenna API host. Default - api.eu.kennasecurity.com')
args = parser.parse_args()
token = args.token
snapshot = args.snapshot
api_host = f'https://{args.api_host}'
headers = {'content-type': 'application/json', 'X-Risk-Token': token}
csv_header = ('CVE','MD5','SHA1','SHA256')

def get_hashes(headers,csv_header,snapshot,api_host)

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

if __name__ == '__main__':
    get_hashes(headers,csv_header,snapshot,api_host)


