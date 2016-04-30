courses = { 'software' : 1 , 'hardware' : 1, 'music' : 2, 'philosophy' : 3}
grade = { 'A' : 5, 'B' : 4, 'C' : 3, 'D' : 2, 'E' : 1, 'F':0 }
results = { 'software': None,'hardware':None ,'music': None , 'philosophy': None }
results['software'] = raw_input ('what did you get in software\n')
results['hardware'] = raw_input ('what did you get in hardware\n')
results['music'] = raw_input ('what did you get in music\n')
results['philosophy'] = raw_input ('what did you get in philosophy\n')

GP = ((courses['software'] * grade[results['software']]) +
      (courses['hardware'] * grade[results['hardware']]) +
      (courses['music'] * grade[results['music']]) +
      (courses['philosophy'] * grade[results['philosophy']]))  / (courses ['software'] + courses ['hardware'] + courses ['music'] + courses ['philosophy'] )

print GP






