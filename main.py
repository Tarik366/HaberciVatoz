import os.path
from discord import *
from discord.ext import commands
from Vars import *
import token_2

Bot = commands.Bot("!", help_command=None)

@Bot.event
async def on_ready():
    print("merhaba")
    await Bot.change_presence(activity=Game(name="Yahudi yakmaca", type=3, application_id=None, details="Yahudi yakıyor", state="Yahudi yakıyor",))

# moderatrör komutları


@Bot.command()
async def clear(ctx, amount=100000000000000000000000):
    await ctx.channel.purge(limit=amount)

@Bot.command()
@commands.has_permissions(ban_members = True)
async def kick(ctx, member : Member, *, reason = None):
    embed = Embed(title="kicklendi", description=f"{member.mention}", color=0x8a0a01)
    await member.kick(reason = reason)
    await ctx.send(embed=embed)

@Bot.command()
@commands.has_permissions(ban_members = True)
async def yak(ctx, member : Member, *, reason = None):
    embed = Embed(title="Yakılanlar listesi", description=f"{member.mention}", color=0x8a0a01)
    await member.ban(reason = reason)
    await ctx.send(embed=embed)


# Help komutu

@Bot.command()
async def yardım(ctx):
    embed = Embed(title="Yardım", description="Yardım komutları", color=0x8a0a01)
    embed.add_field(name="!yardım", value="yardım komutlarını gösterir", inline=False)
    embed.add_field(name="!yak", value="Etiketlenen kişiyi yakar(banlar)", inline=False)
    embed.add_field(name="!kick", value="Etiketlenen kişiyi kickler", inline=False)
    embed.add_field(name="!clear", value="Belirlenen sayıda mesaj siler", inline=False)
    embed.add_field(name="!i", value="110'dan fazla gif veya resimden seçileni atar", inline=False)
    embed.add_field(name="!başvuru", value="Seçilen başvuru formunu gönderir", inline=False)
    embed.add_field(name="!ada", value="İstediğiniz bir şeyi hayalet vatoza adar", inline=False)
    embed.add_field(name="!pp", value="Yazan kişinin profil fotoğrafını atar", inline=False)
    embed.add_field(name="!ideoloji", value="16 ideoloji arasından seçilen ideolojiye geçerim", inline=False)
    embed.add_field(name="!işkence", value="Etiketlenen kişiye işkence yaparım. Fazla kullanmamaya dikkat edin", inline=False)
    await ctx.send(embed=embed)

# gifs


