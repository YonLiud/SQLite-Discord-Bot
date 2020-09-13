import sqlite3
from sqlite3 import Error
import discord

token = open("token.txt", "r").read()
client = discord.Client()
conn_connected = False
conn = None


# ? Database

database_file = r"database.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def display_tables():
    if conn:
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        total_names = ""
        for table_name in tables:
            table_name = table_name[0]
            total_names += table_name + " "
        print(total_names)
        return total_names

def close_conn():
    global conn_connected
    conn_connected = False
    conn.close()
        



def main():

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL
                                );"""

    # create a database connection*
    conn = create_connection(database_file)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")



# ? Discord Bot
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

titleM = 'SQLite Discord Shell'

start_con_message = discord.Embed(title=titleM,description='Starting connection to Database')
close_con_message = discord.Embed(title=titleM,description='Closing Connection to Database')
already_open_con_message = discord.Embed(title=titleM,description='Connection already active')
already_closed_con_message = discord.Embed(title=titleM,description='Connection already closed')
list_table_message = discord.Embed(title=titleM, description=display_tables())
list_missing_message = discord.Embed(title=titleM, description="List request was not specified")

@client.event
async def on_message(message):
    global conn_connected
    if message.author == client.user:
        return

    if message.content.startswith('>db'):
        if (conn_connected==False):
            main()
            await message.channel.send(embed=start_con_message)
            conn_connected = True
        else:
            await message.channel.send(embed=already_open_con_message)

    if message.content.startswith('>quit'):
        if (conn_connected==True):
            close_conn()
            await message.channel.send(embed=close_con_message)
        else:
            await message.channel.send(embed=already_closed_con_message)

    if message.content.startswith('>list'):
        try:
            if message.content.split()[1] == 'tables':
                await message.channel.send(embed=list_table_message)
        except:
                await message.channel.send(embed=list_missing_message)
client.run(token)