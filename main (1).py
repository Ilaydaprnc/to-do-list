
task_secin = """
---------------------------
HATA! Bir task seçin.            
---------------------------"""

class Task:
    def __init__(self,taskNum:int,taskName:str,done:str):
        self.taskNum = taskNum
        self.taskName = taskName
        self.done = done
    
    def createTaskText(self):
        return f"{self.taskName} {'+' if self.done == "1" else "-"}"


class TaskManager:
    def __init__(self):
        action = input("Bir işlem seçin. : ")
        if action == "":
            print("""
---------------------------
HATA! Bir işlem seçin.            

Yapılabilecek işlemler;
1 - Task getir
2 - Tasklar
3 - Task Kaydet
4 - Task Sil
5 - Taskı güncelle
---------------------------""")

        if action == "1":
           return self.getTask()
        if action == "2":
           return self.getTasks()
        if action == "3":
            return self.saveTasks()
        if action == "4":
            return self.deleteTask()
        if action == "5":
            return self.updateTaskDone()
        
    def getTask(self):
       taskNum = input("Bir Task Numarası girin : ")
       if taskNum == "":
           print("""
---------------------------
HATA! Bir task seçin.            
---------------------------""")
           return self.getTask()
       
       print(file.readlines()[int(taskNum)-1])
       file.close()
    
    
    def getTasks(self):

        text = ""
        num = 0

        for i in file.readlines():
            num = num + 1
            text = text + str(num) + "-) " + i + "\n"
        print(text)
        file.close()
    
    
    def saveTasks(self,taskName = ""):

        if taskName == "":
            taskName = input("Task İsmi Giriniz. : ")
        if taskName == "":
            print(task_secin)
            return self.saveTasks("")

        done = input("Task'ın tamamlanıp tamamlanmadığını belirtiniz ('1' tamamlandı, '0' tamamlanmadı.) : ")

        if done == "":
            print("""
---------------------------
HATA! Task'ın tamamlanıp tamamlanmadığını belirtiniz ('1' tamamlandı, '0' tamamlanmadı.)
---------------------------
""")
            return self.saveTasks(taskName)



        l = file.readlines()
        
        newTask = Task(len(l),taskName,done).createTaskText()
        lst = []
        for i in l:
            lst.append(i)
        lst.append(newTask+"\n")
        file.close()
        newFile = open("tasks.txt","w")
        newFile.writelines(lst)
        newFile.close()
        print("Task başarıyla eklendi")
        
    def deleteTask(self):
        taskNum = input("Bir Task Numarası girin : ")
        if taskNum == "":
           print(task_secin)
           return self.getTask()
       
        l = file.readlines()
        l.pop(int(taskNum)-1)
        newFile = open("tasks.txt","w")
        newFile.writelines(l)
        newFile.close()
        file.close()
        print("Task başarıyla silindi.")

    def updateTaskDone(self):
        taskNum = input("Bir Task Numarası girin : ")
        if taskNum == "":
           print(task_secin)
           return self.getTask()
       
        l = file.readlines()
        l[(int(taskNum)-1)] = l[(int(taskNum)-1)].replace("+","-") if "+" in l[(int(taskNum)-1)] else l[(int(taskNum)-1)].replace("-","+") 
        newFile = open("tasks.txt","w")
        newFile.writelines(l)
        newFile.close()
        file.close()
        print("Task başarıyla güncellendi.")



while(True):
    file = open("tasks.txt")
    TaskManager()