#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Prompt 1

name = input('What is your name?')
print("Nice to meet you,", name+'.')


# In[ ]:


#Prompt 2 - Nested If statements

feedback = int(input('How would you rate Ansen from 1-10?'))

if feedback == 10:
    print("Aww you're 10/10 too")

if feedback >10:
    print('Numbers from 1-10 only please!')
    
else:
    if feedback != 10:
        if feedback >=8:
            print("So close! He'll work harder to get to a 10")

        elif feedback < 8 and feedback >= 5:
            print("A lot of work to be done, but Ansen is willing to put in the work")

        elif feedback < 5:
            print("Man...maybe we aren't right for each other")            


# In[ ]:


#Prompt 3 - Regular If statements with string conditions

date = input('Would you want to go on a date with Ansen again? Input only Yes or No').lower()

if date == 'yes':
    print(name+', good decision! Ansen is also on the same page')
    
else:
    print('You might want to reconsider your decision >:[')


# In[ ]:


#Prompt 4 - If & Elifs 

vibes = input('What kind of a date are you feeling? Choose between 1 or 2')

if vibes == '1':
    print (name+ ",you've selected chill vibes")
    print ('*cue OMGKIRBY*')
    
elif vibes == '2':
    print (name+",you've selected drinks")
              
else:
    print('Please re-enter your input. Remember, only choose 1 or 2, this is a basic chatbot')


# In[ ]:


#Prompt 5

when = input('When are you free? Input: dd/mm/yyyy')
print('Cool, Ansen will make time on', when)


# In[ ]:




