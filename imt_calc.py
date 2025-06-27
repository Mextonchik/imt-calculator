print("Привет, это калькулятор ИМТ! Тебе потребуется ввести некоторые данные!") #The initial text
height = float(input("Введите, пожалуйста свой рост (м): ")) #Calculation formulas
weight = float(input("Введите, пожалуйста свой вес (кг): ")) #Calculation formulas
bmi = weight / (height**2) #Calculation formulas
if bmi < 16:
 category = "Выраженный дефицит массы тела!"
elif 16 <= bmi < 18.5:
 category = "Дефицит массы тела!"
elif  18.5 <= bmi < 25:
 category = "Норма!" 
elif 25 <= bmi < 30:
 category = "Избыточная масса тела!"
elif 30 <= bmi < 35:
 category = "Ожирение первой степени!" 
elif 35 <= bmi < 40:
 category = "Ожирение второй степени!" 
else:
 category = "Ожирение третьей степени!" #Possible outcomes, result connection with parameter table
print(f"Твой ИМТ:{bmi: .1f} ({category})") #Output of results

 


