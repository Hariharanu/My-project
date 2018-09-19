def factorial(n):
    m=1
    for i in range(1,n+1):
        m=m*i
    print (m)
def fibonacci(n):
    n1=0
    n2=1
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print(n1)
    else:
        for i in range(n):
            print(n1,end='  ')
            nth = n1 + n2
            n1 = n2
            n2 = nth
def find_gcd(x, y): 
      
    while(y): 
        x, y = y, x % y 
      
    return x 
def gcd(l):
    num1 = l[0] 
    num2 = l[1] 
    gcd = find_gcd(num1, num2) 
    for i in range(2, len(l)):
        gcd = find_gcd(gcd, l[i]) 
    print(gcd)
def find_lcm(num1, num2): 
    if(num1>num2): 
        num = num1 
        den = num2 
    else: 
        num = num2 
        den = num1 
    rem = num % den 
    while(rem != 0): 
        num = den 
        den = rem 
        rem = num % den 
    gcd = den 
    lcm = int(int(num1 * num2)/int(gcd)) 
    return lcm 
      
def lcm(l1):
    num1 = l1[0] 
    num2 = l1[1]
    lcm = find_lcm(num1, num2) 
    for i in range(2, len(l1)): 
        lcm = find_lcm(lcm, l1[i]) 
    print(lcm)
def findvowel(n):
    a=["a","e","i","o","u","A","E","I","O","U"]
    for i in n:
        if i in a:
            print(i,end="")
def findconstant(n):
    a=["a","e","i","o","u","A","E","I","O","U"]
    for i in n:
        if i not  in a:
            print(i,end="")
def countvowel(n):
    a=["a","e","i","o","u","A","E","I","O","U"]
    c=0
    for i in n:
        if i  in a:
            c=c+1
    print(c,end="")
def countconstant(n):
    a=["a","e","i","o","u","A","E","I","O","U"]
    c=0
    for i  in n:
        if i  not in a:
            c=c+1
    print(c,end="")
def primeorcomposite(n):
    if n==1 or n==0:
        print(n,"is neither prime nor composite ")
    if n==2:
        print(n,"is prime number")
    if n>2:
        c=0
        for i in range(2,n):
            if n%i==0:
                c=c+1
                break
        if c==0:
            print(n, "is prime number ")
        else:
            print(n,"is composite number")
def amstrongnumber(n):
	r=len(str(n))
	s=0
	t=n
	while t>0:
		d=t%10
		s=s+d**r
		t=t//10
	if n==s:
		print("yes")
	else:
		print("no")
def Perfectnumber(n):
    sum1=0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n):
        print("yes")
    else:
        print("no")
def strongnumber(Number):
    s= 0
    t = Number
    while(t > 0):
        Factorial = 1
        i = 1
        Reminder = t % 10
        while(i <= Reminder):
            Factorial = Factorial * i
            i = i + 1
        s = s + Factorial
        t = t // 10
    if (s == Number):
        print("yes")
    else:
        print("no")
def celsiustofahrenheit(n):
    f = (n * 1.8) + 32
    print(f)
def sumofnaturalnumbers(n):
	s=0
	for i in range(0,n+1):
		s=s+i
	print(s)
def allprimenumbers(n):
    print("0 and 1 is neither prime nor composite")
    for n in range(2,n+1):
        for i in range(2,n):
            if (n % i) == 0:
                break
        else:
            print(n)
def allcompositenumber(n):
    print("0 and 1 is neither prime nor composite")
    print("2 is prime number")
    for n in range(2,n+1):
        for i in range(2,n):
            if (n % i) == 0:
                print(n)
                break
def kilometerstomiles(n):
    c= 0.621371
    m= n * c
    print(m)
def fahrenheittocelsuis(n):
    c= (n - 32) / 1.8
    print(c)
def milestokilometers(n):
	c= 0.621371
	k = n / c
	print(k)
def decimaltobinary(n):
   if n > 1:
       decimaltobinary(n//2)
   print(n % 2,end = '')
def romantointeger( s):
        romvalue= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        intvalue = 0
        for i in range(len(s)):
            if i > 0 and romvalue[s[i]] > romvalue[s[i - 1]]:
                intvalue += romvalue[s[i]] - 2 * romvalue[s[i - 1]]
            else:
                intvalue += romvalue[s[i]]
        print(intvalue)
       
