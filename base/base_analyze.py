import yaml
import os


def data_analyze(filename, data_key):
    with open(".%sdata%s%s" % (os.sep, os.sep, filename), "r") as f:
        data = yaml.full_load(f)
        data_dict = data[data_key]
        arr = []
        for i in data_dict.values():
            arr.append(i)
        return arr


if __name__ == '__main__':
    print(data_analyze("search_data.yaml", "test_search"))
