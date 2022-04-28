# 法西斯黄貂鱼Discord机器人

[For English site](https://tarik366.github.io/FascistVatoz/EN) 
[日本語サイト用](https://tarik366.github.io/FascistVatoz/JP) 
[Für Deutsch seite](https://tarik366.github.io/FascistVatoz/DE) 
[Türkçe site için](https://tarik366.github.io/FascistVatoz/) 

![Discord Bot](https://top.gg/api/widget/948714385533206548.svg)

[Top.gg](https://top.gg/bot/948714385533206548)

这个机器人是完全开源的，如果它的内容和主题没有被盗，则不能声称盗窃（即您可以获得代码）。

## 发展

**警告**：不要提交您的更改，创建一个拉取请求。

### 机器人变量

```python
Bot = commands.Bot("!")
```

此变量确定机器人命令的前导字符。所以 **!i hans** 命令！标记由该命令确定。

### on_ready

```python
@Bot.event
async def on_ready():
    print("你好呀")
```

此代码将使机器人在启动时打招呼。

### change_presence

```python
await Bot.change_presence(activity=discord.Game(name="犹太人火葬", type=3, application_id=None, details="犹太人在燃烧", state="犹太人在燃烧",))
```

此代码确定机器人正在玩的游戏，它看起来像这样。

![地位](https://github.com/Tarik366/FascistVatoz/blob/gh-pages/images/Statue_CH.png?raw=true)

### commands

#### clear

此命令删除消息。

#### gifs或者i

``` python
    if "x" in args:
        await ctx.send(Vars.x)
```

将 x 替换为您要添加的 gif。

**注意：** 将 gif 文件作为 Vars.py 文件的链接写入。 vars.py 文件中有足够的示例。

#### 申请团队

这部分完全是为 ShiroiSub 服务器制作的。

### Bot.run

此代码使用机器人的令牌启动它。令牌取自您的机器人自己的个人资料。创建一个名为 **token_2.py** 的文件，并在其中写入名为 token 的变量。

```python
token = "在这里写令牌"
```

## 随机 gif

尽管在这个命令上花了几个小时，但我做不到。如果可以，请随时将其添加到机器人中。

## 帮助和沟通

如果有不明白的地方，可以在 [我们的服务器](https://discord.gg/G6uwgEAjSx) 上获得帮助。