@Bot.command()
async def i(ctx, *args):
    if "like" in args:
        await ctx.send(like)
    if "rage" in args:
        await ctx.send(rage)
    if "anakuzusu" in args:
        await ctx.send(anakuzusu)
    if "cry" in args:
        await ctx.send(cry)
    if "freakout" in args:
        await ctx.send(freakout)
    if "haa" in args:
        await ctx.send(haa)
    if "o7konosuba" in args:
        await ctx.send(o7konosuba)
    if "nomnom" in args:
        await ctx.send(nomnom)
    if "like2x" in args:
        await ctx.send(like2x)
    if "shock" in args:
        await ctx.send(shock)
    if "o7" in args:
        await ctx.send(o7)
    if "foksax" in args:
        await ctx.send(foksax)
    if "dwayne" in args:
        await ctx.send(dwayne)
    if "hatsoff" in args:
        await ctx.send(hatsoff)
    if "capitalism" in args:
        await ctx.send(capitalism)
    if "soviet" in args:
        await ctx.send(soviet)
    if "sikin" in args:
        await ctx.send(sikin)
    if "susamuru" in args:
        await ctx.send(susamuru)
    if "fire" in args:
        await ctx.send(fire)
    if "marcharmy" in args:
        await ctx.send(marcharmy)
    if "irumadance" in args:
        await ctx.send(irumadance)
    if "taam" in args:
        await ctx.send(taam)
    if "milf" in args:
        await ctx.send(milf)
    if "stare" in args:
        await ctx.send(stare)
    if "GreatPurge" in args:
        await ctx.send(GreatPurge)
    if "napim" in args:
        await ctx.send(napim)
    if "napimdiyeni" in args:
        await ctx.send(napimdiyeni)
    if "hatayapar" in args:
        await ctx.send(hatayapar)
    if "nazifokları" in args:
        await ctx.send(nazifokları)
    if "darkside" in args:
        await ctx.send(darkside)
    if "troll" in args:
        await ctx.send(troll)
    if "yahudiler" in args:
        await ctx.send(yahudiler)
    if "balanced" in args:
        await ctx.send(balanced)
    if "jii" in args:
        await ctx.send(jii)
    if "shipbang" in args:
        await ctx.send(shipbang)
    if "tank" in args:
        await ctx.send(tank)
    if "degil" in args:
        await ctx.send(degil)
    if "air" in args:
        await ctx.send(air)
    if "kimclap" in args:
        await ctx.send(kimclap)
    if "worry" in args:
        await ctx.send(worry)
    if "muso" in args:
        await ctx.send(muso)
    if "sob" in args:
        await ctx.send(sob)
    if "kannaeat" in args:
        await ctx.send(kannaeat)
    if "baka" in args:
        await ctx.send(baka)
    if "triggered" in args:
        await ctx.send(triggered)
    if "shinobu" in args:
        await ctx.send(shinobu)
    if "shy" in args:
        await ctx.send(shy)
    if "bang2" in args:
        await ctx.send(bang2)
    if "shutup" in args:
        await ctx.send(shutup)
    if "save" in args:
        await ctx.send(save)
    if "aah" in args:
        await ctx.send(aah)
    if "para" in args:
        await ctx.send(para)
    if "yay" in args:
        await ctx.send(yay)
    if "anlıyorum" in args:
        await ctx.send(anlıyorum)
    if "understood" in args:
        await ctx.send(understood)
    if "igetit" in args:
        await ctx.send(igetit)
    if "benzin" in args:
        await ctx.send(benzin)
    if "why" in args:
        await ctx.send(why)
    if "celebrate" in args:
        await ctx.send(celebrate)
    if "braintime" in args:
        await ctx.send(braintime)
    if "drink" in args:
        await ctx.send(drink)
    if "bb" in args:
        await ctx.send(bb)
    if "dot" in args:
        await ctx.send(dot)
    if "confused" in args:
        await ctx.send(confused)
    if "lenny" in args:
        await ctx.send(lenny)
    if "bang" in args:
        await ctx.send(bang)
    if "slap" in args:
        await ctx.send(slap)
    if "mad" in args:
        await ctx.send(mad)
    if "sob2" in args:
        await ctx.send(sob2)
    if "laugh" in args:
        await ctx.send(laugh)
    if "evilsmile" in args:
        await ctx.send(evilsmile)
    if "dissaper" in args:
        await ctx.send(dissaper)
    if "behind" in args:
        await ctx.send(behind)
    if "like3" in args:
        await ctx.send(like3)
    if "whatanime" in args:
        await ctx.send(whatanime)
    if "nomnomnom" in args:
        await ctx.send(nomnomnom)
    if "bonk" in args:
        await ctx.send(bonk)
    if "yarra" in args:
        await ctx.send(yarra)
    if "katon" in args:
        await ctx.send(katon)
    if "hug" in args:
        await ctx.send(hug)
    if "hug2" in args:
        await ctx.send(hug2)
    if "sob3" in args:
        await ctx.send(sob3)
    if "animechild" in args:
        await ctx.send(animechild)
    if "narutodance" in args:
        await ctx.send(narutodance)
    if "darkstare" in args:
        await ctx.send(darkstare)
    if "think" in args:
        await ctx.send(think)
    if "point" in args:
        await ctx.send(point)
    if "bagıs" in args:
        await ctx.send(bagıs)
    if "stalinpoint" in args:
        await ctx.send(stalinpoint)
    if "serve" in args:
        await ctx.send(serve)
    if "waku" in args:
        await ctx.send(waku)
    if "fail" in args:
        await ctx.send(fail)
    if "comunazi" in args:
        await ctx.send(comunazi)
    if "şaak" in args:
        await ctx.send(şaak)
    if "doom" in args:
        await ctx.send(doom)
    if "omori" in args:
        await ctx.send(omori)
    if "callvatoz" in args:
        await ctx.send(callvatoz)
    if "vatozlar" in args:
        await ctx.send(knowvatoz)
    if "papas" in args:
        await ctx.send(papas)
    if "hans" in args:
        await ctx.send(hans)
    if "yummy" in args:
        await ctx.send(yummy)
    if "okay" in args:
        await ctx.send(okay)
    if "what" in args:
        await ctx.send(what)
    if "sad" in args:
        await ctx.send(sad)
    if "gel" in args:
        await ctx.send(gel)
    if "ekonomi" in args:
        await ctx.send(ekonomi)
    if "mikasa" in args:
        await ctx.send(mikasa)
    if "çıldır" in args:
        await ctx.send(çıldır)
    if "kırk" in args:
        await ctx.send(kırk)
    if "drink2" in args:
        await ctx.send(drink2)
    if "fbi" in args:
        await ctx.send(fbi)
    if "want" in args:
        await ctx.send(want)
    if "want2" in args:
        await ctx.send(want2)


# Bug fix
@Bot.command()
async def aki():
    pass


@Bot.command()
async def rank():
    pass

# ekibe başvuru


