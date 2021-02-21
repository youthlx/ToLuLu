# -*- coding:utf-8 -*-
# author xin.luo

import pymysql


# 数据库通用操作流程
def common_operate():
    # 建立数据库连接
    c = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="112358",
        database="lulu",
        charset="utf8"
    )

    # 获取执行游标
    cursor = c.cursor(cursor=pymysql.cursors.DictCursor)

    # 定义要执行的SQL语句
    sql = """
    """

    # 执行SQL语句
    cursor.execute(sql)

    # 关闭光标对象
    cursor.close()

    # 如果数据库使用完，连接需要断开，以下是关闭数据库连接
    c.close()


# 数据库的增删改查
# 数据表详情
# ----------------------------------
# id | name | taste | price| comment
# ----------------------------------
# 1  | MPDF | 3     | 20.5 | great
# ----------------------------------
# 2  | HSR  | 1     | 48   | excellent
# ----------------------------------
# 3  | CZPG | 1     | 32   | well
# ----------------------------------
conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="112358",
    database="lulu",
    charset="utf8"
)


# 新增单条记录
def add_single():
    cursor = conn.cursor()
    sql = 'insert into dish_tab(name,taste,price,comment) values (%s, %s, %s, %s);'
    cursor.execute(sql, ['MPDF', '3', '20.5', 'great'])
    conn.commit()
    cursor.close()


# 新增多条记录
def add_multiple():
    cursor =conn.cursor()
    sql = 'insert into dish_tab(name,taste,price,comment) values (%s, %s, %s, %s);'
    data = [
        ('HSR', '1', '48', 'excellent'),
        ('CZPG', '1', '32', 'well'),
    ]
    cursor.executemany(sql, data)
    conn.commit()
    cursor.close()


# 删
def remove():
    cursor = conn.cursor()
    sql = 'delete from dish_tab where `name`=%s;'
    cursor.execute(sql, ['CZPG'])
    conn.commit()
    cursor.close()


# 改
def update():
    cursor = conn.cursor()
    sql = 'update dish_tab set price=%s where `name`=%s;'
    cursor.execute(sql, ['49', 'HSR'])
    conn.commit()
    cursor.close()


# 查
# 基本查询
def query_base():
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = 'select * from dish_tab'
    cursor.execute(sql)

    data = cursor.fetchall()
    cursor.close()
    print(data)


# 分页查询
def query_page():
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 其中limit为每页数量，offset为页码
    sql = 'select * from dish_tab LIMIT 10 OFFSET 0;'
    cursor.execute(sql)

    data = cursor.fetchall()
    cursor.close()
    print(data)


# 排序查询
def query_order():
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 其中limit为每页数量，offset为页码
    sql = 'select * from dish_tab order by `id` desc;'
    cursor.execute(sql)

    data = cursor.fetchall()
    cursor.close()
    print(data)


if __name__ == '__main__':
    add_single()
    add_multiple()
    remove()
    update()
    query_base()
    query_page()
    query_order()