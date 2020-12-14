Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> # Part 1
def fibonnaci(n):     
    if n==1:
            return 1
    elif n==2:
            return 1
    
    else:
            return (fibonacci(n-1)+fibonacci(n-2))

# Part 2        
def gcd(x,y):
    if y==0:
            return x
    
    else:   
            return (gcd(y, x%y))
        
# Part 3 
def compareTo(s1,s2):        
                
        if (len(s1) == 0 and len(s2) == 0):
                return 0
        
        elif (ord(s1[0]) < ord(s2[0])):
                return (-(ord(s2[0])))
        
        elif (orf(s1[0]) > ord(s2[0])):
                return (abs(ord(s1[0])))
        
        elif (s1[1:2] == '' and s2[1:2] == ''):
                return 0
        
        else:
                return compareTo(s1[1:], s2[1:])
