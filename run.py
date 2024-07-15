import discord
from discord.ext import commands
import base64

fkwoafiosahio = 'TVRJMk1qSXhPVFUzTVRFeU1UYzFOREV4TXcuR2VIdWw4LjlRQ0ZlclFtLWx3X0FOaGkxRnR5OF9FWDB1RWpYclpTRkJaVVln'
jiosfuiowhuog = base64.b64decode(fkwoafiosahio)
kfopwajfisidj = jiosfuiowhuog.decode('utf-8')

sjadoijwiofgh = 'MTI2MDAzMzI5MDk3NTQ0OTEyMA=='
ejfioasiudhui = base64.b64decode(sjadoijwiofgh)
djfioajisojdi = ejfioasiudhui.decode('utf-8')

jwifjasoijdio = 'MTI2MDAzMzI5MDk3NTQ0OTEyMw=='
fiojasiodjiow = base64.b64decode(jwifjasoijdio)
sdwijaiosjfio = fiojasiodjiow.decode('utf-8')

jiwjdwjajdsoi = 'UEMgaXMgYm9vdGVkLg=='
faioskdopwkoo = base64.b64decode(jiwjdwjajdsoi)
odakopfksopos = faioskdopwkoo.decode('utf-8')

intents = discord.Intents.default()
intents.message_content = True 


bot = commands.Bot(command_prefix='grb$', intents=intents)

@bot.event
async def on_ready():
    guild = bot.get_guild(int(djfioajisojdi))
    if guild is None:
        return
    
    channel = guild.get_channel(int(sdwijaiosjfio))
    if channel:
        await channel.send(str(odakopfksopos))

bot.run(str(kfopwajfisidj))