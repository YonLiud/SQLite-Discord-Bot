# SQLite Discord Bot



SQLite Discord Bot is a discord bot, able to connect and manage any SQLite Database.
  - No Premium
  - Access to SQLite .db file
  - Full SQLite shell access

![](https://discordpy.readthedocs.io/en/latest/_images/snake.png)

## About
SQLite Discord Bot is a lightweight python based bot that's built by [Yon Liud](https://github.com/YonLiud) for easier access to SQLite Shell, without the hassle of remote accessing.
A simple setup is required for running the bot,

# ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) Setup
SQLite Discord Bot uses a small number of python modules to work properly:

* [Valid Token](https://discordpy.readthedocs.io/en/latest/discord.html) - A Valid discord bot
* [Python](https://www.python.org/) - Python, duh
* [Discord.py](https://pypi.org/project/discord.py/) - Discord Module
* [SQLite3](https://www.sqlite.org/index.html) - The Database Library

And of course SQLite Discord Bot itself is open source with a [public repository](https://github.com/YonLiud/Discord-Database-Bot/) 
on GitHub.

# ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) Installation

SQLite Discord Bot requires [Python3](https://www.python.org/) & [Discord.py](https://pypi.org/project/discord.py/) to run.

#### Install the modules.

```sh
$ cd Discord-Database-Bot
$ pip3 install -r requirements.txt
```
#### Insert bot's token
How to get a token: https://discordpy.readthedocs.io/en/latest/discord.html

After recieving the token, open the `SQLite-Discord-Bot` Folder & replace your token into the ``.env`` file

### Example of token inside the .env:
```
TOKEN=NzU0NjIzNTQzNTI2MDMxNDgy.X13b8Q.e0V0cwwmc_BYeMHwvJovFQhLBfk
```
(the token is no longer valid, **DO NOT ATTEMPT TO INSERT TOKEN TO PROJECT**)
#### ![#c5f015](https://via.placeholder.com/15/FFFF00/000000?text=+) Running Bot

```sh
$ python3 app.py
```
The bot will create a role called 'dmb'
#### ![#00FF00](https://via.placeholder.com/15/00FF00/000000?text=+) In Server Use

> For being able to execute any command by SQLite Discord Bot, you must assign users with the created 'dmb' role,

for help:
```sql
sql>help
```

#### ![#9400D3](https://via.placeholder.com/15/9400D3/000000?text=+) Basic Commands
| Name | Syntax |
| ------ | ------ |
| Create Table | ``sql>CREATE TABLE IF NOT EXISTS name (parameters)``|
| Select a Value from Table | ``sql>SELECT column-name FROM table-name WHERE type='identifier'`` |
| Insert a Value to row | ``sql>NSERT INTO table-name (parameters) VALUES (values of parameters)``  |
###### If you require additional help with command, check out [this SQLite Cheat Sheet](https://d17h27t6h515a5.cloudfront.net/topher/2016/September/57ed880e_sql-sqlite-commands-cheat-sheet/sql-sqlite-commands-cheat-sheet.pdf)


#### ![#FF69B4](https://via.placeholder.com/15/FF69B4/000000?text=+) Help

for help, run the command ``sql>help``,
for support, please contact me at my [Discord!](https://discord.com/) ``y0nliud#1545``. Hopefully I will be able to assist you! 

License
----

MIT


**Free Software, Hell Yeah!**
