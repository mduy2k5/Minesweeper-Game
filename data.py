try: open('his.txt','a')
except: pass


def save(line):
    
    f = open('his.txt','r')
    a = 0
    for i in f: 
        a +=1
    f.close()
    if a == 0 : 
        f = open('his.txt','a')
        a = str(a+1)
        f.writelines(a+"-"+line)
        f.writelines('\n')
        f.close()
    else:
        sort= []
        line = "0 - "+line
        lines=line.split("-")
        temp = ["0","0"]
        f = open('his.txt','r')
        for i in f:
            c = i.split('-')
            sort.append(c)
        f.close()
        for m in range(a):
            if int(sort[m][2]) < int(lines[2]):
                temp[0] = sort[m][1]
                temp[1] = sort[m][2]
                sort[m][1] = lines[1]
                sort[m][2] = lines[2]
                lines[1] = temp[0]
                lines[2] = temp[1]
                    
        f = open('his.txt','w')
        f.close()
        f = open('his.txt','a')
        for b in range(a):
            f.writelines(sort[b][0]+"-"+sort[b][1]+"-"+str(int(sort[b][2])))
            f.writelines('\n')
        
        if a<10:
            f.writelines(str(a+1)+"-"+lines[1]+"-"+str(int(lines[2])))
            f.writelines('\n')

        f.close()
                
        

            
            

    
def read():
    data = []
    try:
        f = open('his.txt','r')
        
        for i in f:
            data.append(i)
        f.close()
    except:
        pass
    return data
    
# def delete(index):
#     data = []
#     try:
#         f = open('text.txt','r')
        
#         for i in f:
#             data.append(i)
#         f.close()
#     except:
#         pass
#     f = open('text.txt','w')
#     a = 0
#     setid = 1
#     for i in data:
#         if a != index:
#             i = i[2:int(len(i))-1]
#             b = str(setid)
#             f.writelines(b+"-"+i)
#             f.writelines('\n')
#             setid+= 1
#         a+=1
#     f.close()


def rewrite():
    f = open('text.txt','w')
    f.close()

