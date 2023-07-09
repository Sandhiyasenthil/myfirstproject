import re 
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Sandhiya@123",database="newdatabase")


class Register: 

  def signup(self): 

    username=input("enter your user name:") 

    password=input("enter new password:") 

    confirmpassword=input("confirm password:") 

    pat = "^[A-Za-z][A-Za-z0-9_]{7,29}$" 

    paw =  "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    if re.match(pat,username) and re.match(paw,password) and password==confirmpassword : 
      mycursor =con.cursor()
      sql='insert into Signup(username,password) values(%s,%s)'
      user=(username,password)
      mycursor.execute(sql,user)
      con.commit()
      print("************S I G N E D  U P  S U C C E S S F U L L Y*********************") 

    else: 

      print(" username and passowrd doesnot meet the validation need") 

      print("********************************************") 
      
      l.signup()
  
  
  def login(self):
    success=0
    mycursor=con.cursor()
    user_name=input("enter username:")
    pass_word=input("enter your password:")
    sql="select username ,password from Signup"
    mycursor.execute(sql)
    result=mycursor.fetchall()
    

    for i in result:
     print(i)
     if i[0]==user_name and i[1]==pass_word:
       print("************S U C C E S S F U L Y   L O G G E D  I N************************") 
       
       success+=1 
       break 

    if success==0: 

      print("***your username or password is incorrect***") 

      option=input("if you want to try again click 1 or else click 2 for create a new account:")       

      if option==1: 

        print("LOGIN") 

        l.login() 

      else: 

        print("SIGNUP") 

        l.signup() 

    else: 

      return False   

         

l=Register() 

 

      
      



 

   

  