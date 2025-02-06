
def BMI_calculator(weight, height):
    BMI = weight / (height/100)**2
    status = ''
    if BMI < 18.5:
        status = 'underweight'
    elif BMI <= 24.9 and BMI > 18.5:
        status = 'normal'
    elif BMI <= 29.9 and BMI > 24.9:
        status = 'overweight'
    else:
        status = 'obese'

    return BMI,status