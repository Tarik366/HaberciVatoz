# Faşist vatoz discord botu

[For English site](https://tarik366.github.io/FascistVatoz/EN)
[![Discord Bot](https://top.gg/api/widget/948714385533206548.svg)(https://top.gg/bot/948714385533206548)

Bu bot tamamen açık kaynaklı olup içerikleri ve teması çalınmaması durumunda herhangi bir çalınma iddiası oluşturulamaz(yani kodları alabilirsiniz).

## Geliştirme

**UYARI**: kesinlikle yaptığınız değişikliği commitlemeyin, pull request oluşturun.

### Bot değişkeni

```python
Bot = commands.Bot("!")
```

Bu değişken bot komutlarının ön karakterini belirler. Yani **!i hans** komutundaki ! işareti bu komut ile belirlenir.

### on_ready

```python
@Bot.event
async def on_ready():
    print("merhaba")
```

Bu kod bot başlatıldığında merhaba demesini sağlar.

### change_presence

```python
await Bot.change_presence(activity=discord.Game(name="Yahudi yakmaca", type=3, application_id=None, details="Yahudi yakıyor", state="Yahudi yakıyor",))
```

Bu kod botun oynadığı oyunu belirler ve böyle gözükür.

![Statü](https://github.com/Tarik366/FascistVatoz/blob/gh-pages/images/Statue.png?raw=true)

### commands

#### clear

bu komut mesajları siler.

#### ban ve kick

Bu komutlar şuan çalışmıyor.

#### gifler yada i

``` python
    if "x" in args:
        await ctx.send(Vars.x)
```

x yerine eklemek istediğiniz gifleri yazın.
**Not:** gifleri link olarak Vars.py dosyasına yazın. Vars.py dosyasında yeterince örnek var.

#### ekibe başvuru

Bu kısım tamamen ShiroiSub sunucusu için yapılmıştır.

### Bot.run

Bu kod botun tokenini kullanarak başlatır. token botunuzun kendi profilinden alınır. token'ı **token_2.py** adlı bir dosya oluşturup token adlı değişkeni içerisine yazın.

```python
token = "token'ı buraya yazın"
```

## Random gif

Bu komut üzerinde saatlerimi harcamama rağmen yapamadım. Eğer yapabiliyorsanız lütfen bota eklemekten çekinmeyin.

## Yardım ve iletişim

Eğer anlamadığınız bir şey olursa [sunucumuz](https://discord.gg/G6uwgEAjSx) üzerinden yardım alabilirsiniz.
