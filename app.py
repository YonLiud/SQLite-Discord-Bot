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


def select_student_by_ID(user, request):
    if conn is not None:
        c = conn.cursor()
        query = ("SELECT "+ request +" FROM students WHERE id="+user)
        print(query)
        c.execute(query)
        info = ""
        print(c.fetchall())
        return "placeholder"
    return "err"

def close_conn():
    global conn_connected
    conn_connected = False
    conn.close()
        


# ? Discord Bot
@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

titleM = 'SQLite Discord Shell'

start_con_message = discord.Embed(title=titleM,description='Starting connection to Database')
close_con_message = discord.Embed(title=titleM,description='Closing Connection to Database')
already_open_con_message = discord.Embed(title=titleM,description='Connection already active')
already_closed_con_message = discord.Embed(title=titleM,description='Connection already closed')
arg_missing_message_select = discord.Embed(title=titleM, description='an argument is missing ">select [Integer] [COLUMN]"')
arg_missing_message_create_table = discord.Embed(title=titleM, description='an argument is missing ">create [name] []"')


@client.event
async def on_message(message):
    global conn_connected
    if message.author == client.user:
        return

    if message.content.startswith == ('>create'):
        try:
            args1 = message.content.split()[1]
        except:
            await message.channel.send(embed=arg_missing_message_create_table)
            return
        if args1.isAlpha():
            pass


    if message.content.startswith('>select'):
        try:
            args1 = message.content.split()[1]
            args2 = message.content.split()[2]
        except:
            await message.channel.send(embed=arg_missing_message_select)
            return
        if args1.isnumeric():
            await message.channel.send(embed=(discord.Embed(title=titleM, description=select_student_by_ID(args1, args2))))
            return

client.run(token)