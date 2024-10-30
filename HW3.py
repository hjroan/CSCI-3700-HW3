from flask import Flask
import psycopg2 
from psycopg2 import OperationalError

app = Flask (__name__)

def db_connect();
  try:
    connect = psycopg2.connect(host = "127.0.0.1", dbname = "hw3", user = "hjroan", password = "5498", port = 5000)
    return connect
  except OperationalError as e
    print(e)
    return None

@app.route ("/api/update_basket_a")
def(updateA)
  connect = db_connect()

  try:
    cursor = connect.cursor()  
    cursor.execute(INSERT INTO basket_a (a,fruit_a) VALUES (5,"Cherry")
    
    connect.commit()
    connect.close()

    return "Success!"

  except Exception as e:
    connect.rollback()
    return e



@app.route ("/api/unique")
def(uniqueFruits)
  connect = db_connect()

  try:
    cursor = connect.cursor()  
    cursor.execute(
    
    connect.commit()
    connect.close()

  
  
