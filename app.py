from QuizSection import quiz
from Userspecs import student


class QUIZ:      # QUIZ class determines how program will interact with user


    def __init__(self):
        self.all_quizes = {}
        while True:
            print("\n***QUIZ ASSIGNMENT***\n")
            print("Welcome User ! Please Choose Your Account Type :\n1.) Admin\n2.) Student\n3.) Exit\n")
            usr=int(input())
            if usr==1:
                self.admin()    #if you are admin admin function of QUIZ will be called
            elif usr==2:
                self.student()
            else:
                print("\nThankyou for joining. See You Soon !\n")
                break


    def admin(self):
        print("\n**ADMIN SECTION**")
        print('\nWhat do you want to do ?\n1.) Create A Quiz\n2.) Update Your Quiz\n')
        c=int(input())
        print('\nChoose A Title for your Quiz : ')
        qname = input()

        if c==2:    #if admin wants to modify an existing quiz
            if qname in self.all_quizes:
                print('\nQuiz Available !\n')
                print('\n1)Add a Question to the Quiz\n2)Update the existing set of questions.\n')
                s=int(input())
                if s==2:
                    print('\nEnter the Question number that you want to Update.')
                    qno=int(input())
                    self.all_quizes[qname].createquestions(qno)
                elif s==1:
                    l=len(self.all_quizes[qname].question_list)
                    self.all_quizes[qname].createquestions(l+1)
                else:
                    print("\nInvaid Choice !")
            else:
                print('\nError ! No Quiz Available.')
        
        elif c==1:    # if admin wants to create a new quiz
            print('\nPlease Enter the number of Questions for the Quiz !')
            n = int(input())
            self.all_quizes[qname]=quiz()
            for i in range(n):
                self.all_quizes[qname].createquestions(i+1)
           
        else:
            print('\nInvalid Choice Selection !\n')



    def student(self):
        print("\nEnter your student credentials to proceed : \n")
        print('\nYour Name : \n')
        n=input()
        print('\nEmail ID : \n')
        e=input()
        s=student(n,e)
        while True:
            if len(self.all_quizes)==0:
                print('\nNo Quizzes are placed my Admin right now.\nPlease try after some time.')
            else:
                print('\nAVAILABLE QUIZZES : \n')
                for val in self.all_quizes:
                    print(val)
                print('\nPlease Enter the Quiz Name You Want to Attempt : \n')
                choice=input()
                print("\n")
                self.all_quizes[choice].attempt()
                m=self.all_quizes[choice].calculatescore()
                s.getdetails()
                print('\n')
                print(m)
                self.all_quizes[choice].displayanswers()
                break
        print('\nYou have Successfully completed your Quiz.\nCome Back Soon For More Such Quizzes.\nThankYou !')
        

I =QUIZ()