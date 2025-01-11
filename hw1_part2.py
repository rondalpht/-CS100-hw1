# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:00:14 2024

@author: Randy
"""
import math
#inputs minutes
minutes=(input('Minutes ==> '))
print(minutes)
#inputs seconds
seconds=(input('Seconds ==> '))
print(seconds)
#inputs miles
miles=(input('Miles ==> '))
print(miles)
#inputs Targetmiles
targetMiles=(input('Target Miles ==> '))
print(targetMiles)
print()
#converts to int and floats for equations
minutes=int(minutes)
seconds=int(seconds)
miles=float(miles)
targetMiles=float(targetMiles)
#calclates runtime to minutes
runTime=float(minutes+seconds/60)
#calculates minute pace
minPace=int(runTime/miles)
#calculates second pace
secPace=int(((runTime*60)/miles)%60)
#calculates speed
speed=miles/((minutes*60+seconds)/3600)
#used to find how long it would take to run target miles 
timeTarget=targetMiles/(speed)*3600
#prints out facts regarding running times
print('Pace is ' +str(int(minPace))+' minutes and '+str(int(secPace))+' seconds per mile.')
print('Speed is '+"{:.2f}".format(speed)+' miles per hour.')
print('Time to run the target distance of '+"{:.2f}".format(targetMiles)+' miles is '+str(round(timeTarget//60))+' minutes and '+ "{}".format(int(timeTarget%60))+' seconds.')