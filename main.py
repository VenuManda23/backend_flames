from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import mysql.connector
import os

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = mysql.connector.connect(
    host="viaduct.proxy.rlwy.net",
    user="root",
    password="URSAOdXORqpmCLoGCBqJbwGyTRCsOCwM",
    database="railway",
    port=49965
)

cursor = db.cursor()

class Flames(BaseModel):
    name: str
    partner_name: str
    result: str

# Home Route
@app.get("/")
def home():
    return {"message": "Backend working"}

# Create Table Automatically
cursor.execute("""
CREATE TABLE IF NOT EXISTS flames (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    partner_name VARCHAR(100),
    result VARCHAR(50)
)
""")

# Save Data API
@app.post("/flames")
def save_data(data: Flames):

    query = """
    INSERT INTO flames(name, partner_name, result)
    VALUES(%s, %s, %s)
    """

    values = (
        data.name,
        data.partner_name,
        data.result
    )

    cursor.execute(query, values)
    db.commit()

    return {"message": "Data saved successfully"}