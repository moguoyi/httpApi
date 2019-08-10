#!/usr/bin/env python3
def palindrome(s):
   return s==s[::-1]
if _name_=='_main_':
   s=input("Enter a sting:")
   if palindrome(s):
      print("you are ok")
   else:
     print("oh no not")
