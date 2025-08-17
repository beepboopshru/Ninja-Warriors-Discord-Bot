import discord
import os
from discord.ext import commands
import random
import tracemalloc
from alive import keep_alive
from discord.utils import get
import datetime

tracemalloc.start()
client = commands.Bot(command_prefix=">", intents=discord.Intents.all())
channel = 0


@client.command(name='banme')
async def text(ctx):

    await ctx.author.send("https://discord.gg/6SwjyCevKv")
    await ctx.channel.send("bozo just banned himself lmfao")
    await ctx.guild.kick(ctx.author)


@client.event
async def on_ready():
    bot_logs = client.get_channel(873444752798916619)
    await bot_logs.send("Bot Online ")
    vc = client.get_channel(829434299970224208)
    await vc.connect()
    lol = random.sample(range(1, 8), 1)
    print(lol)
    if (lol == [1]):
        await client.change_presence(activity=discord.Game(
            name="with ninjas lolis"))
    elif (lol == [2]):
        await client.change_presence(activity=discord.Game(
            name="Loli smashing simulator"))
    elif (lol == [3]):
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching, name="Redo of healer"))
    elif (lol == [4]):
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching, name="hanime.tv"))
    elif (lol == [5]):
        await client.change_presence(activity=discord.Game(name="AMOONG US"))
    elif (lol == [6]):
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching, name="cocomelon"))
    elif (lol == [7]):
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening,
                                      name="To graeps old voice :grief:"))


@client.command(name='ghost')
@commands.has_role('Staff')
async def ghostPing(ctx):
    if (ctx.channel.id == 505461683955826699):
        await ctx.send("@everyone")
        await ctx.channel.purge(limit=2)
    else:
        await ctx.channel.send("Why you tryna ghost ping everyone bitch")


@client.command(name="test")
@commands.has_role('Manager')
async def embed(ctx):
    embed = discord.Embed(
        title="ABOUT US",
        description=
        "This embed shows you the basic information about the guild Ninja Warriors [NW]",
        color=0x069eea)
    embed.set_thumbnail(url="https://imgur.com/a/qDq471m")
    embed.add_field(
        name=
        "This guild was created on 30th August 2018 by ninjaluv and Haxxxxx  We were a group of friends that played Bedwars together, our group got bigger so we decided to make a guild. ",
        value=
        "The guild was really dead in 2019 and  it continued like that into early 2020, but then the lock downs happened and with nothing to do people started playing hypixel a lot more and we quickly gained more activity and made our way up to top 50.",
        inline=False)
    embed.add_field(name="Guild master", value="ninjaluv", inline=False)
    embed.add_field(name="Owner",
                    value="Haxxxx, Graep, Ghostie20, cFlop",
                    inline=False)
    embed.add_field(name="Officers",
                    value="Vrnn, Fiforious, Hensteve, Leah",
                    inline=False)
    embed.add_field(name="Trial Officers",
                    value="yan, JonJonNinja",
                    inline=False)
    embed.add_field(name="Our Socials", value="Links:", inline=False)
    embed.add_field(
        name="Guild YouTube: ",
        value=" https://www.youtube.com/channel/UCuaTo1pG8h44uaXUcE9vK1g",
        inline=False)
    embed.add_field(name="Guild Twitter",
                    value="https://twitter.com/NinjaWarriorsG",
                    inline=False)
    embed.add_field(name="Guild Discord",
                    value=" https://discord.gg/6SwjyCevKv",
                    inline=False)
    embed.add_field(
        name="Guild Thread",
        value=
        "https://hypixel.net/threads/top-50-theninjawarriors-%E2%98%86ninja%E2%98%86-guild-level-120-open.3847608/",
        inline=False)
    embed.add_field(
        name="Guild Snapchat",
        value=
        "https://www.snapchat.com/invite/NjRjMzdiNTItNTA5Mi00ZmI0LWEwYzItZWNiN2NjMzBlYTRk/ODVlMTFlNjgtNDQyMC00MTIwLTg0NjctMDgxNWMwNDZlZDlj/",
        inline=False)
    embed.add_field(
        name="GvG Captains:",
        value=
        "The Following members are GvG Captains. DM any captain for organizing a GvG or a tryout\n@ninjaluv  (Overall GvG Captain)\nHaxxxxx  /  vrn  (Skywars GvG)\nninjaluv\nHaxxxxx (UHC Duels GvG)\ndephobics (Bridge duels GvG) \nGraep (valorant GvG)",
        inline=False)
    embed.add_field(name="Guilds we are merged with",
                    value="❥ TheEdge \n❥ Valour ",
                    inline=False)
    embed.add_field(
        name="Alliances:",
        value=
        "The Guilds we are allied with\n❥Miscellaneous: https://discord.gg/bHFWukp\n❥Lucid:   https://discord.gg/DDTMad2pYR",
        inline=False)
    embed.set_footer(text="Info Inscribed by Ninjaluv || Coded into by cFlop")
    await ctx.send(embed=embed)


