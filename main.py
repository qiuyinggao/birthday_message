print ("Monday income: ")
Monday_income = int(input())

print ("Tuesday income: " )
tuesday_income = int(input())

print ("Wed income: ")
Wed_income = int(input())

print ("Thur income: " )
thur_income = int(input())

print ("Fir income: ")
Fir_income = int(input())

print ("Sat income: " )
Sat_income = int(input())

print (" Sun income: ")
Sun_income = int(input())

summary_income = Monday_income + tuesday_income + Wed_income + thur_income + Fir_income + Sat_income + Sun_income

print ("visa: ")
visa = int(input())

print ("employee fee: ")
employee_fee = int(input())

print ("cost: ")
cost = int(input())

pure_income = summary_income - visa - employee_fee - cost



print (f"summary income, {summary_income}, \n pure incomes total, {pure_income}")