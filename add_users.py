import sys
import requests
import csv

# Reads a CSV of users with columns 'Email', 'First Name', 'Last Name', 'Phone', 'Roles' and creates users in Kenna
# Script arguments are CSV filename / path and Kenna API token

filename = (sys.argv[1])
token = (sys.argv[2])

headers = {'content-type': 'application/json', 'X-Risk-Token': token}
print (headers)

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

            url = "https://api.eu.kennasecurity.com/users"
            payload = {"user": {"firstname": fname, "lastname": lname, "email": email, "roles": roles}}

            print (payload)

            commit = requests.request("POST", url, json=payload, headers=headers)
            if commit.status_code == 201:
                print ('Success')
            else:
                print ('Failed')
                print (commit.status_code)

if __name__ == '__main__':
    add_users(filename,headers)