import discord
from discord import app_commands
from discord.ext import commands, tasks
import datetime
import asyncio
from enum import Enum
from time import mktime
import random
import tokens
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
randomGen = random.Random()

Meal = Enum("Meal", ["BREAKFAST", "LUNCH", "DINNER"])


breakfast = [
    "Breakfast time poggies we love breakfast :tada:",
    "it is time to consume breakfast :) eat fud and drink woder",
    "Yoooo go eat something\nyou headin out, you need some energy",
    "Snorlax got fed with berries where's your breakfast?????",
    "Consume brekfes or die",
    "Eat breakfast or be thrown into the shadow realm",
    "Break that fast, you need some energy\nCONSUUUUUUMMMME",
]
lunch = [
    ":rotating_light: It's lunch time eat drink please thanks :) :rotating_light: :rotating_light: DON'T FORGET TO DRINK WATER TOO VERY IMPORTANT :rotating_light:",
    "Lunch time baybeeeeee eat that lunch and drink that water and get on that grindset :cold_face: :cold_face: :cold_face:",
    "Yooooooo where lunch?????? Get chomping and sippin",
    "IIIIIIIT'S LUNCH TIME EVERYBODY ANY LUNCHERS IN THE CHAT? ANY LUNCHERS?",
    "Go eat lunch or I will banish you to the shadow realm, Jimbo",
    "You will eat lunch :gun:",
    "My brother in christ please eat lunch it's good for you",
]
dinner = [
    "Consume dinner or perish :gun: :cup_with_straw:",
    "Snorlax is eating berries, where's your dinner??? :thinking: :thinking: :thinking:",
    "It's dinner time! Please eat :) Starving bad",
    "Dinner time go eat :angry: don't forget water dehydration in sleep is bad :angry:",
    "Dinner time's here, find stuff to eat and consume it or face the wrath of `CONTRACTS`",
    "```Java\nif (hungry){\n\tfindFood();\n\teatFood();\n\tdopamine();\n}```",
]

texts = [breakfast, lunch, dinner]

threats = [
    "so you better get eatin",
    ", if you go hungry the Shadow Realm won't",
    " so I hope you've eaten :pensive:",
]

mentions = "<@415276291328311298> <@759970817588068364> <@541202520794726400> <@730284896010108950> <@742595076194172998> <@706321021262888980> <@987465303627821116> <@402639884478840844>"
channel = client.get_channel(916422913052270652)


# creating a loop that runs every day at 8:20 PDT
@tasks.loop(
    time=datetime.time(
        hour=8, minute=20, tzinfo=datetime.timezone(datetime.timedelta(hours=-7))
    )
)
async def breakfast_loop():
    channel = client.get_channel(916422913052270652)
    await channel.send(await genMsg(Meal.BREAKFAST))


# creating a loop that runs every day at 12:30 PDT
@tasks.loop(
    time=datetime.time(
        hour=12, minute=30, tzinfo=datetime.timezone(datetime.timedelta(hours=-7))
    )
)
async def lunch_loop():
    channel = client.get_channel(916422913052270652)
    await channel.send(await genMsg(Meal.LUNCH))


# creating a loop that runs every day at 18:35 PDT
@tasks.loop(
    time=datetime.time(
        hour=18, minute=35, tzinfo=datetime.timezone(datetime.timedelta(hours=-7))
    )
)
async def dinner_loop():
    channel = client.get_channel(916422913052270652)
    await channel.send(await genMsg(Meal.DINNER))


"""# creating a loop that runs every day at 12:30 PDT
@tasks.loop(
    time=datetime.time(
        hour=23, minute=21, tzinfo=datetime.timezone(datetime.timedelta(hours=-7))
    )
)
async def now_loop():
    channel = client.get_channel(250773681872175104)
    await channel.send(await genMsg(Meal.LUNCH))"""

async def genMsg(meal):
    unix_timestamp = round(mktime(datetime.datetime.now().timetuple()))
    ranChoice = round(randomGen.uniform(0, (len(texts[(meal.value - 1)]) - 1)))
    threatChoice = round(randomGen.uniform(0, (len(threats) - 1)))
    return (
        texts[(meal.value - 1)][ranChoice]
        + f"\nI reminded you <t:{unix_timestamp}:R>"
        + threats[threatChoice]
        + " "
        + mentions
    )


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    if not breakfast_loop.is_running():
        breakfast_loop.start()
    if not lunch_loop.is_running():
        lunch_loop.start()
    if not dinner_loop.is_running():
        dinner_loop.start()
    #if not now_loop.is_running():
    #    now_loop.start()


bot = commands.Bot(
    command_prefix="!", intents=discord.Intents.all()
)  # intents are required depending on what you wanna do with your bot
randomGen = random.Random()

channel = bot.get_channel(1105648669962813513)
embed = discord.Embed(
    title="Your death",
    type="rich",
    color=0x661111,  # Dark Red color
    description="Kinda Cringe Bro",
)
embed.add_field(name="Cause of Death:", value="Dysentery, Being cringe, Dying")


@bot.hybrid_command(name="die")
async def die(ctx):
    await ctx.send(
        "And now you die " + ctx.author.display_name,
        embeds=[embed],
    )


@bot.hybrid_command(name="new")
async def new(ctx):
    await ctx.send(
        "And now you die " + ctx.author.display_name,
        embeds=[embed],
    )

@bot.hybrid_command(name="sync")
async def sync(ctx):
    if ctx.author.id == 190273240969641985:
        await ctx.send("You suck Creator " + ctx.author.display_name + " but your shit synced")
        await bot.tree.sync()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

loop = asyncio.get_event_loop()
loop.create_task(bot.start(tokens.TokenHolder.nourish))
loop.create_task(client.start(tokens.TokenHolder.turt))
loop.run_forever()

