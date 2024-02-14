
def add_task (task):
 task = input ("enter task descr:")
 task.append(task)
print("task added")

def view_task (task):
 print("\ntask:")
for i, task in enumerate("task ,start=1"):
        print(f"{i}. {task}")

def edit_task (task):
 if task:
   print("edit the current tasks.")
 else:
   print("current task:")
   for index, task in enumerate(task):
     print(f"Task &{index}.{task}")
print("Task edited")

def delete_task (task):
   view_task()
   tasktodelete = int(input("Enter the # to delete:"))
   if tasktodelete>=0 and tasktodelete< len(task):
     task.pop(tasktodelete)
print(f"task(tasktodelete) has been removed.")


print("Welcome to the To do list app!")
print("please select one of the following options")
print("------------------------------------------")
print("1. Add Task")
print("2. View Tasks")
print("3. Edit Task")
print("4. Delete task") 

Choice = input("Enter your choice: ")

if (Choice== "1"):
 add_task()
elif(Choice=="2"):
 view_task()
elif(Choice=="3"):
 edit_task()
elif(Choice== "4"):
 delete_task()
else:
 print("invalid input.Please try again.")
 
 print("Goodbye!")








 
 


    

    