import sys
import requests
import csv
import argparse

parser = argparse.ArgumentParser( 
    description="Reads a CSV of users with columns 'Email', 'First Name', 'Last Name', 'Phone', 'Roles' and creates users in Kenna.")

parser.add_argument('-t', action='store', dest='token', required=True, help='Kenna API token - place in single quotes to escape special chars')
parser.add_argument('-f', action='store', dest='filename', required=True, help='File path to CSV')
parser.add_argument('-a', action='store', default='api.eu.kennasecurity.com', dest='api_host', required=False, help='Kenna API host. Default - api.eu.kennasecurity.com')
args = parser.parse_args()
token = args.token
filename = args.filename
api_host = f'https://{args.api_host}'

headers = {'content-type': 'application/json', 'X-Risk-Token':token}

def add_users(filename, headers):

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)

        for row in csvreader:
            email = (row[0])
            fname = (row[1])
            lname = (row[2])
            phone = (row[3])
            roles = (row[4]).split(",")

            url = f"{api_host}/users"
            payload = {"user": {"firstname": fname, "lastname": lname, "email": email, "roles": roles}}
            commit = requests.request("POST", url, json=payload, headers=headers)
            if commit.status_code == 201:
                print ('Success - Users added')
            else:
                print ('Failed')
                print (commit.status_code)
                print (commit.text)

if __name__ == '__main__':
    add_users(filename,headers)