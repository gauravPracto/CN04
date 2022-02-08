#!/usr/bin/env python
# coding: utf-8

# In[32]:


'''
type : Class
Name : NormalMessage
Methods : getMessage 
atributes : element , command 
function:class takes element and command and input and have only behaviour function returns a string
'''
class NormalMessage:
    def __init__(self,element , command):
        self.element = element 
        self.command = command 
        
    '''
    this method returns the normal string 
    '''
    def getMessage(self):
        return f"i'm {self.element}! I'm sometimes {self.command}"
'''
type : Class
Name : AbnormalMessage
Methods : getMessage 
atributes : element , command 
function:class takes element and command and input and have only behaviour function returns a string
'''
class AbnormalMessage:
    def __init__(self,element , command):
        self.element = element 
        self.command = command
        
        '''
            this method returns a modified string 
        '''
    def getMessage(self):
        return f"I’m {self.element}! I am {self.command} today"

    
'''
type : Class
Name : ColorGame
Methods : List, subscribeUnsubscribe,printColor,evalInput,printColor
atributes : subscriber , color
function: class define many function to inplement ColorGame
'''
class ColorGame:
    
    '''
    this initialize the subscriber model and set everyone to null later this could be updated using setter
    and has basic color config
    '''
    def __init__(self):
        self.subscriber = {
            "banana":False,
            "ink":False,
            "salt":False,
            "frog":False,
            "blood":False,
            "sky":False,
            "apple":False}
        self.color = {
            "red":["ink","blood","apple"],
            "black":["ink","sky"],
            "yellow":["banana","frog"],
            "green":["apple","banana"],
            "blue":["sky","frog"],
            "white":["salt"]
        }
        
        
    '''
            this will list out all the subscribed items
    '''
    def List(self):
        return [ele for ele in self.subscriber if self.subscriber[ele]]
    
    '''
        this will subscribe or unsubscribe the element given if already subscribed or 
        unsubscribed it will let you know 
    '''
    def subscribeUnsubscribe(self,element , value):
        if self.subscriber[element]==value==True:
            return "already subscribed"
        elif self.subscriber[element]==value==False:
            return "already Unsubscribed"

        self.subscriber[element] = value
        if value:
            return f"subscribing {element}"
        else:
            return f"unsubscribing {element}"
        
    
    '''
    this is a factory function , this takes a command map it and create a message class obj based on the
    command given and return the output array
    '''
    def printColor(self,command):
        outputColors = []
        for element in self.color[command]:
            if self.subscriber[element]:
                if element=="frog":
                    outputColors.append(AbnormalMessage(element,command).getMessage())
                else:
                    outputColors.append(NormalMessage(element,command).getMessage())
        return outputColors
    
    
    '''
    this will evaluate the input based on is it a subscriber string or a color
    ''' 
    def evalInput(self,command):
        if type(command)==str:
            if command=="list":
                return str(self.List())
            if command[0]=="+" and command[1:] in self.subscriber:
                return self.subscribeUnsubscribe(command[1:],True)
            elif command[0]=="-" and command[1:] in self.subscriber:
                return self.subscribeUnsubscribe(command[1:],False)
            elif command[0]=="+" or command[0]=="-":
                return "Invalid Thing Name"
            elif command in self.color:
                return self.printColor(command)
            else:
                return ""
        else:
            return ""
        
    
    
colorGameObj = ColorGame()
print("Whats your command  To exit please write 'exit'")
command = input()
while command!="exit":
    
    if command=='':
        pass
    else:
        result = colorGameObj.evalInput(command.lower().strip())

        if type(result)==list:
            for x in result:
                print(x)
        else:
            print(result)


    command = input()


# In[ ]:





# In[ ]:




