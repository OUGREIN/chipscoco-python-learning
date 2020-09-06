# __author__ = 橙子老师
# __date__ = 2020-08-24

# 导入MySQLdb模块
import MySQLdb
import config


"""
所有回调函数都遵循相同的接口规范，读者在实际开发中，可以将回调函数作为业务层的代码
分离到其它文件
"""

def query_all_employee(table_name, cursor, **kwargs):
    """
    :param table_name: 有效的mysql数据表名
    数据表名的关系模型(id, name)
    :param ursor: 数据库的游标对象
    :return:
    """

    sql = "select id, name from {}".format(table_name)
    cursor.execute(sql)
    for index, row in enumerate(cursor.fetchall()):
        print("{}. 员工编号:{} 员工姓名:{}".format(index+1, row[0], row[1]))


def add_employee(table_name , cursor, **kwargs):
    """
    :param table_name: 有效的mysql数据表名
    数据表名的关系模型(id, name)
    :param cursor: 数据库的游标对象
    :param kwargs: 可变参数，支持传递的参数有db_handler，表示MySQL数据库对象,
    redis_handler表示redis连接对象
    :return:
    """

    employee_name = input("请输入员工的姓名:___\b\b\b")
    employee_age = input("请输入员工的年龄:___\b\b\b")
    employee_salary = input("请输入员工的工资:___\b\b\b")
    employee_sex = input("请输入员工的性别:___\b\b\b")
    sql =  "insert into {} (name, age, salary, sex) values(%s, %s, %s, %s)".format(table_name)

    affected_rows = cursor.execute(sql, (employee_name, employee_age, employee_salary, employee_sex))
    if affected_rows < 1:
        print("数据库操作发生异常")
    else:
        _ = kwargs["db_handler"].commit() if "db_handler" in kwargs else None
        print("员工{}已被添加至数据库".format(employee_name))


def delete_employee(table_name, cursor, **kwargs):
    """
    :param table_name: 有效的mysql数据表名
    数据表名的关系模型(id, name)
    :param cursor: 数据库的游标对象
    :param kwargs: 可变参数，支持传递的参数有db_handler，表示MySQL数据库对象,
    redis_handler表示redis连接对象
    :return:
    """

    try:
        employee_id = int(input("请输入员工的编号:__\b\b"))
    except ValueError:
        employee_id = -1
        print("你输入了无效的员工编号")

    if employee_id > 0:
        sql = "delete from {} where id=%s".format(table_name)
        affected_rows = cursor.execute(sql, (employee_id, ))
        if affected_rows < 1:
            print("员工编号{}不存在".format(employee_id))
        else:
            _ = kwargs["db_handler"].commit() if "db_handler" in kwargs else None
            print("编号为{}的员工已从数据库删除".format(employee_id))


class SimpleEmployeeMs:

    def __init__(self, table_name, cursor, db_handler=None, redis_handler=None):
        self.__db_handler = db_handler
        self.__table_name = table_name
        self.__cursor = cursor
        self.__redis_handler = redis_handler

        """
        定义命令字典结构,格式举例:{
        1: callback_function
        }
        这样用户在输入指定的命令时，直接调用对应的回调函数
        回调函数由用户进行定义
        """
        self.__commands = {}
        self.__begin_prompt = "输入<>中的指令来执行对应的操作:\n"
        self.__quit_prompt = "<quit> 退出员工管理系统\n"
        self.__prompts = []
        self.__command_index = 1

    def __obtain_user_command(self, prompt):

        command = "quit"
        valid = True
        try:
            command = input(prompt)
            _ = self.__commands[int(command)]

        except (ValueError, KeyError):
            if command != "quit":
                command = None
                valid = False
        return command, valid

    def add_command(self, prompt, cb):
        '''

        :param prompt:表示命令行提示消息，eg.:“查询所有员工”
        :param cb: 回调函数，用来支持特定的业务逻辑
        :return:
        '''
        self.__commands[self.__command_index] = cb
        """
        ①__commands是一个字典对象，键名为命令编号
        键值为具体的命令执行，通过回调函数来执行相应的处理
        {
          0:command,
          1:command
        }
        """
        self.__command_index +=1
        self.__prompts.append(prompt)

    def __generate_prompt(self):
        prompt = self.__begin_prompt
        for index, value in enumerate(self.__prompts):
            prompt += "<{}> {}\n".format(index+1, value)
        prompt += self.__quit_prompt
        return prompt


    def serve_forever(self):
        prompt =  self.__generate_prompt()
        while True:
            command, valid = self.__obtain_user_command(prompt)
            if not valid:
                print("你输入了非法的指令!")
                continue

            if command == "quit":
                    break

            self.__commands[int(command)](self.__table_name, self.__cursor,
                                          db_handler = self.__db_handler)
            print("--------------------------------------------\n")

        self.__cursor.close()


if __name__ == "__main__":

    """
    (1)数据库的配置信息
    (2)读者在实际开发中，可以将配置信息单独写到配置文件中，
        将配置信息与具体的业务代码进行分离，有助于提升代码的可维护性
    """
    DB_CONFING = {
        "mysql": {
            "host": "localhost",
            "username": "chipscoco",
            "password": "tesT123.",
            "database": "haipeng"
        },
        "redls": {

        }
    }


    """
    在连接数据库时，需指定数据库的字符编码，否则会出现乱码
    mysql创建数据表时的默认编码为utf8
    """
    try:
            db = MySQLdb.connect(config.DB_CONFIG["mysql"]["host"],config.DB_CONFIG["mysql"]["username"]
            , config.DB_CONFIG["mysql"]["password"],config.DB_CONFIG["mysql"]["database"], charset="utf8")
            mysql_cursor = db.cursor()
            # 如果cursor对象无效或表名table_name不存在，则会产生异常
            table_name = "employee"
            mysql_cursor.execute("select 0 from {}".format(table_name))
            simple_employee_ms = SimpleEmployeeMs(table_name, mysql_cursor, db)

            # 员工管理系统的命令行选项，以及处理逻辑都由用户来进行定义
            simple_employee_ms.add_command("查询所有员工", query_all_employee)
            simple_employee_ms.add_command("添加新员工",  add_employee)
            simple_employee_ms.add_command("删除老员工", delete_employee)
            simple_employee_ms.serve_forever()

    except Exception as e:
            print("数据库连接或获取游标对象时产生异常！{}".format(e))