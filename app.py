import discord

client = discord.Client()
activated = False

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

welcome_message = discord.Embed(title='Prompt',description='Activated')
goodbye_message = discord.Embed(title='Prompt',description='Deactivated')
@client.event
async def on_message(message):
    global activated
    if message.author == client.user:
        return

    if message.content.startswith('>'):
        if (activated==False):
            await message.channel.send(embed=welcome_message)
            activated = True
        else:
            await message.channel.send(embed=goodbye_message)
            activated = False

client.run("NzU0NjIzNTQzNTI2MDMxNDgy.X13b8Q.rp0Yx-Iq8XHFZGyC_G3_nLAZ5K4")