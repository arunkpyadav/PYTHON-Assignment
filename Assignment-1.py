#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Assignment 1
#3. Write a program to find the largest number out of three numbers excepted from the user.
#4. Write a program to accept percentages from the user and display the grade:
#         Marks                                    Grade
#         > 90                                         A
#         > 80 and <= 90                               B
#         >= 60 and <= 80                              C
#         below 60                                     D





# In[16]:


#Write a program to find the largest number out of three numbers excepted from the user.

num1=int(input('Enter a number'))
num2=int(input('Enter a number'))
num3=int(input('Enter a number'))
if num1>num2 and num1>num3:
    print(num1,' ',' is greatest them all')
if num2 > num1 and num2 > num3:
    print(num2,' ', 'is greatest them all')
if num3 > num1 and num3 > num2:
    print(num3,' ', 'is greatest them all')


# In[17]:


#4. Write a program to accept percentages from the user and display the grade:
#         Marks                                    Grade
#         > 90                                         A
#         > 80 and <= 90                               B
#         >= 60 and <= 80                              C
#         below 60                                     D

marks=int(input('Enter Your percentage'))
if marks > 90:
    print('Your grade is A')
if marks > 80 and marks <=90:
    print('Your grade is B')
if marks >=60 and marks <=80:
    print('Your grade is C')
if marks < 60:
    print('Your grade is D')



# In[ ]:




