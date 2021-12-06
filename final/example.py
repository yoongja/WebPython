file = open("score.txt",'r')
file.readline()
dic = {}
for line in file:
    print(line)
    (key,val1,val2,val3)=line.split()
    dic[key]=val3
print (dic)
file.close
    
