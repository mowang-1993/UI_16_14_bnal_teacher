import json, os


class GetData:
    @classmethod
    def get_json_data(cls, name):
        """
        读取json文件数据
        :param name: 文件名字
        :return: 文件数据
        """
        with open("./Data" + os.sep + name, "r", encoding="utf-8") as f:
            return json.load(f)
