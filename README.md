# Slash Command Tools
A Python-based tool to allow you to easily create, list and delete Discord slash commands.
You just need to enter a few details and then the script will handle the rest for you.
Supports global and guild commands.


# Dependencies

Requires the `requests` module to be installed.

Install this through a command line with `pip install requests`

# How to use

**Note:** This is a very basic set of instructions, and may be slightly out of date as this tool is in active development and is constantly changing. Once it's nearer completion, we'll have a more stable tutorial available.

1) Download and run the [Python script](https://github.com/iSaluki/discord-slash-commands/blob/main/discord-slash-commands.py)
2) Make sure you've added the `applications.commands` scope to your bot for the server you want to add the command to (if you're doing guild based). Replace BOT_ID with your bot's client ID in this link: https://discord.com/api/oauth2/authorize?client_id=BOT_ID&scope=applications.commands
2) Enter all the details into the CLI, you will be prompted for them one by one.
3) Head over to Discord and see the new slash commands

Want to run the code in your browser? [Do it here!](https://repl.it/@saluki/discord-slash-commands)

# Features

Main features available now.

`CREATE` a new slash command for a bot, in a specific guild or globally. You can also update these by overriding them.
`LIST` commands for a bot, either globally or in a specific guild.
`DELETE` commands for a bot, either globally or in a specific guild.


# Notes

This script was written in a short period of time and can not do everything, and may also have bugs.
Please feel free to contribute to it, or to open issues with any problems you're having.

This is currently a very basic script, but I plan to add more to it in future. It is not intended for use directly in a bot, but more for testing, and for setting up commands for testing or getting some global commands working.


Enjoy!

# Coming soon

- Python module, allowing devs to install via pip, import into scripts and use in more technical applications.
