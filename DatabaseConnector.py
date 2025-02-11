import mysql.connector
import dotenv 


class db:
    # !!! Currently only for price !!!
    def __init__(self):
        __env__ = dotenv.DotEnv()
        """self.__db__ = mysql.connector.connect(
            host="localhost",
            user=__env__.get("USER"),
            password=__env__.get("PASSWORD"),
            database=__env__.get("DATABASE")
        )"""

        self.__sql__ = f"INSERT INTO price (epoch, eur) VALUES (%s, %s)"
        self.__stack__ = []
        # self.__cursor__ = self.__db__.cursor()


    def addToStack(self, toAdd):
        """Adds a touple to the stack to be send when the next sendStack() is called"""
        self.__stack__.append(toAdd)
    
    def sendStack(self):
        print(self.__sql__, self.__stack__)
        #self.__cursor__.executemany(self.__sql__, self.__stack__)


