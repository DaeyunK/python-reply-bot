#파이썬을 설치 후 CMD 에 "pip install discord" 를 작성해주세요 !
import discord

app = discord.Client()

@app.event
async def on_ready():
    game = discord.Game('서술')
    await app.change_presence(status=discord.Status.online, activity=game)

    print("Discord python Login Success")
    print("디스코드봇 이름:" + app.user.name)
    print("디스코드봇 ID:" + str(app.user.id))
    print("디스코드봇 버전:" + str(discord.__version__))

@app.event
async def on_message(message):
    if message.content.startswith ("안녕"):
        await message.reply("반가워", mention_author=True) #mention_author = 답장 대상 태그 기능 | True 태그 함 , False 태그 안함

app.run("TOKEN")
