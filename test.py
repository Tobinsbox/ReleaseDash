#coding:utf-8
import os
from xml import sax
root_path="C:/ABSuite/Source/trunk/"

class ModelFile(sax.ContentHandler):
    def __init__(self):
        # 初始化数据，并增加一个当前数据
        self.Version = ""
        self.first=0
        self.second=0
        self.third=0

    # 文档启动的时候调用
    def startDocument(self):
        pass

    # 元素开始事件处理
    def startElement(self, name, attrs):
        self.CurrentData=name
        if self.CurrentData=='MetaData':
                self.Version=attrs['Version']
                temp = str(self.Version).split('.')
                versionLen = len(str(self.Version).split('.'))
                if (versionLen == 3):
                    self.first, self.second, self.third = temp
                elif (versionLen == 2):
                    self.first, self.second = temp

    # 文档结束的时候调用
    def endDocument(self):
        pass

def GetAllModelFiles(dir_path):
    pathDir = os.listdir(dir_path)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (dir_path, allDir))
        if os.path.isdir(child):
            if(child!=r'C:/ABSuite/Source/trunk/Debug/bin'):
                GetAllModelFiles(child+r'/')
        elif allDir.endswith(".model"):
            if(os.path.getsize(child)>0):
                handler = ModelFile()
                parser = sax.make_parser()
                parser.setContentHandler(handler)
                try:
                    parser.parse(child)
                    if int(handler.first) < 2 and int(handler.second) < 2 and int(handler.third) < 6:
                        print('Version:'+str(handler.first)+'.'+str(handler.second)+'.'+str(handler.third)+'--->'+child)
                except Exception as e:
                    print(str(e)+'--->'+child)

if __name__ == '__main__':
    GetAllModelFiles(root_path)