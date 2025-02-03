# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
from bottoken import token
import serial
import time

bytedelay = 0.00057346
dot_feed_s = 0.0021
dot_print_s = 0.03
line_spacing = 6

uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=3000)

def write_char(char: str) -> None:
    resume = time.monotonic() + bytedelay
    while time.monotonic() < resume:
        pass
    uart.write(bytes(char, "ascii"))
    if char == "\n":
        resume = time.monotonic() + + line_spacing*dot_feed_s
        while time.monotonic() < resume:
            pass
    
def write(text: str) -> None:
    for char in text:
        write_char(char)
    


description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author.id == bot.user.id:
        return
    if message.content.startswith('Ping'):
        await message.reply('Ping', mention_author=True)
    if message.content.startswith('Print'):
        text = message.content[5:]
        write(text)
        write_char("\n")
        write_char("\n")
        write_char("\n")
        write_char("\n")
        await message.reply('printed:' + text, mention_author=True)
        print('printed: ' + text)

bot.run(token)
