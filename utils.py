# -*- coding: utf-8 -*-
import time
import pymysql
from flask import jsonify

def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年", "月", "日")

def get_conn():
    conn = pymysql.connect(host='localhost', user='root', password='root', db='test', charset='utf8')
    cursor = conn.cursor()  # 获取游标
    return conn, cursor

def close_conn(conn, cursor):
    cursor.close()
    conn.close()

def query(sql,*args):
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res

def get_c1_data():
    sql = "SELECT book_name,url FROM ddpython LIMIT 30"
    res = query(sql)
    return res


if __name__ == '__main__':
    print(get_c1_data())