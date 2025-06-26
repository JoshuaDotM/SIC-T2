while True:
    name=input("Enter your name : ")
    if name.isalpha() and len(name)<50:
        print("Valid Name")
        break
    else:
        input("Re-enter a valid name : ")
    
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
tax=0
if taxable_income > 0 and taxable_income <= 300000:
    pass
elif taxable_income <= 600000:
    tax=taxable_income-(5/100*taxable_income)
elif taxable_income <= 900000:
    tax=taxable_income-(10/100*taxable_income)
elif taxable_income <= 1200000:
    tax=taxable_income-(15/100*taxable_income)
elif taxable_income < 1500000:
    tax=taxable_income-(20/100*taxable_income)
else:
    tax=taxable_income-(30/100*taxable_income)

#-----Section 87A Rebate-----
if taxable_income <= 700000:
    tax=0

h_e_tax=(4/100*taxable_income)
final_tax=tax + h_e_tax
print("The final taxation after adding health and Education cess is :",final_tax)

print('-----Level-4-----')


net_salary=gross_annual_salary-final_tax
print(f"Annual gross salary : {gross_annual_salary} Toatal tax payable : {final_tax}, Annual Net salary : {net_salary}")



print('-----Level-5(Report generation)-----')



print("Employee Details")
print("Name : ",name)
print("Employee ID :",emp_id)
print("Gross annual salary : ",gross_annual_salary)
print("Taxable income : ",taxable_income)
print("Tax payable : ")
print("Standard deduction : Rupees 50000")
print("tax to be paid after the New Regime (2023) : ",tax)
print("Health and Education Cess : ",h_e_tax)
print("total tax to be paid : ",final_tax)
print("Annual net salary : ",net_salary)

#Still working on it to make it more readable