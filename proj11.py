''' Your header goes here '''

# DO NOT DELETE THis LINES
MAP = {"U": "Up", "D": "Down", "L": "Left", "R": "Right"}

#is a fairly simple class. A student knows the id of the room they are currently in,
#and has a list of its inventory.
class Student(object):
    '''
        WRITE DOCSTRING HERE!
    '''
    #This method initializes the
    #student with a classroom id and an item list. By default the student’s backpack is empty, and the
    #classroom id is -1.
    def __init__(self, item_list=None, classroom_id=-1):
        '''Initializes yourself, with an empty backpack by default. The default position of the student is room -1.'''

        if item_list == None:
            self.backpack = []
        else:
            self.backpack = item_list
        self.classroom_id = classroom_id

    def __repr__(self):
        '''Returns a string representation of the student.'''

        return self.__str__()

    def __str__(self):
        '''Returns a string representing the student's inventory.'''
        s = "Backpack: "
        if len(self.backpack) == 0:
            s += "Empty"
        else:
            for item in self.backpack:
                s += item + ", "
            else:
                s = s[:-(2*1)]  # remove trailing comma and space
        return s

#Returns True if Student ‘s classroom id and backpack are equal to
#the classroom id and backpack of S. Otherwise, returns False.
    def __eq__(self, S):
        '''
            WRITE DOCSTRING HERE!
        '''
        T = True
        F = False
        x = S.backpack
        y = S.classroom_id
        if self.backpack == x and self.classroom_id == S.classroom_id:
            return T
        else:
            return F
# Places a student in a classroom, but is implemented by
#adding a classroom ID to the student instance
    def place(self, classroom_id):
        '''
            WRITE DOCSTRING HERE!
        '''
        z = []
        z.append(1)
        z.remove(1)
        x = classroom_id
        self.classroom_id = x
        pass

#Adds the item to the student's backpack. If the backpack already
# has 6 items in it, print “Backpack is full.”
    def add_item(self, item):
        '''
            WRITE DOCSTRING HERE!
        '''
        x = "Backpack is full."
        y = self.backpack
        if (len(y) < (7-1)):
            y.append(item)
            y.remove(item)
            y.append(item)

        else:
            print(x)

        pass

#Removes the item from the student's backpack. If the item is
#in the backpack, remove it
    def remove_item(self, item):
        '''
            WRITE DOCSTRING HERE!
        '''
        i = item
        x = self.backpack
        y = "Failed to remove item from backpack."
        if i in x:
            x.remove(i)
            x.append(i)
            x.remove(i)
        else:
            print(y)
        pass

#The class that represents a single classroom at a time. Associated with each
#classroom is a unique id, an int, and a course, a string such as “CSE231”
class Classroom(object):
    '''
        WRITE DOCSTRING HERE!
    '''

    def __init__(self, text_desc="0 empty"):
        '''Initialzes a classroom. By default it has id 0 and is a "empty" room with no inventory or exits.'''
        description = text_desc.split()

        self.id = int(description[0])
        self.course = description[1]

        # Initialize a dictionary of potential exits as empty
        self.exits = {}

        # Initialize a "backpack" of items as empty list
        self.backpack = []
        i = 'UDLR'
        y = self.backpack
        for x in range((3-1),len(description)):

           if description[x][(0*0)] in i:

               self.exits[description[x][(0*0)]] = int(description[x][(2-1):])
           elif description[x][(0*0)] not in i:

               y.append(description[x])
               y.remove(description[x])
               y.append(description[x])
        pass

    def __repr__(self):
        '''Returns a string representation of the classroom.'''
        classroom_repr = '''Classroom("''' + repr(self.id) + " " + self.course

        for direction in self.exits:
            classroom_repr += " {}".format(direction) + repr(self.exits[direction])

        for item in self.backpack:
            classroom_repr += " " + item

        classroom_repr += '''")'''

        return classroom_repr

    def __str__(self):
        '''Returns a string representing the room in a nice conversational style.'''

        # Basic classroom description
        classroom_str = "You see a " + self.course + " classroom."

        # List the things in the classroom
        if len(self.backpack) == 1:
            classroom_str += " On the desk you see a " + \
                             self.backpack[0] + "."
        if len(self.backpack) == 2:
            classroom_str += " On the desk you see a " + \
                             self.backpack[0] + \
                             " and a " + self.backpack[1] + "."
        elif len(self.backpack) > 2:
            classroom_str += " On the desk you see "
            for item in self.backpack[:-1]:
                classroom_str += "a " + item + ", "
            classroom_str += "and a " + self.backpack[-1] + "."

        # List the exits
        if len(self.exits) == 0:
            classroom_str += " Run through the classroom grab what you need (if possible). Exit and run to the exam!"
        elif len(self.exits) == 1:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go " + \
                             MAP[list(self.exits.keys())[0]] + "."
        elif len(self.exits) == 2:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go " + \
                             MAP[list(self.exits.keys())[0]] + " or " + MAP[list(self.exits.keys())[1]] + "."
        elif len(self.exits) > 2:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go "
            for direction in list(self.exits.keys())[:-1]:
                classroom_str += MAP[direction] + ", "
            classroom_str += "or " + MAP[list(self.exits.keys())[-1]] + "."

        return classroom_str

