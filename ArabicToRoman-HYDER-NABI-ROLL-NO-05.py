"""
    ==THIS SNIPPNET OF CODE IS USED TO CONVERT THE
    ARABIC NUMBERS TO ROMAN NUMBERS USING PYTHON DICTIONARIES. ==
    THE SUPPORTED NUMBERS ARE FROM 1 TO 3,999,999.
    AUTHOR : HYDER NABI.
"""

""" 
=documentation=
            NOTE: DOCUMENTATION WRITTEN IN THIS BLOCK IS APPROPRIATE TO EVERY BLOCK OF IF STATEMENT
               1. PERFORM THE INTEGER DIVISION OF THE NUMBER BY 10(if number is between 10 - 100 or by 100 if 
                the number is between 100 and 1000 and accordingly to other ranges)TO GET ITS
                FIRST DIGHT (LEFT MOST DIGIT).
                i = number // 10;

                2. MULTIPLY RESULT (i) WITH 10(if number is between 10 - 100 or by 100 if 
                the number is between 100 and 1000 and accordingly to other ranges)
                TO GET ITS PLACE VALUE(WHICH IS USED AS INDEX IN DICTIONAORIES OF THAT PARTICULAR NUMBER)
                i*=10;

                3. PRINT THE INTERMEDIATE RESULT 
                Dictionary_name(i)                
                here print(Tens[str(i)];

                4.CONCATENATE THE RESULT FROM DICTIONARY INTO "Roman" VARIABLE
                roman = roman+tens[str(i)]

                5. PERFORM THE MODULO DIVISIO BY 10(if number is between 10 - 100 or by 100 if 
                the number is between 100 and 1000 and accordingly to other ranges)
                TO REMOVE THIS LEFT MOST DIGIT  FROM THE ORIGINAL NUMBER 
                AND LOOP THROUGH AGAIN UNTIL NUMBER BECOMES LESS THAN 0

                number = number % 10 

"""

"""
    =outputs=
    1.
    Enter the Number in Numeric Form = 56783
    :::::::::::::::::::::::::::::::::::::::::::::
    50000  =  Ḹ
    6000  =  ṽM
    700  =  DCC
    80  =  LXXX
    3  =  III
    :::::::::::::::::::::::::::::::::::::::::::::
    The Roman Equivalent is :
    ḸṽMDCCLXXXIII
    
    2.
    Enter the Number in Numeric Form = 1000000
    :::::::::::::::::::::::::::::::::::::::::::::
    1000000  =  Ṁ
    :::::::::::::::::::::::::::::::::::::::::::::
    The Roman Equivalent is :
    Ṁ
    
    3.
    Enter the Number in Numeric Form = 9453
    :::::::::::::::::::::::::::::::::::::::::::::
    9000  =  Īẋ
    400  =  CD
    50  =  L
    3  =  III
    :::::::::::::::::::::::::::::::::::::::::::::
    The Roman Equivalent is :
    ĪẋCDLIII
"""


#ONES HERE
Ones = {
    '1':'I',
    '2':'II',
    '3':'III',
    '4':'IV',
    '5':'V',
    '6':'VI',
    '7':'VII',
    '8':'VIII',
    '9':'IX'
}
#TENS HERE
Tens = {
    '10':'X',
    '20':'XX',
    '30':'XXX',
    '40':'XL',
    '50':'L',
    '60':'LX',
    '70':'LXX',
    '80':'LXXX',
    '90':'XC'
}
#HUNDREDS HERE
Hundreds = {
    '100':'C',
    '200':'CC',
    '300':'CCC',
    '400':'CD',
    '500':'D',
    '600':'DC',
    '700':'DCC',
    '800':'DCCC',
    '900':'CM'
}
#THOUSANDS HERE
Thousands = {
    '1000':'M',
    '2000':'MM',
    '3000':'MMM',
    '4000':'Īṽ',
    '5000':'ṽ',
    '6000':'ṽM',
    '7000':'ṽMM',
    '8000':'ṽMMM',
    '9000':'Īẋ'
}
#TEN THOUSANDS HERE
TenThousands = {
    '10000':'ẋ',
    '20000':'ẋẋ',
    '30000':'ẋẋẋ',
    '40000':'ẋḸ',
    '50000':'Ḹ',
    '60000':'Ḹẋ',
    '70000':'Ḹẋẋ',
    '80000':'Ḹẋẋẋ',
    '90000':'ẋċ'
}
#LAKHS HERE
Lakhs = {
    '100000':'ċ',
    '200000':'ċċ',
    '300000':'ċċċ',
    '400000':'ċḊ',
    '500000':'Ḋ',
    '600000':'Ḋċ',
    '700000':'Ḋċċ',
    '800000':'Ḋċċċ',
    '900000':'ċṀ'
}
#TEN LAKHS HERE
TenLakhs = {
    '1000000':'Ṁ',
    '2000000':'ṀṀ',
    '3000000':'ṀṀṀ'
}
#ENTER INPUT
number = input("Enter the Number in Numeric Form = ")
number = int(number)
Roman = "";
print(":::::::::::::::::::::::::::::::::::::::::::::")
if number>0 and number< 4000000:
    while number > 0:

        if number in range(1,10):
            print(number, " = ", Ones[str(number)])
            Roman = Roman+Ones[str(number)]
            number = number // 10

        if number in range(10,100):
            i = number // 10
            i = i*10
            print(i, " = ", Tens[str(i)])
            Roman = Roman+Tens[str(i)]
            #MODULO DIVISON
            number = number % 10

        if number in range(100,1000):
            i = number // 100
            i = i*100
            print(i, " = ", Hundreds[str(i)])
            Roman = Roman+Hundreds[str(i)]
            number = number % 100

        if number in range(1000,10000):
            i = number // 1000
            i = i*1000
            print(i," = ",Thousands[str(i)])
            Roman = Roman+Thousands[str(i)]
            number = number % 1000

        if number in range(10000,100000):
            i = number // 10000
            i = i*10000
            print(i," = ",TenThousands[str(i)])
            Roman = Roman+TenThousands[str(i)]
            number = number % 10000
        if number in range(100000,1000000):
            i = number // 100000
            i = i*100000
            print(i," = ",Lakhs[str(i)])
            Roman = Roman+Lakhs[str(i)]
            number = number % 100000
        if number in range(1000000,4000000):
            i = number // 1000000
            i = i*1000000
            print(i," = ",TenLakhs[str(i)])
            Roman = Roman+TenLakhs[str(i)]
            number = number % 1000000
    print(":::::::::::::::::::::::::::::::::::::::::::::")
    print("The Roman Equivalent is :")
    #THE FINAL RESULT
    print(Roman)
else:
    print("Please Validate Your Input Between 1-99999")

