import config
from discord.ext.command import Bot
import discord

import asyncio
import logging
import datetime

pBot = Bot(commandprefix=config.PREFIX)

@pBot.event
async def on_ready():
    print('------')
    print('Bot Online')
    print(pBot.user.name)
    print(pBot.user.id)
    print('------')
    await pBot.change_presence(game=discord.Game(type=0,name=config.msg+' | '+config.PREFIX+'help'), afk=False)

@pBot.command()
async def ping():
    return await pBot.say('PONG!')
