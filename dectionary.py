def main():
    

    student=dict(name="bshomil",age=53,work="devlpoer design") 
    
    student["name"]="khaled"
    del student["age"] 
    student["age"]=50
    print(student,type(student))
if  __name__ =='__main__':main()
 
                  