@client.command(name="ticket")
@commands.cooldown(1, 21000, commands.BucketType.user)
async def make_channel(ctx):
    await ctx.channel.purge(limit=1)
    guild = ctx.guild
    member = ctx.author
    category = discord.utils.get(ctx.guild.categories,
                                 name="┌━━━Apps & tickets━━━┐")
    print(category)
    admin_role = get(guild.roles, name="Staff")
    today = datetime.datetime.now()
    date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
    overwrites = {
        guild.default_role:
        discord.PermissionOverwrite(read_messages=False),
        guild.me:
        discord.PermissionOverwrite(read_messages=True),
        admin_role:
        discord.PermissionOverwrite(read_messages=True),
        member:
        discord.PermissionOverwrite(read_messages=True,
                                    read_message_history=True)
    }
    channel = await guild.create_text_channel("📃-ticket",
                                              category=category,
                                              overwrites=overwrites)
    author = ctx.author.id
    await channel.send("TICKET CREATED ON: " + date_time)
    await channel.send(
        '<@' + str(author) + '>' +
        "``` This the ticket that you created. Explain the circumstances to be in direct contact with a staff member.```\n```If you have created this ticket for feedback of an event or a suggestion to be made for the discord you can do that here aswell.```"
    )
    await channel.send(
        "Type >close if your answers have been answered to your satisfaction")


@client.command(name='rng')
async def RandomNumberGenerator(ctx, arg: int):
    if arg < 10000:
        rando = random.sample(range(0, arg), 1)
        embed = discord.Embed(title=rando, color=0x000000)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Enter a proper argument", color=0x000000)
        await ctx.send(embed=embed)


@client.command(name='apply')
@commands.cooldown(1, 21000, commands.BucketType.user)
async def make_channel(ctx):
    await ctx.channel.purge(limit=1)
    guild = ctx.guild
    member = ctx.author
    category = discord.utils.get(ctx.guild.categories,
                                 name="┌━━━Apps & tickets━━━┐")
    today = datetime.datetime.now()
    date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
    admin_role = get(guild.roles, name="Staff")
    overwrites = {
        guild.default_role:
        discord.PermissionOverwrite(read_messages=False),
        guild.me:
        discord.PermissionOverwrite(read_messages=True),
        admin_role:
        discord.PermissionOverwrite(read_messages=True),
        member:
        discord.PermissionOverwrite(read_messages=True,
                                    read_message_history=True)
    }
    channel = await guild.create_text_channel("📃-application",
                                              category=category,
                                              overwrites=overwrites)
    author = ctx.author.id
    random_App = random.sample(range(1, 8), 1)
    await channel.send("APPLICATION CREATED ON: " + date_time)
    if random_App == [1]:
        await channel.send(
            "<@" + "505398389605793792" + ">" +
            " Is assigned to your application. DM him if you require any assistance while making your app"
        )  #cFlop
    elif random_App == [2]:
        await channel.send(
            "<@" + "708721265237819403" + ">" +
            " Is assigned to your application. DM him if you require any assistance while making your app"
        )  #ninja
    elif random_App == [3]:
        await channel.send(
            "<@" + "686360940345819168" + ">" +
            " Is assigned to your application. DM her if you require any assistance while making your app"
        )  #leah
    elif random_App == [4]:
        await channel.send(
            "<@" + "563139104724877312" + ">" +
            " Is assigned to your application. DM him if you require any assistance while making your app"
        )  #pikmin
    elif random_App == [5]:
        await channel.send(
            "<@" + "744997049895747757" + ">" +
            " Is assigned to your application. DM him if you require any assistance while making your app"
        )  #fronga
    elif random_App == [6]:
        await channel.send(
            "<@" + "627335278738276356" + ">" +
            " Is assigned to your application. DM him if you require any assistance while making your app"
        )  #acidist
    elif random_App == [7]:
        await channel.send(
            "<@" + "527889527432413185" + ">" +
            " Is assigned to your application. DM him if you require any assistance while making your app"
        )  #shiny
        await channel.send(
            "<@" + "774281341214392340" + ">" +
            " Is assigned to your application. DM him if you require any assistance while making your app"
        )  #unduel
    await channel.send('<@' + str(author) + '>' + " Apply here")

    await channel.send(
        "```yaml\n-What requirements do you reach -\n-How many hours can you play during the weekends -\n-How did you find the guild -\n-What guild were you in before, and why did you leave -\n-Why do you want to join TheNinjaWarriors -\n-Have you ever been muted or banned in hypixel. Why -\n-Do you have any friends in the guild -\n-What's your timezone -\n-Can you make 25k xp a week -\n-IGN -``` "
    )
    await channel.send(
        "```fix\nCopy and paste the above text ^ and answer the question to form an application\nStaff will review it as soon as possible : ) Good Luck```"
    )


