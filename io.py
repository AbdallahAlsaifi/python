def modify(stdid, field, new_value):
    temp=[]
    with open('students.txt', 'r') as studentsData:
        for line in studentsData:
            data = line.split(",")
            temp.append(data)
    for i in temp:
        if i[0] == stdid:
            if field == 4:
                i[4] = new_value+'\n'
            else:
                i[field] = new_value

    with open('students.txt','w') as studentsData:
        for i in temp:
            x = ",".join(i)
            studentsData.write(x)
                
            
    
    
def display():
    print('#################################################################')
    i=0
    f = open('students.txt','r')
    studentsData = f.readlines()
    f.close()
    for line in studentsData:
        i+=1
        data = line.split(',')
        id = data[0]
        name = data[1]
        cgpa = float(data[2])
        birthdate = data[3]
        gender = data[4]
        print("{}.\t{}\t{}\t{}\t{}\t{}".format(i,id,name,cgpa,birthdate,gender))
    print('#################################################################')

def delete(stdid):
    temp=[]
    with open('students.txt','r') as studentsData:
        
        for line in studentsData:
            data = line.split(",")
            temp.append(data)
    with open('students.txt','w') as studentsData:
        for i in temp:
            x=",".join(i)
            if i[0] == stdid:
                pass
            else:
                studentsData.writelines(x)
        
        
def insert(stdid,name,cgpa,date,gender):
    x = '{},{},{},{},{}'.format(stdid,name,cgpa,date,gender)
    with open('students.txt','a') as studentsData:
        studentsData.writelines(x)
        
def stats():
    students = []
    with open('students.txt','r') as studentsData:
        for line in studentsData:
            data = line.split(",")
            student={'id':data[0],'name':data[1],'cgpa':data[2],'birthdate':data[3],'gender':data[4]}
            students.append(student)
    numberOfStudents=len(students)
    maleStudents = 0
    femaleStudents = 0
    totalCgpa = 0

    for i in students:
        if i['gender'][:1] == "M":
            maleStudents+=1
        else:
            femaleStudents+=1
    for i in students:
        x = float(i['cgpa'])
        totalCgpa += x
    
    averageCgpa = totalCgpa/numberOfStudents
    
    with open('stats.txt','w') as statsFile:
        statsFile.write('Total Students: {}\nFemale Students: {}\nMale Students: {}\nAverage Cgpa: {:.2f}'.format(numberOfStudents,femaleStudents,maleStudents,averageCgpa))


def main():
#    display()
#    modify('9821',2,'2.12')
#    insert('2341','Tom Jones', '3.1','12-08-1991','M')
#    delete('1235')
#    display()
#    stats()
    

if __name__ == '__main__':
    main()     