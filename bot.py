import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('!help'):
        await client.send_message(message.channel, 'usage: \n'
            +'The Armory Bot Help - options and arguments:\n'
            +'!help : display available options\n'
            +'!hello : greet the user\n'
            +'!test  : post the number of messages a user has in a channel\n'
            +'!sleep : put the bot to sleep for 5 seconds\n')

    elif message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run('token_goes_here')