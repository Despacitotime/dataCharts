import configparser


class ConfigParser(object):
    config_dic = {}

    @classmethod
    def get_config(cls, sector, item):
        value = None
        try:
            value = cls.config_dic[sector][item]
        except KeyError:
            cf = configparser.ConfigParser()
            cf.read("configTest.ini", encoding='utf8')
            value = cf.get(sector, item)
            cls.config_dic = value
        finally:
            return value


if __name__ == "__main__":
    con = ConfigParser()
    res = con.get_config('mysql', 'db_user')

print(res)
# 结果： root