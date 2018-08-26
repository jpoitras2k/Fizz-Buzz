# Fizz Buzz - Have been working on learning python and decided to give it a try

print ("This is a math program designed to print Fizz if the number is divisable by 3 and Buzz if the number is divisable by 5.")

startnum = 1 # starting number as a variable
endnum = 100
    

for number in range(startnum, endnum):
     if number %3 == 0 and number % 5 == 0:
        print ('FizzBuzz')
        #exits loop if true - remainder is 0
     elif number % 3 == 0:
        print ('Fizz')
     elif number % 5 == 0:
        print ('Buzz')
     else:
         print (number)
     
        
    
                    