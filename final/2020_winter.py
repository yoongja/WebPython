class MySelfClass:
    def __init__(self,ID,Birthday):
        self.ID = ID
        self.Birthday = Birthday
        
   
    def getStudentID(self):
        Id = self.ID
        if len(Id)<10:
            for i in range(len(Id),11):
                Id.append(0)
        return Id
 
    def  getBirthday(self):
        return self.Birthday
    
    def  getStudentIDByInteger(self):
        return int(self.ID)
    
    def getBirthdayByIntegerSum(self):
        Birthday = self.Birthday
        sum = 0
        for i in Birthday:
            sum = sum + int(i) 
        return sum
    
    def getMaxInteger(self):
        Birthday = self.Birthday
        Id = self.ID
        B = list(Birthday)
        bMAx = max(B)
        I = list(Id)
        iMax = max(I)
        if I>B :
            return I
        else:
            return B
        
    def  getAverageInteger(self):
        Birthday = self.Birthday
        Id = self.ID
        sum = 0
        cnt = 0
        for i in Birthday:
            sum = sum+int(i)
            cnt = cnt +1
        for i in Id:
            sum = sum +int(i)
            cnt = cnt+1
        return sum/float(cnt)
    
    def getBirthdayByMonth(self):
        Birthday = self.Birthday
        month = Birthday[4:6]
        dic = {'01':'JAN','02':'FEB','03':'MAR','04':'APR','05':'MAY','06':'JUN','07':'JUL','08':'AUG','09':'SEP','10':'OCT','11':'NOV','12':'DEC'}
        return dic[month]
    
    
 
yoonji = MySelfClass("2019110628","20000925")

print(yoonji.getBirthday())
print(yoonji.getStudentIDByInteger())
print(yoonji.getBirthdayByIntegerSum())
print(yoonji.getMaxInteger())
print(yoonji.getAverageInteger())
print(yoonji.getBirthdayByMonth())
print(yoonji.getStudentID())

class MyRecordClass:
    def __init__(self,ID,DeadLine,num,first):
        self.ID = ID
        self.DeadLine = DeadLine
        self.num = num
        self.first = first
        self.studentList = [self.ID,self.DeadLine,self.num,self.first]
        
    def makeRecord(self):
        ID = input()
        DeadLine = input()
        num = input()
        first = int(input())
        
        if len(ID)==10:
            self.ID = ID
        else:
            return -1
        if len(DeadLine)==8:
            self.DeadLine = DeadLine
        else:
            return -1
        if len(num)==4:
            self.num =num
        else:
            return -1
        if first>=1 and first <=3:
            self.first=first
        else:
            return -1
        self.studentList = [ID,DeadLine,num,first]
        return self.studentList
    
    def checkDelay(self):
        num = self.num
        Today = self.DeadLine
        
        if num<Today :
            return True
        elif num==Today or num>Today:
            return False
        else:
            return -1
      
    def  deferDeadline(self):
        number = input()
        Delay = int(input())
        
        studentList = self.studentList
        if number not in studentList:
            return -1
        if Delay>14:
            return -2
        studentList[1] = int(studentList[1])+Delay
                                                 
                                                 
        return studentList

yoonji = MyRecordClass("2019110628","20200718","A001",1)
print(yoonji.makeRecord())
daseung = MyRecordClass("9900000029","20210718","A001", 1)
print(daseung.makeRecord())
print(yoonji.deferDeadline())
