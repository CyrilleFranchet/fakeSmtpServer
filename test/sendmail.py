#!/usr/bin/python

""" send mail """

import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = "From: From Person <from@fromdomain.com>\n"
message += "To: To Person <to@todomain.com>\n"
message += "Subject: SMTP e-mail test\n\n"
message += "This is a test e-mail message.\n"
message += "ligne 2\n"
message += "ligne__3"

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print "Successfully sent email"
except smtplib.SMTPException:
   print "Error: unable to send email"