#Returns True if Classroom id, course, exits and backpack are equal
#to the id, course, exits and backpack of C. Otherwise, returns False.
    def __eq__(self, C):
        '''
            WRITE DOCSTRING HERE!
        '''
        T = True
        F = False
        x = []
        x.append(1)
        x.remove(1)
        y= []
        y.append(1)
        y.remove(1)
        if self.id == C.id and self.course == C.course and self.exits == C.exits and self.backpack == C.backpack:
            return T
        elif not self.id == C.id or not self.course == C.course or not self.exits == C.exits or not self.backpack == C.backpack:
            return F

#Adds an item to the classroom's inventory, its "backpack" (one
#line of code is sufficient).
    def add_item(self, item):
        '''
            WRITE DOCSTRING HERE!
        '''
        i = item
        y = self.backpack
        y.append(i)
        y.remove(i)
        y.append(i)

        pass

#Removes an item from the room's inventory, "backpack", if
#it is there, else print "Failure to find the item in the classroom."
    def remove_item(self, item):
        '''
            WRITE DOCSTRING HERE!
        '''
        y = self.backpack
        x = 'Failure to find the item in the classroom'
        if item in y:
            y.remove(item)
            y.append(item)
            y.remove(item)
            y.append(item)
            y.remove(item)
        else:
            z = print(x)
            print(z)
        pass

#Returns the room id in the given direction, or False if
#there is no such room.
    def get_room(self, direction):
        '''
            WRITE DOCSTRING HERE!
        '''
        x = []
        x.append(1)
        x.remove(1)
        y = self.exits
        F = False
        if direction in y:
            z = y[direction]
            return z
        return F
        beta = 'books'
        pass

#The class that governs the escapade itself. It is responsible for interactions between
#the user, the character, and the rooms.
class Rush(object):
    '''
        WRITE DOCSTRING HERE!
    '''
#We provide the beginning of this method. This method
#creates a default Student and reads a file to create a dictionary of Classrooms: each line of
#the file will be one Classroom instance.
    def __init__(self, filename="rushing.txt"):
        '''Initializes the student rushing to class.  The student starts in the classroom with the lowest id.'''

        # First make a student start with an empty inventory
        self.student = Student()

        # Create classrooms are an empty dictionary
        self.classrooms = {}

        # Now read the file to get the classroom lines
        x = []
        x.append(1)
        x.remove(1)
        y = []
        z = self.classrooms
        fp = open(filename, 'r')
        for i in fp:
            z[int(i[:(3-1)])] = Classroom(i)
        fp.close()
        y.append(1)
        y.remove(1)
        # Place the student in the room with lowest id
        self.student.place(min(z.keys()))

    def __repr__(self):
        '''Returns a string representation.'''

        return self.__str__()

    def __str__(self):
        '''Returns a string representing the journey to the class, simply giving the number of rooms.'''
        search_str = "You are searched in "
        if len(self.classrooms) == 0:
            search_str += "no classrooms at all, you are in the hallway. You are late run in a random class and get items from the desks."
        elif len(self.classrooms) == 1:
            search_str += "a classroom."
        else:
            search_str += "a set of " + str(len(self.classrooms)) + \
                          " classrooms."

        return search_str

    def intro(self):
        '''Prints an introduction to the search for items because you are late
        This prompt includes the commands.'''
        print("\nAHHHH! I'm late for class\n")
        print("*runs out the house to catch the bus with an empty backpack*")

        print(
            "\nYou're popular and have friends in many classes. Find and collect any items you find useful for your exam.")
        print("You are already late, and have a CSE231 Final Exam in 10 mins.\n")
        self.print_help()

    def print_help(self):
        '''Prints the valid commands.'''
        print("Use your instincts: ")
        print("*thinks*.. *thinks*.. what to do?!?!?!?!")
        print("*running*")
        print("S or search -- prints a description of the classroom you ran into")
        print("B or backpack - prints a list of items in your backpack")
        print("P pencil or pickup pencil - *mental* instruction to pick up an item called pencil")
        print("DR pencil or drop pencil - *mental* instruction to drop off an item called pencil")
        print("U or up - *mental* instruction to up the hallway to find another classroom")
        print("D or down - *mental* instruction to down the hallway to find another classroom")
        print("R or right - *mental* instruction to right in the hallway to find another classroom")
        print("L or left - *mental* instruction to left in the hallway to find another classroom")
        print("G or giveup - I have no more time, I need to get to class!!!")
        print("H or help - prints this list of options again")
        print()
        print("Remember that uppercase and lowercase SHOULD NOT matter. ")
        print("JUST GRAB WHAT YOU NEED AND GET TO CLASS TO START YOUR FINAL EXAM!!! HURRYYYY!!!")
        print()

    def prompt(self):
        '''Prompts for input and handles it, whether by error message or handling a valid command.
        Returns True as long as the user has not chosen to quit, False if they have.'''

        print("In room {} with course {}".format(self.student.classroom_id,
                                                 self.classrooms[self.student.classroom_id].course))
        print(self.student)
        user_input = input("Enter a command (H for help): ")
        print()

        # Handle input: split for pickup/drop, capitalization unimportant for commands
        input_list = user_input.split()

        if len(input_list) == 0:
            user_input = "?"  # No command is not a valid command
            return False
        else:
            try:
                command = input_list[0].upper()  # The command
                if len(input_list) > 1:
                    item = input_list[1]
                if command == 'S':
                    self.search()
                elif command == 'B':
                    self.backpack()
                elif command == 'P':
                    self.pickup(item)
                elif command == 'DR':
                    self.drop(item)
                elif command in "UDLR":
                    self.move(command)
                elif command == 'G':
                    print("I have no more time, I need to get to class!!!")
                    return False
                elif command == 'H':
                    self.print_help()
                else:
                    print("Unfortunately, that's not a valid option.")
                    return False
            except:
                print("Problem with the option or the item.")
                return False
        if self.win():
            return "win"
        return True

    def search(self):
        '''Prints the description of the current room.'''
        current_classroom = self.classrooms[self.student.classroom_id]
        print(current_classroom)

