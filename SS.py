import pyautogui
import smtplib, ssl

im = pyautogui.screenshot('hacked.png')

port = 465 

smtp_server= "smtp.gmail.com"
sender_email= "Changeme@gmail.com"
reciever_email= "changme@gmail.com"
Password=input("changeme")

message = """\

subject: Testing

This is a messaged being used in a test."""


context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, message)