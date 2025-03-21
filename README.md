# DEVOPS-PY-BASIC

## 01_StaticPrgm.py
- A static program in Python refers to a program that does not take user input dynamically during execution and runs with predefined values. 
- It executes deterministically, meaning its behavior is fixed and does not change based on runtime conditions.

## 02_Print_Keyword_List.py
- This program imports the keyword module and prints a list of all reserved keywords in Python.
- Import the keyword module:
- The keyword module provides a list of reserved words in Python.
- Retrieve the keyword list using keyword.kwlist:
- The kwlist attribute in the keyword module contains a list of all Python reserved keywords.
- Reserved keywords are words that have a special meaning in Python and cannot be used as variable names.
- Print the keyword list:
- This will display all Python reserved keywords.

## 03_DataTypes.py
- Python is a dynamically typed programming languages.

## 04_DataType_bool.py
- Here we are dealing with boolean data types.

## 05_IntegralLiteral.py
- Binary number internally convert into decimal automatically.
- Octal number internally convert into decimal automatically.
- Hexadecimal can convert into decimal and then print by the print function.

## 06_IntegerConv.py
- int() can convert any integral value like binary, octal, hexadecimal into decimal.

## 07_FloatConv.py
- float() can convert any integral value like binary, octal, hexadecimal into float.

## 08_ComplexConv.py
- complex() can convert any integral value like binary, octal, hexadecimal into complex. e.g: 10+2j

## 09_ComplexFunc.py
- complex(a,b). Here a will be treated as real number and b will be treated as imaginary number.

## 10_BoolFunc.py
- bool(). Here 0 will be treated as `False` and 1 will be treated as `True`.

## 11_StringConv.py
- Shows how decimal, binary, float, complex , boolean be converted to float.

## 12_dynamicVariable.py
- dynamic variables refer to variables whose data type and value can change during execution.
- Python is a dynamically typed language, meaning that variables do not have fixed types and can be reassigned to different types of data at runtime.

## 13_RunTimeVariable.py
- Binary Conversion. a=int(input("Enter the binary value: "),2) # 101010
- Octal Conversion. b=int(input("Enter the octal value: "),8) # 67
- Hexadecimal Conversion. c=int(input("Enter the hexadecimal value: "),16) # 2E

## 14_BinaryConversion.py
- Decimal to Binary -> Divide the number by 2 and whatever reminder you get -> 0 or 1 take that from bottom to top
- Octal to Binary -> 001(1) 000(0) 010(2) (421 Rule)
- Hexadecimal to Binary -> 1010(a) 1111(f) 0001(1) 0010(2) (8421 Rule)
- Boolean to Binary -> 0b1
- Boolean to Binary -> 0b0

## 15_OctalConversion.py
- Binary to Octal -> right to left -> 101(5) 010(2) 101(5)
- Decimal to Octal -> Keep dividing the number by 8 till your reach the value to 0. While dividing , arrange all the reminders from Bottom to Top
- Hexadecimal to Octal -> 1*16^3 + 0*16^2 + 2*16^1 + 1*16^0=4129 -> Keep dividing by 8 and whatever reminder you get, read teh reminder from bottom to top -> 10041

## 16_HexaConversion.py
- Binary to Hexadecimal
- 01010101 -> Binary to Decimal
- Binary to Decimal -> 0*2^7+1*2^6+0*2^5+ 1*2^4 + 0*2^3 + 1*2^2 + 0*2^1 + 1 *2^0 =85
- Decimal to Hexadecimal -> 85 keep dividing this number by 16, take the reminder from bottom to top.

- Decimal to Hexadecimal -> 102 keep dividing this number by 16, take the reminder from bottom to top.

- Octal to Hexadecimal
- Octal to Decimal -> 1*8^2 + 0*8^1 + 2*8^0 = 66
- Decimal to Hexadecimal -> 66 keep dividing this number by 16, take the reminder from bottom to top.

## 17_PrintingElement.py
- This programme tells how output values in different values.

