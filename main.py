from fastapi import FastAPI
import mysql.connector

app = FastAPI()

db = mysql.connector.connect(
    host="mysql.railway.internal",
    user="root",
    password="URSAOdXORqpmCLoGCBqJbwGyTRCsOCwM",
    database="railway",
    port=3306
)

cursor = db.cursor()

@app.get("/")
def home():
    return {"message":"DB connected"}