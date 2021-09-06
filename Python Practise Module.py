# To check numbers divisible by 5 & 7 between 1500 and 2800
for i in range(1500,2801):
    if i%5==0 and i%7==0:
        print (i)
        
# To count the number of even & odd numbes from a series of numbers
series = range(1,106)
even_count=0
odd_count=0
for i in series:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("the count of even numbers is :", even_count)
print("the count of odd numbers is : ", odd_count)

#To print series of numbers. Print Fizz for numbers divisible by 3 and print buzz for numbers divisible by 5. 
#Print FizzBuzz for numbers divisible by both 3 & 5

for i in range(0,51):
    if i%3==0 and i%5==0:
        print("FIZZBUZZ")
    elif i%3==0:
       print("FIZZ")
    elif i%5==0:
        print("BUZZ")
    else:
        print (i)
    
#To calculate sum and average of a series of numbers
n = int(input("Enter the range of series: "))
m = int(input("Enter interval of series: "))
for i in range(0,n,m):
    sum += i
    avg = sum/n
print("The sum the series is:", sum)
print("The average of the series is:", avg)