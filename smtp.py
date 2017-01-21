import smtplib
details=True 


while details:
 subject=input("Enter subject: ")
 content=input("Enter  content: ")

 contents="""subject:%s

 %s"""%(subject,content)

 mail=smtplib.SMTP('smtp.gmail.com',587)
 mail.ehlo()
 mail.starttls()
 invalid_login=True
 while invalid_login:
 
  try:
    sender=input("Enter email id: ")
    password=input("Enter password: ")
    mail.login(sender,password)
    invalid_login=False
    invalid_receiver_id=True
    while invalid_receiver_id:
     try:
      receiver=input("Enter receiver's email id: ")
      print(" From:",sender,"\n","To:",receiver,"\n","Subject:",subject,"\n","Content:",content)
      invalid_receiver_id=False
      invalid_key=True
      while invalid_key:
       key= input(" Do you want to send this mail ?\n Enter 1 for Yes and 2 for No: ")
       if key=='1':
        mail.sendmail(sender,receiver,contents)
        mail.close()
        print("your message has been sent")
        invalid_key=False
        details=False
        invalid_login=False
        invalid_receiver_id=False
       elif key=='2':
           details=True
           invalid_receiver_id=False
           invalid_key=False
           invalid_login=False
           
        
        
        
       else:
          print(" Enter valid key")
          invalid_key=True

         
     except  smtplib.SMTPRecipientsRefused:
        print("invalid receiver's id")
        details=False
        invalid_login=False
        invalid_receiver_id=True
   
  except smtplib.SMTPAuthenticationError:
    print("invalid username or password")
    
       
