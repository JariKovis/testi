# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 18:59:32 2019

@author: Jari
"""


import random

state_num = 0
A= 0
B= 0

   
def advance_state_machine(voittaja):
    global A
    global state_num
    global B
    
    if state_num == 0:       # Transition from 0 -0
        if voittaja == 0:
           state_num = 1
           print ("Tulos: 15 - 0")
        else:
            state_num =2
            print ("Tulos: 0 - 15")
    elif state_num == 1:       # Transition from 15 - 0
        if voittaja == 0:
           state_num = 3
           print ("Tulos: 30 - 0")
        else:
            state_num =4
            print ("Tulos: 15 - 15")  
    elif state_num == 2:       # Transition from 0 - 15
        if voittaja == 0:
           state_num = 4
           print ("Tulos: 15 - 15")
        else:
            state_num = 5
            print ("Tulos: 0 - 30")  
    elif state_num == 3:       # Transition from state 0 to state 1
        if voittaja == 0:
           state_num = 6
           print ("Tulos: 40 - 0")
        else:
            state_num = 7
            print ("Tulos: 30 - 15")  
            
    elif state_num == 4:       # Transition from state 0 to state 1
        if voittaja == 0:
           state_num = 7
           print ("Tulos: 30 - 15")
        else:
            state_num = 8
            print ("Tulos: 15 - 30")  
            
    elif state_num == 5:       # Transition from state 0 to state 1
        if voittaja == 0:
           state_num = 8
           print ("Tulos: 15 - 30")
        else:
            state_num = 9
            print ("Tulos: 0 - 40")  
            
    elif state_num == 6:       # Transition from state 0 to state 1
        if voittaja == 0:
           state_num = 10
           A+=1
           print ("Tulos: Voittaja A")
        else:
            state_num = 11
            print ("Tulos: 40 - 15")  
            
    elif state_num == 7:       # Transition from state 0 to state 1
        if voittaja == 0:
           state_num = 11
           print ("Tulos: 40 - 15")
        else:
            state_num = 12
            print ("Tulos: 30 - 30")  
            
    elif state_num == 8:       # Transition from state 0 to state 1
        if voittaja == 0:
           state_num = 12
           print ("Tulos: 30 - 30")
        else:
            state_num = 13
            print ("Tulos: 15 - 40")  
            
    elif state_num == 9:       # Transition from state 0 to state 1
        if voittaja == 0:
           state_num = 13
           print ("Tulos: 15 - 40")
        else:
            state_num = 14
            B+=1
            print ("Tulos: Voittaja B")  
            
    elif state_num == 11:       # Transition from state 0 to state 1
        if voittaja == 0:
           state_num = 10
           A+=1
           print ("Tulos: Voittaja A")
        else:
            state_num = 15
            print ("Tulos: 40 - 30")  
            
    elif state_num == 12:       # Transition from state 0 to state 1
        if voittaja == 0:
           state_num = 15
           print ("Tulos: 40 - 30")
        else:
            state_num = 16
            print ("Tulos: 30 - 40")  
            
    elif state_num == 13:       # Transition from state 0 to state 1
        if voittaja == 0:
           state_num = 16
           print ("Tulos: 30 - 40")
        else:
            state_num = 14
            B+=1
            print ("Tulos: Voittaja B")  
            
    elif state_num == 15:       # Transition from state 0 to state 1
        if voittaja == 0:
           state_num = 10
           A+=1
           print ("Tulos: Voittaja A")
        else:
            state_num = 17
            print ("Tulos: Deuce")  
            
    elif state_num == 16:       # Transition from state 0 to state 1
        if voittaja == 0:
           state_num = 17
           print ("Tulos: Deuce")
        else:
            state_num = 14
            B+=1
            print ("Tulos: Voittaja B")  
            
    elif state_num == 17:       # Transition from state 0 to state 1
        if voittaja == 0:
           state_num = 18
           print ("Tulos: Advantage A")
        else:
            state_num = 19
            print ("Tulos: Advantage B")  
            
    elif state_num == 18:       # Transition from state 0 to state 1
        if voittaja == 0:
           state_num = 10
           A+=1
           print ("Tulos: Voittaja A")
        else:
            state_num = 17
            print ("Tulos: Deuce")  
            
    else :
               # Transition from state 0 to state 1
        if voittaja == 0:
           state_num = 17
           print ("Tulos: Deuce")
        else:
            state_num = 14
            B+=1
            print ("Tulos: Voittaja B")  
            
while A < 6 and B < 6:
    while state_num != 10 and state_num != 14:
        voittaja = random.randint(0,1)
        advance_state_machine(voittaja)
    state_num = 0
print("A: ", A, " B: ", B)