import os


def get_file_size(func):
    def wrapper(file_name, file_extension):
        # path = f"./data/{file_name}.{file_extension}"
        # statinfo = os.stat(path=path)
        # print(statinfo.st_size)
        func(file_name, file_extension)
    return wrapper