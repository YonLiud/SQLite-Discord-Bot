import sqlite3
from sqlite3 import Error
import discord

token = open("token.txt", "r").read()
client = discord.Client()
conn_connected = False
conn = None


# Database

database_file = r"database.db"

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def close_conn():
    conn_connected = False
    if conn:
        conn.close()
    print("closed conn")


def main():
    print("accessed main")

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
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

    # create a database connection
    conn = create_connection(database_file)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")



# Discord Bot
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

start_con_message = discord.Embed(title='Prompt',description='Starting connection to Database')
close_con_message = discord.Embed(title='Prompt',description='Closing Connection to Database')
already_open_con_message = discord.Embed(title='Prompt',description='Connection already active')
already_closed_con_message = discord.Embed(title='Prompt',description='Connection already closed')
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

client.run(token)