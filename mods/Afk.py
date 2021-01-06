import discord 
import asyncio
import random
import datetime

intents = discord.Intents.all()
intents.members = True

from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


#from PIL import Image, ImageOps, ImageDraw, ImageFilter, ImageFont
#from io import BytesIO

client = commands.Bot(command_prefix="&", intents=intents)

@client.event
async def on_ready():

    await client.change_presence(status=discord.Status.online, activity=discord.Game("Playing Ghost of War"))

    print("The bot is ready")

    #@client.event
#async def on_ready():
    # setting play
   ## await client.change_presence(activity=discord.Game(name=f"on {len(client.guilds)} server"))
    # setting stream
  ##  await client.change_presence(activity=discord.Streaming(name"My Stream", url=my_twitch_url))
    # setting status
  ##  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name))

 #@client.event
 #async def on_member_join(member):
     #channel = discord.utils.get(member.guild.channels, name="『🔺』welcome")
     #await channel.send(f"**{member.mention}** welcome test {len(list(member.guild.member))}")

def convert(time):
    pos =["s","m","h","d"]
    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}
    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


@client.command()

async def hello(ctx):

 await ctx.send("Hi")

@client.command(aliases=['c'])

@commands.has_permissions(manage_messages = True)

async def clear(ctx, amount=2):

     await ctx.channel.purge(limit=amount)

     await ctx.send(f"{amount} message were cleared")

@client.command(aliases=['k'])

@commands.has_permissions(kick_members = True)

async def kick(ctx,member : discord.Member,*,reason= "no reason Provided"):

   await member.send("You have been kicked from the server, if you think it's an mistake please kindly contact in our mail benzitczo2015@gmail.com or contact any of the staff members from the server Reason: "+reason)

   await member.kick(reason=reason)

   embed = discord.Embed(title='Kicked', description=f"{member} has been Kicked from the server", color=discord.Color(0xf00))

   await ctx.send(embed=embed)

@client.command(aliases=['b'])

@commands.has_permissions(ban_members = True)

async def ban(ctx,member : discord.Member,*,reason= "no reason Provided"):

    await member.send("You have been Banned from the server, if you think it's an mistake please kindly contact in our mail benzitczo2015@gmail.com or DM any of the staff members from the server Reason: "+reason)

    await member.ban(reason=reason)

    embed = discord.Embed(title='Banned', description=f"{member} has been banned from the server", color=discord.Color(0xf00))

    await ctx.send(embed=embed)

@client.command()

async def codes(ctx):

 await ctx.send("""
    Code: GIFT - 100 Gold
 Code: EXLEGIONARY - 100 = Gold
 Code: ALPHA - 50 Gold
 Code: W3N3SDAY - 100 Gold [Expired]
 Code: BF2611 - 1 key Oro [Expired]
 Code: G19KY - 100 
 Code: G1EF9 1 key gold [Expired]
 Code: G1FU8 2 key gold [Expired]
 Code: G1PQ3 50 gold [Expired]
 Code: G1ALO 2000 silver [Expired]
 Code: G1RC9 2 silver key [Expired]
 Code: G1L3Z skin ppsh [Expired]
 
 **More codes will be available soon!**""")

@client.command()
@commands.has_permissions(manage_messages = True)
async def suggests(ctx):
 await ctx.send("""
In suggestion channel users we write their suggestions and when they are done the bot should automatically send their message in the suggestion-report channel""")

 ##embed = discord.Embed(title='Banned', description=f"{member} has been banned from the server", color=discord.Color(0xFF))

 ##await ctx.send(embed=embed)

@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)

async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            #await ctx.send(f'{member} has been unbanned from the server')
            embed = discord.Embed(title='UnBanned', description=f"{member} has been ubanned from the server", color=discord.Color(0x33))
            await ctx.send(embed=embed)
            return

@client.command()
async def suggest(ctx,*,message):
    imgembed= discord.Embed(title="SUGGESTIONS", description=f"{message}")
    imgembed.set_footer(text=f"By: {ctx.author}", icon_url=ctx.author.avatar_url)
    ##imgembed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    try:
        image = ctx.message.attachments[0].url
        imgembed.set_image(url=image)
    except IndexError:
        image = None
    message = await ctx.send(embed=imgembed)
    await ctx.message.delete()
    await message.add_reaction("✅")
    await message.add_reaction("❌")

@client.command()
async def wanted(ctx, member: discord.Member = None):
    if member == None:
        user = ctx.author
    else:
        user = member
    
    wanted = Image.open("Wanted.jpg")

    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((345,345)) 

    wanted.paste(pfp, (135,295))

    wanted.save("profile.jpg")

    await ctx.send(file = discord.File("profile.jpg"))

@client.command()
async def avatar(ctx, member: discord.Member):
    show_avatar = discord.Embed(
        title =f'{member}',
        color = discord.Color.dark_blue()
    )
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=show_avatar)

@client.command()
async def ping(ctx):
    await ctx.channel.send(f"ping {round(client.latency*1000)} ms")

@client.command()
#commands.has_guild_permissions
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, words):
    await asyncio.sleep(1)
    await ctx.message.delete()
    await ctx.send(f"{words}" .format(words))
    embed = discord.Embed (title=f'{ctx.author}')   

