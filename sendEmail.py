import sys
import smtplib

#######################################################################
#
# Step 1: Disable 2-step verification:
# https://myaccount.google.com/security?utm_source=OGB&utm_medium=act#signin
#
# Step 2: Allow less secure apps
# https://myaccount.google.com/u/1/lesssecureapps?pli=1&pageId=none
# 
#######################################################################

# ----------------------------- sendEmail -------------------------------------
def sendEmail(
  sender,
  password,
  smtp_server,
  recipient,
  subject,
  message_body):

  message="Subject: "+subject+"\n"+message_body

  print("\nFrom   : "+sender)
  print("To     : "+recipient)
  print("Subject: "+subject)
  print("Message: "+message_body)

  confirm=input("\n\nsend? (y)? ")
  if ((len(confirm) != 0) and (confirm.lower() != 'y')):
    exit()

  try:
    server=smtplib.SMTP(smtp_server, 587)
    #server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, message)
    server.quit()
    print("\n\nEmail Sent!\n\n")
  except:
    print("Failed to connect to email server")


# ------------------------------- main ----------------------------------------
if (len(sys.argv) != 4):
  print("\nUSAGE: python sendEmail.py recipientEmail subject emailBody\n\n")
  exit()


PASSWORD="password"         # replace it with your password
SENDER="sender@gmail.com"   # replace it with your gmail account
SMTP_SERVER="smtp.gmail.com"
sendEmail(SENDER, PASSWORD, SMTP_SERVER, sys.argv[1], sys.argv[2], sys.argv[3])

#######################################################################
#
# Sample run:
#
# USAGE: python sendEmail.py recipientEmail subject emailBody
#
# G:\> python sendEmail.py receiver@yahoo.com testing5 "test 5 message"
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

