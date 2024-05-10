import random

def get_data() -> str:
    with open("./src/data.lib", 'r', encoding='utf-8') as f:
        data = f.readline()
    f.close()
    # data  = 'dsngjlaghRWOUGHOURHGAOHODUHDnjldNDKHGpgojreoihoureyq974y09tue][GOE'
    return data


