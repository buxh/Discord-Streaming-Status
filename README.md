# Discord Streaming Status
https://solo.to/buxh

## Preview 
![](https://raw.githubusercontent.com/buxh/Discord-Streaming-Status/main/images/1.png)

![](https://raw.githubusercontent.com/buxh/Discord-Streaming-Status/main/images/2.png)

![](https://raw.githubusercontent.com/buxh/Discord-Streaming-Status/main/images/3.png)

![](https://raw.githubusercontent.com/buxh/Discord-Streaming-Status/main/images/4.png)

## How to use
Install [python](https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe). Make sure you install python to [path](https://raw.githubusercontent.com/buxh/Discord-Streaming-Status/main/images/0_7nOyowsPsGI19pZT.png).

Install requirement "discord" using `pip install discord`. If you need help click [this](https://phoenixnap.com/kb/install-pip-windows).

Locate your discord token & copy it to clipboard. If you need help click [this](https://www.androidauthority.com/get-discord-token-3149920/).

Right click `main.py` and open with **Notepad**.

On the last line you will see the following:
```python
client.run("TOKEN", bot=False, reconnect=True)
```
Replace `"TOKEN"` with your discord token.

Save the file.

Double click `run.bat`.

Go to any text channel and type `$stream` followed by your custom stream message for example `$stream hello`, this will stream the word "hello".

Keep the py file open in the background so your streaming status doesn't expire.

## Help

If you are in need of help open an issue or contact me on discord: `larp#4324`.
