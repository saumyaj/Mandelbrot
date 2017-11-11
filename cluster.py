#!/usr/bin/env python
import subprocess
#import matplotlib.pyplot as plt

init = 10
# Running the codes

time_serial=[]
size=[]
val_serial = []
print "This is Serial Execution"
for i in range(1,5):
	
	#size.append(init)			
	init = init *10
	subprocess.call(["gcc","-fopenmp","serial.c","-lm"])	
	cmd = ["./a.out",str(init),str(1)]
	output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
	print output
	time_serial.append(float(output.split(' ')[0]))
	#val_serial.append(float(output.split(' ')[0]))


time_parallel=[]
badi_list=[]
#val_parallel=[]
init = 10
probsize = [100,1000,10000,100000]
threadarr = [2,4,6,8,10,12]

print "This is Parallel Execution"
subprocess.call(["gcc","-fopenmp","parallel.c","-lm"])
for i in range(0,len(threadarr)):			
	n_thread = threadarr[i]
	print "Number of threads are "+str(threadarr[i])
	temp=[]
	for j in range(0,len(probsize)):
		print "probsize is " + str(probsize[j])	
		cmd = ["./a.out",str(probsize[j]),str(threadarr[i])]
		output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
		print output
		#badi_list.append(float(output.split(' ')[1]))
		temp.append(float(output.split(' ')[0]))
			#val_parallel.append(float(output.split(' ')[0]))
	time_parallel.append(temp)
			


	
print size
#print val_serial
#print val_parallel
print time_serial

speedup =[]
efficiency =[]
#calculating speedup
for j in range(0,len(threadarr)):
	temp = []
	for k in range(0,len(time_parallel[j])):
		temp.append(time_serial[k]/time_parallel[j][k])
	speedup.append(temp)
	#print "speedup for "+str(threadarr[j]) + " " + str(temp)
	newList = [x / threadarr[j] for x in temp]
	efficiency.append(newList)
	#print "efficiecy for "+str(threadarr[j]) + " " +str(newList)



print "parallel time"
for i in range(0,len(time_parallel)):
	print str(time_parallel[i]) + " #" + str(threadarr[i])


print "SPEEDUP"
for i in range(0,len(speedup)):
	print str(speedup[i]) + " #" + str(threadarr[i])


print "EFFICIENCY"
for i in range(0,len(efficiency)):
	print str(efficiency[i]) + " #" + str(threadarr[i]) 
#overhead=[]
speedup2=[]
speedup4=[]
speedup6=[]
speedup12=[]
eff2=[]
eff4=[]
eff6=[]
eff12=[]

'''for j in range(0,5):
	overhead.append(time_serial[j]-badi_list[j*5])
	speedup2.append(time_serial[j]/badi_list[j*5 + 1])
	eff2.append(speedup2[j]/2)
	speedup4.append(time_serial[j]/badi_list[j*5 + 2])
	eff4.append(speedup4[j]/4)
	speedup6.append(time_serial[j]/badi_list[j*5 + 3])
	eff6.append(speedup6[j]/6)
	speedup12.append(time_serial[j]/badi_list[j*5 + 4])
	eff12.append(speedup12[j]/12)

print "Overhead"
print overhead
print "Speedup of different threads"
print speedup2
print speedup4
print speedup6
print speedup12
print "Efficiency of different threads"
print eff2
print eff4
print eff6
print eff12
plt.plot(speedup, size)
plt.plot()
plt.xlabel('Problem Size')
plt.ylabel('Speedup')
plt.show()
"""
'''
