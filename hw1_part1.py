# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:13:22 2024

@author: Randy
"""
#Creates madlib
madlib='Good morning <proper name>!\n\n  This will be a/an <adjective> <noun>! Are you <verb> forward to it?\n  You will <verb> a lot of <noun> and feel <emotion> when you do.\n  If you do not, you will <verb> this <noun>.\n\n  This <season> was <adjective>. Were you <emotion> when <team-name> won\n  the <noun>?\n\n  Have a/an <adjective> day!'
print('Let\'s play Mad Libs for Homework 1')
print('Type one word responses to the following:\n')
#Ask's for word to input into Madlib
name = input('proper_name ==> ').strip()
print(name)
adj1=input('adjective ==> ').strip()
print(adj1)
noun1=input('noun ==> ').strip()
print(noun1)
verb1=input('verb ==> ').strip()
print(verb1)
verb2=input('verb ==> ').strip()
print(verb2)
noun2=input('noun ==> ').strip()
print(noun2)
emo1=input('emotion ==> ').strip()
print(emo1)
verb3=input('verb ==> ').strip()
print(verb3)
noun3=input('noun ==> ').strip()
print(noun3)
season=input('season ==> ').strip()
print(season)
adj2=input('adjective ==> ').strip()
print(adj2)
emo2=input('emotion ==> ').strip()
print(emo2)
teamname=input('team-name ==> ').strip()
print(teamname)
noun4=input('noun ==> ').strip()
print(noun4)
adj3=input('adjective ==> ').strip()
print(adj3)
print()
#replaces words in Madlib
madlib=madlib.replace('<proper name>',name)
madlib=madlib.replace('<adjective>',adj1,1)
madlib=madlib.replace('<noun>',noun1,1)
madlib=madlib.replace('<verb>',verb1,1)
madlib=madlib.replace('<verb>',verb2,1)
madlib=madlib.replace('<noun>',noun2,1)
madlib=madlib.replace('<emotion>',emo1,1)
madlib=madlib.replace('<verb>',verb3,1)
madlib=madlib.replace('<noun>',noun3,1)
madlib=madlib.replace('<season>',season)
madlib=madlib.replace('<adjective>',adj2,1)
madlib=madlib.replace('<emotion>',emo2,1)
madlib=madlib.replace('<team-name>',teamname,1)
madlib=madlib.replace('<noun>',noun4,1)
madlib=madlib.replace('<adjective>',adj3,1)
print('Here is your Mad Lib...')
print()
#prints madlib
print(madlib.strip())

