import requests
import discord
import json
import random
from happytransformer import HappyTextToText,TTSettings
from pyaspeller import YandexSpeller
import asyncio
import nest_asyncio
from jokeapi import Jokes
from bs4 import BeautifulSoup



my_secret = BOT_TOKEN

#setting intent settings
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

nest_asyncio.apply()


#defining events
#1)welcome msg
@bot.event
async def on_ready():
  print(f'WE HAVE LOGGED IN AS {bot.user}')



#2)messages
@bot.event
async def on_message(message):  #fetches meanings of words from a vocab API

  if (message.author == bot.user):
    return
    #making case insensitive
  contents = message.content.lower()

  if contents.startswith('!hello'):
    await message.channel.send('HELLO I AM GRAMMAR-GIRAFFE,YOUR LANGUAGE ASSISTANT BOT.TYPE !HELP TO HOW I CAN HELP YOU.')
    #introduction
  elif contents.startswith('!intro'):
    await message.channel.send("MEET GRAMMAR GIRAFFE, YOUR TRUSTY LANGUAGE COMPANION! 🦒✨ WITH THE GRACE OF A GIRAFFE, I'LL HELP YOU SOAR THROUGH THE WORLD OF WORDS. FROM FETCHING MEANINGS TO FIXING SENTENCES, CORRECTING SPELLINGS, AND EVEN MAKING YOU SMILE WITH JOKES AND QUOTES, I'M HERE TO MAKE YOUR LANGUAGE JOURNEY DELIGHTFUL. DON'T FORGET TO ASK ME ABOUT THE WORD OF THE DAY TO EXPAND YOUR VOCABULARY. LET'S EXPLORE THE WORLD OF LANGUAGE TOGETHER!")
  
  
  elif contents.startswith('!how are you today'):
    await message.channel.send("I AM GREAT.I HOPE YOU'RE FINE TOO:))")

  elif contents.startswith('!goodbye'):
    await message.channel.send("GOODBYE FOR NOW! REMEMBER, I'M JUST A CHAT AWAY WHEN YOU NEED A FRIEND OR A BIT OF HELP. TAKE CARE AND SEE YOU SOON!:)")  
  elif contents.startswith('!thank you'):
    await message.channel.send("GLAD TO BE OF HELP!")
  elif contents.startswith('!help'):
    await message.channel.send("1 !intro-just an introduction. \n 2.!hello-greeting \n 3.!how are you today \n 4.!goodbye \n 5.!thank you \n 6.!meaning-get the meaning of a word. \n 7.!check-corrects spelling and grammar of a sentence. \n 8.!flash-to take a vocab quiz. \n 9.!joke-get a joke to brighten your day. \n 10.!quotes-to fetch a motivational quote. \n 11.!wotd-discover a new word everyday. \n -you can also type !wotd yyyy/m/d to get the word of that specific day. \n 12.!help-get a list of available commands and their description.")

  elif contents.startswith('!meaning'):
    word = contents[len('!meaning'):].strip()
    meaning= fetch_meaning(word)
    try:
     if meaning is not None:
       await message.channel.send(f'THE MEANING OF THE WORD,{word} IS {meaning}')
                                 
     else:
       await message.channel.send(f'SORRY I COULDNT FIND THE MEANING OF{word}')
    except Exception as e:
      await message.channel.send(f'ERROR OCCURED OF THE FORM {str(e)}')

 

  elif contents.startswith('!check'):
    sentence = contents[len('!check'):].strip()
    correct_sent = correct_grammar_and_spell(sentence)
    await message.channel.send(f'THE CORRECTED SENTENCE IS {correct_sent}')
   
   

  elif contents.startswith('!flash'):
    quiz_q=flash_questions()
    await message.channel.send(f'WHAT IS THE MEANING OF "{quiz_q["word"]}"?')
    incorrect_def=[quiz_q["incorrect_def1"],quiz_q["incorrect_def2"],quiz_q["incorrect_def3"]]
    correct_choice=(quiz_q["meaning"])
    incorrect_def.insert(random.randint(0,2),correct_choice)
    options='ABCD'
    correct_opt_ind=incorrect_def.index(correct_choice)
    for i,choice in enumerate(incorrect_def):
      correct_opt=options[correct_opt_ind]
      await message.channel.send(f'{options[i]}.{choice}')

    await asyncio.sleep(1)
  
    await message.channel.send("ENTER YOUR CHOICE NOW-A/B/C/D")
    def response(response):
      return response.author == message.author and response.channel==message.channel
    try:
        user_ans= await bot.wait_for('message',check=response,timeout=60)
        user_ans=user_ans.content.upper()
        if user_ans==correct_opt:
          await message.channel.send("YAYY!! YOU GOT THE CORRECT ANSWER. KEEP GOING!! ")
          await asyncio.sleep(1)
          await message.channel.send(f'AN EXAMPLE IS-"{quiz_q["sentence"]}".')
        else:
          await message.channel.send(f'OOPSIE!! WRONG ANSWER. BETTER LUCK NEXT TIME.THE CORRECT MEANING IS "{quiz_q["meaning"]}".')
          await asyncio.sleep(1)
          await message.channel.send(f'AN EXAMPLE IS-"{quiz_q["sentence"]}".')
        
               
    except asyncio.TimeoutError:
         await message.channel.send("SORRY YOU RAN OUT OF TIME")

  elif contents.startswith('!joke'):
    Jk=await Jokes()
    joke=await Jk.get_joke(category=['programming','dark'])
    if joke["type"]=="single":
      await message.channel.send(joke["type"])
    else:
      await message.channel.send(joke["setup"])
      await message.channel.send(joke["delivery"])
    await message.channel.send("I HOPE YOU LAUGHED;))")
 
  elif contents.startswith('!quotes'):
    quotes,author=fetch_quotes()
    await message.channel.send(f'{quotes} by :{author}')
    

  elif contents.startswith('!wotd'):
    date=contents[len('!wotd'):].strip()
    word_of_the_day,definition=fetch_word_of_the_day(date)
    await message.channel.send(f'THE WORD OF THE DAY IS:  {word_of_the_day}')
    await message.channel.send(f'IT MEANS: {definition}')
   
  else:
    await message.channel.send("LOOKS LIKE YOU'VE ENTERED A WRONG COMMAND:((.TYPE !HELP TO TAKE A LOOK AT MY COMMANDS.")








  

