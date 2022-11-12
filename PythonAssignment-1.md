## Assignment Part-1
Q1. Why do we call Python as a general purpose and high-level programming language?
 >> It is used in many different fields like web programming AI etc. and it is called high level because it writtern in human readable format and when we run it is than converted to machine understandable format with the help of interpreter.
 
Q2. Why is Python called a dynamically typed language?
 >>Because the type of variable's is determined during runtime.
 
Q3. List some pros and cons of Python programming language?
 >Pros: Readable code, Dynamically Typed, Open-Source
  Cons:Python alloes single thread to run at a time. where as if we talk about jave it is multi threaded which means it can concurrently run multiple threads  at the same time.

Q4. In what all domains can we use Python?
>> Data Engineering, AI, Web Devlopment,etc

Q5. What are variable and how can we declare them?
>> memory location that stores value/data. 
>> val = 10 

Q6. How can we take an input from the user in Python?
>> input()

Q7. What is the default datatype of the value that has been taken as an input using input() function?
>> String

Q8. What is type casting?
>> Converting one datatype to another

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?
>> yes we can take more than one input from the user using single input... 
>> input().split()

Q10. What are keywords?
>>Reserver words for example for, while etc

Q11. Can we use keywords as a variable? Support your answer with reason.
>>No, Becase these are reserverd words.

Q12. What is indentation? What's the use of indentaion in Python?
>> It is basically a space and we can say that it is used to define the scope of any block/elements in python.

Q13. How can we throw some output in Python?
>>Print("")

Q14. What are operators in Python?
>> Operators are used to define operations between different operands. 

Q15. What is difference between / and // operators?
>>10//2 o/p will be INT value
>>10/2 o/p will be float

Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```
print("iNeuron"*4)

Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
>> val = input()
>> if val%2 == 0:
>>     print("Num is even")

Q18. What are boolean operator?
>> logical operations like: And or !

Q19. What will the output of the following?
```
1 or 0 
>> 1

0 and 0
>> 0
True and False and True
>>Falsse

1 or 0 or 0
>>1
```

Q20. What are conditional statements in Python?
>>if, else, elif

Q21. What is use of 'if', 'elif' and 'else' keywords?
>>if  - check single condition
>>elif - Run if confition inside else
>> else - if codition fails then this will run

Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
>>val = int(input())
>>if age>=18:
>>   print("I can vote")
>>elif age<18:
>>    print("I can't vote")


Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
>>sum([val for val in numbers if val%2 == 0])


Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
>>max(list(map(int, input().split())))


Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
```
>>numbers = [12, 75, 150, 180, 145, 525, 50]
>>lst = []
>>for val in numbers:
>>    if val%5 == 0:
>>        lst.append(val)
>>    if val>150:
>>        pass
>>    if val>500:
>>        break
>>print(lst)
```