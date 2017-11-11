# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:38:13 2016

@author: good
"""
import matplotlib.pyplot as plt
import numpy as np
prosize = [800,1000,1200,1400]
#prosize = [2,3,4,5]
t_serial = [0.81662100000000004, 1.2976240000000001, 1.8690770000000001, 2.5614309999999998]
t_p2=[0.44462699999999999, 0.71340899999999996, 1.0064249999999999, 1.2781629999999999] #2
t_p4=[0.215002, 0.33808500000000002, 0.48510799999999998, 0.66124499999999997] #4
t_p6=[0.14654600000000001, 0.23019899999999999, 0.33264100000000002, 0.44735000000000003] #6
t_p8=[0.111278, 0.17352600000000001, 0.249666, 0.33984199999999998] #8
t_p10=[0.089074, 0.139045, 0.200127, 0.27216600000000002] #10
t_p12=[0.074470999999999996, 0.116005, 0.16676099999999999, 0.22781000000000001] #12

#Overhead
over = [-2.1999999999999993e-05, -0.0003700000000000001, -0.008225, -0.05964500000000003, -0.9725860000000002]
#Speedup of different threads
sp2=[1.8366428489497939, 1.8189061253782897, 1.8571448443748917, 2.0039940132831258] #2
sp4=[3.7982018771918402, 3.8381590428442554, 3.8529090429347694, 3.8736489500865789] #4
sp6=[5.5724550653037275, 5.6369662770038103, 5.6189014583289492, 5.725787414775902] #6
sp8=[7.3385664731573179, 7.4779802450353259, 7.4863097097722564, 7.537123133691539] #8
sp10=[9.1678941105148528, 9.3324031788269988, 9.3394544464265206, 9.4112820851980032] #10
sp12=[10.965624202709781, 11.18593164087755, 11.208118205095916, 11.243716254773714] #12

#Efficiency of different threads
ef2=[0.91832142447489695, 0.90945306268914483, 0.92857242218744585, 1.0019970066415629] #2
ef4=[0.94955046929796005, 0.95953976071106384, 0.96322726073369236, 0.96841223752164474] #4
ef6=[0.92874251088395454, 0.93949437950063508, 0.93648357638815816, 0.95429790246265034] #6
ef8=[0.91732080914466474, 0.93474753062941573, 0.93578871372153205, 0.94214039171144237] #8
ef10=[0.91678941105148526, 0.9332403178826999, 0.93394544464265206, 0.94112820851980028] #10
ef12=[0.91380201689248175, 0.93216097007312915, 0.93400985042465967, 0.93697635456447614] #12


ef2 = np.array(ef2);
ef4 = np.array(ef4);
ef6 = np.array(ef6);
ef8 = np.array(ef8);
ef10 = np.array(ef10);
ef12 = np.array(ef12);


t_serial=np.array(t_serial);


t_p2=np.array(t_p2);
t_p4=np.array(t_p4);
t_p6=np.array(t_p6);
t_p8=np.array(t_p8);
t_p10=np.array(t_p10);
t_p12=np.array(t_p12);


sp2 = np.array(sp2);
sp4 = np.array(sp4);
sp6 = np.array(sp6);
sp8 = np.array(sp8);
sp10 = np.array(sp10);
sp12 = np.array(sp12);
#kp2 = 1/sp2 -  
plt.plot(prosize,sp2, '-o', label = '2 Threads' )
plt.plot(prosize,sp4, '-o',label = '4 Threads')
plt.plot(prosize,sp6, '-o',label = '6 Threads')
plt.plot(prosize,sp8, '-o',label = '8 Threads')
plt.plot(prosize,sp10,'-o', label = '10 Threads')
plt.plot(prosize,sp12, '-o',label = '12 Threads')
#plt.ylim(0.5,6.50);


#plt.plot(prosize , t_serial , '-b' , label = 'Time for serial');
#plt.plot(prosize , t12 , '-r' , label = 'Time for parallel(12 Threads)');

plt.legend(loc='upper left');
plt.title('Speedup Vs Resolution')
plt.xlabel('Resolution (N X N)')
plt.ylabel('Speedup')
plt.show()
plt.figure(2)
plt.plot(prosize,ef2,'-o', label = '2 Threads')
plt.plot(prosize,ef4,'-o', label = '4 Threads')
plt.plot(prosize,ef6,'-o', label = '6 Threads')
plt.plot(prosize,ef8,'-o', label = '8 Threads')
plt.plot(prosize,ef10,'-o', label = '10 Threads')
plt.plot(prosize,ef12, '-o',label = '12 Threads')
#plt.ylim(0.5,6.50);
plt.legend(loc='upper left');
plt.title('Efficiency Vs Resolution')
plt.xlabel('Resolution (N X N)')
plt.ylabel('Efficiency')
plt.show()
plt.figure(3)
plt.plot(prosize,t_p2, '-o',label = '2 Threads')
plt.plot(prosize,t_p4,'-o', label = '4 Threads')
plt.plot(prosize,t_p6, '-o',label = '6 Threads')
plt.plot(prosize,t_p8,'-o', label = '8 Threads')
plt.plot(prosize,t_p10, '-o',label = '10 Threads')
plt.plot(prosize,t_p12, '-o',label = '12 Threads')
plt.plot(prosize,t_serial,'-o', label = 'Serial')
#plt.ylim(0.5,6.50);
plt.legend(loc='upper left');
plt.title('Execution Time in sec Vs Resolution')
plt.xlabel('Resolution (N X N)')
plt.ylabel('Execution Time (sec)')
plt.show()

"""
[10000, 100000, 1000000, 10000000, 100000000]
[4580.0, 45307.0, 455528.0, 4545324.0, 45459784.0]
[4580.0, 45307.0, 455528.0, 4545324.0, 45459784.0]
[0.000237, 0.002954, 0.020792, 0.209382, 1.567748]
[0.000279, 0.00074, 0.005613, 0.048451, 0.297026]
[0.8494623655913978, 3.991891891891892, 3.704257972563692, 4.321520711646818, 5.278150734279153]
Overhead
[-1.1999999999999994e-05, 0.0004940000000000001, -0.003984999999999999, -0.035274, -0.8707440000000002]
Speedup of different threads
[0.5780487804878048, 1.459486166007905, 1.0190658236533843, 1.1530925251813222, 1.1317862139564163]
[0.948, 2.1768607221812823, 1.7554880108071598, 2.0296426978926347, 1.9905332896564507]
[1.1074766355140186, 2.7659176029962547, 1.9639180126570326, 2.9370046709963393, 2.7685521041199426]
[0.8494623655913978, 3.991891891891892, 3.704257972563692, 4.321520711646818, 5.278150734279153]
Efficiency of different threads
[0.2890243902439024, 0.7297430830039525, 0.5095329118266921, 0.5765462625906611, 0.5658931069782082]
[0.237, 0.5442151805453206, 0.43887200270178994, 0.5074106744731587, 0.4976333224141127]
[0.18457943925233644, 0.46098626716604246, 0.3273196687761721, 0.4895007784993899, 0.4614253506866571]
[0.07078853046594981, 0.3326576576576577, 0.30868816438030766, 0.3601267259705682, 0.4398458945232628]
"""