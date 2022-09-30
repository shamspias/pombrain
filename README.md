# Python AI Discord Bot
USING GPT-3 it will do magic!

## Disclaimer

Slash commands can take some time to get registered globally, so if you want to test a command you should use
the `@app_commands.guilds()` decorator so that it gets registered instantly. Example:

```
py
@commands.hybrid_command(
  name="command",
  description="Command description",
)
@app_commands.guilds(GUILD_ID) # Place your guild ID here
```

When using the template you confirm that you have read the [license](LICENSE.md) and comprehend that I can take down
your repository if you do not meet these requirements.

Please do not open issues or pull requests about things that are written in the [TODO file](TODO.md), they are **already** under work for a future version of the template.

## How to set up

To set up the bot I made it as simple as possible. I now created a [config.json](config.json) file where you can put the
needed things to edit.

Here is an explanation of what everything is:

| Variable                  | What it is                                                            |
| ------------------------- | ----------------------------------------------------------------------|
| YOUR_BOT_PREFIX_HERE      | The prefix you want to use for normal commands                        |
| YOUR_BOT_TOKEN_HERE       | The token of your bot                                                 |
| YOUR_BOT_PERMISSIONS_HERE | The permissions integer your bot needs when it gets invited           |
| YOUR_APPLICATION_ID_HERE  | The application ID of your bot                                        |
| OWNERS                    | The user ID of all the bot owners                                     |


## How to start

To start the bot you simply need to launch, either your terminal (Linux, Mac & Windows), or your Command Prompt (
Windows)
.

Before running the bot you will need to install all the requirements with this command:

```
pip install -r requirements.txt
```

If you have multiple versions of python installed (2.x and 3.x) then you will need to use the following command:

```
python3 bot.py
```

or eventually

```
python3.x bot.py
```
Replace `x` with the version of Python you have installed.

<br>

If you have just installed python today, then you just need to use the following command:

```
python bot.py
```

## Issues or Questions

If you have any issues or questions of how to code a specific command, you can:

* Join my discord server [here](https://discord.gg/6CFSRxWTWw)
* Post them [here](https://github.com/shamspias/pombrain/issues)

Me or other people will take their time to answer and help you.

## Versioning

We use [SemVer](http://semver.org) for versioning. For the versions available, see
the [tags on this repository](https://github.com/shamspias/pombrain/tags).

## Built With

* [Python 3.9.12](https://www.python.org/)

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details
