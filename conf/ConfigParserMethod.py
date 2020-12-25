import configparser
config = configparser.ConfigParser()
config.read("configTest.ini")

# 获取所用的section节点程序
print(config.sections())
# 结果：['mysql', 'personal information']

# 获取指定section的options
r = config.options('mysql')
print(r)
# 结果：['db_host', 'db_port', 'db_user', 'db_pass']

# 获取指定section下指定option的值
r = config.get('mysql', 'db_host')
print(r)
# 结果：127.0.0.1

# 将读出配置文件某个section内所有键值对
r = config.items("mysql")
print(r)
# 结果：[('db_host', '127.0.0.1'), ('db_port', '3306'), ('db_user', 'root'), ('db_pass', 'password')]

# 修改某个option的值
config.set("mysql", "db_MaxConnections", "100")
config.write(open("configTest.ini", "w"))
r = config.items("mysql")
print(r)
# 注意：即使没有存储成功，也能在当前程序下正确读取新修改的值（只是路劲错误，未存储成功）
# 结果: [('db_host', '127.0.0.1'), ('db_port', '3306'), ('db_user', 'root'), ('db_pass', 'password'), ('db_maxconnections', '100')]

# 检查section或option是否存在，返回布尔值
# 检查section
a = config.has_section("personal information")
print(a)
# 结果: True
# 检查option
b = config.has_option("personal information", "address")
print(b)
# 结果: False

# 添加section和option
if not config.has_section("Grade"):
    config.add_section("Grade")
if not config.has_option("Grade", "English"):
    config.set("Grade", "English", "93")
config.write(open("configTest.ini", "w"))
print(config.items("Grade"))
# 结果: [('english', '93')]

# 删除section和option
print(config.sections())
# 结果: ['mysql', 'personal information', 'Grade']
config.remove_section("Grade")
config.write(open("configTest.ini", "w"))
print(config.sections())
# 结果: ['mysql', 'personal information']

