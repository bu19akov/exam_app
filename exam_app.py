import random

class Exam:
    def __init__(self, n):
        self.n = n

    def save_result(self):
        name = input("What is your name? ")
        with open("results.txt", "a") as file:
            if self.level == "1":
                file.write(f"{name}: {self.n}/5 in level {self.level} ({self.level_one})")
            else:
                file.write(f"{name}: {self.n}/5 in level {self.level} ({self.level_two})")
            print('The results are saved in "results.txt".')

    def level(self):
        while True:
            self.level_one = "1 - simple operations with numbers 2-9"
            self.level_two = "2 - integral squares of 11-29"
            self.level = input(f"Which level do you want? Enter a number:\n{self.level_one}\n{self.level_two} ")
            if self.level == "1" or self.level == "2":
                self.questions()
                break
            else:
                print("Incorrect format.")
                continue

    def questions(self):
        if self.level == "1":
            for i in range(5):
                self.level_1()
        else:
            for i in range(5):
                self.level_2()
        save = input(f"Your mark is {self.n}/5. Would you like to save the result? Enter yes or no. ")
        if save in "yes, YES, y, Yes":
            self.save_result()
        else:
            exit()

    def level_1(self):
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        op = random.choice("+*-")
        print(x, op, y)
        while True:
            try:
                answer = int(input())
            except ValueError:
                print("Incorrect format.")
                continue
            else:
                if answer == eval(f"{x} {op} {y}"):
                    print("Right!")
                    self.n += 1
                    break
                else:
                    print("Wrong!")
                    break

    def level_2(self):
        x = random.randint(11, 29)
        print(x)
        while True:
            try:
                answer = int(input())
            except ValueError:
                print("Incorrect format")
            else:
                if answer == x**2:
                    print("Right!")
                    self.n += 1
                    break
                else:
                    print("Wrong!")
                    break

exam = Exam(0)
exam.level()
