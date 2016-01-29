import smtplib
f=True 


while f:
 subject=input("Enter subject: ")
 content=input("Enter  content: ")

 contents="""subject:%s

 %s"""%(subject,content)

 mail=smtplib.SMTP('smtp.gmail.com',587)
 mail.ehlo()
 mail.starttls()
 g=True
 while g:
 
  try:
    sender=input("Enter email id: ")
    password=input("Enter password: ")
    mail.login(sender,password)
    g=False
    h=True
    while h:
     try:
      receiver=input("Enter receiver's email id: ")
      print(" From:",sender,"\n","To:",receiver,"\n","Subject:",subject,"\n","Content:",content)
      h=False
      j=True
      while j:
       k= input(" Do you want to send this mail ?\n Enter 1 for Yes and 2 for No: ")
       if k=='1':
        mail.sendmail(sender,receiver,contents)
        mail.close()
        print("your message has been sent")
        j=False
        f=False
        g=False
        h=False
       elif k=='2':
           f=True
           h=False
           j=False
           g=False
           
        
        
        
       else:
          print(" Enter valid key")
          j=True

         
     except  smtplib.SMTPRecipientsRefused:
        print("invalid receiver's id")
        f=False
        g=False
        h=True
   
  except smtplib.SMTPAuthenticationError:
    print("invalid username or password")
    
     
  
 

    
