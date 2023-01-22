from cmath import log
from distutils.sysconfig import PREFIX
import discord, asyncio
from dotenv import load_dotenv
import os
from discord.ext import commands
import time
from youtube_dl import YoutubeDL
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get 
from discord import FFmpegPCMAudio
from random import *

load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

## client bot && variable declaration ##

client = commands.Bot(command_prefix='!',intents=discord.Intents.all())
nickname_ = []
affiliation_ = []
rname_ = []
## meta data ##



## 실명:디코아이디 data base ##
tag_name_dict = {'박서용':7961, '천태성':9185, '김민혁':4379, '이건희':5105, '박희영':5169, '정연승':6332, '김연호':6561, '김남준':4641, '최영현':'0865', '이하원':8198, '안태현':1169, '유 찬':9241, '오민규':7426, '안세은':3901, '이건희':5624, '정요셉':8845, '박희민':8158, '장재성':7719, '이헌재':8500, '김영환':7004}
# 최영현:0865 호출할 땐 예외처리로 문자열 -> 실수 변환 해주어야 함
## define channel ID ##

mainchat = 1013358240857333812 # general chat
announcement_ = 1066219293995438170

vc_general1 = 1003592936367337543 # general voice chat
vc_general2 = 988806641669529650
vc_general3 = 1030821683914874890

## Main event ##

@client.event
async def on_ready() :
    await client.change_presence(status=discord.Status.online, activity=discord.Game("덴지군, 야한 짓은 말이야 상대방의 감정을 이해하면 이해할 수록 기분이 좋아질수 있다고 나는 생각해"))


@client.command(aliases = ['마키마소환'])
async def enter_voice(ctx):
    global vc
    vc = await ctx.author.voice.channel.connect()
    await ctx.send(embed = discord.Embed(description = "지배의 아쿠마, 두둥등장", color = 0xa53939))

@client.command(aliases = ['마키마봉인'])
async def exit_voice(ctx):
    try :
        await client.voice_clients[0].disconnect()
        await ctx.send(embed = discord.Embed(description = "나 갈게~", color = 0xa53939))
    except :
        await ctx.channel.send("음성채널에서 이미 나갔어요")

@client.command(aliases = ['마키마노래'])
async def makima_play_url(ctx, *, url):
    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + url + "을(를) 재생하고 있습니다.", color = 0x00ff00))
    else:
        await ctx.send("노래가 이미 재생되고 있습니다!")


@client.command(aliases = ['마키마재생'])
async def makima_play(ctx, *, msg):
    if not vc.is_playing():
        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
        chromedriver_dir = "자신의 경로를 적어주세요!"
        driver = webdriver.Chrome(chromedriver_dir)
        driver.get("https://www.youtube.com/results?search_query="+msg)
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + entireText + "을(를) 재생하고 있습니다.", color = 0xff0000))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await ctx.send("이미 노래가 재생 중이라 노래를 재생할 수 없어요!")

@client.command(aliases = ['마키마묵찌빠'])
async def makima_rock_scissor_paper(ctx, msg) :
    if ctx.message.content == "!마키마묵찌빠 가위":
        await ctx.channel.send("바위")
    elif ctx.message.content == "!마키마묵찌빠 주먹":
        await ctx.channel.send("보자기")
    elif ctx.message.content == "!마키마묵찌빠 보자기":
        await ctx.channel.send("가위")
    elif ctx.message.content == "!마키마묵찌빠 묵":
        await ctx.channel.send("보자기")
    elif ctx.message.content == "!마키마묵찌빠 빠":
        await ctx.channel.send("가위")
    elif ctx.message.content == "!마키마묵찌빠 찌":
        await ctx.channel.send("바위")
    elif ctx.message.content == "!마키마묵찌빠 바위":
        await ctx.channel.send("보자기")
    elif ctx.message.content == "!마키마묵찌빠 보":
        await ctx.channel.send("가위")
    else :
        await ctx.channel.send("인간녀석, 지배의 악마를 이길 순 없다 !")


