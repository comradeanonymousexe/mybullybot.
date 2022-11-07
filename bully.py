import discord
from discord import client
from discord import message
from discord.ext import commands
import asyncio
import random
import json


intents = discord.Intents.default()
intents.members = True
description = '''A private Entertainment Bot Made By Sarge'''


bot = commands.Bot(command_prefix='.', intents=intents)


#-----------------outter funcs---------------
def bly():
    bully_list = ["ছাগল","ময়লা","রম্বস","ফইন্নি","হাঁদা","বেকুব"]    
    str = "তুমি একটা " + random.choice(bully_list)
    return str

def sorry():
    sry_list = ["Hey Amigo, Perhaps you messed the structure of command a lil bit.Try again- best of luck",
    "That's not how I take commands- Check the help section and type **.help**","এমন কমান্ড দিলে তোমার নানাও বুঝবেনা"]
    return random.choice(sry_list)

channels =[934804254810595399,935082320954790028,938784833457500180,934804254810595402,1004257457419325451,
1004257546346963016,940121410083389460,939035539376599061,947732892136656966,935178965025439804,935047327222206504]






#--------------------initiate bot--------------------------
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening , name = " Sarge."))
    print('working') 






#-------------------my utilizes-----------------------------
@bot.command(aliases=['av'])
async def avatar(ctx , member:discord.Member):
    title  = f"{member.name}\'s Avatar"

    status = ["Cute :kissing_heart:","Horny :hot_face:" , "Ugly :poop:","Savage :imp:", "Devil :smiling_imp:","Extremely খ্যাঁত :nauseated_face: ","Normie :disguised_face:","গ্রামের কাযিন :woman_tone5_beard:","আবাল মার্কা DP :yawning_face:","সীমিত খ্যাত :face_exhaling:","Lovely :heart_eyes:"]
    Percentage  = str(random.randint(50,700))
    description = "**"+random.choice(status)+" at "+Percentage+"% capacity"+"**"
    embed = discord.Embed(color = discord.Colour.dark_green(),description=description,title=title)
    embed.set_image(url=member.avatar_url)
    an = f"Here you go {ctx.author}"
    embed.set_author(name=an,icon_url=ctx.author.avatar_url)
    try:
        await ctx.send(embed=embed)
    except:
        await ctx.reply(sorry())



@bot.command(aliases=['bly'])
async def bully(ctx , member:discord.Member):
    id = member.id
    priv_list = [723225265664163955,853107487791120394]
    try:
        if id not in priv_list:
            for i in range(5):

                get_bully = bly()
  
                await ctx.send(f"<@{member.id}> {get_bully}")

        else:
            await ctx.send("Watch out!! whom you're trying to bully is privileged")

    except Exception as e:
        await ctx.reply(sorry())
        await ctx.send(f"Hello Sarge, {e}")

        
@bot.command(aliases = ["pdct"])
async def predict(ctx , member:discord.Member):

    age = str(random.randint(17,32))
    arranged_marij_case = ["`A nigro` :woman_tone5_beard:","`A business Magnet` :levitate_tone1:","`An International চোর` :woman_detective_tone1: ","`Cousine` :couple: ","`Chotobelar classmate` :family_man_boy: ","`20 বছরের সিনিওর` :older_man_tone1: / :older_adult_tone1: ","`A Khataish Motku` :disguised_face: ","`A cute person` :smiling_face_with_3_hearts:"]
    arranged_marij = "It looks like Tomar `Arranged Marriage` Hobe :smiling_face_with_tear:  with"+"`"+random.choice(arranged_marij_case)+"`"+ "At the age of " + age
    love_marij_case = ["`Your Lover` :heartbeat: ","`Ex` :broken_heart: ","`Lover (But pore janba : YOU HAVE BEEN CHEATED FOR ALL THE TIME)` :anatomical_heart: ","`Tomar Crush` :heart_eyes: "]
    l_m_status =  ["Bari theke paliye :person_running_tone1: ","Court marriage :man_judge_tone1: ","Baba-Mar oshommotite :unamused:"]
    love_marij = "Hmmmmm :face_with_monocle:  tumi  `Love marriage` :mending_heart:  korba  "+random.choice(l_m_status)+"  with " + random.choice(love_marij_case) + age + " bochor boyoshe."    
    marij = [love_marij,arranged_marij]  
    marij_info = "**1.Marriage Status:** "+ random.choice(marij)+ "\n \n \n"


    edu_status = ["`Phd`","`Graduate`","`MBA`","`BBA`","`Jhore Pora Student`","`Student politician`"]
    edu_subject = ["Medical","EEE","ChuChulogy","Charukola","Computer science [UwU]","ToTo company"]
    edu_info = "**2.Education Status:** Tumi poralekha shuru korbe "+ random.choice(edu_subject) + " niye and will end up as a/an " + random.choice(edu_status) 


    baccha = str(random.randint(1,8))
    lis= ["Natural","Current er SHock kheye","Panite Dube","Life partner er hate mair kheye","Suicide :|","Otirikto gaja kheye"]
    death_stat = random.choice(lis)
    death_age = str(random.randint(32,120))
    life_end_info = f"**3.Finally:** Tumi {baccha} jon baccha rekhe {death_age} bochor boyoshe mara jabe. Mrittuta hobe {death_stat}"


    try:
        await ctx.reply(marij_info) 
        await ctx.send(edu_info)
        await ctx.send(life_end_info)

    except:
        await ctx.reply(sorry())



@bot.command()
async def warn(ctx , member:discord.Member, * , reason="no reason"):

    try:
        desc = f"{member.name} "+ reason
        emb = discord.Embed(color=discord.Colour.red(),title= "WARNING!!!",description=desc)

        emb.set_image(url = member.avatar_url)
        emb.set_author(icon_url=ctx.author.avatar_url,name = ctx.author)
    
        await ctx.send(embed=emb)
        await member.send(embed=emb)
    except:
        await ctx.reply(sorry())






        
 

        


bot.run("MTAzODcwMTQ4MDY4NjkxOTcwMA.G54SmR.o4LsDxUEnBz_DFWEzJi2v5WGbBbta3907qKjO4")