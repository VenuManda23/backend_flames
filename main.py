from fastapi import FastAPI
import mysql.connector

app = FastAPI()

db = mysql.connector.connect(
    host="viaduct.proxy.rlwy.net",
    user="root",
    password="URSAOdXORqpmCLoGCBqJbwGyTRCsOCwM",
    database="railway",
    port=49965
)

cursor = db.cursor()

@app.get("/")
def home():
    return {"message":"DB connected"}