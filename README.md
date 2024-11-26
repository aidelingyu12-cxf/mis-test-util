说明书

项目搭建：
1、构建python基础运行环境：复制当前目录下python-Dockerfile至其他目录并命名为Dockerfile，执行docker build -t python3.6.3 . 以构建基础python3.6.3镜像
2、构建项目dockerfile: 修改当前目录下Dockerfile内容来创建构建本项目的基础镜像
3、创建jenkin流水线并修改、复制当前目录下jenkins-pipeline文件的内容至jenkins流水线内已完成jenkins流水线的创建
4、修改流水线代码分支，并执行流水线以启动项目



接口自动化使用方法：
1、在app/atf/resources目录下创建interfaceInfo.xlsx用于存放接口信息并填写接口
2、在app/atf/resources目录下创建requestData目录用于存放请求数据
3、修改app/atf下的startUp.py
4、在app/atf下创建当前项目的case目录用于存放case
5、修改app/atf/resources目录下的conf.yml
5、编写case，导入
    import unittest      
    from app.atf.cases import Logger, cr, req, skip 
    from parameterized import parameterized
    创建项目类，创建setUpClass和tearDownClass
    创建测试方法，模板：
        uri = '/banner/list'
        resp = req.getResp(dataMap=self.dataMap, uri=uri)
        print(resp)
        self.assertEqual(resp['code'], '00000', "code:返回实际结果是->:%s" % resp['code'])
    

