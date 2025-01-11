# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:12:21 2024

@author: Randy
"""
import math
#asking for character to make box out o
character=str(input('Enter frame character ==> ')).strip()
print(character)
#asking for height of box
height=str(input('Height of box ==> ')).strip()
print(height)
#asking for width of box
width=str(input('Width of box ==> ')).strip()
print(width)
w=int(width)
h=int(height)
#creates top and bottom part of box
top_bottom=(character*w)
#creates the text in the frame 
pad=math.floor((w-len(width+'x'+height)-2)/2)
pad2=math.ceil((w-len(width+'x'+height)-2)/2)
stringer=character+' '*pad+width+'x'+height+' '*pad2+character
#creates the top part of the characters between the ceiling of the box and the text
tween1=(character+' '*(w-2)+character+'\n')*(math.floor((h+1)/2-2))
#creates the bottom part of the characters between the floor of the box and the text
tween2=(character+' '*(w-2)+character+'\n')*(math.ceil((h+1)/2-2))
print()
#prints box
print('Box:')
print(top_bottom)
print(tween1,end="")
print(stringer)
print(tween2,end="")
print(top_bottom)

