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

## 45_printNos_while.py (Important)
- Display range of numbers from 1 to 10 using while statement.

## 46_while1.py (Important)
- Write a python program to count the number of digits of the given number
- Solution 1: using str() method
- Solution 2: using while() loop and floor division of 10

## 47_while2.py (Important)
- Write a python program to reverse a given number.

## 48_palindrome.py (Important)
- To check if the given number entered is palindrome or not.

## 49_SumOfDigit.py (Important)
- To find the sum of individual digits of a given number.

## 50_ArmstrongNum.py (Important)
- To check if a number is an armstrong number of not.

## 51_PalindromeRange.py (Important)
- To check the range of numbers from 2 values given by the user and filter out the number is a palindrome or not.

## 52_ArmstrongRange.py (Important)
- To check the range of number from 2 values given by the user and filter out the numbers that is armstrong or not.

## 53_FuncDefinition.py
- This is a simple function call without any parameters passed.

## 54_FuncWithData.py
- This is a simple function call with parameters passed.

## 55_Func_GenerateRange.py
- This is a simple function call without any parameters passed -> if no parameters -> a default value will be taken.
- This is a simple function call with a parameter passed -> use that parameter and get the range.

## 56_Func_ReturnValue.py
- Function call by passing parameters. Each function will return the value.

## 57_Func_FormalAndActualParam.py
- This programme will show what is formal and actual parameter.

## 58_Func_PositionArg.py (Important)
- This programme will show how position argument affects the final result set.

## 59_Func_KeywordArgs.py (Important)
- This programme will show how keyword argument affects the final result set.

## 60_Func_DefaultArgs.py (Important)
- This programme will show how the function will be executed if values are not passed. Provided default values are present in the function.

## 61_Func_VariableLength.py (Important)
- This programme will show a function will accept n number of arguments using variable length parameter.

## 62_stringHandle_1.py
- The programme shows the different way the string is represented. 

## 63_evalMethod.py
- eval() method -> we have to specify the value in single qoutes(''). This is how we enter the value for eval.

## 64_string_lengthOfString.py (Important)
- Length of the string using len method + for loop method.

## 65_string_indexing.py (Important)
- Positive Index -> Forward Access -> Left to right.
- Negative Index -> Backward Acces -> Right to Left.

## 66_slicing.py (Important)
- Programme focuses on string slicing.
- string[start:stop:step]
- start: index to begin the slice (inclusive)
- stop: index to end the slice (exclusive)
- step: how many characters to move forward (default is 1)

## 67_string_concat.py (Important)
- Programme focuses on string concat and string repetition.

## 68_string_strip.py (Important)
- Programme focuses on string strip.
- strip() method in Python is used to remove leading and trailing whitespace (or specified characters) from a string.

## 69_string_find.py (Important)
- Programme focuses on string find().
- find() method in Python is used to search for a substring within a string and returns the index of the first occurrence.
- If the substring is not found, it returns -1.
- string.find(substring, start, end)
- substring: Required. The string to search for.
- start: Optional. The starting index (default is 0).
- end: Optional. The ending index (default is end of string).

## 70_string_replace.py (Important)
- Programme focuses on string replace. 
- replace() method in Python is used to replace occurrences of a substring with another substring.
- string.replace(old, new, count)
- old: The substring you want to replace.
- new: The substring you want to replace it with.
- count (optional): Number of occurrences to replace. If omitted, replaces all.

## 71_string_join.py (Important)
- Programme focuses on string join.
- join() method in Python is used to combine a list (or any iterable) of strings into a single string, using a separator.
- separator.join(iterable)
- separator: The string that will be placed between the elements.
- iterable: The list, tuple, or other iterable of strings to join.

## 72_tuple.py (Important)
- Programme explore tuple.
- Tuple is one of the collection data structure.
- When we want to define a variable with more than one value,
- we can allow to collect like `Tuple`
- Indexing and slicing in tuple
- Looping in tuple
- Convert tuple to list
- Convert list to tuple

## 73_tuple_methods.py (Important)
- Programme focuses on methods of tuple.
- len() ==> used to find the length of the tuple
- count() ==> return the number of occurrences of the specified element within the tuple
- index() ==> to get the index of the specified element, we can use "index()".
- sorted() ==> to sort the tuple, we can use "sorted()"

## 74_string_valid_startswith.py
- Checks whether the string has started with given set of characters or not, to check "startswith()" can be used.

## 75_string_valid_endswith.py
- when we need to check whether the string is ended with specified group of characters or not.

## 76_string_valid_isaplha.py
- Whether the given string is defined with only alphabets or not.

## 77_string_valid_isalnum.py
- whether the given string is with all alphabets and digits or not.

## 78_string_valid_islower.py
- if the string is with only lower case alphabets, islower() can return "True". Otherwise it returns "False".

## 79_string_valid_isupper.py
- When the string with upper case alphabets isupper() ===> True otherwise: isupper() ==> False

## 80_string_valid_isdigit.py
- if the string with digits: isdigit() ==> True otherwise: isdigit() ==> False

