# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:38:13 2016

@author: good
"""
import matplotlib.pyplot as plt
import numpy as np
maxIteration = [100, 1000, 10000, 100000]
prosize = [2,3,4,5]
t_serial = [0.192104, 1.030823, 9.156345, 89.837565]
t_p2=[0.091678, 0.553099, 4.610147, 45.843086] #2
t_p4=[0.036773, 0.244734, 2.316362, 23.014105] #4
t_p6=[0.027131, 0.180098, 1.696166, 16.803785] #6
t_p8=[0.02094, 0.143086, 1.325095, 13.211088] #8
t_p10=[0.0179, 0.117634, 1.099393, 10.890836] #10
t_p12=[0.015342, 0.101195, 0.947121, 9.400603] #12
#Overhead
over = [-2.1999999999999993e-05, -0.0003700000000000001, -0.008225, -0.05964500000000003, -0.9725860000000002]
#Speedup of different threads
sp2=[2.095420929775955, 1.863722407742556, 1.9861286418849549, 1.9596753368654107] #2
sp4=[5.224050254262639, 4.212013859945901, 3.952898985564433, 3.9035871696944113] #4
sp6=[7.080608897571044, 5.723678219635976, 5.398259958046559, 5.346269605329989] #6
sp8=[9.174021012416427, 7.204219839816615, 6.90995362596644, 6.800163998604808] #8
sp10=[10.732067039106145, 8.762968189469031, 8.328545843024287, 8.248913582024374] #10
sp12=[12.521444400990744, 10.18650130935323, 9.667555676624211, 9.556574721855608] #12

#Efficiency of different threads
ef2=[1.0477104648879776, 0.931861203871278, 0.9930643209424774, 0.9798376684327054] #2
ef4=[1.3060125635656596, 1.0530034649864752, 0.9882247463911082, 0.9758967924236028] #4
ef6=[1.1801014829285073, 0.9539463699393292, 0.8997099930077598, 0.8910449342216649] #6
ef8=[1.1467526265520533, 0.9005274799770768, 0.863744203245805, 0.850020499825601] #8
ef10=[1.0732067039106146, 0.8762968189469031, 0.8328545843024286, 0.8248913582024373] #10
ef12=[1.0434537000825619, 0.8488751091127692, 0.8056296397186843, 0.7963812268213006] #12


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
plt.title('Speedup Vs Max. Iterations per pixel')
plt.xlabel('Iterations(log scale)')
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
plt.title('Efficiency Vs Max. Iterations per pixel')
plt.xlabel('Iterations(log scale)')
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
plt.title('Execution Time in sec Vs Max. Iterations per pixel')
plt.xlabel('Iterations(log scale)')
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
