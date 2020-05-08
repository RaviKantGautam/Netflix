import smtplib
import email.message

# sender = 'python.vmm@gmail.com'
# password = 'vmmpython'

sender = 'tania.vmmteachers23@gmail.com'
password = 'Teachers@123'


# receiver = 'rahul@vmmeducation.com'
def send_Mail(receiver,msg=None):
    try:
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        # smtpserver.ehlo
        smtpserver.login(sender, password)
        if msg==None:
            body = "your password is  change after login"
            subject = "Subject:teacher password \n\n "
            msg = subject + body
        smtpserver.sendmail(sender, receiver, msg)
        print('Sent')
        smtpserver.close()
    except smtplib.SMTPException:
        print("Not Sent")


def checkthis():
    receiver = 'rkb9874@gmail.com'
    username = 'Rahul'
    mobile = '6280995201'
    print(mobile)
    sender = 'tania.vmmteachers23@gmail.com'
    password = 'Teachers@123'

    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(sender, password)
    body = f"""
                <html>
                <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                </head>
                <body>
                    <table  width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4"">
                    <tr>
                        <td></td>
                        <td> {username}</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td>Tap the button below to log in to your Zomato account</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td><a  href="127.0.0.1/opt_login?user={receiver}">Log in Zomato</a></td>
                        <td></td>
                    </tr>
                </table>
            </body>
                """
    msg = email.message.Message()
    msg['Subject'] = 'Signup in Zomato'

    msg['From'] = sender
    msg['To'] = receiver
    password = password
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)
    smtpserver.sendmail(sender, receiver, msg.as_string())
    print('Sent')
    smtpserver.close()

# checkthis()