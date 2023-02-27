from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host="redis", port=6379)

import debugpy
debugpy.listen(("0.0.0.0", 5678))

@app.get("/")
def read_root():
    return {"Hello": "Back to Kenji"}

@app.get("/pings")
def read_root():
    r.incr("pings")
    return {"num_pings": r.get("pings")}
