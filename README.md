# Slash Command Generator
A Python system to easily push custom slash commands to Discord.
You just need to enter a few details and then it produces the request, prints it out and sends it off to Discord to add your command.
Supports global and guild commands.


# Dependencies

Requires the `requests` module to be installed.

Install this through a command line with `pip install requests`

# How to use

1) Download and run the Python script (https://github.com/iSaluki/discord-slash-commands/blob/main/discord-slash-commands.py)
2) Make sure you've added the `applications.commands` scope to your bot for the server you want to add the command to (if you're doing guild based). Replace BOT_ID with your bot's client ID in this link: https://discord.com/api/oauth2/authorize?client_id=BOT_ID&scope=applications.commands
2) Enter all the details into the CLI, you will be prompted for them one by one.
3) Head over to Discord and see the new slash commands

# Notes

This script was written in a short period of time and can not do everything, and may also have bugs.
Please feel free to contribute to it, or to open issues with any problems you're having.

This is currently a very basic script, but I plan to add more to it in future. It is not intended for use directly in a bot, but more for testing, and for setting up commands for testing or getting some global commands working.


Enjoy!
