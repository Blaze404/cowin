import smtplib, ssl

def send_email(name, email, pincode):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "cowinnotificationb@gmail.com"  # Enter your address
    receiver_email = email  # Enter receiver address
    password = "Debba*23"
    message = """\
    Subject: Alert for availability of Vaccine.

    Hi {}. 
    This email is to inform you that vaccines are now available
    in the pincode you provided: {}. Please be quick to register.
    
    Stay Safe. Stay Healthy 
    
    Regards, 
    Cowin Notifications. """.format(name, pincode)

    context = ssl.create_default_context()
    print("sending email to {}".format(email) )
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

