import smtplib


to = input("enter the emmail address of the reciever : ")
messege = input("Enter your messege : ")

def sendEmail(to , messege):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('rexc2769@gmail.com', 'cart dvhu poup etxh')
    server.sendmail('rexc2769@gmail.com', to, messege)
    server.close()
    

sendEmail(to, messege)
