import config
from discord.ext.commands import Bot
import discord

import asyncio
import logging
import datetime

import websockets

pBot = Bot(command_prefix=config.PREFIX)

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

#Command for testing purposes
@pBot.command(hidden=True)
async def socket(ptoken):
    for name, service in config.services.items():
        async with websockets.connect(service['url']) as websocket:
            msg = ptoken
            await websocket.send(msg)

            resp = await websocket.recv()
            await pBot.say(resp)

pBot.run(config.TOKEN)
