# Faschistischer Stachelrochen-Discord-Bot

[For English site](https://tarik366.github.io/FascistVatoz/EN) 
[日本語サイト用](https://tarik366.github.io/FascistVatoz/JP) 
[Türkçe site için](https://tarik366.github.io/FascistVatoz/) 
[中文网站](https://tarik366.github.io/FascistVatoz/CH) 

![Discord-Bot](https://top.gg/api/widget/948714385533206548.svg)

[Top.gg](https://top.gg/bot/948714385533206548)

Dieser Bot ist vollständig Open Source und wenn sein Inhalt und Thema nicht gestohlen werden, können keine Ansprüche auf Diebstahl gestellt werden (dh Sie können die Codes erhalten).

## Entwicklung

**WARNUNG**: Bestätigen Sie Ihre Änderungen nicht, erstellen Sie eine Pull-Anforderung.

### Bot-Variable

```python
Bot = commands.Bot("!")
```

Diese Variable bestimmt das führende Zeichen von Bot-Befehlen. Also der Befehl **!i hans** ! Marke wird durch diesen Befehl bestimmt.

### on_ready

```python
@Bot.event
async def on_ready():
    print("Hallo")
```

Dieser Code lässt den Bot beim Start Hallo sagen.

### change_presence

```python
await Bot.change_presence(activity=discord.Game(name="jüdische Einäscherung", type=3, application_id=None, details="Jude brennt", state="Jude brennt",))
```

Dieser Code bestimmt das Spiel, das der Bot spielt, und es sieht so aus.

![Statü](https://github.com/Tarik366/FascistVatoz/blob/gh-pages/images/Statue_DE.png?raw=true)

### commands

#### clear

Dieser Befehl löscht Nachrichten.

#### gifs oder i

``` python
    if "x" in args:
        await ctx.send(x)
```

Ersetzen Sie x durch die Gifs, die Sie hinzufügen möchten.

**Hinweis:** Schreiben Sie die Gifs als Link zur Vars.py-Datei. Es gibt genügend Beispiele in der Datei vars.py.

#### beim Team bewerben

Dieser Teil ist vollständig für den ShiroiSub-Server gemacht.

### Bot.run

Dieser Code startet es mit dem Token des Bots. Das Token wird dem eigenen Profil Ihres Bots entnommen. Erstellen Sie eine Datei namens **token_2.py** und schreiben Sie die Variable namens token hinein.

```python
token = "Schreiben Sie Token hier"
```

## Zufälliges gif

Obwohl ich Stunden mit diesem Befehl verbrachte, konnte ich es nicht. Bitte zögern Sie nicht, es dem Bot hinzuzufügen, wenn Sie können.

## Hilfe und Kommunikation

Wenn Sie etwas nicht verstehen, können Sie auf [unserem Server] (https://discord.gg/G6uwgEAjSx) Hilfe erhalten.
