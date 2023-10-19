import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    
    username = "Your email address"
    password = "You email password"
    
    receiver = "Your reciver email address"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

if __name__ == "__main__":

    send_email("testing")