##creating database connectivity
import datetime
import random
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",database="hospital")
cursor=con.cursor()

#printing option
print("""
                                                                                1. SIGN IN (LOGIN)
                                                                                2. SIGN UP (REGISTER)
                                                                                """)
r=int(input("enter your choice:"))
    
    
    
        #IF USER WANTS TO REGISTER
if r==2:
        print("""

                                                    =================================================================================
                                                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!PLEASE REGISTER YOURSELF!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                                    =================================================================================
                                                    """)
        u=input("ENTER YOUR PREFERRED USERNAME!!:")
        p=input("ENTER YOUR PREFERRED PASSWORD (PASSWORD SHOULD BE STRONG!!!:")
            #ENTERING THE ENTERED VALUE TO THE USER_DATA TABLE
        cursor.execute("insert into user_data values('"+u+"','"+p+"')")
        con.commit()
    
    
        print("""
                                                    =================================================================================
                                                    !!!!!!!!!!!!!!!!!!!!!!!!!!!REGISTERED SUCCESSFULLY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                                    =================================================================================
                                                    """)
            
        #IF USER WANTS TO LOGIN
elif r==1:
        
        #PRINTING THE SINGIN OPTION AGAIN TO THE USER AFTER REGISTRATION

        print("""
                                                        =================================================================================
                                                        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  {{SIGN IN }}  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                                        =================================================================================
                                                        """)
        un=input("ENTER THE USERNAME!!:")
        ps=input("ENTER THE PASSWORD!!:")
                
        cursor.execute("select password from user_data where username='"+un+"'")
        row=cursor.fetchall()

                            ##displaying the task you can perform
while True:
        print("""
                                                                      1.ADMINISTRATION
                                                                      2.PATIENT (ADMISSION NAD DISCHARGE PROCESS)
                                                                      3.SIGN OUT
                                                                      
                                                                      """)

        break
    

                            ##asking for the task from user
a=int(input("ENTER YOUR CHOICE:"))
                            #if user wants to enter administration option

if a==1:
        print("""
                                                                          1. SHOW DETAILS
                                                                          2. ADD NEW MEMBER
                                                                          3. DELETE EXISTING ONE
                                                                          4. GO TO MAIN MENU
                                                                          5. EXIT
                                                                          """)
        b=int(input("ENTER YOUR CHOICE:"))
                                #showing the existing details
        if b==1:
                print("""
                                                                                1. DOCTOR DETAILS
                                                                                2. NURSE DETAILS
                                                                                3. OTHER WORKERS
                                                                                """)
                                    
                                    #ASKING USER'S CHOICE
                c=int(input("ENTER YOUR CHOICE:"))
                                    #if user wants to see the details of doctors
                if c==1:
                        cursor.execute("select * from doctor_details")
                        row=cursor.fetchall()
                        for i in row:
                                b=0
                                v=list(i)
                                k=["NAME","SPECIALISATION","AGE","ADDRESS","CONTACT","FEES","MONTHLY_SALARY"]
                                d=dict(zip(k,v))
                                print(d)
                                     #if user wants to see the details of nurses
                elif c==2:
                        cursor.execute("select * from nurse_details")
                        row=cursor.fetchall()
                        for i in row:
                                v=list(i)
                                k=["NAME","AGE","ADDRESS","CONTACT","MONTHLY_SALARY"]
                                d=dict(zip(k,v))
                                print(d)
                                    #if user wants to see the details of other_workers
                elif c==3:
                        cursor.execute("select * from other_workers_details")
                        row=cursor.fetchall()
                        for i in row:
                                v=list(i)
                                k=["NAME","AGE","ADDRESS","CONTACT","MONTHLY_SALARY"]
                                d=dict(zip(k,v))
                                print(d)
                                #IF USER WANTS TO ENTER DETAILS

        elif b==2:
                print("""

                                                                                    1. DOCTOR DETAILS
                                                                                    2. NURSE DETAILS
                                                                                    3. OTHER WORKERS
                                                                                    
                                                                                    """)
                c=int(input("ENTER YOUR CHOICE:"))
                seq=int(input("enter the element:"))
                for i in range(seq):
                        
                                    #FOR ENTERING DETAILS OF DOCTORS
                        if c==1:
                                      #ASKING THE DETAILS
                                name=input("ENTER DR. NAME:")
                                spe=input("ENTER SPECIALISATION:")
                                age=input("ENTER AGE:")
                                add=input("ENTER ADDRESS:")
                                cont=input("ENTER CONTACT NO.:")
                                fees=input("ENTER FEES:")
                                ms=input("ENTER MONTHLY_SALARY:")
                                      #INSERTING VALUES ENTERED INTO THE DOCTORS_TABLE
                                cursor.execute("insert into doctor_details values('"+name+"','"+spe+"','"+add+"','"+fees+"','"+cont+"','"+ms+"','"+age+"')")
                                con.commit()
                                print("SUCCESSFULLY ADDED")
                                    #for entering nurse details
                        elif c==2:
                                      #ASKING THE DETAILS
                                name=input("ENTER NURSE NAME:")
                                age=input("ENTER AGE:")
                                add=input("ENTER ADDRESS:")
                                cont=input("ENTER CONTACT NO.:")
                                ms=int(input("ENTER MONTHLY_SALARY:"))
                                      #INSERTING VALUES ENTERED TO THE TABLE
                                cursor.execute("insert into nurse_details values('"+name+"','"+age+"','"+add+"','"+cont+"','"+str(ms)+"')")
                                con.commit()
                                print("SUCCESSFULLY ADDED")
                                    #for entering workers details
                        elif c==3:
                                  #ASKING THE DETAILS
                                name=input("ENTER WORKER NAME:")
                                age=input("ENTER AGE:")
                                add=input("ENTER ADDRESS:")
                                cont=input("ENTER CONTACT NO.:")
                                ms=input("ENTER MONTHLY_SALARY:")
                                      #INSERTING VALUES ENTERED TO THE TABLE
                                cursor.execute("insert into other_workers_details values('"+name+"','"+age+"','"+add+"','"+cont+"','"+ms+"')")
                                con.commit()
                                print("SUCCESSFULLY ADDED")
                                #if unser wants to delete data

        elif b==3:
                print("""
                                                                                    1. DOCTOR DETAILS
                                                                                    2. NURSE DETAILS
                                                                                    3. OTHER WORKERS
                                                                                    
                                                                                    """)
                c=int(input("ENTER YOUR CHOICE:"))
                                   #deleting doctor's details
                if c==1:
                        name=input("ENTER DOCTOR'S NAME:")
                        cursor.execute("select * from doctor_details where name='"+name+"'")
                        row=cursor.fetchall()
                        print(row)
                        p=input("you really wanna delete this data? (y/n):")
                        if p=="y":
                                cursor.execute("delete from doctor_details where name='"+name+"'")
                                con.commit()
                                print("SUCCESSFULLY DELETED!!")
                        else:
                                print("NOT DELETED")
                                       
                                      
                                   #deleting nurse details
                elif c==2:
                        nname=input("ENTER NURSE NAME:")
                        cursor.execute("select * from nurse_details where name='"+nname+"'")
                        row=cursor.fetchall()
                        print(row)
                        p=input("you really wanna delete this data? (y/n):")
                        if p=="y":
                                cursor.execute("delete from nurse_details where name='"+nname+"'")
                                con.commit()
                                print("SUCCESSFULLY DELETED!!")
                        else:
                                print("NOT DELETED")
                                  #deleting other_workers details
                elif c==3:
                        oname=input("ENTER THE WORKER NAME:")
                        cursor.execute("select * from other_workers_details where name='"+oname+"'")
                        row=cursor.fetchall()
                        print(row)
                        p=input("you really wanna delete this data? (y/n):")
                        if p=="y":
                                cursor.execute("delete from other_workers_details where name='"+oname+"'")
                                con.commit()
                                print("SUCCESSFULLY DELETED!!")
                        else:
                                print("NOT DELETED")



        
                

                            #entering the patient details table

        