@client.command(aliases = ['마키마운세'])
async def makima_l(ctx, content) :
    await ctx.channel.send(embed = discord.Embed(title = "모든 운세는 순수히 랜덤한 결과로 결정 됩니다. 너무 맹신하지 마세요", color = 0xff0000))
    애정 = ['무난할 것 같지만, 매우 큰 이별을 맞이하고 절망에 빠집니다', '정말 좋네요, 진심으로 사랑하는 사람과 만나 영원히 살게 됩니다', '애인에게 배신을 당하고서 헤어지는 안좋은 결말이네요', '마치 자기 자신인듯 마음이 척척 잘맞는 애인과 결혼하여 무난한 생활을 살게 됩니다', '응 모솔 ㅋ', '거울을 봐라']
    재물 = ['돈은 많지만, 쓸데가 없네요 펑펑 벌게됩니다', '거지는 아니지만 살아갈 수 있을 만큼 벌게 됩니다', '돈이 거의 없어 빚에 시달리며 살게 됩니다', '남부럽지 않게 더도말고 덜도말고 적당히 벌고 하고픈 일 할수  있는 만큼 법니다', '누더기 옷을 입고, 꿰멘 양말을 겨우 신는 힘든 생활이 됩니다']
    장래 = ['원하는 꿈을 이루고 평생직장을 가져 살아가게 됩니다', '원하는 꿈을 이루진 못하였지만 남부럽지 않은 삶을 살아가게 됩니다', '자신이 자신있는 분야에서 크게 성공하여 이름을 남기며 살아갑니다', '주식과 도박에 빠져 우울한 삶을 살게 됩니다', '안좋은 길로 걸어 남을 괴롭히며 사는 삶이 됩니다', '해외에서는 유명한 사업가가 됩니다']   
    행운 = ['운이 지지리도 없어서 매번 벌칙내기 하면 걸리기만 하는 운', '운이 나쁜 편은 아닌데 매번 내기만 하면 지는 운', '운이 겁나 좋아서 3연 로또 당첨은 식은 죽 먹기인 운', '운이 딱 반반인 운 그냥 무난함', '운이 더럽게 안좋아서 도박같은거만 하면 돈 다잃고 파산할 운', '운이 좋아 하는 일 족족 해낼 수 있는 운']
    if content == '애정' :
        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = '당신의 애정운은?',description = choice(애정)))
    elif content == '재물' :
        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = '당신의 재물운은?',description = choice(재물)))
    elif content == '장래' :
        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = "당신의 장래운은?", description = choice(장래)))
    elif content == '행운' :
        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = "당신의 장래운은?", description = choice(행운)))
    else :
        await ctx.channel.send("이상한 운세는 안봐줘~")
    

@client.command(aliases = ['마키마타자연습'])
async def makimagame1(ctx, mode, diff) :
    global timeouts
    try :
        if mode == '타자연습' :
            if diff == "초보" :
                timeouts = 10
            elif diff == "중수" :
                timeouts = 7
            elif diff == "극한" :
                timeouts = 5
            ranges = 12
            picked_sent = ''
            picked_sent1 = ''
            sentances = ['냉수 먹고 속 차려라', '논을 사려면 두렁을 보라', '닭의 갈비 먹을 것 없다', '가까이 앉아야 정이 두터워진다', '담화는 마음의 보다 즐거운 향연이다', '건넛산 보고 꾸짖기', '고기 보고 부럽거든 가서 그물을 떠라', '기회는 하느님의 또 다른 별명이다', '나라 상감님도 늙은이 대접은 한다', '밑빠진 가마에 물 붓기', '바늘 구멍으로 하늘 보기', '산에서 우는 작은 새여, 꽃이 좋아 산에서 사노라네', '아첨은 비굴의 표시이다', '정이월에 큰항아리 터진다', '중이 제 머리 못 깎는다', '가난과 거지는 사촌간이다', '가는 말이 고와야 오는 말이 곱다', '가마 속의 콩도 삶아야 먹는다', '금일 충청도 명일 경상도', '까마귀 제 소리 하면 온다', '나는 세계 시민이다', '낮말은 지게문이 듣는다', '내 것도 내 것 네 것도 내 것', '내 배가 불러야 남의 배도 부르다']
            points = 000
            for ranges in range(1, 13, 1) :
                picked_sent = choice(sentances)
                if picked_sent != picked_sent1 :
                    await ctx.channel.send(embed = discord.Embed(title = "타자 연습 %d" % ranges, description = str(picked_sent), color = 0xa53939))
                    
                    timeout = timeouts
                    def check(m) :
                        return m.author == ctx.message.author and m.channel == ctx.message.channel

                    try :
                        
                        msg = await client.wait_for('message', check=check, timeout=timeout)
                            
                    except asyncio.TimeoutError :
                        await ctx.send("당신은 지배의 악마를 이길 수 없다![-50점]")
                        points -= 50
                    else :
                        if msg.content == picked_sent:
                            await ctx.send("이 녀석 좀 하는데?[+50점]")
                            points += 50
                        elif msg.content != picked_sent:
                            await ctx.send("잘못 쳤지롱~[-50점]")
                            points -= 50
            if points == 600 :
                await ctx.send(embed = discord.Embed(title = "결과", description = "엄청잘하네~[%d점]" % points, color = 0xa53939)) 
            elif points < 600 :
                await ctx.send(embed = discord.Embed(title = "결과", description = "%d점 정도야 무난하지만! 날 이길 순 없다!" % points, color = 0xa53939))
            elif points < 0 :
                await ctx.send(embed = discord.Embed(title = "결과", description = "%d점? 사람이냐...." % points, color = 0xa53939))
        elif mode == '' :
            pass
    except :
        await ctx.channel.send(embed = discord.Embed(title = "명령어 사용방법", description = "!마키마게임 타자연습 {argments;difficulty(초보,중수,극한)}", color = 0xa53939))