#3)new user intro msg
@bot.event
async def new_member(member):
  channel = member.guild.system_channel
  if channel:
    await channel.send(
        f'WELCOME {member.mention} TO THE SERVER.TYPE !HELP TO UNDERSTAND WHAT I DO')
    


def fetch_meaning(word):  
  api_key =API_KEY
  url = f'https://dictionaryapi.com/api/v3/references/sd3/json/{word}?key={api_key}'
  response = requests.get(url)
  if response.status_code == 200:
    content = response.json()
    meaning = content[0]["def"][0]["sseq"][0][0][1]["dt"][0][1].strip("{bc}")
    return meaning
  
  
def correct_grammar_and_spell(sent):
  speller = YandexSpeller()
  fixed = speller.spelled(sent)
  happy_tt=HappyTextToText("T5", "vennify/t5-base-grammar-correction")
  args = TTSettings(num_beams=5, min_length=1)
  result = happy_tt.generate_text(fixed,args=args)
  return result.text

def flash_questions():
  with open('vocab.json','r') as file:
    vocab_data=json.load(file)
    quiz_q=random.choice(vocab_data)
    return quiz_q
  
def fetch_quotes():
  try:
    url='https://type.fit/api/quotes'
    response=requests.get(url)
    if response.status_code==200:
      quote=response.json()
      random_quote=random.choice(quote)
      quote_text=random_quote.get("text","some quote")
      author=random_quote.get("author","some author").strip(", type.fit")
      return quote_text,author
    else:
      return ("UNABLE TO FETCH A QUOTE AT THE MOMENT")
  except Exception as e:
    return str(e)

def fetch_word_of_the_day(date):
  try:
   url=f'https://www.wordnik.com/word-of-the-day/{date}'
   info=requests.get(url)
   if info.status_code==200:
    soup=BeautifulSoup(info.text,'html.parser')
    wotd=soup.select_one('#wotd > div.content_column > h1 > a')
    word=wotd.text.strip()
    define=soup.select_one('#define > div > ul > li:nth-child(1)')
    definition=define.text.strip()
    return word,definition
  except Exception as e:
    return ("EXCEPTION OCCURED")







  

 
  
    
  
loop=asyncio.get_event_loop()
loop.run_until_complete(on_ready())

bot.run(my_secret)

