import pymysql
import configparser


cf = configparser.ConfigParser()

cf.read("config.ini")

sections = cf.sections()

for section in sections:
    print(section)