import xmind
import os
import shutil
import zipfile
from openpyxl import load_workbook
import platForm.otherUtil.excel_to_xmind as ex
import time




def extract(d_path, f_path):
    """
    zip解压缩乱码问题处理
    :param d_path:
    :param f_path:
    :return:
    """
    global zf
    # os.chdir(root_path)
    root = d_path
    if not os.path.exists(root):
        os.makedirs(root)
    # print('ffff',os.getcwd())
    zf = zipfile.ZipFile(f_path,"r")

    for n in zf.infolist():
        srcName = n.filename
        try:
            decodeName = srcName.encode("cp437").decode("utf-8")
        except:
            try:
                decodeName = srcName.encode("cp437").decode("gbk")
            except:
                decodeName = srcName
        spiltArr = decodeName.split("/")
        path = root
        for temp in spiltArr:
            path = os.path.join(path, temp)

        if decodeName.endswith("/"):
            if not os.path.exists(path):
                os.makedirs(path)
        else:
            if not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            f = open(path, "wb")
            f.write(zf.read(srcName))
            f.close()
    zf.close()


# 修复无法打开xmind文件的问题
def aftertreatment(path):

    # 修改名字
    retval = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.dirname(path)
    name = os.path.basename(path)
    unzip_folder = os.path.splitext(name)[0]
    zip_name = unzip_folder + ".zip"
    os.chdir(folder)
    os.rename(name, zip_name)
    os.chdir(retval)
    # 解压
    unzip_path = os.path.join(folder, unzip_folder)
    if not os.path.exists(unzip_path):
        os.mkdir(unzip_path)

    inf_folder = os.path.join(unzip_path, "META-INF")
    if not os.path.exists(inf_folder):
        os.mkdir(inf_folder)

    extract(unzip_path, os.path.join(folder, zip_name))
    shutil.copyfile("./main_fest.xml", os.path.join(inf_folder, "manifest.xml"))
    os.remove(os.path.join(folder, zip_name))
    shutil.make_archive(unzip_path, 'zip', unzip_path)
    file_path = unzip_path + '.zip'
    # print(file_path)
    os.chdir(os.path.dirname(file_path))
    os.rename(os.path.basename(file_path), name)
    os.chdir(retval)
    shutil.rmtree(unzip_path)


# 转化成xmind文件
def gen_xmind_file(xls, save_path,filename):
    # begin_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    # ex.save_path = ex.root_path + begin_time + r'-save_xmind'
    #
    # os.mkdir(ex.save_path)
    os.chdir(ex.file_path)

    global sub_topic
    readbook = load_workbook(xls)

    sheet_list = readbook.get_sheet_names()
    count_sheets = len(sheet_list)
    try:
        for i in range(count_sheets):
            sheet_name = sheet_list[i]
            workbook = xmind.load(filename+ sheet_name + '.xmind')

            first_sheet = workbook.getPrimarySheet()
            # 根节点
            root_topic = first_sheet.getRootTopic()
            root_topic.setTitle(sheet_name)
            sheet = readbook.get_sheet_by_name(sheet_name)

            # 统计sheet有多少列
            count = 0
            for i in list(sheet.rows)[0]:
                # print(i.value)
                if i.value is None:
                    break
                count += 1
            for row in list(sheet.rows)[1:]:
                for c in range(count):
                    m = 0
                    if row[c].value is None:
                        value = '空'
                    else:
                        value = row[c].value
                    if c == 0:
                        if len(root_topic.getSubTopics()) == 0:
                            sub_topic = root_topic.addSubTopic()
                            sub_topic.setTitle(value)
                        else:
                            for j in root_topic.getSubTopics():
                                m += 1
                                if value == j.getTitle():
                                    sub_topic = j
                                    break
                                elif m == len(root_topic.getSubTopics()):
                                    sub_topic = root_topic.addSubTopic()
                                    sub_topic.setTitle(value)
                    else:
                        if len(sub_topic.getSubTopics()) == 0:
                            sub_topic = sub_topic.addSubTopic()
                            sub_topic.setTitle(value)
                        else:
                            for k in sub_topic.getSubTopics():
                                m += 1
                                if value == k.getTitle():
                                    sub_topic = k
                                    break
                                elif m == len(sub_topic.getSubTopics()):
                                    sub_topic = sub_topic.addSubTopic()
                                    sub_topic.setTitle(value)
            xmind.save(workbook, path=filename +sheet_name + '.xmind')
            # 修复
            aftertreatment(r'./' + filename + sheet_name + '.xmind')

        os.chdir(ex.file_path)
        path = os.getcwd()
        path_list = os.listdir(path)
        for filename in path_list:
            if filename[-6:] == '.xmind':
                shutil.move(filename, save_path)

        # # 如果有多个xmind文件则打包
        # os.chdir(ex.save_path)
        # path_list = os.listdir(ex.save_path)
        # if len(path_list) > 1:
        #     shutil.make_archive('./xmind_file','zip','./')
        #     # 删除多余文件
        #     for filename in path_list:
        #         if os.path.splitext(filename)[1] == '.xmind':
        #             os.remove(filename)
        return 'OK'
    except:
        pass


def zip_ya(start_dir):
    start_dir = start_dir  # 要压缩的文件夹路径
    file_news = start_dir + '.zip'  # 压缩后文件夹的名字

    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(start_dir):
        f_path = dir_path.replace(start_dir, '')  # 这一句很重要，不replace的话，就从根目录开始复制
        f_path = f_path and f_path + os.sep or ''  # 实现当前文件夹以及包含的所有文件的压缩
        for filename in file_names:
            z.write(os.path.join(dir_path, filename), f_path + filename)
    z.close()
    return file_news

if __name__ == '__main__':
    gen_xmind_file(xls=r'./创客拉新需求app部分_测试用例.xls')