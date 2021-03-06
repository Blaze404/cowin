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


def send_initial_email(name, email, pincode):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "cowinnotificationb@gmail.com"  # Enter your address
    receiver_email = email  # Enter receiver address
    password = "Debba*23"
    message = """\
    Subject: Alert for availability of Vaccine.

    Hi {}. 
    Thank You for registering To covin notifications.
    Your registered pincode is: {}. If this pincode is incorrect, kindly register again.
    Your further notifications will come via this email only, so if its somehow going into spam,
    please mark it as not.
    
    Stay Safe. Stay Healthy 
    
    Regards, 
    Cowin Notifications. """.format(name, pincode)

    context = ssl.create_default_context()
    print("sending email to {}".format(email) )
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except:
        pass
