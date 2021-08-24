import pymysql
class Mysqlimplement():
#---------------------------------------初始化
    def __init__(self,username,passwordname,hostname,databasename,portname,charsetname):
        self.data=databasename
        self.user=username
        self.host=hostname
        self.password=passwordname
        self.port=portname
        self.charset=charsetname
        self.web=pymysql.connect(user=self.user,password=self.password,host=self.host,db=self.data,port=self.port,charset=self.charset)
        self.cursor=self.web.cursor()
#---------------------------------------创建表格(createtable)
    def createtable(self,tablename,tablelengh):
        self.table=tablename
        self.tableiengh=tablelengh
        self.cursor.execute('create table if not exists '+self.table+' ('+self.tableiengh+');')
#---------------------------------------读取数据(readall)
    def readall(self,tablename):
        self.table=tablename
        self.cursor.execute('select * from '+self.table+';')
        for self.row in self.cursor.fetchall():
            print(self.row)
#--------------------------------------读取指定数据(find)
    def find(self,tablename,object,where=None):
        self.table=tablename
        self.object=object
        self.where=where
        if self.where==None:
            self.cursor.execute('select '+self.object+' from '+self.table+';')
            for self.row in self.cursor.fetchall():
                print(self.row)
        else:
            self.cursor.execute('select '+self.object+' from '+self.table+' where '+self.where+';')
            for self.row in self.cursor.fetchall():
                print(self.row)
#--------------------------------------更新部分数据(updatesth)
    def updatesth(self,tablename,newfield,object):
        self.table=tablename
        self.new=newfield
        self.object1=object
        self.cursor.execute('update '+self.table+' set '+self.new+' where '+self.new+';')
#--------------------------------------更新全部数据(updateall)
    def updateall(self,tablename,field):
        self.newfield=field
        self.table=tablename
        self.cursor.execute('update '+self.table+' set '+self.newfield+';')
#-------------------------------------插入数据(insert)
    def insert(self,tablename,field):
        self.field=field
        self.table=tablename
        self.cursor.execute('insert into '+self.table+' values ('+self.field+');')
#-------------------------------------删除数据表(deletetable)
    def deletetable(self,tablename):
        self.table=tablename
        self.cursor.execute('drop table '+self.table+';')
#-------------------------------------删除字段(deletefield)
    def deletefield(self,tablename,field):
        self.table=tablename
        self.field=field
        self.cursor.execute('alter table '+self.table+' drop '+self.field+';')
#-------------------------------------添加字段(addfield)
    def addfield(self,tablename,fieldlengh):
        self.table=tablename
        self.fieldlengh=fieldlengh
        self.cursor.execute('alter table '+self.table+' add '+self.fieldlengh+';')
#-------------------------------------修改字段数据类型(editfield)
    def editfield(self,tablename,fieldname,fieldlengh):
        self.table=tablename
        self.fieldlengh=fieldlengh
        self.field=fieldname
        self.cursor.execute('alter table '+self.table+' modify '+self.field+' '+self.fieldlengh+';')
#-------------------------------------修改字段名(renamefield)
    def renamefield(self,tablename,oldfield,newfield,newfieldlengh):
        self.table=tablename
        self.oldfield=oldfield
        self.newfield=newfield
        self.newfieldlengh=newfieldlengh
        self.cursor.execute('alter table '+self.table+' change '+self.oldfield+' '+self.newfield+' '+newfieldlengh+';')
#-------------------------------------修改表名（renametable)
    def renametable(self,oldtable,newtable):
        self.oldtable=oldtable
        self.newtable=newtable
        self.cursor.execute('alter table '+self.oldtable+' rename to '+self.newtable+';')
#-------------------------------------统计某一列列不为空的数据总数(countnum)
    def countnum(self,field,tablename):
        self.field=field
        self.table=tablename
        self.cursor.execute('select count('+self.field+') from '+self.table+';')
        for self.row in self.cursor.fetchall():
            print(self.row)
#-------------------------------------计算指定列的最大值，如果指定列是字符串类型则使用字符串排序运算(maxnum)
    def maxnum(self,field,tablename):
        self.field=field
        self.table=tablename
        self.cursor.execute('select max('+self.field+') from '+self.table+';')
        for self.row in self.cursor.fetchall():
            print(self.row)
#-------------------------------------计算指定列的最小值，如果指定列是字符串类型则使用字符串排序运算(minnum)
    def minnum(self,which=None,field=None,tablename=None):
        self.table=tablename
        self.field=field
        self.which=which
        if self.which==None:
            self.cursor.execute('select min('+self.field+') from '+self.table+';')
            for self.row in self.cursor.fetchall():
                print(self.row)
        else:
            self.cursor.execute('select '+self.which+' min('+self.field+') from '+self.table+';')
            for self.row in self.cursor.fetchall():
                print(self.row)
