import os
import datetime
import operator
from operator import itemgetter, attrgetter
import sys
finaloutput = []
unique_users = []
path = os.environ.get("LOGDIR")
fileList = os.listdir(path)
for i in fileList:
   file = open(os.path.join(path + i), 'r')
   lines=file.readlines()
   #unique_users=[]
   for x in lines:
    line = x.split(' ')[6]
    if line.count('/') > 2 and line.split('/')[3].split('?', 1)[0] not in unique_users:
       unique_users.append(line.split('/')[3].split('?', 1)[0])
       #unique_users.append(line.split('/')[3])
   file.close()



for j in unique_users:
    path = os.environ.get("LOGDIR")
    fileList = os.listdir(path)
    pages = 0
    sessions = 0
    
    longest = datetime.timedelta(minutes =0)
    shortest = datetime.timedelta(minutes =1)
    tprev = datetime.datetime(2012, 4 ,13)
    for i in fileList:
       file = open(os.path.join(path + i), 'r')
       lines=file.readlines()
       for x in lines:
           if '/' + j + '/' in x.split(' ')[6]:
             tcurrnative = x.split(' ')[3]
             tcurr = datetime.datetime.strptime(tcurrnative, "%d/%b/%Y:%H:%M:%S")
             tnext = tprev + datetime.timedelta(minutes =10)
             pages += 1
             #print (j, tcurr, tprev)
             if tcurr < tnext:
               dcurr = tcurr - tprev
               if dcurr < shortest and dcurr > datetime.timedelta(minutes =0):
                  shortest = dcurr
                  #print (str(shortest))
               elif dcurr > longest:
                  longest = dcurr
               tprev = tcurr
             else:
               sessions += 1
               tprev = tcurr
    print (j, int(pages), sessions, str(longest), str(shortest))
