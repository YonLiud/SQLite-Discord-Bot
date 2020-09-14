import sqlite3
from sqlite3 import Error
import discord

token = open("token.txt", "r").read()
client = discord.Client()
conn_connected = False


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

def main():

    sql_create_students_table = """CREATE TABLE IF NOT EXISTS students (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    GPA integer NOT NULL,
                                    major text NOT NULL
                                );"""

    # create tables
    if conn is not None:
        create_table(conn, sql_create_students_table)
    else:
        print("Error! cannot create the database connection.")


def execute_query(query):
    if conn is not None:
        output = ""
        c = conn.cursor()
        print(query)
        c.execute(query)
        info = c.fetchall()
        conn.commit()
        for value in info:
            output += str(value) + " "
        return output
    return "err"


def close_conn():
    global conn_connected
    conn_connected = False
    conn.close()
        


# ? Discord Bot
@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

title = 'SQLite Discord Shell'
arg_missing_message = discord.Embed(title=title, description='Arguments are missing')


@client.event
async def on_message(message):
    global conn_connected
    if message.author == client.user:
        return

    if message.content.startswith == ('>create'):
        try:
            args1 = message.content.split()[1]
        except:
            await message.channel.send(embed=arg_missing_message)
            return
        if args1.isAlpha():
            pass


    if message.content.startswith('>_'):
        try:
            args1 = message.content.split()[1] 
        except:
            await message.channel.send(embed=arg_missing_message)
            return
        query = ""
        for word in message.content.split():
            query += word + " "
        query = query.replace('>_', '')
        print("query = " + query)
        await message.channel.send(embed=(discord.Embed(title=title, description=str(execute_query(query)))))

client.run(token)