#from email.mime.text import MIMEText
#import smtplib
#from email.MIMEText import MIMEText

#Création de l'email
msg = MIMEText("Hello, this is a test email.")
msg['Subject'] = "Test Email"
msg['From'] = "rwarnod@yahoo.fr"
msg['To'] = "rwarnod@yahoo.fr"

# Envoi de l'email
# server smtp 
server = smtplib.SMTP('smtp.gmail.com')# peut etre que ca marche
server.login("rwarnod@yahoo.fr", "password")
server.sendmail("rwarnod@yahoo.fr", "rwarnod@yahoo.fr", msg.as_string())
server.quit()
