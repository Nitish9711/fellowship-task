import sys
from os import path
import datetime 

if(not path.exists('todo.txt')):
    todo = open('todo.txt', 'w')
    todo.close()

if(not path.exists('done.txt')):
    done = open('done.txt', 'w')
    done.close()

n = len(sys.argv)

task_count = 0

def help():
    help_string = "Usage :-\n$ ./todo add \"todo item\"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics"
    sys.stdout.buffer.write(help_string.encode('utf8'))


def ls():
    todo = open('todo.txt', 'r')
    tasks = todo.readlines()
    if(len(tasks) == 0):
        output = "There are no pending todos!"
        sys.stdout.buffer.write(output.encode('utf8'))
    else:
        for task in tasks:
            sys.stdout.buffer.write(task.encode('utf8'))
    
    todo.close()


def add(s):
    todo = open('todo.txt', 'r')
    tasks = todo.readlines()
    count = len(tasks)
    todo.close()
    # print(tasks)
    add_task = "[" + str(count+1) + "] " + s + '\n'
    todo = open('todo.txt', 'w')
    todo.write(add_task)
    for task in tasks:
        todo.write(task)
    
    todo.close()
    output  = "Added todo: \"" + s + "\""
    sys.stdout.buffer.write(output.encode('utf8'))



    


def delete(i):  
    todo = open('todo.txt', 'r')
    tasks = todo.readlines()
    count = len(tasks)
    todo.close()
    if(int(i) > count or int(i) <=0):
        msg = "Error: todo #" + str(i) + " does not exist. Nothing deleted."
        sys.stdout.buffer.write(msg.encode('utf8'))
    
    else:
        for task in tasks:
            if(task[1] == str(i)):
                tasks.remove(task)
                break
        count2 = len(tasks)
        if(count2 == count):
            msg = "Deleted todo #" + str(i)
            sys.stdout.buffer.write(msg.encode('utf8'))
        else:
            todo = open('todo.txt', 'w')
            for task in tasks:
                todo.write(task)
            
            todo.close()
            msg = "Deleted todo #" + str(i)
            sys.stdout.buffer.write(msg.encode('utf8'))
            
    


def done(i):
    todo = open('todo.txt', 'r')
    tasks = todo.readlines()
    count = len(tasks)
    todo.close()
    for task in tasks:
        if(task[1] == str(i)):
            tasks.remove(task)
            break
    if(len(tasks) == count):
        msg = "Error: todo #" + str(i)+ " does not exist."
        sys.stdout.buffer.write(msg.encode('utf8'))
    
    else:
        done = open('done.txt', 'a')
        output = "x " + str(datetime.date.today()) + " " + task[4:]
        done.write(output)

        todo = open('todo.txt', 'w')
        for task in tasks:
            todo.write(task)
        
        todo.close()

        msg = "Marked todo #"+ str(i) +" as done."
        sys.stdout.buffer.write(msg.encode('utf8'))


def report():
    todo = open('todo.txt' , 'r')
    tasks = todo.readlines()
    pending = len(tasks)
    todo.close()
    # print(tasks)

    done = open('done.txt' , 'r')
    tasks = done.readlines()
    completed = len(tasks)
    done.close()
    # print(tasks)

    msg = str(datetime.date.today()) + " Pending :" + " " + str(pending) + " Completed : " + str(completed)
    sys.stdout.buffer.write(msg.encode('utf8'))

    

if(n == 1 or (n ==2 and sys.argv[1] == "help")):
    help()

elif(n == 2 and sys.argv[1] == 'ls'):
    ls()

elif(n ==2 and sys.argv[1] == "report"):
    report()
  
elif(n == 2 and sys.argv[1] == 'add'):
    msg = "Error: Missing todo string. Nothing added!"
    sys.stdout.buffer.write(msg.encode('utf8'))

elif(n ==2 and sys.argv[1] == 'del'):
    msg = "Error: Missing NUMBER for deleting todo."
    sys.stdout.buffer.write(msg.encode('utf8'))

elif(n ==2 and sys.argv[1] == 'done'):
    msg = "Error: Missing NUMBER for marking todo as done."
    sys.stdout.buffer.write(msg.encode('utf8'))

elif(n == 3 and sys.argv[1] == 'add'):
    add(sys.argv[2])

elif(n >=3 and sys.argv[1] == 'add'):    
    for i in range(2, n):
        add(sys.argv[i])

elif(n == 3 and sys.argv[1] == 'del'):
    delete(sys.argv[2])

elif(n == 3 and sys.argv[1] == 'done'):
    done(sys.argv[2])

