
SMTP stands for Simple Mail Transfer Protocol. SMTP is used when email is delivered from an email client to an email server or when email is delivered from one email server to another. SMTP uses port 25


WHAT HAPPENS WHEN YOU SEND A MAIL?


You send an email with your webmail or mail client from your address (e.g. mark@website.com) to a given recipient (e.g. jane@domain.com).The message is sent normally via port 25 to an SMTP server (named for instance mail.website.com) which is given to your client when you set it up and acts as a Message Transfer Agent or MTA. Client and server start a brief "conversation" where the latter checks all the data concerning the message's transmission (sender, recipient, domains, etc.). Then, if the domain where your recipient has his account is directly connected to the server, the email is immediately delivered. If it's not the case, the SMTP hands it to another incoming server closer to the recipient 

    
