from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command
async def ゾラ・マグダラオス(ctx):
    embed = discord.Embed(title="ゾラ・マグダラオス", color=0xff3300)
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/e3KTLkU4xuFllQQUjAXezCEW1MDmN08eZGjfQE_-yU4/https/monsterhunterworld.wiki.fextralife.com/file/Monster-Hunter-World/Zorah-Magdaros-mhw-Icon-small.png")
    embed.add_field(name="属性", value=":fire:火", inline=True)
    embed.add_field(name="属性やられ", value=":fire:火属性やられ")
    embed.add_field(name="弱点", value=":dragon:龍(:star::star::star:)\n\n:sweat_drops:水(:star::star::star:)")
    embed.add_field(name="抵抗", value=":fire:火")
    embed.add_field(name="基礎体力", value="12000")
    embed.add_field(name="サイズ", value="♝最小冠：0\n♔銀冠：0\n♕金冠：0")
    embed.set_image(url="https://pbs.twimg.com/media/DOFaYWmU8AAo1a6.png")

    await ctx.send(embed=embed)



bot.run(token)
