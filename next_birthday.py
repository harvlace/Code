# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:33:42 2023

A program to get the next birthday of an input dob....

@author: Harvey W Lacey
"""
import datetime


#dob_string= input("enter date: ")
def get_next_birthday(dob_string):
    
    dob_date = datetime.datetime.strptime(dob_string, "%d/%m/%Y").date()
    today = datetime.date.today()
    birthday = datetime.date(today.year, dob_date.month, dob_date.day)
    
    if today > birthday:
        birthday = ((today.year + 1), dob_date.month, dob_date.day)
    else:
        birthday = ((today.year), dob_date.month, dob_date.day)
        
    day = str(birthday[2])
    month = str(birthday[1])
    year = str(birthday[0])
    birthday_date = (f"{day}/{month}/{year}")
    next_birthday = datetime.datetime.strptime(birthday_date, "%d/%m/%Y").date().strftime("%d/%m/%Y")
    return(next_birthday)
   # print(birthday[2],"/",birthday[1],"/",birthday[0],sep="")
  

    

         
        
                
   # return(frequencies_dict)


# takes a single string parameter representing someone’s date of birth in the format dd/mm/YYYY

# determines their next birthday

# returns a string representing their next birthday in the format dd/mm/YYYY 

# The function will need to:

# Convert the date of birth into a date object

# Get the current year

# Create a date object for their birthday this year

# If their birthday this year has passed, then

# Create a date object for their birthday next year

# Return the birthday in the form dd/mm/YYYY 