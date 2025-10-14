import smtplib

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('rexc2769@gmail.com', 'Castro1225!')
    server.sendmail('rexc2769@gmail.com', 'libem13885@gta5hx.com', 'Subject: Test\n\ntesting email automation')
    server.quit()
    print("✅ Email sent successfully!")

sendEmail()