@Bot.command()
async def başvuru(ctx, *args):
    if "mangaçevirmen" in args:
        tr = Embed(
            title="Manga çevirmen başvuru formu",
            description="Daha önce başka bir ekipte çalıştın mı?\n\nBağımsız da olsa deneyimin var mı?\n\nİngilizce seviyen nedir?\n\nEn çok hangi tür mangaları seviyorsun?\n\nHaftada kaç bölüm çevirebilirsin?\n\nVe bu örnek sayfayı çevirmeni istiyoruz\nhttps://drive.google.com/file/d/1_qfW23Wvda94S19U3f4x8eCe6YEqFCug/view?usp=sharing\nSon olarak yeni-gelenlere kanalına bakmayı unutmayın"
        )
        await ctx.send(embed=tr)
    if "mangaeditör" in args:
        ed = Embed(
            title="Manga editör başvuru formu",
            description="Daha önce başka bir ekipte çalıştın mı?\n\nBağımsız da olsa deneyimin var mı?\n\nHaftada kaç bölüm editleyebilirsin?\n\nPhotoshop seviyene 5 üzerinden puan verebilir misin?\n\nVe bu örnek sayfayı editlemeni istiyoruz\nhttps://drive.google.com/file/d/1-B-xLpofKmmyx86_wOuOA4ii-LfG4hb9/view?usp=sharing\nSon olarak yeni-gelenlere kanalına bakmayı unutmayın")
        await ctx.send(embed=ed)
    if "webçevirmen" in args:
        wtr = Embed(
            title="Webtoon çevirmen başvuru formu",
            description="Daha önce başka bir ekipte çalıştın mı?\n\nBağımsız da olsa deneyimin var mı?\n\nİngilizce seviyen nedir?\n\nEn çok hangi tür webtoonları seviyorsun?\n\nHaftada kaç bölüm çevirebilirsin?\n\nVe bu örnek sayfayı çevirmeni istiyoruz\nSon olarak yeni-gelenlere kanalına bakmayı unutmayın")
        await ctx.send(embed=wtr)
    if "webeditör" in args:
        wed = Embed(
            title="Webtoon editör başvuru formu",
            description="Daha önce başka bir ekipte çalıştın mı?\n\nBağımsız da olsa deneyimin var mı?\n\nHaftada kaç bölüm editleyebilirsin?\n\nPhotoshop seviyene 5 üzerinden puan verebilir misin?\n\nVe bu örnek sayfayı editlemeni istiyoruz\nhttps://drive.google.com/drive/folders/12spp_Y4xTWLRJ8HxLsaom4B5Ilord0_7?usp=sharing\nSon olarak yeni-gelenlere kanalına bakmayı unutmayın"
        )
        await ctx.send(embed=wed)


# Adak sistemi


@Bot.command()
async def ada(ctx, *args):
    author = str(ctx.message.author)
    ad = "adaklar/"+ author +".txt"
    if "temizle" in args:
        os.remove(ad)
        embed = Embed(title="Adağınız başarıyla temizlendi.")
        await ctx.send(embed=embed)
    if os.path.exists(ad) == True and "temizle" in args:
        msg = Embed(title="Adağınız kabul edildi")
        await ctx.send(embed=msg)
        ada = open(str(ad), "w")
        a = str(author)+str(args)
        ada.write(a)
    if os.path.exists(ad) == False and "temizle" not in args:
        msg = Embed(title="Adağınız kabul edildi")
        await ctx.send(embed=msg)
        ada = open(str(ad), "x")
        ada = open(str(ad), "w")
        a = str(author)+str(args)
        ada.write(a)


@Bot.command()
async def pp(ctx):
    ppp = ctx.author.avatar_url
    await ctx.send(ppp)


