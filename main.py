import os
import csv
import json
import sys

url_link = sys.argv[1]
url_link = url_link + "/wp-json/wp/v2/posts/?per_page=100"

print("Url: " + sys.argv[1])
from urllib.request import Request, urlopen

req = Request(url_link, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()  

# Write data to file
filename = "raw_data.txt"
file_ = open(filename, 'wb')
file_.write(webpage)
file_.close()

def save_to_file (fn, row, fieldnames):
    
        if (os.path.isfile(fn)):
            m="a"
        else:
            m="w"
         
        with open(fn, m, encoding="utf8", newline='' ) as csvfile: 
          
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if (m=="w"):
                writer.writeheader()
            writer.writerow(row)

with open(filename) as json_file:
    json_data = json.load(json_file)

C_data = []

for n in json_data:  
 
    r={}
    r["Modified"] = n['modified']
    r["Title"] = n['title']['rendered']
    r["Content"] = n['content']['rendered']
    r["Link"] = n['link']

    # JSON Conversion

    j_data = {
        "modified/posted" : r["Modified"],
        "title" : r["Title"],
        "content" : r["Content"],
        "link" : r["Link"]
    }

    C_data.append(j_data)
    print("Title: " + r["Title"])
    print("Status: Downloaded")
    
json_object = json.dumps(C_data, indent = 4) 

# Writing to sample.json 
with open("data.json", "w") as outfile: 
    outfile.write(json_object) 

print("Extracted Successfully")

    