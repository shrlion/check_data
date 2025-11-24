import pymysql
import configparser
import logging


# 读取配置文件函数
def config():

    cf = configparser.ConfigParser()
    cf.read('config.ini')



    sections = cf.sections()

    for section in sections:

        host = cf.get(section, 'host')
        user = cf.get(section, 'user')
        passwd = cf.get(section, 'password')
        db = cf.get(section, 'database')

        db_conn(host, user, passwd, db)


        print(section)

    print(sections)


# 连接数据库函数
def db_conn(host,user,passwd,db):

    logging.basicConfig(
        level = logging.DEBUG,
        format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filename = "./logs/db.conn.log"
    )

    try:
        db = pymysql.connect(
            host = host,
            user = user,
            passwd = passwd,
            database = db
        )
    except Exception as e:
        logging.error(f"This is {e}")


    cursor = db.cursor()

    cursor.execute('show database')


    db.close()








if __name__ == "__main__":
    config()