@client.command(name='acceptapp')
@commands.has_role('Staff')
async def accepting(ctx, arg: discord.User):
    await ctx.channel.purge(limit=1)
    await ctx.send("Your application to the Ninjawarriors has been accepted ")
    await ctx.send(
        "Please Verify in the discord in #verify once you have joined the guild so you can recieve the necessary roles"
    )
    await ctx.send(
        "You will be invited as soon as possible make sure u have left your previous guild"
    )


@client.command(name='declineapp')
@commands.has_role('Staff')
async def accepting(ctx, arg: discord.User):
    await ctx.channel.purge(limit=1)
    await ctx.send("Your application to the Ninjawarriors has been declined ")
    await arg.send("Your application to the Ninjawarriors has been declined")


@client.command(name="close")
async def close_channel(ctx):
    if (ctx.channel.name == "📃-ticket" or ctx.channel.name == "📃-application"):
        await ctx.channel.delete()
    else:
        await ctx.channel.send("Dont try deleting other channels dumbass")


@client.command(name='test2')
@commands.has_role('Staff')
async def test2sa(ctx):
    embed = discord.Embed(
        title="TICKET INFO",
        description=
        "Tickets are to be created to complete any of the following tasks:\n1) For feedback on an event which recently took place\n 2) For changes/feedback that can be introduced to the server\n 3) An issue that has been brought to your notice that requires staff attention(Issues regarding members in discord/guild, Bot spam from a member of our server, phishing links that you have received) ",
        color=0xff0000)
    await ctx.send(embed=embed)
    await ctx.channel.send(
        "Type *>ticket* to create a ticket and follow the instructions in the channel you are pinged in"
    )


@client.command(name="mutee")
@commands.has_role('Staff')
async def fake_mute(ctx, arg: discord.User):
    await ctx.channel.purge(limit=1)
    await ctx.channel.send(
        "<@" + str(arg.id) +
        "> you are being quite annoying it would be quite nice if you can shut the fuck up dumbass"
    )


@client.command(name='mute', aliases=['stfu'])
@commands.has_role('Staff')
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole,
                                          speak=False,
                                          send_messages=False,
                                          read_message_history=True,
                                          read_messages=False)
    embed = discord.Embed(
        title="muted",
        description=
        f"{member.mention} was muted, Message staff if you wish to be unmuted",
        colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(
        f" You have been muted from: {guild.name} reason: {reason}")


@client.command(name="unmute")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await member.send(f" You have been unmuted from: - {ctx.guild.name}")
    embed = discord.Embed(title="You have been unmuted BE CAREFUL NEXT TIME",
                          description=f" unmuted-{member.mention}",
                          colour=discord.Colour.light_gray())
    await ctx.send(embed=embed)


@client.command(name='ban')
@commands.has_role("Staff")
async def ban(ctx, member: discord.User = None, reason=None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason == None:
        reason = "For being a jerk!"
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} is banned!")


@client.command(name="ping")
@commands.cooldown(1, 10, commands.BucketType.guild)
async def testAlive(ctx):
    await ctx.send('Pong! {0}'.format(round(client.latency, 1)))


@client.command(name='cf', aliases=['coinflip', 'flip'])
async def coinflip(ctx):
    if ctx.author.id != 864910612241055797:
        choice = random.randint(0, 1)
        if (choice == 0):
            await ctx.reply('Heads')
        elif (choice == 1):
            await ctx.reply('Tails')


@client.command(name='presence')
@commands.cooldown(1, 5, commands.BucketType.guild)
@commands.has_role('Staff')
async def change_presence(ctx):
    await ctx.send("Changing Presence Hold on")
    lol = random.sample(range(1, 8), 1)
    print(lol)
    if (lol == [1]):
        await client.change_presence(activity=discord.Game(
            name="with ninjas lolis"))
    elif (lol == [2]):
        await client.change_presence(activity=discord.Game(
            name="Loli smashing simulator"))
    elif (lol == [3]):
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching, name="Redo of healer"))
    elif (lol == [4]):
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching, name="hanime.tv"))
    elif (lol == [5]):
        await client.change_presence(activity=discord.Game(name="AMOONG US"))
    elif (lol == [6]):
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching, name="cocomelon"))
    elif (lol == [7]):
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening,
                                      name="To graeps old voice :grief:"))
    await ctx.send("Done")


