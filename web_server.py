from flask import Flask, request
from threading import Thread
import json

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
  app.run(host='0.0.0.0',port=8080)



def keep_alive():  
    t = Thread(target=run)
    t.start()
