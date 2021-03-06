import winsound
import sys
import time
from decimal import *
getcontext().prec=1000	# precision of decimal

'''
musicnum=7
if len(sys.argv)>1:
	musicnum=float(sys.argv[1])
seq=str(Decimal(musicnum).sqrt()).replace('.','')	# sqrt melody
'''
#seq=str(Decimal(1).exp()).replace('.','')	# e melody
seq=str(Decimal( sum(1/Decimal(16)**k * 
          (Decimal(4)/(8*k+1) - 
           Decimal(2)/(8*k+4) - 
           Decimal(1)/(8*k+5) -
           Decimal(1)/(8*k+6)) for k in range(1000)))).replace('.','')	# pi (BBP formula) melody
           
print 'Now play...'
note_list=[0,2,4,5,7,9,11,12 ,14,16]	# major tunes of equal temperament
for num in seq: 
	sys.stdout.write(num)
	num=int(num)
	if num == 0:
		time.sleep(0.200)
	else:
		note = int(2**(note_list[num-1]/12.0)*261)
		winsound.Beep(note,200)
