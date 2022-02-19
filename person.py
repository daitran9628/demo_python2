class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printName(self):
        return ("Your name is {} {}".format(self.fname, self.lname))

class Student(Person):
    def __init__(self, fname, lname, gender, age):
        Person.__init__(self, fname, lname)
        #super().__init__(fname, lname):
        self.gender = gender
        self.age    = age

    def printName(self):
        return Person.printName(self) + " " + str(self.age)

if __name__ == "__main__":
    p = Person("John", "Yahoo")
    print(p.printName())
    s = Student("Mary", "Google", "F", 21)
    print(s.printName())