## 18_Operators.py
- This programme deals with Operators. The various operators in this prgrm: Arthimatic, Assignment and Relational Operator.

## 19_TrnOprt_eg1.py
- Ternary Opertaor
- Write a python programme using conditional operator to find whether the given number is positive or negative

## 20_TrnOprt_eg2.py
- Ternary Opertaor
- Write a python programme to accept the user input to check whether the user is eligible to vote or not

## 21_TrnOprt_eg3.py
- Ternary Opertaor
- Write a python programme to accept the number as input. To check whether the number is even or odd

## 22_TrnOprt_eg4.py
- Ternary Opertaor
- WRITE A PYTHON PROGRAM TO FIND WHICH NUMBER IS BIGGER AMONG THE TWO GIVEN INTEGERS USING CONDITIONAL OPERATOR

## 23_LogicalAnd.py
- Logical AND operator with BOOLEAN, INTEGER, FLOAT, COMPLEX, STRING

## 24_LogicalOr.py
- Logical OR operator with BOOLEAN, INTEGER, FLOAT, COMPLEX, STRING

## 25_LogicalNot.py 
- Logical NOT operator with BOOLEAN, INTEGER, FLOAT, COMPLEX, STRING

## 26_BitWiseOprt.py
- BitWise operator: & (AND), | (or), ^ (XOR), ~ (NOT), << (LEFT SHIFT), >> (RIGHT SHIFT), Special Operator (id, is, is not), Membership Operator (in, not in)

## 27_IfElse.py
- If Else statement example.

## 28_IfElifElse.py
- If Elif Else statement example.

## 29_Usrnm_Psswd.py
- To check if the entered username and password matches or not.

## 30_BllngSys_1.py
- Billing System part 1

## 31_BllngSys_2.py
- Billing System part 2

## 32_EvenOdd.py
- To find the given number is even or odd.

## 33_SmallAmong4.py
- To find the smallest among 4 numbers.

## 34_range.py
- Examples related to range

## 35_even_range.py
- Display list of even number based on the range entered by the user

## 36_odd_range.py
-  Display list of odd number based on the range entered by the user

## 37_even_sum_range.py
- Display SUM of even number based on the range entered by the user

## 38_odd_sum_range.py
- Display SUM of odd number based on the range entered by the user

## 39_NestedForLoop.py
- Nested for loop example.

## 40_NestedForLoop_MultTbl.py
- Nested for loop to generate multiplication table.

## 41_Nfl_SumofPerfectNums.py
- Write a python program to print all perfect numbers from 1 to 100
- Perfect number: Sum of all the factors of the given number excluding itself is equal to given number is called as "Perfect number"
- ex: 48 ==> 1,2,3,4,6,8,12,16,24,48
- 1+2+3+4+6+8+12+16+24+48 ==>78
- 78 == 48 ==> is not a perfect number

## 42_PrimeNumber_break.py
- The programme will generate the rnage of numbers to check which are prime numbers based on the value entered by the user.
- break command was used.

## 43_break.py
- Display range of numbers from 1 to 11 and when it 7 break.

## 44_continue.py
- Display range of numbers from 1 to 11 and when it 7 , it will display all the numbers except for 7.

## 45_printNos_while.py
- Display range of numbers from 1 to 10 using while statement.

## 46_while1.py
- Write a python program to count the number of digits of the given number
- Solution 1: using str() method
- Solution 2: using while() loop and floor division of 10

## 47_while2.py
- Write a python program to reverse a given number.

## 48_palindrome.py
- To check if the given number entered is palindrome or not.

## 49_SumOfDigit.py
- To find the sum of individual digits of a given number.

## 50_ArmstrongNum.py
- To check if a number is an armstrong number of not.

## 51_PalindromeRange.py
- To check the range of numbers from 2 values given by the user and filter out the number is a palindrome or not.

## 52_ArmstrongRange.py
- To check the range of number from 2 values given by the user and filter out the numbers that is armstrong or not.




