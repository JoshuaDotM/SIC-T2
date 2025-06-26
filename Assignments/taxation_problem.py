name=input("Enter your name : ")
emp_id=int(input("Enter your unique employee ID : "))
basic_salary=int(input("Enter your basic salary : "))
special_allowances=int(input("Enter your monthly special allowances : "))
bonus_percentage=int(input("Enter your annual bonus percentage :"))
gross_monthly_salary=basic_salary+special_allowances
gross_annual_salary=(gross_monthly_salary*12)
bonus=gross_annual_salary*(bonus_percentage/100)
gross_annual_salary=gross_annual_salary+bonus

print("-----Employee Details-----")
print(f"Name : {name}, Employee ID : {emp_id}")
print(f"Gross monthly salary : {gross_monthly_salary}, Annual gross salary : {gross_annual_salary}")

print('-----level-2-----')

taxable_income=gross_annual_salary-50000
print(f"Name : {name}, Employee ID : {emp_id}")
print(f" Annual gross salary : {gross_annual_salary} , Standard deduction : 50000 ,Taxable income : {taxable_income}")

print('-----Level-3-----')

if taxable_income>0 and taxable_income <= 300000:
    pass
elif taxable_income <= 600000:
    taxable_income=taxable_income-(5/100*taxable_income)
elif taxable_income <= 900000:
    taxable_income=taxable_income-(10/100*taxable_income)

#Still working on it to make it more readable