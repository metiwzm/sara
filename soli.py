
from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.raw import functions
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone
from re import match
import random
from datetime import datetime
import os ; os.chdir(os.path.dirname(os.path.abspath(__file__)))
def if_not_exist_creat(filename):
    if not os.path.isfile(filename):
        with open(filename , "w") as f:
            f.write("")
            f.close() 
def write(filename , text):
    with open(filename , "w") as f:
        f.write(text)
        f.close() 
def read(filename):
    with open(filename , "r") as f:
        return f.read()

org = [":", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
fonts = [["౾", "𝟶", "𝟷", "𝟸", "𝟹", "𝟺", "𝟻", "𝟼", "𝟽", "𝟾", "𝟿​"],
["౾", "𝟘", "𝟙", "𝟚", "𝟛", "𝟜", "𝟝", " 𝟞", "𝟟", "𝟠", "𝟡"],
["౾", "𝟬", "𝟭", "𝟮", "𝟯", "𝟰", "𝟱", "𝟲", "𝟳", "𝟴", "𝟵"],
["౾", "𝟎", "𝟏", "𝟐", "𝟑", "𝟒", "𝟓", "𝟔", "𝟕", "𝟖", "𝟗"],
["౾", "⓪","①","②","③","④","⑤","⑥","⑦","⑧","⑨"],
["౾", "❬𝟎❭","❬𝟏❭","❬𝟐❭","❬𝟑❭","❬𝟒❭","❬𝟓❭","❬𝟔❭","❬𝟕❭","❬𝟖❭","❬𝟗❭"],
["౾","𝟬","𝟭","𝟐","❬𝟑❭", "𝟜","⑤","❬𝟔❭","𝟽","𝟴","❬𝟗❭"],
["౾","⁰","¹","²","³","⁴","⁵","⁶","⁷","⁸","⁹"]]

if_not_exist_creat("timeinname")
if_not_exist_creat("timeinbio")

api_id = 9738142
api_hash = '7dae2610f4073be1575c8022ad7ef37a'
app = Client("metiwz", api_id, api_hash)

def create_time():
    a = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")
    ran = random.choice(fonts)
    for char in a :
        a = a.replace(char , ran[int(org.index(str(char)))])
    return a
time = ""
def job():
    global time
    if time != datetime.now(timezone("Asia/Tehran")).strftime("%H:%M"):
        if read("timeinname") == "on":
            try:
                app.send(functions.account.UpdateProfile(last_name=f'| {create_time()}'))
            except Exception as e:
                print(e)
        if read("timeinbio") == "on":
            try:
                app.send(functions.account.UpdateProfile(about=f'-'))
            except Exception as e:
                print(e)
        time = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")

@app.on_message(filters.me and filters.text)
def tool(app, m:Message):
    chat_id, message_id, text = m.chat.id, m.message_id, m.text
    if match(r"^[Hh][Ee][Ll][Pp]$", text):
          app.edit_message_text(m.chat.id , m.message_id , """
╔════❰**🅗︎🅔︎🅛︎🅟︎**❱═❍⊱❉ 
║╭━━━━━━━━━━━━━━━➣  
║┣⪼❉ `Timebio` -> [ on - off ]
║┣⪼❉ `Timename` -> [ on - off ]
║┣⪼❉  Cᴏᴅᴇᴅ Bʏ Mᴇᴛɪᴡᴢ Tᴇᴀᴍ 👨🏻‍💻
║┣⪼❉  @Metiwz | @Metiwz_Team
║╰━━━━━━━━━━━━━━━➣ 
╚════════════❍⊱❉ """)
    elif match(r"^[Tt][Ii][Mm][Ee][Nn][Aa][Mm][Ee]$", text.split()[0]):
        if match(r"^[Oo][Nn]$", text.split()[1]):
            write("timeinname", "on")
            app.edit_message_text(chat_id, message_id, "𝐓𝐢𝐦𝐞 𝐢𝐧 𝐧𝐚𝐦𝐞 [ `𝐨𝐧` ]")
        else:
            write("timeinname", "off")
            app.edit_message_text(chat_id, mrssage_id, "𝐓𝐢𝐦𝐞 𝐢𝐧 𝐧𝐚𝐦𝐞 [ `𝐨𝐟𝐟` ]")
    elif match(r"^[Tt][Ii][Mm][Ee][Bb][Ii][Oo]$", text.split()[0]):
        if match(r"^[Oo][Nn]$", text.split()[1]):
            write("timeinbio", "on")
            app.edit_message_text(chat_id, message_id, "𝐓𝐢𝐦𝐞 𝐢𝐧 𝐛𝐢𝐨 [ `𝐨𝐧` ]")
        else:
            write("timeinbio", "off")
            app.edit_message_text(chat_id, message_id, "𝐓𝐢𝐦𝐞 𝐢𝐧 𝐛𝐢𝐨 [ `𝐨𝐟𝐟` ]")
scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=5)
scheduler.start()
app.start(), idle(), app.stop()
