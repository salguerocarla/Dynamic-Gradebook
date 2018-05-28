'''
Carla Salguero

Recieved some help in tutoring on how to repeat the loop! Great help always! 

'''
#Part 2: Dynamic Gradebook

while True: #setting up a while loop allows us to continually ask the user for an input until number is greater than 0. 
    students = int(input("How many students in your class? "))
    if students <= 0:
        print ("Invalid # of students, try again.")
    else:
        break # if all is good, then we print a break and go to the next part. 
    
while True: #another while loop is necessary so that we can also validate the number of test scores. 
    tests = int(input("How many tests in this class? "))
    if tests <=0: #exams can be 1 or greater. 
            print ("Invalid # of tests, try again.")
    else:
        break #we break once the amount of test scores are validated. 
print()
print("Here we go!")
print()
averages = 0
for i in range (1,students+1): #here we set up a range, so that we can give scores for each student. 
    score = 0
    print ("**** Student #"+str(i)+"****")
    for j in range (1,tests+1): #now within each students name (#), we enter a score repeately until we each the test amount +1. 
        question = "Enter score for test #"+str(j)+": "
        
        while True: #i have a while loop here to make sure the scores are validated. only postiive values. 
            score1 = int(input(question))
            if score1 <0:
                print ("Invalid Score, try again.")
                
            else:
                score = score + score1 #once the user inputs a valid score, then it will be added together. 
                break
    answer = score/tests
    averages = averages + answer #the averages are computed here. 
    a = format(answer, ".2f")  # iwe have to have a float with two decimal places. 
    
    print ("Average score for student #"+str(i)+" is "+str(a)) #n order to make this number show up in the string, we have to format string.  
    print()
    

print ("Average score for all students is:", format(averages/students, ".2f"))
#After the entire for loop finishes, we then print out the average score for all of the students!!!
#Nice! 
