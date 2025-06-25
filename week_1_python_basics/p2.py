'''
Accept the average score from the student and give her the results as follows:(for ease of understanding)
0 to 69 Fail
70 to 84 Second class
85 to 95 First class
96 to 100 Excellent
'''
#since the conditions are already ordered, from the second conditional statement the first half of the condition  can be removed, but for a more optimised code ; ex. in auniversity, there are more people who can score excellent. therefore the conditional statement with that can be placed first to increase the efficiency. in such cases since the conditions are not order we have to specify the extra conditions.
average_score=int(input("Enter the student average score: "))  
if average_score >=0 and average_score <= 69:
    print("Result is Fail")
elif average_score >= 70 and average_score <= 84:
    print("Result is Second class")
elif average_score >=85 and average_score <=95:
    print("Result is First class")
elif average_score >=96 and average_score <=100:
    print("The result is excellent")
else:
    print("Invalid input")