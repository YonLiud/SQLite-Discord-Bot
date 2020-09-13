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

def main(request = None, identifier = 0, column = ""):

    sql_create_students_table = """CREATE TABLE IF NOT EXISTS students (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    GPA integer NOT NULL,
                                    major text NOT NULL
                                );"""

    # create a database connection*
    conn = create_connection(database_file)
    # create tables
    if conn is not None:
        create_table(conn, sql_create_students_table)
    else:
        print("Error! cannot create the database connection.")

    if(request == "select_by_id"):
        return select_student_by_ID(conn, identifier, column)


def select_student_by_ID(conn, user, request):
    try:
        c = conn.cursor()
        query = ("SELECT * FROM students WHERE id=",user)
        print(query)
        c.execute(query)
        info = ""
        print(c.fetchall())
        return info
    except Exception as e:
        print(e)

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
arg_missing_message = discord.Embed(title=titleM, description='an argument is missing ">select [Integer] [COLUMN]"')

@client.event
async def on_message(message):
    global conn_connected
    if message.author == client.user:
        return

    if message.content.startswith('>connect'):
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

    if message.content.startswith('>select'):
        try:
            args1 = message.content.split()[1]
            args2 = message.content.split()[2]
        except:
            await message.channel.send(embed=arg_missing_message)
            return
        if args1.isnumeric():
            output = ""
            print(main("select_by_ID", args1, args2))
            await message.channel.send(embed=(discord.Embed(title=titleM, description="placeholder")))

client.run(token)