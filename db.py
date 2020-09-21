#!/usr/bin/env python

# Config -------------------------------------------------------------------------------------------------------------->
import config

# Modules ------------------------------------------------------------------------------------------------------------->
import sys
import mysql.connector

# Functions ----------------------------------------------------------------------------------------------------------->
def connect_to_database():
  """Create connection to database"""

  return mysql.connector.connect(
    host= config.db_ip,
    user=config.db_user,
    password=config.db_password
  )

def drop_database(mydb):
  """"""

  mycursor = mydb.cursor()
  mycursor.execute("DROP DATABASE IF EXISTS %s;" % (config.db_name))

def create_database(mydb):
  drop_database(mydb)

  mycursor = mydb.cursor()

  mycursor.execute("CREATE DATABASE IF NOT EXISTS %s;" % (config.db_name))
  mycursor.execute("USE %s;" % (config.db_name))
  mycursor.execute("CREATE TABLE IF NOT EXISTS users(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, login varchar(255), email varchar(255), password varchar(255));")
  mycursor.execute("CREATE TABLE IF NOT EXISTS collections(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name varchar(255), description varchar(255), users varchar(255));")
  mycursor.execute("CREATE TABLE IF NOT EXISTS cards(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, question varchar(255), answer varchar(255), collection varchar(255));")

if __name__ == "__main__":
  if len(sys.argv) > 1:
    if sys.argv[1] == "create":
      print("Ok, CREATE database")
      create_database(connect_to_database())
    elif sys.argv[1] == "drop":
      print("Ok, DROP database")
      drop_database(connect_to_database())
    else:
      print("Incorect parametrs")