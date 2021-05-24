from QuestionBank import question
class quiz:

    def __init__(self):         #quiz has an empty dict of questions at the time of obj creation.
        self.question_list={}   #this dict will be used to store reference to all the question objects belonging to a particular quiz


    def createquestions(self,j):
        print('\nType Your Question from Here : \n')
        qs=input()
        print('\nAssign the Options for the Question : ')
        opl=[]
        for i in range(4):        #taking 4 options
            print(i+1,end=' ')
            opl.append(input())
        print('\nEnter the correct option number : ')
        a=int(input())
        self.question_list[j]=question(qs,opl,a)  #reference of question stored in dict



    def attempt(self):                                  #quiz would be attempted using 2 methods...display first and then selectoption
        for i in range(len(self.question_list)):
            self.question_list[i+1].displayquestion()
            self.question_list[i+1].selectoption()


    def calculatescore(self):
        marks=0
        length=len(self.question_list)
        total=2*length
        for i in range(len(self.question_list)):
            if self.question_list[i+1].test():     #marks will be increases whenever test function of question obj returns true
                marks+=2
        return 'Your Score is ' + str(marks) +'/'+ str(total)
    
    def displayanswers(self):
        for i in range(len(self.question_list)):
            print('ANSWER : ',i+1,end=' ')
            x=self.question_list[i+1].correct
            print(x,self.question_list[i+1].options[x-1])