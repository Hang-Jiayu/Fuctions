import sys
import xml.etree.ElementTree as ET
import json
class File():
#------------------------------------------------------初始化
    def __init__(self,filename=None):
        self.filename=filename
        self.__get_f=None
        if self.filename==None:
            print("请提供文件名！")
            return False
        try:
            self.__get_f=open(self.filename,'a',encoding='utf8')
        except:
            print("打开%s文件有问题！"%(self.filename))
            return False
#------------------------------------------------------写普通文件
    def writeSimplefile(self,element):
        try:
           self.__get_f.write(element+'\n')
        except:
            print("往%s文件里写%s出错！"%(self.filename,element))
            sys.exit()
#------------------------------------------------------关闭文件
    def closefile(self):
        if self.__get_f:
            self.__get_f.close()
#------------------------------------------------------写XML文件
    def writeXMLfile(self,element):
        self.build=File(self.filename)
        self.buildname=element
        self.__get_f=open(self.filename,'a',encoding='utf8')
        if type(element)==dict:
            for self.get in element.items():
                if self.buildname[1][0]==0 :
                    self.__get_f.write(self.get[1][1]+'\n')
                else:
                    self.__get_f.write(' '*self.bget[1][0]+self.get[1][1]+'\n')
#-----------------------------------------------------写json文件
    def writeJsonfile(self,element):
        self.flag=False
        self.element2=element
        if type(self.element2)!=dict:
            return self.flag
        try:
            self.j_file=open(self.filename,'w')
            json.dump(self.element2,self.j_file,ensure_ascii=False)
            self.flag=True
        except:
            print("往%s里写数据出错！"%(self.filename))
        finally:
            if self.flag:
                self.j_file.close()
            return self.flag
#------------------------------------------------------重写Json文件
    def rewriteJsonfile(self,element):
        self.flag=False
        self.element2=element
        if type(self.element2)!=dict:
            return self.flag
        try:
            self.j_file=open(self.filename,'a')
            json.dump(self.element2,self.j_file,ensure_ascii=False)
            self.flag=True
        except:
            print("往%s里写数据出错！"%(self.filename))
        finally:
            if self.flag:
                self.j_file.close()
            return self.flag
#------------------------------------------------------读Json文件
    def readJsonfile(self):
        self.flag1=False
        self.dictObject={}
        try:
            self.j_file=open(self.filename,'r',encoding='utf8')
            self.dictObject=json.load(self.j_file)
            self.flag1=True
        except:
            print('从%s里读JSON数据出错！'%(self.filename))
        finally:
            if self.flag1:
                self.j_file.close()
            return (self.dictObject)
#-----------------------------------------------------读普通文件
    def readSimplefile(self):
        self.f=open(self.filename,'r')
        self.__L_s=self.f.readlines()
        return (self.__L_s)
#-----------------------------------------------------读XML文件
    def readXMLfile(self):
        self.xml_file=self.filename
        self.tree=ET.parse(self.xml_file)
        self.root=self.tree.getroot()
        for self.child in self.root[0][1][0]:
            return (self.child.tag,"------",self.child.attrib)
#-----------------------------------------------------根据标签名查找XML文件
    def findXMLfile(self,items):
        self.xml_file=self.filename
        self.tree=ET.parse(self.xml_file)
        self.root=self.tree.getroot()
        self.items=items
        self.captionlist=self.root[0][1][0]
        return (self.captionlist[0].tag,':',self.captionlist[0].text)
#-----------------------------------------------------修改XML文件
    def editXMLfile(self,list,Attribute,items):
        self.xml_file=self.filename
        self.tree=ET.parse(self.xml_file)
        self.root=self.tree.getroot()
        self.items=items
        self.captionlist=self.root[0][1][0]
        self.Attribute=Attribute
        self.list=list
        self.items2=items
        self.captionlist[0].set(self.list,self.Attribute)
        self.captionlist[0].text=self.items2
        self.tree.write(self.xml_file)
#-----------------------------------------------------