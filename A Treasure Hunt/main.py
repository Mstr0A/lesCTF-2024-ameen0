###############################
# Question: A treasure hunt   #
# Author: Ameen0              #
# Category: misc or smth, idc #
#                             #   P.S. RUN THIS IN DEV MODE
# If you're here, how?        #
#                             #
# I'm Sorry                   #
###############################

import asyncio
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Flag(BaseModel):
    flag: str = "lesCTF(h0p3_u_enjoy3d_the_st0ry)"

@app.get("/")
def honey_im_home():
    return {
        "Hello": "Creature",
        "Hope you're ready": "Lets get started, this one is on me, go to /magic-number."
    }

@app.get("/magic-number")
async def the_secret_to_life():
    return {
        "magic_number": 420,
        "Hint": "Did you know I have unicorns, each one has an ID so I can keep track of it, you should check them out."
    }

@app.get("/unicorns/{unicorn_id}")
async def my_little_pony(unicorn_id: str = "69"):
    return {
        "unicorn": unicorn_id,
        "color": "rainbow",
        "Hint": "Oh no, a goblin stole one of them, he says he needs food in order to give it back."
    }

@app.get("/goblin/{food}")
async def goblin_deez_nuts(food: str = "Ramen"):
    return {
        "goblin": "Gnavin",
        "food": food,
        "status": "happy",
        "Hint": "The unicorn is safe now, but the goblin jumped in a weird portal, could it go to a universe parallel to ours?"
    }

@app.get("/parallel-universes")
async def steven_parallel_universe():
    return {
        "universes": ["universe-1", "universe-2", "universe-3"],
        "Hint": "okay yeah, this is definetly a parallel universe, what year are we in right now?."
    }

@app.get("/year/{year}")
async def screw_the_time_i_guess(year: int = 420):
    return {
        "message": f"Welcome to the year {year}, watch out for dinosaurs!",
        "Hint": "okay enough moving around time and space, Im hungry, I could go for some food, maybe a taco."
    }

@app.get("/taco")
async def taco_chewsday_innit():
    return {
        "taco": "BEANZ",
        "status": "delicious",
        "Hint": "dang it a cat stole my taco."
    }

@app.get("/cat")
async def meow():
    return {
        "state": ["alive", "dead", "somewhere in between"],
        "Hint": "running after the cat ended up hurting me, I stepped on a banana peel, I dont think I need to explain what happened."
    }

@app.get("/slip")
async def slip_on_banana():
    return {
        "status": "slipped on banana",
        "injury_level": "minor, full information can be found in the DOCS", #/docs
        "Hint": "congrats, the flag is in /flag"
    }

@app.get("/flag")
async def flag_fr_fr():
    await asyncio.sleep(300)
    return {
        "Flag": "TlUgVUgh", # NU UH!
        "Note": "Go back to where you found this and read CLOSER"
    }

@app.post("/8caf62544742edd3b35fe60b7cbf9508")
def ignore_this(flag: Flag):
    return {"How did you get here?": flag}