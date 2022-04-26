# Fascist stingray discord bot

[For Turkish site](https://tarik366.github.io/FascistVatoz/)

This bot is completely open source and if its contents and theme are not stolen, no claims of stealing can be made (so you can get the codes).

## Developing

**ATTENTION**: Definitely do not commit, create a pull request.

### Bot variable

```python
Bot = commands.Bot("!")
```

This variable change the leading character of bot commands. So the **!i hans** command ! mark is determined by this command

### on_ready

```python
@Bot.event
async def on_ready():
    print("Hello")
```

This code will make the bot say hello when it starts.

### change_presence

```python
await Bot.change_presence(activity=discord.Game(name="jewish burning", type=3, application_id=None, details="bur the jewish", state="jewish burning",))
```

This code determines the statue of bot and it looks like this.

![Statue](images/statue_EN.png)

### commands

#### clear

This command deletes messages.

#### ban ve kick

This commands are not working now.

#### gifs or i

``` python
    if "x" in args:
        await ctx.send(Vars.x)
```

Replace x with the gifs you want to add.
**Note:** Write the gifs as a link to the Vars.py file. There are enough examples in the vars.py file.

#### joining the team

This part is made entirely for the ShiroiSub server.

### Bot.run

This code starts it using the bot's token. The token is taken from your bot's own profile. Create a file named **token_2.py** and write the variable named token in it.

```python
token = "write your token here"
```

## Random gif

I spending my hours on this command, I couldn't. Please add it to the bot if you can.

## Help and contact

If there is something you do not understand, you can get help on [our server](https://discord.gg/G6uwgEAjSx).
