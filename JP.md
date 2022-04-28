# ファシストアカエイDiscordボット

[For English site](https://tarik366.github.io/FascistVatoz/EN) 
[Türkçe site için](https://tarik366.github.io/FascistVatoz/) 
[Für Deutsch seite](https://tarik366.github.io/FascistVatoz/DE) 
[中文网站](https://tarik366.github.io/FascistVatoz/CH) 

![Discordボット](https://top.gg/api/widget/948714385533206548.svg)

[Top.gg](https://top.gg/bot/948714385533206548)

このボットは完全にオープンソースであり、そのコンテンツとテーマが盗まれていない場合、盗んだと主張することはできません（つまり、コードを入手できます）。

## 発達

**警告**：変更をコミットせず、プルリクエストを作成してください。

### ボット変数

```python
Bot = commands.Bot("!")
```

この変数は、ボットコマンドの先頭文字を決定します。したがって、**！i hans **コマンド！マークはこのコマンドで決定されます。

### on_ready

```python
@Bot.event
async def on_ready():
    print("merhaba")
```

このコードは、ボットが起動したときにhelloと言うようにします。

### change_presence

```python
await Bot.change_presence(activity=discord.Game(name="ユダヤ人の火葬", type=3, application_id=None, details="ユダヤ人は燃えています", state="ユダヤ人は燃えています",))
```

このコードは、ボットがプレイしているゲームを判別し、次のようになります。

![状態](https://github.com/Tarik366/FascistVatoz/blob/gh-pages/images/Statue_JP.png?raw=true)

### commands

#### clear

このコマンドはメッセージを削除します。

#### gifまたはi

``` python
    if "x" in args:
        await ctx.send(Vars.x)
```

xを追加するgifに置き換えます。

**注:**gifをVars.pyファイルへのリンクとして書き込みます。 vars.pyファイルには十分な例があります

#### チームに申し込む

この部分はすべてShiroiSubサーバー用に作成されています

### Bot.run

このコードは、ボットのトークンを使用して開始します。トークンは、ボット自身のプロファイルから取得されます。 ** token_2.py **という名前のファイルを作成し、その中にtokenという名前の変数を書き込みます。 70

```python
token = "ここにトークンを書く"
```

## ランダムGIF

このコマンドに何時間も費やしたにもかかわらず、私はできませんでした。可能であれば、ボットに自由に追加してください。

## ヘルプとコミュニケーション

わからないことがあれば、[私たちのサーバー]（https://discord.gg/G6uwgEAjSx）で助けを得ることができます。