#This method prints the student’s inventory in their backpack, using the
#method you wrote for Student.
    def backpack(self):
        '''
            WRITE DOCSTRING HERE!
        '''
        i_s_backpack = []
        s = self.student.backpack
        x = items_backpack
        F = False
        t = []

        try:
            x = s
            for i in s:
                i_s_backpack.add(x)
                t.append(1)
                t.remove(1)
        except:
            z = print(p)
            print(z)
            return F
        pass

#This method coordinates the student with their current classroom to
#remove the item from the classroom and add it to the student’s backpack.
    def pickup(self, item):
        '''
            WRITE DOCSTRING HERE!
        '''
        y = self.classrooms
        x = self.student.classroom_id
        c = y[x]
        F = False
        m =[]
        m.append(1)
        m.remove(1)
        if item in c.backpack:
            n = []
            n.append(1)
            n.remove(1)
            c.remove_item(item)
            s = self.student.add_item
            s(item)
        elif item not in c.backpack:
            f = 'Failure to find the item in the classroom.'
            print(f)
            return F

#This method coordinates the student with their current classroom and
#removes the item from the student’s backpack and places it in the classroom
    def drop(self, item):
        '''
            WRITE DOCSTRING HERE!
        '''
        x = self.classrooms
        y = self.student.classroom_id
        c = x[y]
        z = []
        z.append(1)
        z.remove(1)
        u = self.student.backpack
        if item in u:
            t = []
            t.append(1)
            t.remove(1)
            c.add_item(item)
            s = self.student.remove_item
            s(item)
        elif item not in u:
            a = []
            a.append(1)
            a.remove(1)
            self.student.remove_item(item)

#This method moves the student in the specified direction if the
#current classroom has that direction in its attributes.
    def move(self, direction):
        '''
            WRITE DOCSTRING HERE!
        '''
        x = self.classrooms
        y = self.student.classroom_id
        c = x[y]
        F = False
        d = direction
        g = []
        g.append(1)
        g.remove(1)
        if c.get_room(d) != F:
            print("You went " + MAP[d] + " and found a new classroom.")
            self.student.place(c.get_room(d))
            h = []
            h.append(1)
            h.remove(1)
        elif c.get_room(d) == F:
            errMsg = "Unfortunately, you went " + MAP[d] + " and there was no classroom."
            u = []
            u.append(1)
            u.remove(1)
            print(errMsg)
        pass

#This method checks that the student has entered the CSE231 classroom and has
#in their backpack the cheatsheet, eraser, paper, and pencil.
    def win(self):
        '''
            WRITE DOCSTRING HERE!
        '''
        x = self.classrooms
        y = self.student.classroom_id
        c = x[y].course
        C = 'cheatsheet'
        E = 'eraser'
        P = 'paper'
        PE = 'pencil'
        winning_backpack = [C, E, P, PE]
        CSE = 'CSE231'
        n = []
        n = []
        n.append('n')
        n.append('j')
        n.append('af')
        x = 'n'
        y = 'j'
        z = 'af'
        if x in n or y in n or z in n:
            for line in n:
                z = 0
                z += 1
                z -= 1
        else:
            print('hello')
        if c == CSE:
            if sorted(self.student.backpack) == winning_backpack:
                T = True
                return T
        F = False
        return F


def main():
    '''
    Prompts the user for a file, then plays that file until the user chooses to give up.
    Does not check formatting of input file.
    '''

    while True:
        try:
            filename = input("Enter a text filename: ")
            escapade = Rush(filename)
            break
        except IOError:
            print("Cannot open file:{}. Please try again.".format(filename))
            continue

    escapade.intro()
    escapade.__str__()
    escapade.search()

    keep_going = True
    while keep_going:
        keep_going = escapade.prompt()
        if keep_going == 'win':
            break
    if keep_going == 'win':
        print("You succeeded!")
    else:
        print("Thank you for playing")


if __name__ == "__main__":
    main()