@Bot.command()
async def ideoloji(ctx, *args):
    if "demokrat" in args:
        dem = open("ppler/demkrat_vatoz.jpg", 'rb')
        demo = dem.read()
        await Bot.change_presence(activity=Game(name="Oy saymaca"))
        await Bot.user.edit(username="Demokrat Vatoz", avatar=demo)
        vatoz = "demokrat"
        embed = Embed(title="Herkes adaletli istiklalde eşit olacak")
        await ctx.send(embed=embed)
    if "faşist" in args:
        fas = open("ppler/fasist_vatoz.jpg", 'rb')
        fasc = fas.read()
        await Bot.change_presence(activity=Game(name="Yahudi yakmaca"))
        await Bot.user.edit(username="Faşist Vatoz", avatar=fasc)
        vatoz = "faşist"
        embed = Embed(title="Köklerime döndüm")
        await ctx.send(embed=embed)
    if "anarko ilkel" in args:
        ail = open("ppler/Anarko-ilkelcilik_vatoz.jpg", 'rb')
        ailk = ail.read()
        await Bot.change_presence(activity=Game(name="Hayvan avlıyor"))
        await Bot.user.edit(username="Anarko-ilkelci Vatoz", avatar=fasc)
        vatoz = "anarko ilkelci"
        embed = Embed(title="Yeni dünya boş asıl olay geçmişte var")
        await ctx.send(embed=embed)
    if "anarko kapitalist" in args:
        fas = open("ppler/Anarko-kapitalist_vatoz.jpg", 'rb')
        fasc = fas.read()
        await Bot.change_presence(activity=Game(name="Tüccarlık yapıyor"))
        await Bot.user.edit(username="Anarko Vatoz", avatar=fasc)
        vatoz = "anarko kapitalist"
        embed = Embed(title="Serbest piyasasında tüccarlık yapacağım")
        await ctx.send(embed=embed)
    if "anarşist" in args:
        fas = open("ppler/anarsist_vatoz.jpg", 'rb')
        fasc = fas.read()
        await Bot.change_presence(activity=Game(name="Otoriteye küfür ediyor"))
        await Bot.user.edit(username="Anarşist Vatoz", avatar=fasc)
        vatoz = "anarşist"
        embed = Embed(title="Otoritede ne?")
        await ctx.send(embed=embed)
    if "fabrika" in args:
        fas = open("ppler/fabrika_vatoz.jpg", 'rb')
        fasc = fas.read()
        await Bot.change_presence(activity=Game(name="Edit yapıyor"))
        await Bot.user.edit(username="Fabrika Vatoz", avatar=fasc)
        vatoz = "fabrika"
        embed = Embed(title="İdeolojiler ben edit yapacağım")
        await ctx.send(embed=embed)
    if "kuma" in args:
        fas = open("ppler/kuma vatoz.jpg", 'rb')
        fasc = fas.read()
        await Bot.change_presence(activity=Game(name="Dünyayı kumalıyor"))
        await Bot.user.edit(username="Kuma Vatoz", avatar=fasc)
        vatoz = "kuma"
        embed = Embed(title="Kuma kuma kuma bear izleyip geldim")
        await ctx.send(embed=embed)
    if "liberteryanist" in args:
        fas = open("ppler/Liberteryenist_vatoz.jpg", 'rb')
        fasc = fas.read()
        await Bot.change_presence(activity=Game(name="Özgürlüğün dibine vuruyor"))
        await Bot.user.edit(username="Liberteryanist Vatoz", avatar=fasc)
        vatoz = "liberteryanist"
        embed = Embed(title="Özgürlük, özgürlük ve daha fazla özgürlük")
        await ctx.send(embed=embed)
    if "mao" in args:
        fas = open("ppler/maocu_vatoz.jpg", 'rb')
        fasc = fas.read()
        await Bot.change_presence(activity=Game(name="Kırlarda hazırlanıyor"))
        await Bot.user.edit(username="Maocu Vatoz", avatar=fasc)
        vatoz = "maocu"
        embed = Embed(title="Çin Komünizmi hiç fikrim yok")
        await ctx.send(embed=embed)
    if "radyoaktif" in args:
        fas = open("ppler/radyoaktif_vatoz.jpg", 'rb')
        fasc = fas.read()
        await Bot.change_presence(activity=Game(name="α ışıması yapıyor"))
        await Bot.user.edit(username="Radyoaktif Vatoz", avatar=fasc)
        vatoz = "radyoaktif"
        embed = Embed(title="Yanlışlıkla Uranyuma dokundum")
        await ctx.send(embed=embed)
    if "turan" in args:
        fas = open("ppler/turancı vatoz.jpg", 'rb')
        fasc = fas.read()
        await Bot.change_presence(activity=Game(name="Haritayı açık maviye boyuyor"))
        await Bot.user.edit(username="Turancı Vatoz", avatar=fasc)
        vatoz = "turancı"
        embed = Embed(title="Türkler üstün ırktır ve bende görevim olan cihan fethini gerçekleştireceğim")
        await ctx.send(embed=embed)


# İşkence

@Bot.command()
async def işkence(ctx, member: Member):
    if vatoz == "faşist":
        user = await Bot.fetch_user(member.id)
        await user.send("天皇陛下万歳")
        await user.send("天皇陛下万歳")
        await user.send("天皇陛下万歳")
        await user.send("天皇陛下万歳")
        await user.send("天皇陛下万歳")
        await user.send("天皇陛下万歳")
        await user.send("天皇陛下万歳")
        await user.send("天皇陛下万歳")
        await user.send("天皇陛下万歳")
        await user.send("天皇陛下万歳")
        embed = Embed(description=f"{member.mention} iskence yapıldı")
        await ctx.send(embed=embed)


Bot.run(token_2.token)