## 81_list.py
- using []
- using list()

## 82_list_split.py
- split() method

## 83_list_type.py
- Lists are of 2 types: Homogenous List and Heterogenous List.
- 1.List is ordered.
- 2.Indexing is possible.
- 3.Slicing is also possible.
- 4.List is Homogeneous ==> when the list is defined with same datatype.
- 5.List is Heterogeneous ==> when the list is defined with different datatypes
- 6.List is mutable datatype
- Display the list of elements using positive index.
- Display the list of elements using negative index.

## 84_list_traverse.py
- Traversing the list using positive index and negative index.

## 85_list_func_count.py
- 1.count()
- When we want to count the number of occurrences of each element/specified element in a list we can use count().

## 86_list_func_index.py
- 2.index()
- to find the first occurrence of the specified element in a list, we can use index()

## 87_list_func_append.py
- 3.append()
- when we want to add the element at the last in the list, we can use append()

## 88_list_func_insert.py
- 4.insert()
- When we want to add the element at the specified index/position of the list, we can use insert()

## 89_list_func_remove.py
- 5.remove()
- When we want to remove the specified element from the list, we can use remove().

## 90_list_func_pop.py
- 6.pop()
- When we want to remove the specified element from the list, we can use pop().

## 91_list_func_reverse.py
- 7.reverse()
- When we want to reverse the list we use

## 92_list_func_sort.py
- 8.sort()
- When we want to sort the list we use sort()

## 93_set.py
- #Set Data Structure:
- () ==> allows duplication
- [] ==> allows duplication
- {} ==> not allows the duplication
- 1) When we need to create the data structure which is not with any duplication then, we can use the set.
- 2) set can be defined with {} all the elements {} must be separate with comma.
- 3) set can possible to define homogeneous elements and with heterogeneous elements also.
- 4) Set is also the pre-defined data, so we have a pre-defined class named as "set".
- Is set ordered data -> Not ordered.
- indexing is not possible.
- slicing also not possible.
- Is set mutable or immutable -> Mutable

## 94_set_add.py
- add():
- if you want to add only one element to the set at any random position, we can use "add()".
- set-data.add(element)

## 95_set_update.py
- update():
- when we want to add more than one element to the set, we can use "update()"
- set-data.update([e1, e2, e3,...])

## 96_set_pop.py
- pop():
- pop() can remove any element randomly from the set.
- set-data.pop()

## 97_set_remove.py
- remove():
- when we want to remove the specified element from the set we can use "remove()".
- set-data.remove(element)
- if the specified element is not in the set, remove() can give "key error".

## 98_set_discard.py
- discard():
- also remove the specific element from the set.
-	set-data-name.discard(element)
- No math operations like concatenation and repetition allowed on  sets.

## 99_dict.py
- When we want to create the data structures with key-value pairs, we can use "dictionaries".
- dictionary-name = {key1 : val1, key2 : val2, ......}
- Ex: Web application
- registration form
-	user-name : xxxxxx
-	mobile: xxxxxx
-	age : xxx
- Dictionary is also a pre-defined data structure because it has pre-defined class "dict".
- How to access dictionary elements:
- no index is possible to access the dictionary.
- to access the dictionary elements, we can use "keys".
- Syntax:
-	dictionary-name[key]
- Is dictionary ordered -> Yes
- Is dictionary mutable or immutable -> mutable

## 100_dict_len.py
- len():
- to get the length of the dictionary, we can use "len()"

## 101_dict_get.py
- get():
- i) when we want to access any value of the dictionary with respect to the key, we can use "get()".
- dictionary-name.get(key)
- ii) When we want to set new default value for any existing key of the dictionary, we can use get().
- But if the specified key is already existed with some value, then we can get with existed value. Otherwise we can get the specified key with default value.
- Syntax:
-	dictionary-name.get(key, default-value)

## 102_dict_keys_values.py
- keys()
- dictionary-name.keys()
- values()
- dictinary-name.values()
- Note:
- In dictionary:
-	keys ==> unique
-	values ==> unique or duplicate

## 103_dict_items.py
- items():
- Syntax:
-	dictionary-name.items()

## 104_dict_popitem.py
- popitem():
- Syntax:
-	d.popitem()
- In Python dictionaries, keys must be unique. 
- If the same key appears more than once, the last occurrence overwrites the earlier ones.

## 105_MyClassAndMyObject.py
- A class is like a blueprint or template for creating objects. It defines properties (variables) and behaviors (functions/methods)
- that the objects created from the class will have.
- An object is an instance of a class. It is created using the class blueprint and holds actual data.
- This programme focus on how to create class and its attributes
- Create objects from the class and access the attribute value.

## 106_StudentAndMethod_no_params.py
- This progamme will teach how to create class and method with no parameter.
- Create object from the class and call the method using that object

## 107_StudentAndMethod_yes_params.py
- This progamme will teach how to create class and method with parameter.
- Create object from the class and call the method by passing parameter.

## 108_CalculaotrAndMethod_ReturnType.py
- This programme will teach how to create class and method with return type.
- Create object from the class with return type.

