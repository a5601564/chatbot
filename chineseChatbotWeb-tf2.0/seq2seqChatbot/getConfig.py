import os
from configparser import SafeConfigParser

def get_config(config_file=r'seq2seq.ini'):

    f = open(config_file)  # 打开训练数据集所在的文档
    bool1 = os.path.exists(config_file)

    parser = SafeConfigParser()
    parser.read(config_file)
    parser.sections()
    # get the ints, floats and strings
    _conf_ints = [ (key, int(value)) for key,value in parser.items('ints') ]
    #_conf_floats = [ (key, float(value)) for key,value in parser.items('floats') ]
    _conf_strings = [ (key, str(value)) for key,value in parser.items('strings') ]
    return dict(_conf_ints  + _conf_strings)