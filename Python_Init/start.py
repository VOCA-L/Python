from enum import Enum

class Command(Enum):
    START = 1
    RUNNING = 2
    STOP = 3






if __name__ == '__main__':
    
    command = input("Enter your command\n").upper()
    print(Command[command].value)