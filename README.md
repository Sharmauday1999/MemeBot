# MemeBot
###### A discord Meme "Karma" Tracking bot


![alt text](https://www.ginx.tv/uploads2/Streamers___Twitch/juan_joya_borja.jpg?ezimgfmt=ng%3Awebp%2Fngcb5%2Frs%3Adevice%2Frscb5-1)

## Dependancies
Make sure you have pymongo installed and a mongodb cluster setup with two collections. 

```
pip install pymongo
pip install tabulate
```

## Usage
You can either run this locally, make sure to create a `.env` file and define the variables used in `bot.py` and `db.py`

Run with `python bot.py`


## Deployment
This is currently deployed on repl.it with an uptime bot pinging a flask endpoint that was opened up on localhost, it shouldn't be too hard to set that up. 
