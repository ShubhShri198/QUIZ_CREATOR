class student:

    def __init__(self,name,email):
        self.name=name
        self.email=email

    def getdetails(self):
        print('Name: ',self.name)
        print('Email-id: ',self.email)