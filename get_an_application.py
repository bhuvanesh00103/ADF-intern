n=0
user_details = {}
while True:
    d={}
    d['name'] = input('Enter Your Name:- ')
    d['age'] = int(input('Enter Your Age:- '))
    d['gender'] = input('Enter Your Gender(male or female):- ')
    d['salary'] = float(input('Enter Your Salary:- '))
    d['state'] = input('Enter Your State:- ')
    d['city'] = input('Enter Your City:- ')
    try:
        if (not d['name'].isalpha()) or (not str(d['age']).isdigit()) or d['gender'] not in ['male','female']:
            raise Exception
    except Exception:
        print('Enter the Correct Inputs')
    else:
        user_details[n] = d
        n += 1
        if (n == 2): break
print(user_details)