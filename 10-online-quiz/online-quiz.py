import os
import json
import numpy as np
from datetime import datetime
from functools import wraps

def log_activities(action):
    def decorator(func):
        @wraps(func)
        def wrapper(self,*args,**kwargs):
            result = func(self,*args,**kwargs)
            if result is not False:
                timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                arg_str = ",".join([str(arg) for arg in args])
                log_msg = f"[{timestamp} SUCCESS: {action} | {arg_str}]\n"
                try:
                    with open(self.log_file,'a')as file:
                        file.write(log_msg)
                except IOError as e:
                    print(f"[WARNING] Failed to write to log file. Error: {e}")
            return result
        return wrapper
    return decorator

class Quiz:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.quiz_file = os.path.join(base_dir,"quiz.json")
        self.attempt_file = os.path.join(base_dir,"attempt.json")
        self.log_file = os.path.join(base_dir,"logs.txt")
        self.create_file_if_not_exists()
        self.quiz = self.load_que()
        self.attempt = self.load_attempt()
        self.attempts = 1

    def create_file_if_not_exists(self):
        files = [self.quiz_file,self.attempt_file]
        for file in files:
            if not os.path.exists(file):
                try:
                    with open(file, 'w')as f:
                        json.dump({},f)
                except Exception as e:
                    print(f"Error: {e}")
        if not os.path.exists(self.log_file):
            try:
                with open(self.log_file,'r')as f:
                    f.write("\n============ LOGS ============\n")
            except IOError as e:
                pass

    def load_que(self):
        try:
            with open(self.quiz_file, 'r')as file:
                return json.load(file)
        except Exception as e:
            print(f"Error: {e}")
            return {}

    def save_que(self):
        try:
            with open(self.quiz_file, 'w')as file:
                json.dump(self.quiz, file, indent=4)
        except Exception as e:
            print(f"Error: {e}")

    def load_attempt(self):
        try:
            with open(self.attempt_file, 'r')as file:
                return json.load(file)
        except Exception as e:
            print(f"Error: {e}")
            return {}

    def save_attempt(self):
        try:
            with open(self.attempt_file, 'w')as file:
                json.dump(self.attempt, file, indent=4)
        except Exception as e:
            print(f"Error: {e}")

    def analysis(self):
        self.attempt = self.load_attempt()
        scores = []
        for info in self.attempt.values():
            for i in info['Score']:
                scores.append(i)
        print(f"Highest Score: {np.max(scores)}")
        print(f"Lowest Score: {np.min(scores)}")
        print(f"Average Score: {np.mean(scores):.2f}")

class CreateQuiz(Quiz):

    @log_activities("Add Question")
    def add_que(self,que,ans):
        que_num = 0
        if len(que.strip())<=0:
            print("\nQuestion or Answer cannot be blank\n")
            return
        for q_num,q in self.quiz.items():
            que_num = q_num
            if que in q['Que'] or ans in  q['Ans']:
                print(f"\nQuestion or Answer is already present\n")
                return
        self.quiz[int(que_num)+1] = {"Que": que.strip(), "Ans": ans.strip()}
        self.save_que()
        print("\nQuestion saved successfully\n")

    @log_activities("Delete Question")
    def delete_que(self,que):
        del_num = 0
        if not self.quiz:
            print("\nNo Question present\n")
            return
        for num,info in self.quiz.items():
            if que in info['Que']:
                del_num = int(num)
        if del_num == 0:
            print("\nQuestion not present\n")
            return
        if del_num in self.quiz.keys():
            del self.quiz[del_num]
        for i in list(self.quiz.keys()):
            if int(i) > del_num:
                self.quiz[str(int(i)-1)] = self.quiz.pop(i)
        self.save_que()
        print("Removed")
        print("\nQuestion removed successfully\n")

    def view_que(self):
        print("\n---------- QUIZ ----------\n")
        for q_num, info in self.quiz.items():
            print(f"Q{q_num}. {info['Que']}\nAns. {info['Ans']}\n")
 
    def quiz_main(self):
        while True:
            print(f"\n1. Add Question\n"
                  f"2. Delete Question\n"
                  f"3. View Question\n"
                  f"4. Exit to Home\n")
            try:
                choice = int(input("Enter your choice:"))
                if choice == 1:
                    que = input("Enter Question:")
                    ans = input("Enter Answer:")
                    self.add_que(que,ans)

                elif choice == 2:
                    que = input("Enter Question:")
                    self.delete_que(que)

                elif choice == 3:
                    self.view_que()

                elif choice == 4:
                    return
                else:
                    print("\nInvalid Choice\n")
            except Exception as e:
                print(f"Error: {e}")

class AttemptQuiz(Quiz):

    @log_activities("Takes Quiz")
    def take_quiz(self,name):
        with open("quiz.json", "r") as que:
            data = json.load(que)
        if not data:
            print("\nNo question present\n")
            return
        if len(name)==0:
            print("\nName cannot be blank\n")
        self.quiz = self.load_que()
        score = 0
        for q_num, info in self.quiz.items():
            print(f"Q{q_num}. {info['Que']}")
            attempt_ans = input("Enter answer:")
            if attempt_ans == info['Ans']:
                score += 1
        if name not in self.attempt:
            self.attempt[name] = {'Attempts': 1, 'Score': [score]}
        else:
            self.attempt[name]['Attempts'] += 1
            self.attempt[name]['Score'].append(score)
        self.save_attempt()
        print("\nQuiz complete\n")

    def view_score(self,name):
        if name not in self.attempt:
            print("\nParticipant not found\n")
            return
        print("\n----Participant Score----\n")
        for names, details in self.attempt.items():
            if name == names:
                print(f"Name: {name}\nAttempts: {details['Attempts']}\nScores: {details['Score']}\n")

    def attempt_main(self):
        while True:
            print(f"\n1. Take Quiz\n"
                  f"2. View Score\n"
                  f"3. Exit to Home\n")
            try:
                choice = int(input("Enter your choice:"))
                if choice == 1:
                    name = input("Enter participant name:")
                    self.take_quiz(name)

                elif choice == 2:
                    name = input("Participant Name:")
                    self.view_score(name)

                elif choice == 3:
                    return
                else:
                    print("\nInvalid Choice\n")
            except Exception as e:
                print(f"Error: {e}")

def main():
    quiz = Quiz()
    admin = CreateQuiz()
    student = AttemptQuiz()
    while True:
        print("\n=============== HOME ===============\n")
        choice = input("Enter (Admin/Student/Analysis/Exit):")

        if choice.title() == "Admin":
            admin.quiz_main()

        elif choice.title() == "Student":
            student.attempt_main()

        elif choice.title() == "Analysis":
            quiz.analysis()

        elif choice.title() == "Exit":
            print("Thank You")
            break

        else:
            print("Invalid Input")
if __name__ == "__main__":
    main()