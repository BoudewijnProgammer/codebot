token = "NDM1NTA2ODA5MDMwMDQ5ODA1.DpGRug.2MCFnFLe3-k2gSaPemGz7-zGd6M"
# Your token is required for this bot to work.

print('Loading CodeAdmin')

import discord
import logging
from discord.ext import commands
import asyncio
import datetime
# Required imports for this bot to work.

client = commands.Bot(command_prefix = '<')
Client = discord.Client
# Defines the discord client.

name = "CodeAdmin"
# Some definitions for this bots own usage.

logging.basicConfig(level=logging.INFO)
# Sets the logging level.


@client.event
async def on_member_join(member):
    await client.send_message(member, 'Welcome to the server! If you want to invite CodeAdmin u can just click this link: https://discordapp.com/oauth2/authorize?client_id=435506809030049805&scope=bot&permissions=8 Have fun!')
    print('Sent message to ' + member.name)



@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name= str(len(client.servers)) + " servers", type=3)) 
    print("-------------")
    print(name + ". Running as " + client.user.name + " with the ID " + client.user.id + ".")
    print("-------------")
    
# Shows message on boot and sets game.

@client.command(pass_context=True)
async def ban(ctx, member: discord.Member = None):
    author = ctx.message.author
    channel = ctx.message.channel
    if ctx.message.author.server_permissions.ban_members:
        if member is None:
            embed = discord.Embed(color=0xfffdfd, timestamp=datetime.datetime.utcnow())
            embed.add_field(name=":exclamation: | Error", value="Please specify a user for me to ban!", inline=False)
            embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/435510609388503051/495969309764354048/3.png", text="Kick Error")
            await client.say(embed=embed)
        else:
            await client.ban(member)
            embed = discord.Embed(color=0xfffdfd, timestamp=datetime.datetime.utcnow())
            embed.add_field(name=":white_check_mark: | Banned User:", value=f"{member.mention}", inline=False)
            embed.add_field(name="Banned By:", value=f"{author.mention}", inline=True)
            embed.add_field(name="Banned In:", value=f"{channel.mention}", inline=True)
            embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/435510609388503051/495969309764354048/3.png", text="Banned user")
            await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0xfffdfd, timestamp=datetime.datetime.utcnow())
        embed.add_field(name=":exclamation: | Error", value="You do not have the right permission. Required Permissions for this is: **Ban Members**", inline=False)
        embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/435510609388503051/495969309764354048/3.png", text="CodeAdmin Ban Error")
        await client.say(embed=embed)


@client.command(pass_context=True)
async def kick(ctx, member: discord.Member = None):
    author = ctx.message.author
    channel = ctx.message.channel
    if ctx.message.author.server_permissions.ban_members:
        if member is None:
            embed = discord.Embed(color=0xfffdfd, timestamp=datetime.datetime.utcnow())
            embed.add_field(name=":exclamation: | Error", value="Please specify a user for me to kick!", inline=False)
            embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/435510609388503051/495969309764354048/3.png", text="Kick Error")
            await client.say(embed=embed)
        else:
            await client.kick(member)
            embed = discord.Embed(color=0xfffdfd, timestamp=datetime.datetime.utcnow())
            embed.add_field(name=":white_check_mark: | Kicked User:", value=f"{member.mention}", inline=False)
            embed.add_field(name="Kicked By:", value=f"{author.mention}", inline=True)
            embed.add_field(name="Kicked In:", value=f"{channel.mention}", inline=True)
            embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/435510609388503051/495969309764354048/3.png", text="Kicked user")
            await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0xfffdfd, timestamp=datetime.datetime.utcnow())
        embed.add_field(name=":exclamation: | Error", value="You do not have the right permission. Required Permissions for this is: **Kick Members**", inline=False)
        embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/435510609388503051/495969309764354048/3.png", text="CodeAdmin Kick Error")
        await client.say(embed=embed)


@client.command(pass_context=True)
async def clear(ctx, amount=None):
    if ctx.message.author.server_permissions.manage_messages:
        if amount is None:
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the amount of messages you want me to delete!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            channel = ctx.message.channel
            author = ctx.message.author
            messages = []
            async for message in client.logs_from(channel, limit=int(amount)):
                messages.append(message)
            await client.delete_messages(messages)
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Clear - Information')
            embed.add_field(name='Amount:', value='**I have deleted {} messages**'.format(amount), inline=False)
            embed.add_field(name='Author:', value='**{}**'.format(author.name), inline=False)
            msg = await client.say(embed=embed)
            await asyncio.sleep(5)
            await client.delete_message(msg)
    else:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You cant use this command. Permission Required: ``Manage Messages``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)



@client.command()
async def invite():
    embed = discord.Embed(color=0xfffdfd, timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Invite Link ***__Regular__***", value="[__Link Here__](https://discordapp.com/oauth2/authorize?client_id=435506809030049805&scope=bot&permissions=8)", inline=False)
    await client.say(embed=embed)


@client.command()
async def codeadmin():
    embed = discord.Embed(color=0xfffdfd, timestamp=datetime.datetime.utcnow())
    embed.add_field(name="CodeAdmin Help", value="Prefix = < Commands = info(mention), invite, kick, ban, clear and much more!(https://discordapp.com/oauth2/authorize?client_id=435506809030049805&scope=bot&permissions=8)", inline=False)
    await client.say(embed=embed)


@client.command()
async def developer():
    embed = discord.Embed(color=0xfffdfd, timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Developer", value="CodeAdmin is created by Boudewijn#6466", inline=False)
    await client.say(embed=embed)


@client.command(pass_context=True)
async def userinfo(ctx, user: discord.Member = None):
    if user is None:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! Please specify a user for me to give info about!', inline=False)
        await client.say(embed=embed)
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x36393E)
    embed=discord.Embed(color=0x36393E)
    embed.add_field(name="**Users Name Is:**", value="{}".format(user.name), inline=False)
    embed.add_field(name="**Highest Role Is:**", value="{}".format(user.top_role), inline=False)
    embed.add_field(name="**Users ID Is:**", value="{}".format(user.id), inline=False)
    embed.add_field(name="**Users Nickname Is:**", value="{}".format(user.nick), inline=False)
    embed.add_field(name="**Users Status Is:**", value="{}".format(user.status), inline=False)
    embed.add_field(name="**Users Game Is:**", value="{}".format(user.game), inline=False)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)





@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

players = {}
@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

client.run(token)

