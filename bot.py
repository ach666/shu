from keep_alive import keep_alive
import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(game=discord.Game(name="please help me get a date with nito"))

@client.event
async def on_message(message):
    if message.author != client.user:
      if ("nazuna" in message.content.lower()) or ("nito" in message.content.lower()):
          await client.send_message(message.channel,"NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO NITO")

      elif ("pussy" in message.content.lower()):
        if (message.author.bot):return
        await client.send_message(message.channel,"pussy")
      
      elif ("father???" in message.content.lower()):
        await client.send_message(message.channel,"yes, son.")

      elif ("turks" in message.content.lower()) or ("the turk" in message.content.lower()):
        if (message.author.bot):return
        await client.send_message(message.channel,"fuck the turks.")

      elif ("fuck you miles" in message.content.lower()):
        if (message.author.bot):return
        await client.send_message(message.channel,"fuck you miles")

      ##elif (":nauseated_face:" in message.content):
        ##await client.send_message(message.channel,"shu")

      elif("gay" in message.content.lower()):
        await client.send_message(message.channel,"僕は誇り高い同性愛者の斎宮宗なのだよ！だからこそ警察を引っ叩くのが趣味で決まってるんだろう")
      
      elif ("dab" in message.content.lower()):
        if (message.author.bot):return
        await client.send_file(message.channel,"dab.png")

      elif ("stan 2wink" in message.content.lower()):
        await client.send_message(message.channel,"i fucking stan 2wink bitch")

      elif ("2wink" in message.content.lower()):
        await client.send_message(message.channel,"my actual legitimate children")

      elif ("shubot is dead" in message.content.lower()):
        await client.send_message(message.channel,"fuck you")
      
      elif ("wonder" in message.content.lower()) or ("wwtl" in message.content.lower()):
        await client.send_message(message.channel,"""Suyasuya machi ga nemuri ni tsuite tokei no hari ga kasanaru koro
Heya no mado o sotto akete oide yo
Konya wa pink na unicorn ga kimi o annaishitekurerunda
Minna no yume ga tsumatta basho
Youkoso Toyland
 
Tanoshii nakama to issho ni asobou
Kodomo dake ga atsumaru bouken no sekai e
 
Kikoeru fanfare no aizu
Hajimaru Wonder Wonder Story
Mukuchi na omochatachi mo koko de dake wa oshaberi
Ano sora ga kyoukaisen
Saa, hoshi o kette oikakekkoshiyou
Asahi ga kimi o torimodosu made wa bokutachi no jikan
 
Ojigishita no wa buriki no heitai
Ouji-sama no tonari ni wa crown
Minna o shoukaisuru ne
Hayaku uchitoketai na
 
Hiruma naiteta kimi wa mou inai yo
Shiawase na kao dake de mitasareteku yoru ni Ah
 
Waraiau koe ga hibiite
Umareru Wonder Wonder Story
Nozomeba nandatte kanau, sora datte toberu ne
Omoikkiri jiyuu nanda
Saa, yokubari ni boukenshiyou yo
Asa ni wa zenbu yume ni nattetatte, yume janai kara
 
Mezameru tabi otona ni naru
Tokei wa tomaranai
Eien no naka de warau
Bokutachi no koto douka wasurenaide
 
Yamanai fanfare ni notte
Tsuzuiteku Wonder Wonder Story
Mukuchi na omochatachi mo koko de dake wa oshaberi
Ano sora ga kyoukaisen
Saa, hoshi o kette doko made mo ikou
Asahi ga kimi o torimodosu made wa bokutachi no jikan""")

      elif ("send pics" in message.content.lower()):
        await client.send_file(message.channel,random.choice(["adorablenazu.png","amazingnito.png","beautifulnito.png","brightnito.png","cheerfulnito.png","cutenito.png","deliciousnazu.png","delightfulnito.png","faitonito.png","fuwanito.png","gentlenazu.png","gorgeousnito.png","i-is_that_a_love_letter_for_me.png","i_would_die_for_you_nito.png","incrediblenito.png","lovelynito.png","lovingnito.png","mynazu.png","ohwonderfulnazu.png","rawrnito.png","sillynazu.png","strongnito.png","sweetnazu.png","talentednito.png"]))

      elif ("sand pics" in message.content.lower()):
        await client.send_file(message.channel,random.choice(["ohnazu.png","please_dont_despair_kawaii_boku_no_koibito.png"]))
      
      elif ("shunazu" in message.content.lower()):
        await client.send_file(message.channel,"nito_please_marry_me.png")

      elif ("shu" in message.content.lower()):
        await client.send_message(message.channel,"僕")

      elif ("love" in message.content.lower()):
        if (message.author.bot):return
        await client.send_message(message.channel,"well i love nito so much i love him he is the love of my life have you seen nito he is adorable is he not yes nito is the absolute love of my life")
      
      elif ("mika" in message.content.lower()) or ("kagehira" in message.content.lower()):
        await client.send_message(message.channel,"hmph. i'm sure kagehira is off running around like a lost kitten. there is no need to worry about that idiot, as his girlfriend will go find him soon.")
      
      elif ("koreaboo" in message.content.lower()):
        await client.send_message(message.channel,"笑 idil is a koreaboo")

      elif ("kys" in message.content.lower()) or ("kill yourself" in message.content.lower()) or ("kill urself" in message.content.lower()):
        await client.send_message(message.channel,"kill me yourself you fucking failure of a human. you cannot even create art.")
      
      ##elif ("i have" in message.content.lower()):
        ##await client.send_message(message.channel,"good for you.")

      elif ("hamburger" in message.content.lower()):
        await client.send_file(message.channel,"MUNCHNITO.png")

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
