import http.client
import math,random

def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def send_Otp(mobile):
    mobile = mobile
    n = generateOTP()
    msg = "your otp is " + str(n)
    print(msg)
    msg = msg.replace(" ", "%20")
    conn = http.client.HTTPConnection("server1.vmm.education")
    conn.request('GET',
                         '/VMMCloudMessaging/AWS_SMS_Sender?username=djangoJan2020&password=QZLIU7IH&message=' + msg + '&phone_numbers=' + str(
                         mobile))
    response = conn.getresponse()
    return n

def confirm_Msg(mobile,msg):
    msg = msg.replace(" ", "%20")
    conn = http.client.HTTPConnection("server1.vmm.education")
    conn.request('GET',
                 '/VMMCloudMessaging/AWS_SMS_Sender?username=djangoJan2020&password=QZLIU7IH&message=' + msg + '&phone_numbers=' + str(
                     mobile))
    response = conn.getresponse()
    print(response)