# encoding=utf-8

import sys
from ..FileProcessBasic import FileProcessBasic
# sys.path.append("..")

class Processor(FileProcessBasic):
    'GPR_S3S4文件处理类'

    # 查找关键字
    def findKeywords(self):
        pass

    # 寻找上下文
    def findContent(self):
        pass

    # 后续的处理
    def subsequentProcess(self):
        pass

    def run(self,inputpath,ouputpath):
        print("hello world \t"+inputpath+"\t"+ouputpath)