#-------------------------------------计算指定列的数值和，如果指定列类型不是数值类型则计算结果为0(sumnum)
    def sumnum(self,field,tablename):
        self.field=field
        self.table=tablename
        self.cursor.execute('select sum('+self.field+') from '+self.table+';')
        for self.row in self.cursor.fetchall():
            print(self.row)
#-------------------------------------计算指定列的平均值，如果指定列类型不是数值类型则计算结果为0(avgnum)
    def avgnum(self,field,tablename):
        self.field=field
        self.table=tablename
        self.cursor.execute('select avg('+self.field+') from '+self.table+';')
        for self.row in self.cursor.fetchall():
            print(self.row)
#--------------------------------------获得日期，时间(now)
    def now(self,addorsub=None,num=None,what=None):
        self.how=addorsub
        self.num=num
        self.what=what
        if self.how==None:
            self.cursor.execute('SELECT NOW();')
            for self.row in self.cursor.fetchall():
                print(self.row)
        elif self.how=='add':
            self.cursor.execute('SELECT DATE_ADD(NOW(),INTERVAL '+self.num+' '+self.what+');')
            for self.row in self.cursor.fetchall():
                print(self.row)
        else:
            self.cursor.execute('SELECT DATE_SUB(NOW(),INTERVAL '+self.num+' '+self.what+');')
            for self.row in self.cursor.fetchall():
                print(self.row)
#--------------------------------------获得现在的日期(nowdate)
    def nowdate(self):
        self.cursor.execute('SELECT DATE (NOW());')
        for self.row in self.cursor.fetchall():
            print(self.row)
#--------------------------------------获得现在的时间(nowtime)
    def nowtime(self):
        self.cursor.execute('SELECT TIME (NOW());')
        for self.row in self.cursor.fetchall():
            print(self.row)
#--------------------------------------获得现在的月份(nowmounth)
    def nowmounth(self):
        self.cursor.execute('SELECT MONTH (NOW());')
        for self.row in self.cursor.fetchall():
            print(self.row)
#--------------------------------------获得现在的年份(nowmounth)
    def nowyear(self):
        self.cursor.execute('SELECT YEAR (NOW());')
        for self.row in self.cursor.fetchall():
            print(self.row)
#--------------------------------------获得从之前的日期到下个日期的天数(days)
    def days(self,date1,date2):
        self.date1=date1
        self.date2=date2
        self.cursor.execute('select datediff('+self.date1+','+self.date2+');')
        for self.row in self.cursor.fetchall():
            print(self.row)
#--------------------------------------判断某个字段的值是否在指定集合中(intable)
    def intable(self,tablename,object,ifnot=None):
        self.table=tablename
        self.object=object
        self.ifnot=ifnot
        if self.ifnot==None:
            self.cursor.execute('select * from '+self.table+' where sid in ('+self.object+');')
            for self.row in self.cursor.fetchall():
                print(self.row)
        else:
            self.cursor.execute('select * from '+self.table+' where sid not in ('+self.object+');')
            for self.row in self.cursor.fetchall():
                print(self.row)
#--------------------------------------判断某个字段的值是否在指定的范围之内。如果字段的值在指定范围内，则将所在的记录将查询出来(between)
    def between(self,tablename,object,lengh1,lengh2,ifnot=None):
        self.table=tablename
        self.object=object
        self.lengh1=lengh1
        self.lengh2=lengh2
        self.ifnot=ifnot
        if self.ifnot==None:
            self.cursor.execute('select * from '+self.table+' where '+self.object+' between '+self.lengh1+' and '+self.lengh2+';')
            for self.row in self.cursor.fetchall():
                print(self.row)
        else:
            self.cursor.execute('select * from '+self.table+' where '+self.object+' not between '+self.lengh1+' and '+self.lengh2+';')
            for self.row in self.cursor.fetchall():
                print(self.row)
#-------------------------------------判断字段的值是否为空值(isnull)
    def isnull(self,tablename,field):
        self.table=tablename
        self.field=field
        self.cursor.execute('select * from '+self.table+' where '+self.field+' is not null;')
        for self.row in self.cursor.fetchall():
            print(self.row)
#-------------------------------------连接两个或者多个查询条件的查询(andsth)
    def andsth(self,tablename,lengh1,lengh2):
        self.table=tablename
        self.lengh1=lengh1
        self.lengh2=lengh2
        self.cursor.execute('select * from '+self.table+' where '+self.lengh1+' and '+self.lengh2+';')
        for self.row in self.cursor.fetchall():
            print(self.row)
#-------------------------------------连接多个査询条件，只要记录满足其中任意一个条件就会被查询出来(orsth)
    def orsth(self,tablename,lengh1,lengh2):
        self.table=tablename
        self.lengh1=lengh1
        self.lengh2=lengh2
        self.cursor.execute('select * from '+self.table+' where '+self.lengh1+' or '+self.lengh2+';')
        for self.row in self.cursor.fetchall():
            print(self.row)