@client.command(aliases = ['마키마공지'])
async def announcement (ctx, tit, cont) :

    result = cont.replace('/',' ')
    chann = client.get_channel(1066219293995438170)
    await chann.send(embed = discord.Embed(title = tit, description = str(result), color = 0xa53939))

@client.command(aliases = ['마키마일시정지'])
async def makima_pause(ctx) :
    try :
        vc.pause()
        await ctx.send(embed = discord.Embed(description = "지금 재생 중인 노래, 잠깐 멈췄어~", color = 0xa53939))
    except :
        await ctx.send(embed = discord.Embed(description = "노래도 안틀어놓고 멈추긴 멀 멈춰", color = 0xa53939))

@client.command(aliases = ['마키마정지'])
async def makima_stop(ctx) :
    try :
        vc.stop()
        await ctx.send(embed = discord.Embed(description = "지금 재생 중인 노래, 내가 멈췄어~", color = 0xa53939))
    except :
        await ctx.send(embed = discord.Embed(description = "듣고 있던 노래가 있어야지 그만하든지 하지!", color = 0xa53939))

@client.command(aliases = ['마키마다시재생'])
async def makima_resume(ctx) :
    try :
        vc.resume()
        await ctx.send(embed = discord.Embed(description = "지금 멈춰 있던 노래, 다시 재생 했어~", color = 0xa53939))
    except :
        await ctx.send(embed = discord.Embed(description = "아무것도 멈춘 적이 없는데..?", color = 0xa53939))


@client.command()
async def 마키마도움 (ctx) :
    await ctx.channel.send(embed = discord.Embed(title = "접두사 : \{!마키마\}", description = "사용할 수 있는 명령어는 다음과 같아요 \n\n!마키마소환 : 현재 사용 중인 음성채널에 마키마 봇을 호출합니다\n!마키마봉인 : 현재 음성채널을 사용중인 마키마 봇을 퇴장시킵니다\n!마키마노래 \{argments;URL\} : 해당 유튜브 링크를 재생합니다\n!마키마재생 \{argments;str\} : 봇이 검색어를 검색했을 때 최상단에 노출되는 영상을 재생합니다\n!마키마묵찌빠 \{argments;rockscissorpaper\} : 마키마와 가위바위보 내기를 합니다(참고로 인간님들은 지배의 아쿠마를 이길수 엄슴)\n!마키마운세 \{argments;애정,재물,장래,행운\} : 해당하는 운세를 봐 줍니다(마키마가)\n!마키마\{argments;타자연습\} \{argments;초보,중수,극한\} : 마키마와 게임을 합니다(이길 수 있나?)", color = 0xa53939))



try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