@client.command(name='text_apply')
async def text(ctx):
    embed = discord.Embed(
        title="REQUIREMENTS",
        description="If you reach any of the following requirements do >apply",
        color=0x1E97E7)
    embed.add_field(
        name="Hypixel Network Level 100",
        value="This is a compulsary requirement(Can be ommited sometimes)",
        inline=False)
    embed.add_field(
        name="Major Requirements",
        value=
        "You can join the guild if you have any one of the below requirement",
        inline=False)
    embed.add_field(name="Bedwars Requirement",
                    value="100 stars or 1,500 wins",
                    inline=False)
    embed.add_field(name="Ranked Bedwars Elo ",
                    value="800 i.e. 800 elo from the starting elo rank",
                    inline=False)
    embed.add_field(name="Skywars Requirement",
                    value="Level 14 and 2000 wins",
                    inline=False)
    embed.add_field(name="Duels Requirement", value="3000 wins", inline=False)
    embed.add_field(name="x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x",
                    value="x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x",
                    inline=False)
    embed.add_field(name="Minor Requirements",
                    value="You need any 2 of the requirements to join",
                    inline=False)
    embed.add_field(name="Bedwars Requirement",
                    value="100 stars and 1000 wins",
                    inline=False)
    embed.add_field(name="Ranked Bedwars Elo ",
                    value="600 i.e. 600 elo from the starting elo rank",
                    inline=False)
    embed.add_field(name="Skywars Requirement",
                    value="Level 13 and 1000 wins",
                    inline=False)
    embed.add_field(name="Duels Requirement",
                    value="2,500 wins and diamond in atleast one game",
                    inline=False)
    embed.add_field(name="Arcade Games Requirement",
                    value="2,000 wins",
                    inline=False)
    embed.add_field(name="Murder Mystery Requirement",
                    value="1000 wins and 1,500 kills",
                    inline=False)
    embed.add_field(name="Blitz SG Requirement",
                    value="1,500 wins and atleast 1 Level X Kit / 100 wins",
                    inline=False)
    embed.add_field(name="TNT Games Requirement",
                    value="2,500 overall wins",
                    inline=False)
    embed.add_field(name="Smash heroes Requirement",
                    value="Level 200 and 3 prestiges",
                    inline=False)

    await ctx.send(embed=embed)
    await ctx.send(
        "Type *>apply* to create an application and follow the instructions in the new channel where you are pinged"
    )


@client.command(name="log")
@commands.has_any_role('Staff', 'GvG Captain')
async def logger(ctx):
    await ctx.channel.send(
        'Scrims Logger has started. Answer the questions that come up')
    await ctx.channel.send('Q1: What is the scrim number')

    def check(m):
        return m.author.id == ctx.author.id

    Scrim_Number = await client.wait_for('message', check=check, timeout=60)

    await ctx.channel.send('Q2: Who were on Team 1?')
    Team1log = await client.wait_for('message', check=check, timeout=60)

    await ctx.channel.send('Q3: Who were on Team 2?')
    Team2log = await client.wait_for('message', check=check, timeout=60)

    await ctx.channel.send("Q4: What was Team 1's score?")
    score1 = await client.wait_for('message', check=check, timeout=60)

    await ctx.channel.send("Q5: What was Team 2's score?")
    score2 = await client.wait_for('message', check=check, timeout=60)

    await ctx.channel.send("Q6: Who was Team 1 MVP?")
    mvp1 = await client.wait_for('message', check=check, timeout=60)

    await ctx.channel.send("Q7: Who was Team 2 MVP?")
    mvp2 = await client.wait_for('message', check=check, timeout=60)

    await ctx.channel.send("Q8: Any notes?")
    Notes = await client.wait_for('message', check=check, timeout=60)

    scrims_logs = client.get_channel(919331784808869908)

    embed = discord.Embed(
        title="Premium Game Number: " + str(Scrim_Number.content),
        description="_______________________________________",
        color=0xAE16EC)
    embed.add_field(name="🟥 Team Red - " + str(score1.content),
                    value=str(Team1log.content) + "\n🏅 MVP: " +
                    str(mvp1.content),
                    inline=False)
    embed.add_field(name="🟦 Team Blue - " + str(score2.content),
                    value=str(Team2log.content) + "\n🏅 MVP: " +
                    str(mvp2.content),
                    inline=False)
    embed.add_field(name="Notes", value=str(Notes.content), inline=False)
    await scrims_logs.send(embed=embed)


@client.command(name='goodbye')
@commands.has_role('Manager')
async def accepting(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.channel.send("Goodbye guys, I had alot of fun on this server")
    await ctx.channel.send("I'm going to sleep for a long time now")
    await ctx.channel.send("See you on the other side")


keep_alive()
my_secret = os.environ['DISCORD_TOKEN']
client.run(my_secret)
