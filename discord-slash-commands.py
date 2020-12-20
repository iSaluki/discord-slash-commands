import requests

application_id = input("Enter application ID: ")
while not application_id.isdigit():
    application_id = input("Enter application ID: ")
token = input("Enter bot token: ")
cmdType = input("Global or Guild?: ")
if cmdType.lower() == "global":
    url = "https://discord.com/api/v8/applications/"+application_id+"/commands"
elif cmdType.lower() == "guild":
    guild_id = input("Enter guild ID: ")
    while not guild_id.isdigit():
        guild_id = input("Enter guild ID: ")
    url = "https://discord.com/api/v8/applications/"+application_id+"/guilds/"+guild_id+"/commands"
else:
    print ("Please choose a valid option.")

cmd_name = input("Enter command name: ")
cmd_description = input("Enter command description: ")
value_name = input ("Value name: ")
value_description = input("Value description: ")
#cmd_Type = input("Enter command type (integer): ")
cmd_isRequired = input("Is the command required? (True/False): ")
cmd_isRequired = bool(cmd_isRequired)
#while not cmd_Type.isdigit():
#    cmd_Type = input("Enter command type (integer): ")
#cmd_Type = int(cmd_Type)

print ("Starting choices editor...")


json = {
    "name": cmd_name,
    "description": cmd_description,
    "options": [
        {
            "name": value_name,
            "description": value_description,
            "type": 3,
            "required": cmd_isRequired,

        },
    ]
}

headers = {
    "Authorization":"Bot "+ token 
}

print(json)
print(headers)

r = requests.post(url, headers=headers, json=json)
print(r.content)
