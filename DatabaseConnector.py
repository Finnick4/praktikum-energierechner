import mysql.connector
import dotenv 
from abc import ABC


class db(ABC):
    def __init__(self):
        self.__db__ = mysql.connector.connect(
            host="localhost",
            user=dotenv.get_key(dotenv.find_dotenv(), "USER"),
            password=dotenv.get_key(dotenv.find_dotenv(), "PASSWORD"),
            database=dotenv.get_key(dotenv.find_dotenv(), "DATABASE"),
        )
        self._sql_ = ""
        self.__stack__ = []
        self.__cursor__ = self.__db__.cursor()


    def addToStack(self, toAdd):
        """Adds a touple to the stack to be send when the next sendStack() is called"""
        self.__stack__.append(toAdd)
    
    def sendStack(self):
        #print(self._sql_, self.__stack__)
        self.__cursor__.executemany(self.__sql__, self.__stack__)



class priceDB(db):
    def __init__(self):
        super().__init__()
        self._sql_ = "INSERT INTO price (epoch, eur) VALUES (%s, %s)"



class freqDB(db):
    def __init__(self):
        super().__init__()
        self._sql_ = "INSERT INTO frequency (epoch, eur) VALUES (%s, %s)"
