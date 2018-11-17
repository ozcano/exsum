# -*- coding: utf-8 -*-
''' Created on Tue Oct 23 20:17:52 2018
@author: Onur Y. Ozcan <http://ozcan.io> '''

# Test cases

t_assistant_names = ('Ali Ozturk','Arzu Hakan','Ayse Gungor','Cem Cesur','Mehmet Celik','Meral Vardar')

t_assistant_schedule = {
    'Ali Ozturk' : 'R,Teaching CEV 202,MON,1030,1230;R,Teaching CEV 202,TUE,1430,1630;R,Teaching CEV 202,WED,1330,1530;R,Teaching CEV 202,THU,930,1230;R,Teaching CEV 202,FRI,1330,1730;I,Conference,MON,ALL_DAY,12.11.2018;I,Conference,TUE,ALL_DAY,13.11.2018;I,Conference,WED,ALL_DAY,14.11.2018;I,Conference,THU,ALL_DAY,15.11.2018;I,Conference,FRI,ALL_DAY,16.11.2018',
    
    'Arzu Hakan' : 'R,Teaching CEV 202,TUE,1330,1630;R,Teaching CEV 202,WED,1030,1230;R,Teaching CEV 202,WED,1330,1530;R,Teaching CEV 202,FRI,930,1130;R,Teaching CEV 202,FRI,1330,1530;I,Doctor\'s appointment,THU,1330,1730,22.11.2018',
    
    'Ayse Gungor' : 'R,Teaching CEV 202,MON,930,1230;R,Teaching CEV 202,MON,1330,1530;R,Teaching CEV 202,WED,1330,1530;R,Teaching CEV 202,WED,930,1230;R,Teaching CEV 202,FRI,930,1130',
    
    'Cem Cesur' : 'R,Teaching CEV 202,MON,1330,1530;R,Teaching CEV 202,THU,1030,1230;R,Teaching CEV 202,THU,1430,1630;R,Teaching CEV 202,FRI,930,1130;R,Teaching CEV 202,FRI,1330,1530',
    
    'Mehmet Celik' : 'R,Teaching CEV 202,WED,930,1230;R,Teaching CEV 202,WED,1430,1630;R,Teaching CEV 202,THU,930,1230;R,Teaching CEV 202,THU,1330,1530;R,Teaching CEV 202,FRI,930,1130',
    
    'Meral Vardar' : 'R,Teaching CEV 202,MON,1130,1330;R,Teaching CEV 202,TUE,930,1030;R,Teaching CEV 202,WED,1030,1230;R,Teaching CEV 202,THU,1330,1530;R,Teaching CEV 202,FRI,930,1230'
}

print(t_assistant_schedule['Ali Ozturk'])

# using 'with ... as' closes any open files automatically
# when the code block is done
filepath = 'input/assistants.txt'
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        print("Line {} : {}".format(cnt, line))