@client.command()
async def gow(ctx, member : discord.Member): 
    img = Image.open("gowperfil.png")
    draw = ImageDraw.Draw(img)
    number1 = random.randrange(0,999999)
    number2 = random.randrange(0,999999)
    number3 = random.randrange(0,999999)
    font = ImageFont.truetype("arial.ttf", 24)
    draw.text((75,45), f"{member.name}#{member.discriminator}", (255, 255, 255), font = font)
    # Here \/
    draw.text((456,50), f"{number1}", (255, 255, 255), font = font)
    draw.text((674,50), f"{number2}", (255, 255, 255), font = font)
    draw.text((885,50), f"{number3}", (255, 255, 255), font = font)
    img.save("gowfake.png")
    await ctx.send(file = discord.File("gowfake.png"))


@client.command(aliases=['user','info'])
@commands.has_permissions(kick_members=True)
async def whois(ctx, member: discord.Member = None):
    roles = [role for role in member.roles]
    embed = discord.Embed(title = member.name , status = member.status , description = member.mention , color = discord.Colour.green())
    embed.add_field(name="Created Account:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name = "ID" , value = member.id , inline = True)
    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    embed.add_field(name="Status:", value = member.status)
    ##print(member.top_role.mention)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member:discord.Member, *, reason=None):
 arg=reason
 author=ctx.author
 guild=ctx.message.guild
 overwritee = discord.PermissionOverwrite()
 overwrite = discord.PermissionOverwrite()
 channel = get(guild.text_channels, name='〘📋〙log')
 mrole = get(ctx.guild.roles, name="Multi-Galaxy")

 if channel is None:
  channel = await guild.create_text_channel('〘📋〙log', category=category)
  overwritee.read_messages = False
  overwritee.read_message_history = False
  overwritee.send_messages = False
  overwrite.read_messages = True
  overwrite.read_message_history = True
  overwrite.send_messages = True
  await channel.set_permissions(guild.default_role, overwrite=overwritee)
  await channel.set_permissions(mrole, overwrite=overwrite)

 if member is None:
  await ctx.send("Please specify a user and/or reason!")

 await channel.send(f'{member.mention} got warned for: ```\n{arg}\n``` Warned by: {author}')
 await member.send(f'You got warned for: ```\n{arg}\n``` Warned by: {author} - Server: **{guild.name}**')
 await ctx.send(f'{member.mention} got warned for: ```\n{arg}\n``` Warned by: {author}')
 await ctx.message.delete()


@client.command()
@commands.has_role("[🌕] Giveaway Manager") #[🌕] Giveaway Manager - #tetstt
async def giveaway(ctx):
    await ctx.send("Lets start with this giveaway! Asnwer these Questions within 15 seconds!")
    Questions = ["Which Channel should it be hosted in?",
                 "What should be the uration of the giveaway? example: 1s (seconds) , 1m (minutes) , 1h (hour) , 1d (day)",
                 "How many winners?",
                 "What is the prize of the giveaway?"]

    asnwers = []
    def check(m):
      return m.author == ctx.author and m.channel == ctx.channel

    for i in Questions:
        await ctx.send(i)

        try:
           msg = await client.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
           await ctx.send('You didn\'t asnwer in time, please be quicker next time!')
           
        else:
            asnwers.append(msg.content)

        try:
         c_id = int(asnwers[0][2:-1])
        except:
           await ctx.send(f"You didnt mention a channel properly do it like this {ctx.channel.mention} next time.")
        

    channel = client.get_channel(c_id)

    time = convert(asnwers[1])
    amt_winners = asnwers[2]
    try: 
        int(amt_winners)
    except ValueError:
        await ctx.send("Error message here if amount of winners is not an integer")
        

    if time == -1:
        await ctx.send(f"You didnt asnwer the time with a proper unit. Use (s|m|h|d next time!")
        
        
    elif time == -2:
        await ctx.send(f"The time must be an integer. Please enter an integer next time")
        

    prize = asnwers[3]
    role = ctx.guild.get_role(791305176098275328)
    #await ctx.send(f"The giveaway will be in {role.mention} and will last {asnwers[1]}!")
    imgembed = discord.Embed(title = "GIVEAWAY! | GHOSTS OF WAR", description = f"{prize}", color = ctx.author.color)
    try:
        image = ctx.message.attachments[0].url
        imgembed.set_image(url=image)
    except IndexError:
        image = None
    #embed.set_footer(text = f"Amount of Winners: {asnwers[2]}")

    ##end = datetime.datetime.utcnow() + datetime.timedelta(seconds = min*60)
    ##imgembed.add_field(name = "End At:", value = f"{end}")
    imgembed.add_field(name = "Amount of Winners:", value = asnwers[2])
    imgembed.add_field(name = "Hosted by:", value = ctx.author.mention)
    imgembed.set_footer(text = f"Ends at {asnwers[1]} from now")

    my_msg = await channel.send(embed = imgembed)

    await my_msg.add_reaction("🎉")

    await asyncio.sleep(time)
  
    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winners = []
    for i in range(int(asnwers[2])):
     user = random.choice(users)
     while user.mention in winners:
       user = random.choice(users)
     winners.append(user.mention)
    
    await channel.send(f"Congratulations! {', '.join([winner for winner in winners])} for winning {prize}! - Please messages private write to {ctx.author.mention}")

@client.command()
@commands.has_role("[🌕] Giveaway Manager")
async def reroll(ctx, channel : discord.TextChannel, id_ : int):
       try:
        new_msg = await channel.fetch_message(id_)
       except:
         await ctx.send("The id was entered incorrectly.")
         return

       users = await new_msg.reactions[0].users().flatten()
       users.pop(users.index(client.user))

       winner = random.choice(users) 

       await channel.send(f"Congratulations! {winner.mention} won {prize}!")





client.run("NzgyNzE2MjQ1OTMyOTAwNDQz.X8QPTw.4gYl3rLfhfdoOGPEa1XOp7DjfNQ")



