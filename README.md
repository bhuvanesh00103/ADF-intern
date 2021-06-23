# ADF-Day1
Ex-1 :- uniquewords_from_file.py
Q :- Program to read a file and store the unique words in a list sorted based on the length of word in a new file along with each word length appended to it.
    1. input.txt file has been opened with write mode (file.open('input.txt','w')), some text content has been wrote into the file using file.write('') and then closed the file using file.close().
    2. input.txt file has been opened with read mode (file.open('input.txt','r')), each words in the file had been stored in list.
    3. closing the input.txt file.
    4. removing duplicates from the list by using method (find_unique_words).
    5. sorting the list based on length of the word.(by using list method 'l.sort(key=len)')
    6. opening output.txt with append mode and writing the word with its length into the file.
    7. closing the file output.txt.

Ex-2 :- read_CSV.py
Q :- Program to read a CSV (CSV with n number of columns) and store it in DICT of list.
    1. importing pandas library.
    2. reading the csv file using pandas.read_csv(filename) and selecting n columns using iloc[:,:n]
    3. converting the csv file read into dict of list (dataframe.to_dict('list'))

Ex-3 :- PrimeNumber.py
Q :- Program to Print all Prime Numbers in an Interval of 5 seconds
    1. Getting a number 'n', prime numbers in the range 2 to n will be get printed.
    2. ranging from 2 to n and checking for prime or not using user-defined method (prime).
    3. if ranged number is prime, then delaying for 5secs and print the number.

Ex-4 :- gcd.py
Q :- Program to Find HCF or GCD
    1. Getting the numbers.
    2. Passing the numbers into the method gcd(a,b).
    3. Calling the method recursively gcd(b,a%b) with condition b!=0.
    4. When b==0 returning a which is GCD of a,b.

Ex-5 :- dec_to_bin,oct,hex.py
Q :- Program to Convert Decimal to Binary, Octal and Hexadecimal
    1. Converting Decimal to Binary, Octal and Hexadecimal using in-built methods bin(),oct(),hex() respectively.

Ex-6 :- char_to_ascii.py
Q :- Program to Find ASCII Value of Character.
    1. if input value is single character then converting it to ascii value using the method ord(), else throwing exception.

Ex-7 :- get_an_application.py
Q :- Program to get an application (name , age , gender, salary, state, city)
    1. Getting the values for the given field using input() and typecasting to respective type.
    2. storing the data into user_details dictionary.