# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mail_co.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/20 15:32:18 by cosaph            #+#    #+#              #
#    Updated: 2023/10/25 11:11:01 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

""" L'idée c'est de relier un serveur smtp a notre application pour
envoyer des mails a un utilisateur lorsque sur son groupe de critères 
favoris a une nouvelle offre de stage.

"""
from email.message import EmailMessage
import smtplib

sender = "stagefinderensai@outlook.com"
recipient = "coralie.cottet@eleve.ensai.fr"
message = "IT WORKS"

email = EmailMessage()
email["From"] = sender
email["To"] = recipient
email["Subject"] = "Test Email"
email.set_content(message)

smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
smtp.starttls()
smtp.login(sender, "123456abc@@@")
smtp.sendmail(sender, recipient, email.as_string())
smtp.quit()
