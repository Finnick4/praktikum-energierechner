import mysql.connector
import dotenv 

env = dotenv.DotEnv()

db = mysql.connector.connect(
  host="localhost",
  user=env.get("USER"),
  password=env.get("PASSWORD")
)

