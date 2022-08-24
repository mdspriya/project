import sqlite3
con = sqlite3.connect("halfyearly.db")

def insertData(Name,language1,language2,maths,science,social,total,average,Remarks):
    
    qry="insert into halfyearly(NAME,language1,language2,maths,science,social,total,average,Remarks) values (?,?,?,?,?,?,?,?,?);"
    
    con.execute(qry,(Name,int(language1),int(language2),int(maths),int(science),int(social),int(total),int(average),str(Remarks)))
    con.commit()
    print(" STUDENT halfyearly mark  added Sucessfully")
    
def updateData(Name,language1,language2,maths,science,social,total,average,Remarks,ID):
    qry="update halfyearly set NAME=?,language1=?,language2=?,maths=?,science=?,social=? ,total=? ,average=? ,Remarks=? where ID =?;"
    con.execute(qry,(Name,int(language1),int(language2),int(maths),int(science),int(social),int(total),int(average),str(Remarks),ID))
    con.commit()
    print(" STUDENT halfyearly mark  updated Sucessfully")   
    
def deleteData(ID):
    qry="delete from halfyearly where ID =?;"
    con.execute(qry,(ID))
    con.commit()
    print(" STUDENT halfyearly mark  Deleted Sucessfully")   


def selectData(ID):
    qry="select name,language1,language2,maths,science,social from halfyearly where ID=?;"
    result=con.execute(qry,(ID))
    con.commit()
    for row in result:
        print(row)     

def Remarks():
    qry="select from halfyearly where language1>=35 and language2>=35 and maths>=35 and science>=35 and social>=35; " 
    qry="select from halfyearly where language1<35 or language2<35 or maths<35 or science<35 or social<35; "
    if  int(language1>=35 and language2>=35 and maths>=35 and science>=35 and social>=35):
        print("pass")
    else:
       print("fail")
       con.execute(qry)
       con.commit()       

    
   
    
print("""
1.Insert
2.Update
3.delete
4.Select
""")

ch=1
while ch==1:
   c=int(input("Select Your Choice  :  "))
   if (c==1):
        print("Add New Record")
        Name=input("Enter Name  :  ")
        language1=int(input("Enter language1 Tamil mark :  "))
        language2=int(input("Enter language2 English mark :  "))
        maths=int(input("Enter Maths mark  :  "))
        science=int(input("Enter Science Mark  :  "))
        social=int(input("Enter Social mark  :  ")  )
        total=int(language1)+int(language2)+int(maths)+int(science)+int(social)
        average=int(total)/500*100 
        if int(language1>=35) and int(language2>=35) and int(maths>=35) and int(science>=35) and int(social>=35):
            print("pass")
        else:
            print("fail")        
          
        insertData(Name,language1,language2,maths,science,social,total,average,Remarks)
   elif(c==2):
        print("Edit A Record")
        ID=int(input("Enter ID NO  :  "))
        Name=input("Enter Name  :  ")
        language1=int(input("Enter language1 Tamil mark :  "))
        language2=int(input("Enter language2 English mark :  "))
        maths=int(input("Enter Maths mark  :  "))
        science=int(input("Enter Science Mark  :  "))
        social=int(input("Enter Social mark  :  ")  )
        total=int(language1)+int(language2)+int(maths)+int(science)+int(social)
        average=int(total)/500*100 
        if int(language1>=35) and int(language2>=35) and int(maths>=35) and int(science>=35) and int(social>=35):
            print("pass")
        else:
            print("fail") 
        updateData(Name,language1,language2,maths,science,social,total,average,Remarks,ID)
   
       
   elif(c==3):
       print("Delete a Record ;  ")
       ID=input("Enter ID NO  :  ")
       
       deleteData(ID)
       
   elif(c==4):
       print("Select a Record ;  ")
       ID=input("Enter ID NO  :  ")
       
       selectData(ID)       
   else:
        print("Invalid Selection ;  ")    
   ch=int(input("Enter 1 to continue  :"))
print("Thank You")