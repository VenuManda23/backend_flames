# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import mysql.connector

# app=FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )
# db=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="1234",
#     database="flamesdb"
# )
# cursor=db.cursor()

# class Flames(BaseModel):
#     name:str
#     partner_name:str
#     result:str
# # @app.post('/flames')
# # def save_data(data:Flames):
# #     print(data)
# #     query=""" insert into flames(name,partner_name,result) values(%s,%s,%s) """
# #     values=(data.name,data.partner_name,data.result)
# #     cursor.execute(query,values)
# #     db.commit()
# #     return{
# #         "msg":"data saved successfully"
# #     }
# @app.get("/")
# def home():
#     return {'msg':'backend'}

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "working"}