import csv
import json
with open("user.csv","r")as csv_file:
    reader=csv.DictReader(csv_file)
    data=list(reader)
with open("user.json","w")as json_file:
    json.dump(data,json_file,indent=4)
print("user.csv has been converted to user.json sucessfully.")