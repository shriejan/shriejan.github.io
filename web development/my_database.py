class Todolist:
    def __init__(self):
        self.database = {'0':'task1','1':'task2','2':'task3','3':'task4','4':'task5'}
        
    def add_task(self,task_number,task):
        '''ádd task to the database'''
        if task_number in self.database:
            raise ValueError("Task already exists")
        else: 
            file = open("tasks.txt", "a")
            file.write(f"{task_number},{task}\n")
            file.close()


    def remove_task(self,task_number):
        '''remove task from the database'''	
        return self.database[task_number]
    
    def get_all_tasks(self):
        '''return all tasks in the database'''
        file2 = open("tasks.txt", "r")
        data = file2.read()
    
        for line in data:
            a,b = line.split(",")
            self.database[a] = b
        return self.database


    


