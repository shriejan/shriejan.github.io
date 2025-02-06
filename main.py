from flask import Flask, render_template, request
from myFunctions import BMI_calculator
from my_database import Todolist

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Shriejan'
    lst= ["blue", "red", "yellow", "green", "orange"]
    name_age={"shriejan": 21,"Ali": 7.9, "umair": 10, "shruti": 5}


    return render_template('index.html',name = name,colors = lst,name_age = name_age)




@app.route('/shriejan')
def index2():
    return 'Hello, Shriejan!'


@app.route('/bmi_calculator',methods=['GET','POST'])
def index3():
    weight  = request.form.get('weight')
    height = request.form.get('height')
    
    weight = float(weight)
    height = float(height)
    BMI, status = BMI_calculator(weight, height)
    
    

    return render_template('bmi_calculator.html',BMI = BMI, status = status)

todo = Todolist()
@app.route('/todo',methods=['GET','POST'])
def index4():
    if request.method == 'POST': # check if the request is a POST request if somone submits the form
        todo.add_task(request.form.get('number'),request.form.get('todo'))
    
    tasks = todo.get_all_tasks()
    return render_template('todo.html',todo = tasks)
    

   

if __name__ == '__main__':
    app.run(debug=True)