class question:

    def __init__(self,s,option_list,ans=0):      #a question is created with a statement options and correct choice
        self.statement=s
        self.options=option_list
        self.correct=ans


    def selectoption(self):         #we create a new attribute choice for every question instance when user marks an answer
        self.choice=int(input())

    def displayquestion(self):   #This method displays question with options on screen
        print(self.statement)
        for i in range(4):
            print(i+1,self.options[i])

    def test(self):               # if the choice of user is correct returns true ....false other wise
        if self.choice==self.correct:
            return True
        else:
            return False