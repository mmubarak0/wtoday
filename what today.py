#!/usr/bin/env python3
""" this program show me what task I have to compelete today """

##############
"""
first function :
1-Start
2-read all my classes
3-give me 3 diffrent classes every day
4-END
"""
##############
"""
second function :
1-Start
2-ask me if i complete the task you give me today
3-if yes assign that
4-is there any task left ? if yes return to '2' if no go to '4'
5-tell me all progress I have done so far in all subj
END
"""
##############
"""
third function :
1-Start
2-get the progress of this day
3-add it to the data base
4-print all time progress from (data base)
5-END
"""
##############
"""
fourth function :
1-Start
2-loop over all subj and get pages
3-check if pages reach the limit
4-print congrats if done
5-remove it from JOBS
6-END
"""
##############

import time
import random
import ftu
import shelve
import os
import sys
import pwd


#####
def get_username():
    return pwd.getpwuid(os.getuid())[0]

user        = get_username()
parent_dir  = "/home/"+user
db          = os.path.join(parent_dir, ".local/wtoday")

try:
    os.makedirs(db)
except Exception:
    pass

dbfile = os.path.join(db, "db")
task   = os.path.join(db, "task.txt")

TASK = ftu.read_file_for_me(task)
JOB = ftu.split_file_by_line(TASK)
#####


shelfFile = shelve.open(dbfile)

if len(sys.argv) >= 2:
    if sys.argv[1] == "n":
        JOBS = JOB
        shelfFile["jobs"] = JOBS
    elif sys.argv[1] == "clear":
        shelfFile.clear()
        JOBS = JOB
        shelfFile["jobs"] = JOBS
    if sys.argv[1] == "o":
        os.system('touch %s' %task)
        os.system('xed %s' %task)
        #####
        try:
            JOBS = shelfFile["jobs"]
        except Exception:
            shelfFile["jobs"] = JOB
            JOBS = shelfFile["jobs"]
        #####
    else:
        #####
        try:
            JOBS = shelfFile["jobs"]
        except Exception:
            shelfFile["jobs"] = JOB
            JOBS = shelfFile["jobs"]
        #####
else:
    #####
    try:
        JOBS = shelfFile["jobs"]
    except Exception:
        shelfFile["jobs"] = JOB
        JOBS = shelfFile["jobs"]
    #####

# pages = int(input("enter the number of pages you read tody : "))
today_task = []
subj = {}

def first_function():
    """
    show how task is 
    going in a the progress
    """
    
    for i in range(3):
        num = random.randint(0, len(JOBS)-2)
        if not JOBS[num] in today_task:
            today_task.append(JOBS[num])
    print("Today Task :")
    print("you have to read 5 pages from >> ")
    ftu.num_list_for_me(today_task)
    return today_task


def counter(x):
    """
    Check weather I am done 
    reading 5 pages or not
    """
    Counter = {}
    for i in range(len(x)):
        global pages
        if len(sys.argv) >= 2:
            if sys.argv[1] == 'pages':
                try:
                    pages = int(input(f"how many pages did you read from {x[i]} ? "))
                except Exception:
                    print("ERROR")
                    pages = 5
            else:
                pages = 5
        else:
            pages = 5
        answer = input(f"did you read {pages} page from %s today ? " %x[i])
        if answer.lower() == "y" or answer.lower() == "yes":
            Counter[x[i]] = True
        else:
            Counter[x[i]] = False
    return Counter


def data(x, y):
    """
    save my progress to the data base
    """
    for i in range(len(x)):
        if y[x[i]]:
            # Do

            try:
                shelfFile[x[i]] += pages
            except Exception:
                shelfFile[x[i]] = pages

            nu = shelfFile[x[i]]
            subj[x[i]] = nu

            print(f"Done added {pages} pages to {x[i]} ✅")

        else:
            pass
    return subj


def congrats(x, y, d):
    for i in range(len(x)):
        if y[x[i]]:
            if x[i] == JOBS[0]:
                if d[x[i]] >= 50:
                    print(f"Congratulations You have completed {x[i]} succesfully ")
                    JOBS.pop(i)
                    print(f"there is {len(JOBS)-1} more remaining classes")
                    shelfFile["jobs"] = JOBS
            elif x[i] == JOBS[1]:
                if d[x[i]] >= 70:
                    print(f"Congratulations You have completed {x[i]} succesfully ")
                    JOBS.pop(i)
                    print(f"there is {len(JOBS)-1} more remaining classes")
                    shelfFile["jobs"] = JOBS
            elif x[i] == JOBS[2]:
                if d[x[i]] >= 130:
                    print(f"Congratulations You have completed {x[i]} succesfully ")
                    JOBS.pop(i)
                    print(f"there is {len(JOBS)-1} more remaining classes")
                    shelfFile["jobs"] = JOBS
            elif x[i] == JOBS[3]:
                if d[x[i]] >= 130:
                    print(f"Congratulations You have completed {x[i]} succesfully ")
                    JOBS.pop(i)
                    print(f"there is {len(JOBS)-1} more remaining classes")
                    shelfFile["jobs"] = JOBS
            elif x[i] == JOBS[4]:
                if d[x[i]] >= 130:
                    print(f"Congratulations You have completed {x[i]} succesfully ")
                    JOBS.pop(i)
                    print(f"there is {len(JOBS)-1} more remaining classes")
                    shelfFile["jobs"] = JOBS
            elif x[i] == JOBS[5]:
                if d[x[i]] >= 130:
                    print(f"Congratulations You have completed {x[i]} succesfully ")
                    JOBS.pop(i)
                    print(f"there is {len(JOBS)-1} more remaining classes")
                    shelfFile["jobs"] = JOBS
            elif x[i] == JOBS[6]:
                if d[x[i]] >= 130:
                    print(f"Congratulations You have completed {x[i]} succesfully ")
                    JOBS.pop(i)
                    print(f"there is {len(JOBS)-1} more remaining classes")
                    shelfFile["jobs"] = JOBS
            elif x[i] == JOBS[7]:
                if d[x[i]] >= 130:
                    print(f"Congratulations You have completed {x[i]} succesfully ")
                    JOBS.pop(i)
                    print(f"there is {len(JOBS)-1} more remaining classes")
                    shelfFile["jobs"] = JOBS
            elif x[i] == JOBS[8]:
                if d[x[i]] >= 10:
                    print(f"Congratulations You have completed {x[i]} succesfully ")
                    JOBS.pop(i)
                    print(f"there is {len(JOBS)-1} more remaining classes")
                    shelfFile["jobs"] = JOBS
            
    

x = first_function()
time.sleep(30)
y = counter(x)
d = data(x, y)
congrats(x, y, d)
shelfFile.close()
