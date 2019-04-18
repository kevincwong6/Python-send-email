import sys
import smtplib

#######################################################################
#
# USAGE: python sendEmail.py recipientEmail subject emailBody
#
#######################################################################
#
# Step 1: Disable 2-step verification:
# https://myaccount.google.com/security?utm_source=OGB&utm_medium=act#signin
#
# Step 2: Allow less secure apps
# https://myaccount.google.com/u/1/lesssecureapps?pli=1&pageId=none
# 
#######################################################################

if (len(sys.argv) != 4):
  print("\nUSAGE: python sendEmail.py recipientEmail subject emailBody\n\n")
  exit()

recipient=sys.argv[1]
subject=sys.argv[2]
message_body=sys.argv[3]
message="Subject: "+subject+"\n"+message_body

PASSWORD="password"       # replace it with your password
SENDER="sender@gmail.com" # replace it with your gmail account
SMTP_SERVER="smtp.gmail.com"
LOGIN=SENDER

print("\nFrom   : "+SENDER)
print("To     : "+recipient)
print("Subject: "+subject)
print("Message: "+message_body)

confirm=input("\n\nsend? (y)? ")
if ((len(confirm) != 0) and (confirm.lower() != 'y')):
  exit()

try:
  server=smtplib.SMTP(SMTP_SERVER, 587)
  #server.set_debuglevel(1)
  server.ehlo()
  server.starttls()
  server.login(SENDER, PASSWORD)
  server.sendmail(SENDER, recipient, message)
  server.quit()
  print("\n\nEmail Sent!\n\n")
except:
  print("Failed to connect to email server")


#######################################################################
#
# Sample run:
#
# G:\python sendEmail.py yyyyy@yahoo.com testing5 "test 5 message"
#
# From   : sender@gmail.com
# To     : yyyyy@yahoo.com
# Subject: testing5
# Message: test 5 message
#
#
# send? (y)? y
#
# Email Sent!
# 
#

