import json
with open ("member.json","r")as file:
    users=json.load(file)
for user in users:
    if user["active"]==True:
        with open("active_member.txt","a")as txt:
            txt.write(user["username"]+"\n")
print("Active members have been saved.")