#-------------------------------------判断两个字符串是否相匹配(likesimple)
    def likesimple(self,tablename,field,string):
        self.table=tablename
        self.string=string
        self.field=field
        self.cursor.execute('select * from '+self.table+' where '+self.field+' like '+self.string+';')
        for self.row in self.cursor.fetchall():
            print(self.row)
#-------------------------------------用于匹配任意长度的字符串(likeall)例如，字符串“a%”匹配以字符a开始任意长度的字符串
    def likeall(self,tablename,field,string):
        self.table=tablename
        self.string=string
        self.field=field
        self.cursor.execute('select * from '+self.table+' where '+self.field+' like '+self.string+';')
        for self.row in self.cursor.fetchall():
            print(self.row)
#------------------------------------下划线通配符(wildcard)只匹配单个字符，如果要匹配多个字符，需要连续使用多个下划线通配符。例如，字符串“ab_”匹配以字符串“ab”开始长度为3的字符串，如abc、abp等等；字符串“a__d”匹配在字符“a”和“d”之间包含两个字符的字符串，如"abcd"、"atud"等等
    def wildcard(self,tablename,field,string):
        self.table=tablename
        self.string=string
        self.field=field
        self.cursor.execute('select * from '+self.table+' where '+self.field+' like '+self.string+';')
        for self.row in self.cursor.fetchall():
            print(self.row)
#------------------------------------限制查询结果的数量(limit)
    def limit(self,tablename,field,lengh):
        self.table=tablename
        self.field=field
        self.lengh1=lengh
        self.cursor.execute('select * from '+self.table+' order by '+self.field+' asc limit '+self.lengh1+';')
#------------------------------------为表和字段取別名(astable)，该别名代替表和字段的原名参与查询操作
    def astable(self,tablename,another):
        self.table=tablename
        self.another=another
        self.cursor.execute('select * from '+self.table+' as '+self.another+';')
#------------------------------------GROUP BY 子句可像切蛋糕一样将表中的数据进行分组(group)，再进行查询等操作
    def easygroup(self,field,tablename,condition=None):
        self.field=field
        self.table=tablename
        self.condition=condition
        if self.condition==None:
            self.cursor.execute('select count(*),'+self.field+' from '+self.table+' group by '+self.field+';')
            for self.row in self.cursor.fetchall():
                print(self.row)
        else:
            self.cursor.execute('select count(*),'+self.field+' from '+self.table+' where '+self.condition+' group by '+self.field+';')
            for self.row in self.cursor.fetchall():
                print(self.row)
    #--------------------------
    def difgroup(self,field,field2,tablename,condition=None):
        self.field=field
        self.field2=field2
        self.table=tablename
        self.condition=condition
        self.object=object
        if self.condition==None:
            self.cursor.execute('select sum('+self.field2+'),'+self.field+' from '+self.table+' group by '+self.field+';')
            for self.row in self.cursor.fetchall():
                print(self.row)
        else:
            self.cursor.execute('select sum('+self.field2+'),'+self.field+' from '+self.table+' group by '+self.field+' having sum('+self.field2+')'+self.condition+';')
            for self.row in self.cursor.fetchall():
                print(self.row)
#----------------------------------使用ORDER BY(orderby)对查询结果进行排序
    def orderby(self,tablename,field,ascordesc=None):
        self.field=field
        self.table=tablename
        self.ifnot=ascordesc
        if self.ifnot==None:
            self.cursor.execute('select * from '+self.table+' order by '+self.field+' asc;')
            for self.row in self.cursor.fetchall():
                print(self.row)
        elif self.ifnot=='asc':
            self.cursor.execute('select * from '+self.table+' order by '+self.field+' asc;')
            for self.row in self.cursor.fetchall():
                print(self.row)
        else:
            self.cursor.execute('select * from '+self.table+' order by '+self.field+' desc;')
            for self.row in self.cursor.fetchall():
                print(self.row)
#-----------------------------------关联查询(findwith)
    def findwith(self,tablename1,table1field,tablename2,table2field1,table2field2,table2field2lengh):
        self.table1=tablename1
        self.table2=tablename2
        self.field1=table1field
        self.field2=table2field1
        self.field3=table2field2
        self.lengh=table2field2lengh
        self.cursor.execute('select * from '+self.table1+' where '+self.field1+'= (select '+self.field2+' from '+self.table2+' where '+self.field3+'='+self.lengh+');')
        for self.row in self.cursor.fetchall():
            print(self.row)
#----------------------------------关联关系的删除数据(deletedata)
    def deletedata(self,tablename1,table1field,tablename2,table2field1,table2field2,table2field2lengh):
        self.table1=tablename1
        self.table2=tablename2
        self.field1=table1field
        self.field2=table2field1
        self.field3=table2field2
        self.lengh=table2field2lengh
        self.cursor.execute('delete from '+self.table1+' where '+self.field1+'=(select '+self.field2+' from '+self.table2+' where '+self.field3+'='+self.tableiengh+');')
        self.cursor.execute('delete from '+self.table2+' where '+self.field3+'='+self.tableiengh+';')
#---------------------------------