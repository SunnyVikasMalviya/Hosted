#! python3
# emailVerification.py
# 1. Creates a random string CODE of 10 characters.
# 2. Sends an email to the new user's email id with the CODE.
# 3. Verifies the code entered by the user.
# 4. Sends a successful user creation confirmation mail to users email id.

#TODO: Import libraries for random string generation, sending email.
import random
import string
import smtplib

codeMailBody = '''
    Hi {},
    Thanks for registering on Hosted!
    Use below code to verify your email id and complete user registration.
    {}

    Thanks,
    Team Hosted
'''
confirmationMailBody = '''
    Hi {},
    Congratulations on successful completion of user registration.

    Thanks,
    Team Hosted
'''
    

class EmailVerify:
    def __init__(self, email, username, password):
        self.sender = ""
        self.scoody = ""
        self.code = self.codeGenerator()
        self.email = email
        self.username = username
        self.password = password
        self.codeMailBody = codeMailBody.format(self.username, self.code)
        self.confirmationMailBody = confirmationMailBody.format(self.username)
 
    def codeGenerator(self):
        return "".join(random.sample(string.ascii_letters + '0123456789', 10))
    
    def sendCodeMail(self):
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(self.sender, self.scoody)
        session.sendmail(self.sender, self.email, self.confirmationMailBody)
        session.quit()
    
    def verifyCode(self, userCode):
        if userCode == self.code:
            return True
        else:
            return False

    def sendConfirmationMail(self):
        #TODO: Call method to save users data to database
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(self.sender, self.scoody)
        session.sendmail(self.sender, self.email, self.confirmationMailBody)
        session.quit()

    
if __name__ == "__main__":
    verifyObject = EmailVerify("vikasmalviya98+Hosted@gmail.com", "HostedTestUser", "Hosted")
    verifyObject.sendCodeMail()







