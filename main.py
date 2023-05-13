TOKEN = '' #input Token here

import discord
import fact
import user_help
import animals
import chat

#allows bot to read all messages
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

Mess = True
add = False


@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  global Mess
  global add

  if message.author == client.user:
    return

  if Mess == True:
    intro = f'Welcome {message.author.mention} !\nI am your Daily Dose of Mother Earth Bot.\nType $help to see the availiable commands (❁´◡`❁)'
    await message.channel.send(intro)
    await message.channel.send(file=discord.File('Earth.gif'))
    #source of gif: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F565342559472609097%2F&psig=AOvVaw04o3I_0jhJUDyqo2ibb52_&ust=1682786975994000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCNiUw5KEzf4CFQAAAAAdAAAAABAE
    Mess = False

  else:
    if message.content == '$fact':
      await message.channel.send(fact.printFact())

    elif message.content.startswith('$help'):
      await message.channel.send(user_help.help())

    elif message.content.startswith('$animals'):
      if message.content.lower() == '$animals africa':
        select = animals.info('africa')
        await message.channel.send(select[0])
        await message.channel.send(file=discord.File(select[1]))
      elif message.content.lower() == '$animals australia':
        select = animals.info('australia')
        await message.channel.send(select[0])
        await message.channel.send(file=discord.File(select[1]))
      elif message.content.lower() == '$animals america':
        select = animals.info('america')
        await message.channel.send(select[0])
        await message.channel.send(file=discord.File(select[1]))
      elif message.content.lower() == '$animals europe':
        select = animals.info('europe')
        await message.channel.send(select[0])
        await message.channel.send(file=discord.File(select[1]))
      elif message.content.lower() == '$animals antartica':
        select = animals.info('antartica')
        await message.channel.send(select[0])
        await message.channel.send(file=discord.File(select[1]))
      elif message.content.lower() == '$animals asia':
        select = animals.info('asia')
        await message.channel.send(select[0])
        await message.channel.send(file=discord.File(select[1]))

    else:
      await message.channel.send(chat.reply(message.content.lower()))
      print(message.content)

client.run(TOKEN)
