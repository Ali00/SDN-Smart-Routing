#Created By Ali Malik 
import zmq
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink
#----
import sys
import fnss
import random
import sched
import time
from threading import Thread
import math
import numpy as np
from threading import Timer
from collections import defaultdict
import datetime
from random import randint
import networkx as nx, igraph as ig
import pylab as plt
from collections import Counter
from itertools import tee, izip
import string
import heapq
#-------------------------------------------------------------------------------
#context = zmq.Context()
#socket = context.socket(zmq.REQ)
#socket.connect("tcp://localhost:5556")

net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )
G = nx.Graph()
Global_Failure_Counter=0  # Global counter to keep the number of all links failure

def topology():

        global net

        # Add hosts and switches 
        #h1= net.addHost( 'h1', mac="00:00:00:00:00:01" )
        #h2 = net.addHost( 'h2', mac="00:00:00:00:00:02" )
        S1 = net.addSwitch( 's1')
        S2 = net.addSwitch( 's2')
        S3 = net.addSwitch( 's3')
        S4 = net.addSwitch( 's4')
        S5 = net.addSwitch( 's5')
        S6 = net.addSwitch( 's6')
        S7 = net.addSwitch( 's7')
        S8 = net.addSwitch( 's8')
        S9 = net.addSwitch( 's9')
        S10 = net.addSwitch( 's10')
        S11 = net.addSwitch( 's11')
        S12 = net.addSwitch( 's12')
        S13 = net.addSwitch( 's13')
        S14 = net.addSwitch( 's14')
        S15 = net.addSwitch( 's15')
        S16 = net.addSwitch( 's16')
        S17 = net.addSwitch( 's17')
        S18 = net.addSwitch( 's18')
        S19 = net.addSwitch( 's19')
        S20 = net.addSwitch( 's20')
        S21 = net.addSwitch( 's21')
        S22 = net.addSwitch( 's22')
        S23 = net.addSwitch( 's23')
        S24 = net.addSwitch( 's24')
        S25 = net.addSwitch( 's25')
        S26 = net.addSwitch( 's26')
        c0 = net.addController( 'c0', controller=RemoteController, ip='127.0.0.1', port=6633 )

        # Add links (42 Links in the US_Topology) 

        #10
        net.addLink (S1, S25)
        net.addLink (S1, S3)
        net.addLink (S1, S21)
        net.addLink (S2, S8)
        net.addLink (S2, S18)
        net.addLink (S2, S23)
        net.addLink (S2, S4)
        net.addLink (S2, S7)
        net.addLink (S3, S21)
        net.addLink (S3, S22)
        #10
        net.addLink (S4, S19)
        net.addLink (S4, S10)
        net.addLink (S5, S8)
        net.addLink (S5, S9)
        net.addLink (S5, S24)
        net.addLink (S5, S25)
        net.addLink (S6, S24)
        net.addLink (S6, S19)
        net.addLink (S7, S9)
        net.addLink (S7, S19)
        #10
        net.addLink (S8, S17)
        net.addLink (S8, S14)
        net.addLink (S9, S24)
        net.addLink (S9, S19)
        net.addLink (S10, S20)
        net.addLink (S10, S26)
        net.addLink (S10, S11)
        net.addLink (S11, S12)
        net.addLink (S11, S23)
        net.addLink (S12, S20)
        #10
        net.addLink (S12, S23)
        net.addLink (S13, S17)
        net.addLink (S13, S18)
        net.addLink (S13, S15)
        net.addLink (S14, S17)
        net.addLink (S14, S22)
        net.addLink (S15, S17)
        net.addLink (S16, S24)
        net.addLink (S16, S25)
        net.addLink (S18, S23)
        #2
        net.addLink (S20, S26)
        net.addLink (S22, S25)

        # Build The Network 
        net.build()
        c0.start()
        S1.start(  [c0] )
        S2.start(  [c0] )
        S3.start(  [c0] )
        S4.start(  [c0] )
        S5.start(  [c0] )
        S6.start(  [c0] )
        S7.start(  [c0] )
        S8.start(  [c0] )
        S9.start(  [c0] )
        S10.start(  [c0] )
        S11.start(  [c0] )
        S12.start(  [c0] )
        S13.start(  [c0] )
        S14.start(  [c0] )
        S15.start(  [c0] )
        S16.start(  [c0] )
        S17.start(  [c0] )
        S18.start(  [c0] )
        S19.start(  [c0] )
        S20.start(  [c0] )
        S21.start(  [c0] )
        S22.start(  [c0] )
        S23.start(  [c0] )
        S24.start(  [c0] )
        S25.start(  [c0] )
        S26.start(  [c0] )

        #print "*** Running CLI"
        #CLI( net )

        #print "*** Stopping network"
        #net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
    #Topology Graph
    G.add_edges_from([(1, 25), (1, 3), (1, 21), (2, 8), (2, 18), (2, 23), (2, 4), (2, 7), (3, 21)
                       , (3, 22), (4, 19), (4, 10), (5, 8), (5, 9), (5, 24), (5, 25), (6, 24), (6, 19), (7, 9), (7, 19)
                       , (8, 17), (8, 14), (9, 24), (9, 19), (10, 20), (10, 26), (10, 11), (11, 12), (11, 23), (12, 20), (12, 23)
                       , (13, 17), (13, 18), (13, 15), (14, 17), (14, 22), (15, 17), (16, 24), (16, 25), (18, 23), (20, 26), (22, 25)])

    Nodes= nx.nodes(G)
    Edges= nx.edges(G)
    print 'The nodes are', Nodes
    print 'The edges are', Edges

    #Dictionary of switches to return --> e.g.  Link (1,2) --> (s1, s2)
    Switches_Dictionary = { (1): 's1', (2): 's2', (3): 's3',(4): 's4', (5): 's5', (6): 's6',
                           (7): 's7', (8): 's8', (9): 's9', (10): 's10', (11): 's11', (12): 's12', (13): 's13', (14): 's14',
                           (15): 's15', (16): 's16', (17): 's17', (18): 's18', (18): 's18', (19): 's19', (20): 's20', (21): 's21',
                           (22): 's22', (23): 's23', (24): 's24', (25): 's25', (26): 's26'}
    #Link's Length Dictionary
    Links_Lengths_Dictionary = { (1, 25): 668, (1, 3): 216, (1, 21): 223, (2, 8): 992,
                                 (2, 18): 362, (2, 23): 918, (2, 4): 1067, (2, 7): 383, (3, 21): 306,
                                 (3, 22): 327, (4, 19): 897, (4, 10): 597, (5, 8): 405, (5, 9): 371,
                                 (5, 24): 265, (5, 25): 423, (6, 24): 571, (6, 19): 663, (7, 9): 581,
                                 (7, 19): 350, (8, 17): 346, (8, 14): 546, (9, 24): 422, (9, 19): 383,
                                 (10, 20): 599, (10, 26): 1127, (10, 11): 584, (11, 12): 368, (11, 23): 937,
                                 (12, 20): 559, (12, 23): 1127,(13, 17): 683, (13, 18): 511, (13, 15): 1077,
                                 (14, 17): 364, (14, 22): 531,(15, 17): 976, (16, 24): 381,(16, 25):145,
                                 (18, 23): 1085, (20, 26): 1094, (22, 25): 489}
    #-------------------------------------------------------------------------------------------------------------
    #generate the gamma parameter for all the links in the network topology
    Gama = []
    #for i in range (len(Edges)):
        #Gama.append(random.uniform(0.01, 0.05))
    x = len(Edges)
    Gama = np.random.uniform(0.002, 0.006, x)
    print 'The links Gama is :\n', Gama
    #-------------------------------------------------------------------------------------------------------------
    print 'The minimum Length in the dictionary is:'
    print Links_Lengths_Dictionary[min(Links_Lengths_Dictionary, key=lambda k: Links_Lengths_Dictionary[k])]
    #-------------------------------------------------------------------------------------------------------------
    #Now, We will compute the MTBF value of each link in this topology...
    #Through the formuls -->  MTBF_link[i]= (CC_link[i]*365*24)/Lenght of link[i],      where CC=Cable_Cut
    minimum = Links_Lengths_Dictionary[min(Links_Lengths_Dictionary, key=lambda k: Links_Lengths_Dictionary[k])]
    cc=[]
    for i in range (len(Edges)):
       cc.append((Links_Lengths_Dictionary[Edges[i]] / minimum))
    print "The cable cut per year \n", cc
    #-------------------------------------------------------------------------------------------------------------
    MTBF=[]
    for i in range (len(Edges)):
        MTBF.append((cc[i]*365*24)/Links_Lengths_Dictionary[Edges[i]])
    print "The MTBF of each link: \n", MTBF
    #-------------------------------------------------------------------------------------------------------------
    MTTR=[]
    Length_Sum=0
    #for i in range (len(Edges)):
        #Length_Sum= Length_Sum + Links_Lengths_Dictionary[Edges[i]]
    #print 'The Total length is :', Length_Sum
    for i in range (len(Edges)):
        #MTTR.append (round(float(Links_Lengths_Dictionary[Edges[i]]) / (float (Length_Sum)) *100))
        #MTTR.append (float(Links_Lengths_Dictionary[Edges[i]]) / (float (Length_Sum))) # stopped currently
        mttr = (round(Links_Lengths_Dictionary[Edges[i]] * Gama[i]))
        if mttr < 1:
           mttr = 1
        MTTR.append (mttr)
        #MTTR.append (round(Links_Lengths_Dictionary[Edges[i]] * Gama[i]))
    print "The MTTR of each link: \n", MTTR
    #-------------------------------------------------------------------------------------------------------------
    class PriorityQueue:
          def __init__(self):
              self._queue = []
              self._index = 0

          def push(self, item, priority):
              heapq.heappush(self._queue, (priority, self._index, item)) # (-priority) for highest first
              self._index += 1

          def pop(self):
              return heapq.heappop(self._queue)[-1]

          def isEmpty(self):
              return self._queue == []

          def size(self):
              return len(self._queue)
    #--------------------------------------------------------------------------------------------------------------
    q = PriorityQueue() # Object of priorityQueue class
    #--------------------------------------------------------------------------------------------------------------

    #Implement the Links to define network links with different parameters
    class Links(object):

          def __init__(self, ID=None, Name=None, Length=None, MTBF=None, MTTR=None, Next_Failure=None,  F_Count=None, P_Failure=None,  Link_state=None):
              self.ID = ID                      # Link's ID e.g. (node1, node2)
              self.Name = Name                  # Link's name (e.g. 0 , 1, etc.)
              self.Length = Length              # Link's length
              self.MTBF = MTBF                  # Mean Time Between Failure
              self.MTTR = MTTR                  # Mean Time To Recover
              self.Next_Failure = Next_Failure  # Time To failure event
              self.F_Count= F_Count             # Lcal Counter of link failure 
              self.P_Failure= P_Failure         #Links_ Probability of link failure
              self.Link_state = Link_state      # Boolean indicator to indicate whether link down/up
    #------------------------------------------------------------------------------

    L=[] # List that contains a set of links as a class objects
    for i in range (len(Edges)): # To initailize the link objects
        L.append((Links(Edges[i], i , Links_Lengths_Dictionary[Edges[i]], MTBF[i], MTTR[i], 0, 0, 0, True)))

    for i in range (len(Edges)): # Generate the initial "Next_Failure" for all links
        TTF= np.random.exponential(scale=L[i].MTBF, size=1) # Exponential Distribution[Mean= MTBF of current link]
        L[i].Next_Failure = round(TTF)

    for i in range (len(Edges)):
        print "Link %s that named % s with Length %s and MTBF equals to %s and MTTR %s and Next_Failure is %s and Failure counter equals to %s and failure probability equals to %s and the Link_state is %s" % (L[i].ID, L[i].Name, L[i].Length, L[i].MTBF, L[i].MTTR, L[i].Next_Failure, L[i].F_Count, L[i].P_Failure, L[i].Link_state)


    for i in range (len(Edges)):
        q.push(L[i].Name, L[i].Next_Failure)

    print 'Test Q size', q.size()
    #------------------------------------------------------------------------------
    #Schedular and it's related functions
    scheduler = sched.scheduler(time.time, time.sleep)
    now = datetime.datetime.now()
    #------------------------------------------------------------------------------
    def push(link_return):
        global net

        if (L[link_return].Link_state == False):
           L[link_return].Link_state = True
           print 'The Link', L[link_return].ID, 'with Next_Failure =', L[link_return].Next_Failure ,'will be returened'
           TTF2= np.random.exponential(scale=L[link_return].MTBF, size=1)
           L[link_return].Next_Failure = round(TTF2)
           switches_R = L[link_return].ID
           switch1 = Switches_Dictionary [switches_R[0]]
           switch2 = Switches_Dictionary [switches_R[1]]
           net.configLinkStatus(switch1, switch2,'up')
           print '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
           print 'The repaired link is ', switch1, '--', switch2
           print '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
           q.push(L[link_return].Name, L[link_return].Next_Failure)
           print 'The new Next_Failure of link', L[link_return].ID, 'is :', round(TTF2)
        else:
             print 'The link', L[link_return].ID ,'will be returened'
             TTF2= np.random.exponential(scale=L[link_return].MTBF, size=1)
             L[link_return].Next_Failure = round(TTF2)
             q.push(L[link_return].Name, L[link_return].Next_Failure)
             print 'The new Next_Failure of link', L[link_return].ID, 'is :', round(TTF2)

    #------------------------------------------------------------------------------
    def Send_To_Controller(lnk):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        #global socket
        socket.connect("tcp://localhost:5556")
        x = str(lnk)
        LinkPrediction = {"type": "LinkFailure", "link": x}
        #send command of failure link event 
        socket.send_json(LinkPrediction)
        #For every time you use a send method you need to run the receive method
        resp = socket.recv_json()
        # close the socket when you're done
        socket.close()
    #------------------------------------------------------------------------------
    def schedule(link):
        global net
        print time.time()

        if (L[link].Link_state == False):
          print 'The link', L[link].ID, ' poped out with Next_Failure =', L[link].Next_Failure
          switches_F = L[link].ID
          switch1 = Switches_Dictionary [switches_F[0]]
          switch2 = Switches_Dictionary [switches_F[1]]
          net.configLinkStatus(switch1, switch2,'down')
          print '********************************************'
          print 'The failed link is ', switch1, '--', switch2
          print '********************************************'
          mu = (math.log(L[link].MTTR) - ((0.5) * math.log(1 + ((0.6 * L[link].MTTR)**2 / L[link].MTTR**2))))
         sig = math.sqrt((math.log (1 + ((0.6 * L[link].MTTR)**2 / L[link].MTTR**2))))
          Log_Normal = np.random.lognormal(mu, sig, 1) #Lognormal #distribution for the next Time To Recover event
          print 'The link', L[link].ID, 'will wait up to', round(Log_Normal), 'to get recovery'
          scheduler.enter(round(Log_Normal)*60, 1, push, (L[link].Name,))
          get_out() #calling the function to schedule the next link failure
          scheduler.run()
        else:
           print 'The link', L[link].ID ,'will not wait and directly returned to the Q with a new Next_Time _To_Failure'
           scheduler.enter(2, 1, push, (L[link].Name,))
           get_out() #calling the function to schedule the next link failure
           scheduler.run()
    #------------------------------------------------------------------------------
    def get_out():
        global Global_Failure_Counter

        if q.isEmpty() != True:
           F_Flag = True  #indicator
           x = q.pop()
           Dicision_F = random.randint(0, 1) #To decide if the link is gonna faile or not
           if Dicision_F == 1: #Means the link is gonna fail in reality
              F_Flag = False
              L[x].Link_state = False #change link state to false as an indicator
              L[x].F_Count+=1              # Increment the failure counter of the current link
              Global_Failure_Counter+= 1   # Increment the global failure counter

           L[x].P_Failure = (float(L[x].F_Count) / float(Global_Failure_Counter)) * 100
           print 'Link ', L[x].ID , 'will pop out from the Q with Next time to failure =', L[x].Next_Failure
           print 'The probability of failure to the link', L[x].ID, 'is ', L[x].P_Failure, '%'
           if (L[x].P_Failure > 0):  #The threshold condition is greater than 0% 
                    print 'The link', L[x].ID, 'Has a failure probability over the threshould'
                    Dicision = random.randint(0, 1)
                    if Dicision == 1 :  #Means the controller will receive a notification and its a true positive
                           if ((L[x].Next_Failure) > 2):
                              wt = (L[x].Next_Failure) - 2
                              print 'The controller will receive a notification after', wt, 'mins'
                              scheduler.enter(wt*60, 1, Send_To_Controller, (L[x].ID,)) #send a notification 
                                                #about the link who will fail after two mins (i.e. wt * 60)
                           else:
                                  print 'There is no enough time to send a notification to the controller, sorry'
                                  #scheduler.enter(2, 1, Send_To_Controller, (L[x].ID,)) #send a notification after 2 sec
           else:
                print 'The link', L[x].ID, 'Has a failure probability below the threshould'
           scheduler.enter((L[x].Next_Failure)*60, 1, schedule, (L[x].Name,)) # Next_Failure *60 --> in minutes

        else:
               print 'The Q is empty ... '
        scheduler.run() #running the schedular
    #------------------------------------------------------------------------------
    print '**************************************'
    print 'START TIME:', time.time(), '-->', now
    print '**************************************'
    time.sleep(120) # Wait up to 2 mins then start the event failure simulation
    get_out()


