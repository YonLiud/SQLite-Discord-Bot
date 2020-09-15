import sqlite3
from sqlite3 import Error
import discord

token = open("token.txt", "r").read()
client = discord.Client()

# ? Database

database_file = r"database.db"

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

conn = create_connection(database_file)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def execute_query(query):
    if conn is not None:
        try:            
            output = ""
            c = conn.cursor()
            try:
                c.execute(query)
            except Exception as e:
                return e
            info = c.fetchall()
            conn.commit()
            for value in info:
                output += str(value) + "\n"
            if output=="":
                return "No Output / Empty"
            return output
        except Exception as e:
            return e
    return "Error! the database connection was not created."
        


# ? Discord Bot


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

title = 'SQLite Discord Shell'
arg_missing_message = discord.Embed(title=title, description='Arguments are missing')
blue_color = discord.Color.blue()
gray_color = discord.Color.light_gray()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #TODO  >>> ADD PERMISSIONS HERE <<<

    if message.content == ('>_help'):
        await message.channel.send(embed=(discord.Embed(title=title, description="""For More Help, visit SQLite's website:
         https://www.sqlite.org/doclist.html
         For support, visit alTab Developers:
         http://www.altab.dev/
         """, color=blue_color)))
        return


    if message.content.startswith('>_'):
        query = ""
        for word in message.content.split():
            query += word + " "
        query = query.replace('>_', '')
        if(query == " "):
            await message.channel.send(embed=arg_missing_message)
            return
        await message.channel.send(embed=(discord.Embed(title=title + " Query Output:", description=str(execute_query(query)), color=gray_color)))

client.run(token)