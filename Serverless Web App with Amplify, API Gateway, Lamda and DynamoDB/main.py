import boto3
dynamodb = boto3.resource('dynamodb')

def bmi():
    number1 = float(input(number1))
    number2 = float(input(number2))
    bmi_cal = (number1)/(number2*number2)
    print("Your BMI is:",bmi_cal)


def main():
    bmi()