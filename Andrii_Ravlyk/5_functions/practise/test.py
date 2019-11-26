# test
import sys
sys.path.append("E:/Python/ITEA/ITEA-BC/Andrii_Ravlyk/5_functions")
sys.path.append("E:/Python/ITEA/ITEA-BC/Andrii_Ravlyk/5_functions/practise")
sys.path.append("E:/Python/ITEA/ITEA-BC/Andrii_Ravlyk/5_functions/hw")
print(sys.path)
from my_max import fmax as fmax1
from practise import my_len
from find_vowel import fvowel
from hw5 import max_in_list

f=fmax1
print ("======test function fmax========")
print("1 vs 2 ", f(1, 2))
print("3 vs 1 ", f(3, 1))
print("2 vs 2 ", f(2, 2))

print ("======test function flen========")
print("len(abcdefg)", my_len.flen('abcdefg'))
print("len(123)", my_len.flen('123'))
print("len()", my_len.flen(''))

#test map
#s = input('ff/dd')
#a,b,c = map(int,s.split('/'))
#print(f"a{a}b{b}c{c}")
print ("======test function fvowel========")
print ('s',fvowel('s'))
print ('a',fvowel('a'))
print ('b',fvowel('b'))
print ("======test hw5========")
print ("max_in_list 1,3,6,3,5 =", max_in_list(1,3,6,3,5));
print ("max_in_list 1,3,7,3,5,9 =", max_in_list(1,3,7,3,5,9));