elif a==2:
        print("""
                                                                          1. SHOW  PATIENT DETAILS
                                                                          2. ADD  NEW PATIENT
                                                                          3. BILL CALCULATION AND DISCHARGE PATIENT
                                                                          4. EXIT
                                                                          """)
        b=int(input("ENTER YOUR CHOICE:"))
        
                
                                #showing the existing details
                                #if user wants to see the details of PATIENT
        if b==1:
                        cursor.execute("select * from patient_details")
                        row=cursor.fetchall()
                        for i in row:
                                b=0
                                v=list(i)
                                k=["NAME","GENDER","AGE","ADDRESS","DOCTOR_RECOMMENDED"]
                                d=dict(zip(k,v))
                                print(d)
           
                                #adding new patient
        elif b==2:
                seq=int(input("enter the element:"))
                for i in range(seq):
                
                        pname=str(input("ENTER NAME: "))
                        gender=str(input("ENTER GENDER: "))
                        age=str(input("ENTER AGE: "))
                        address=str(input("ADDRESS: "))
                        doctor_recommended=str(input("ENTER DOCTOR RECOMMENDED: "))
                        cursor.execute ("insert into patient_details values('"+str(pname)+"','"+str(gender)+"','"+str(age)+"','"+str(address)+"','"+str(doctor_recommended)+"')")
                        con.commit()
                
                        print("""
                                                        =================================================================================
                                                        !!!!!!!!!!!!!!!!!!!!!!!!!!!REGISTERED SUCCESSFULLY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                                        =================================================================================
                                                        """)
                                
        elif b==3:
                pname=input("ENTER THE PATIENT NAME:")
                cursor.execute("select * from patient_details where name='"+pname+"'")
                row=cursor.fetchall()
                print(row)
                no=int(input("NO. OF DAYS PATIENT WAS ADMITTED :- "))
                per=int(input("PER DAYS CHARGES(based on room):- "))
                print("TOTAL CHARGES:-" ,per*no)#total cahrges
                pid=per*no
                gst=0.25*pid
                print("TOTAL BILL:-",gst+pid)
                total=gst+pid
                bill=input("HAS THE PATIENT PAID ALL THE BILLS ? (y/n):")
                if bill=="y":
                        cursor.execute("delete from patient_details where name='"+str(pname)+"'")
                        con.commit()
                        print("SUCCESFULLY DISCHARGED")
                              
        elif b==4:
                         exit


                                                                                                                                                  
                                                                
                
                            ###SIGN OUT
elif a==3:
      
                 exit    
                                
                   #IF THE USERNAME AND PASSWORD IS NOT IN THE DATABASE
else:
                 exit
                                   

