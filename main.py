import discord
import requests

from discord import Embed

import secreto
import asyncio
from PIL import Image, ImageDraw, ImageFont, ImageOps
from io import BytesIO


client = discord.Client()

COR =0xFF8CD9
token = secreto.seu_token()
msg_id = None
msg_user = None


@client.event
async def on_ready():
    print('BOT ONLINE - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('---------------')


@client.event
async def on_message(message):

    if message.content.lower().startswith("-aov"):
     embed1 =discord.Embed(
        title="Olá conquistador, esse será o canal onde você irá pegar o seu cargo baseado no seu ELO dentro do jogo, lembre de ser honesto na hora de pegar o cargo e não ficar brincando com o BOT, se fizer isso será bloqueado deste canal até segunda ordem",
        color=COR,
        description="- Para pegar a TAG do ELO bronze, clique aqui | \n<:bronze:485539684274012172>\n"
                    "- Para pegar a TAG do ELO prata, clique aqui | \n<:prata:485539685075255318> \n"
                    "- Para pegar a TAG do ELO ouro, clique aqui | \n<:ouro:485539684835917835>\n"
                    "- Para pegar a TAG do ELO platina, clique aqui | \n<:platina:485539679861604364>\n"
                    "- Para pegar a TAG do ELO diamante, clique aqui | \n<:diamante:485539668109164544>\n"
                    "- Para pegar a TAG do ELO mestre, clique aqui | \n<:mestre:485539672869699584>",
     )
     embed1.set_thumbnail(url='https://cdn.discordapp.com/attachments/485692496886890508/485692634342621202/1535837776653.png')
     botmsg = await client.send_message(message.channel, embed=embed1)

     await client.add_reaction(botmsg, ":bronze:485539684274012172")
     await client.add_reaction(botmsg, ":prata:485539685075255318")
     await client.add_reaction(botmsg, ":ouro:485539684835917835")
     await client.add_reaction(botmsg, ":platina:485539679861604364")
     await client.add_reaction(botmsg, ":diamante:485539668109164544")
     await client.add_reaction(botmsg, ":mestre:485539672869699584")


     global msg_id
     msg_id = botmsg.id

     global msg_user
     msg_user = message.author


@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji.id == "485539684274012172" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bronze", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji.id == "485539685075255318" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Prata", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji.id == "485539684835917835" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Ouro", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji.id == "485539679861604364" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Platina", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji.id == "485539668109164544" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Diamante", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji.id == "485539672869699584" and msg.id == msg.id and user!= client.user:
     role = discord.utils.find(lambda r: r.name == "Mestre", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji.id == "485539684274012172" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bronze", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji.id == "485539685075255318" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Prata", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji.id == "485539684835917835" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Ouro", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji.id == "485539679861604364" and msg.id == msg_id: #and user = msg_user:
     role = discord.utils.find(lambda r: r.name == "Platina", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji.id == "485539668109164544" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Diamante", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji.id == "485539672869699584" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Mestre", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

@client.event
async def on_ready():
 await client.change_presence(game=discord.Game(name='discord.gg/MWrMXFE by:Gzin', url='https://www.twitch.tv/aquelarivengod', type=1))


@client.event
async def on_member_join(member):
    channel = client.get_channel("485889954719858688")
    regras = client.get_channel("485535843415621652")
    msg = "<a:BlobHyper:485912331323310130> ** Seja bem vindo(a) **{} **ao Arena of Valor Brasil! leia as** {}".format(member.mention, regras.mention)

    url = requests.get(member.avatar_url)
    avatar = Image.open(BytesIO(url.content))
    avatar = avatar.resize((130, 130));
    bigsize = (avatar.size[0] * 3,  avatar.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(avatar.size, Image.ANTIALIAS)
    avatar.putalpha(mask)

    output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    output.save('avatar.png')

    #avatar = Image.open('avatar.png')
    fundo = Image.open('bemvindo.png')
    fonte = ImageFont.truetype('BebasNeue.ttf',55)
    escrever = ImageDraw.Draw(fundo)
    escrever.text(xy=(180,172), text=member.name,fill=(0,0,0),font=fonte)
    fundo.paste(avatar, (40, 90), avatar)
    fundo.save('bv.png')

    await client.send_file(channel, 'bv.png', content=msg)




client.run(token)