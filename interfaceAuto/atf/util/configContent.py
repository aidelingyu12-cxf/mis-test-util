import os, yaml

class confContent():

    def getAppConfigs(self, test_or_dev):
        global configFilePath
        projectPath = os.path.dirname(os.path.dirname(__file__))  # 工程主路径
        # 根据传参，选择测试或生产环境的配置
        if test_or_dev == 'test':
            configFilePath = projectPath + "/resources/requestData/appData/test_conf.yml"
        elif test_or_dev == 'dev':
            configFilePath = projectPath + "/resources/requestData/appData/dev_conf.yml"
        conf = open(configFilePath, encoding='utf8').read()  # 配置文件内容
        ConfigFileContent = yaml.load(conf, Loader=yaml.FullLoader)
        return ConfigFileContent

    def getMiniAppConfigs(self, test_or_dev):
        global configFilePath
        projectPath = os.path.dirname(os.path.dirname(__file__))  # 工程主路径
        if test_or_dev == 'test':
            configFilePath = projectPath + "/resources/requestData/miniappData/test_conf.yml"
        elif test_or_dev == 'dev':
            configFilePath = projectPath + "/resources/requestData/miniappData/dev_conf.yml"
        conf = open(configFilePath, encoding='utf8').read()  # 配置文件内容
        ConfigFileContent = yaml.load(conf, Loader=yaml.FullLoader)
        return ConfigFileContent

    def getApph5Configs(self):
        projectPath = os.path.dirname(os.path.dirname(__file__))  # 工程主路径
        configFilePath = projectPath + "/resources/requestData/apph5Data/dev_conf.yml"
        conf = open(configFilePath, encoding='utf8').read()  # 配置文件内容
        ConfigFileContent = yaml.load(conf, Loader=yaml.FullLoader)
        return ConfigFileContent