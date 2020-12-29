import requests


def CreateCommand():
    application_id = input("Enter application ID: ")
    while not application_id.isdigit():
        application_id = input("Enter application ID: ")
    token = input("Enter bot token: ")
    cmdType = input("[Gl]obal or [G]uild?: ").lower()
    if cmdType == "global" or "gl":
        url = "https://discord.com/api/v8/applications/"+application_id+"/commands"
    elif cmdType == "guild" or "gu":
        guild_id = input("Enter guild ID: ")
        while not guild_id.isdigit():
            guild_id = input("Enter guild ID: ")
        url = "https://discord.com/api/v8/applications/" + \
            application_id+"/guilds/"+guild_id+"/commands"
    else:
        print("Please choose a valid option.")

    cmd_name = input("Enter command name: ")
    cmd_description = input("Enter command description: ")
    value_name = input("Value name: ")
    value_description = input("Value description: ")
    #cmd_Type = input("Enter command type (integer): ")
    cmd_isRequired = input("Is the command required? (True/False): ")
    cmd_isRequired = bool(cmd_isRequired)
    # while not cmd_Type.isdigit():
    #    cmd_Type = input("Enter command type (integer): ")
    #cmd_Type = int(cmd_Type)

    print("Starting choices editor...")

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
        "Authorization": "Bot " + token
    }

    print(json)
    print(headers)

    r = requests.post(url, headers=headers, json=json)
    print(r.content)
    funcSelector()


def DeleteCommand():
    application_id = input("Enter application ID: ")
    while not application_id.isdigit():
        application_id = input("Enter valid application ID: ")
    token = input("Enter token: ")
    command_id = input("Enter command ID: ")
    while not command_id.isdigit():
        command_id = input("Ented valid command ID: ")
    cmd_Type = input("[Gl]obal or [G]uild?: ").lower()

    if cmd_Type == "guild" or "gu":
        guild_id = input("Enter guild ID: ")
        while not guild_id.isdigit():
            guild_id = input("Enter valid guild ID: ")
            url = "https://discord.com/api/v8/applications/" + \
                application_id+"/guilds/"+guild_id+"/commands/"+command_id
    elif cmd_Type == "global" or "gl":
        url = "https://discord.com/api/v8/applications/" + \
            application_id + "/commands/" + command_id
    else:
        print("Invalid response")

    headers = {
        "Authorization": "Bot " + token
    }

    r = requests.delete(url, headers=headers)
    print(r.content)
    if r.status_code == 204:
        print("Operation success!")
    else:
        print("It looks like something went wrong.")


def GetCommand():
    application_id = input("Enter application ID: ")
    while not application_id.isdigit():
        application_id = input("Enter valid application ID: ")
    token = input("Enter bot token: ")
    cmd_Type = input("[Gl]obal or [G]uild?: ").lower()
    if cmd_Type == "guild":
        guild_id = input("Enter guild ID: ")
        while not guild_id.isdigit():
            guild_id = input("Enter guild ID: ")
        url = "https://discord.com/api/v8/applications/" + \
            application_id+"/guilds/"+guild_id+"/commands"
    elif cmd_Type == "global" or "gl":
        url = "https://discord.com/api/v8/applications/" + application_id + "/commands"
    else:
        print("Invalid response")

    headers = {
        "Authorization": "Bot " + token
    }
    r = requests.get(url, headers=headers)
    print(r.content)
    funcSelector()
    
def funcSelector():
	print("")
	print("Please select a function")
	print("")
	print("To update a command, create a new command with the same name, this will override it.")
	print("")
	print("[C]reate command")
	print("[D]elete command")
	print("[G]et commands")
	print("")
	fSel = input("Enter function: ")[0].lower()
	
	if fSel == "c":
	    CreateCommand()
	elif fSel == "d":
	    DeleteCommand()
	elif fSel == "g":
	    GetCommand()
	else:
	    print("Invalid function.")
funcSelector()
