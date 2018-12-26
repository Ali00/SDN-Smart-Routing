#Created By Ali Malik
#Brite Topology 70 nodes 140 links
#With failure events generator

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

import networkx as nx #, igraph as ig

import pylab as plt

from collections import Counter

from itertools import tee, izip

import string

import heapq
import scipy as sp
import math

#-------------------------------------------------------------------------------

#context = zmq.Context()

#socket = context.socket(zmq.REQ)

#socket.connect("tcp://localhost:5556")

TP = "F_set.csv" 
csv1 = open(TP, "a")
columnTitle1 = "Link, State\n"
csv1.write(columnTitle1)
csv1.close()

net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )

G = nx.Graph()

Global_Failure_Counter= 1 # Global counter to keep the number of all links failure

X_param = 1               # Global counter to avoid the first false failure (division by zero)
#sp.random.seed(1234)


def topology():



        global net

        # Add hosts and switches

        #h1= net.addHost( 'h1', mac="00:00:00:00:00:01" )

        #h2 = net.addHost( 'h2', mac="00:00:00:00:00:02" )

        S1 = net.addSwitch('s1')
        S2 = net.addSwitch('s2')
        S3 = net.addSwitch('s3')
        S4 = net.addSwitch('s4')
        S5 = net.addSwitch('s5')
        S6 = net.addSwitch('s6')
        S7 = net.addSwitch('s7')
        S8 = net.addSwitch('s8')
        S9 = net.addSwitch('s9')
        S10 = net.addSwitch('s10')
        S11 = net.addSwitch('s11')
        S12 = net.addSwitch('s12')
        S13 = net.addSwitch('s13')
        S14 = net.addSwitch('s14')
        S15 = net.addSwitch('s15')
        S16 = net.addSwitch('s16')
        S17 = net.addSwitch('s17')
        S18 = net.addSwitch('s18')
        S19 = net.addSwitch('s19')
        S20 = net.addSwitch('s20')
        S21 = net.addSwitch('s21')
        S22 = net.addSwitch('s22')
        S23 = net.addSwitch('s23')
        S24 = net.addSwitch('s24')
        S25 = net.addSwitch('s25')
        S26 = net.addSwitch('s26')
        S27 = net.addSwitch('s27')
        S28 = net.addSwitch('s28')
        S29 = net.addSwitch('s29')
        S30 = net.addSwitch('s30')
        S31 = net.addSwitch('s31')
        S32 = net.addSwitch('s32')
        S33 = net.addSwitch('s33')
        S34 = net.addSwitch('s34')
        S35 = net.addSwitch('s35')
        S36 = net.addSwitch('s36')
        S37 = net.addSwitch('s37')
        S38 = net.addSwitch('s38')
        S39 = net.addSwitch('s39')
        S40 = net.addSwitch('s40')
        S41 = net.addSwitch('s41')
        S42 = net.addSwitch('s42')
        S43 = net.addSwitch('s43')
        S44 = net.addSwitch('s44')
        S45 = net.addSwitch('s45')
        S46 = net.addSwitch('s46')
        S47 = net.addSwitch('s47')
        S48 = net.addSwitch('s48')
        S49 = net.addSwitch('s49')
        S50 = net.addSwitch('s50')
	S51 = net.addSwitch('s51')
	S52 = net.addSwitch('s52')
	S53 = net.addSwitch('s53')
	S54 = net.addSwitch('s54')
	S55 = net.addSwitch('s55')
	S56 = net.addSwitch('s56')
	S57 = net.addSwitch('s57')
	S58 = net.addSwitch('s58')
	S59 = net.addSwitch('s59')
	S60 = net.addSwitch('s60')
	S61 = net.addSwitch('s61')
	S62 = net.addSwitch('s62')
	S63 = net.addSwitch('s63')
	S64 = net.addSwitch('s64')
	S65 = net.addSwitch('s65')
	S66 = net.addSwitch('s66')
	S67 = net.addSwitch('s67')
	S68 = net.addSwitch('s68')
	S69 = net.addSwitch('s69')
	S70 = net.addSwitch('s70')
	
	

        c0 = net.addController( 'c0', controller=RemoteController, ip='127.0.0.1', port=6633 )

        # Adding 140 Links of the Brite_Topology 

        net.addLink (S1 ,S3 )
	net.addLink (S1 ,S4 )
	net.addLink (S1 ,S5 )
	net.addLink (S1 ,S8 )
	net.addLink (S1 ,S11 )
	net.addLink (S1 ,S16 )
	net.addLink (S1 ,S57 )
	net.addLink (S1 ,S28 )
	net.addLink (S2 ,S65 )
	net.addLink (S2 ,S3 )
	net.addLink (S2 ,S6 )
	net.addLink (S2 ,S7 )
	net.addLink (S2 ,S9 )
	net.addLink (S2 ,S23 )
	net.addLink (S2 ,S14 )
	net.addLink (S2 ,S17 )
	net.addLink (S2 ,S19 )
	net.addLink (S2 ,S55 )
	net.addLink (S2 ,S39 )
	net.addLink (S2 ,S26 )
	net.addLink (S3 ,S4 )
	net.addLink (S3 ,S69 )
	net.addLink (S3 ,S22 )
	net.addLink (S3 ,S28 )
	net.addLink (S4 ,S32 )
	net.addLink (S4 ,S34 )
	net.addLink (S4 ,S5 )
	net.addLink (S4 ,S33 )
	net.addLink (S4 ,S8 )
	net.addLink (S4 ,S42 )
	net.addLink (S4 ,S12 )
	net.addLink (S4 ,S15 )
	net.addLink (S4 ,S31 )
	net.addLink (S5 ,S6 )
	net.addLink (S5 ,S8 )
	net.addLink (S5 ,S11 )
	net.addLink (S5 ,S49 )
	net.addLink (S5 ,S26 )
	net.addLink (S6 ,S35 )
	net.addLink (S6 ,S7 )
	net.addLink (S6 ,S10 )
	net.addLink (S6 ,S12 )
	net.addLink (S6 ,S20 )
	net.addLink (S7 ,S19 )
	net.addLink (S7 ,S34 )
	net.addLink (S7 ,S13 )
	net.addLink (S7 ,S51 )
	net.addLink (S7 ,S23 )
	net.addLink (S7 ,S61 )
	net.addLink (S8 ,S9 )
	net.addLink (S8 ,S10 )
	net.addLink (S8 ,S13 )
	net.addLink (S8 ,S48 )
	net.addLink (S8 ,S36 )
	net.addLink (S9 ,S49 )
	net.addLink (S9 ,S14 )
	net.addLink (S11 ,S66 )
	net.addLink (S11 ,S67 )
	net.addLink (S11 ,S15 )
	net.addLink (S11 ,S16 )
	net.addLink (S11 ,S35 )
	net.addLink (S11 ,S52 )
	net.addLink (S11 ,S29 )
	net.addLink (S12 ,S20 )
	net.addLink (S12 ,S18 )
	net.addLink (S12 ,S22 )
	net.addLink (S13 ,S51 )
	net.addLink (S13 ,S52 )
	net.addLink (S13 ,S14 )
	net.addLink (S14 ,S38 )
	net.addLink (S14 ,S43 )
	net.addLink (S14 ,S45 )
	net.addLink (S14 ,S17 )
	net.addLink (S14 ,S21 )
	net.addLink (S14 ,S25 )
	net.addLink (S15 ,S66 )
	net.addLink (S15 ,S40 )
	net.addLink (S15 ,S21 )
	net.addLink (S15 ,S54 )
	net.addLink (S16 ,S19 )
	net.addLink (S16 ,S24 )
	net.addLink (S16 ,S25 )
	net.addLink (S17 ,S18 )
	net.addLink (S17 ,S53 )
	net.addLink (S18 ,S33 )
	net.addLink (S18 ,S70 )
	net.addLink (S18 ,S50 )
	net.addLink (S18 ,S53 )
	net.addLink (S18 ,S27 )
	net.addLink (S19 ,S62 )
	net.addLink (S20 ,S59 )
	net.addLink (S20 ,S46 )
	net.addLink (S21 ,S47 )
	net.addLink (S21 ,S31 )
	net.addLink (S22 ,S57 )
	net.addLink (S23 ,S41 )
	net.addLink (S23 ,S56 )
	net.addLink (S23 ,S24 )
	net.addLink (S23 ,S29 )
	net.addLink (S24 ,S42 )
	net.addLink (S24 ,S27 )
	net.addLink (S24 ,S30 )
	net.addLink (S25 ,S62 )
	net.addLink (S25 ,S44 )
	net.addLink (S25 ,S46 )
	net.addLink (S26 ,S36 )
	net.addLink (S26 ,S63 )
	net.addLink (S27 ,S37 )
	net.addLink (S27 ,S58 )
	net.addLink (S27 ,S59 )
	net.addLink (S27 ,S30 )
	net.addLink (S28 ,S63 )
	net.addLink (S29 ,S32 )
	net.addLink (S29 ,S40 )
	net.addLink (S30 ,S50 )
	net.addLink (S30 ,S60 )
	net.addLink (S30 ,S47 )
	net.addLink (S32 ,S56 )
	net.addLink (S33 ,S38 )
	net.addLink (S34 ,S44 )
	net.addLink (S34 ,S43 )
	net.addLink (S35 ,S37 )
	net.addLink (S35 ,S39 )
	net.addLink (S36 ,S64 )
	net.addLink (S36 ,S48 )
	net.addLink (S37 ,S68 )
	net.addLink (S37 ,S45 )
	net.addLink (S38 ,S54 )
	net.addLink (S38 ,S41 )
	net.addLink (S42 ,S60 )
	net.addLink (S45 ,S55 )
	net.addLink (S46 ,S67 )
	net.addLink (S46 ,S57 )
	net.addLink (S47 ,S65 )
	net.addLink (S51 ,S58 )
	net.addLink (S58 ,S61 )
	net.addLink (S58 ,S70 )
	net.addLink (S60 ,S69 )
	net.addLink (S63 ,S64 )
	net.addLink (S67 ,S68 )
        

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
        S27.start(  [c0] )
        S28.start(  [c0] )
        S29.start(  [c0] )
        S30.start(  [c0] )
        S31.start(  [c0] )
        S32.start(  [c0] )
        S33.start(  [c0] )
        S34.start(  [c0] )
        S35.start(  [c0] )
        S36.start(  [c0] )
        S37.start(  [c0] )
        S38.start(  [c0] )
        S39.start(  [c0] )
        S40.start(  [c0] )
        S41.start(  [c0] )
        S42.start(  [c0] )
        S43.start(  [c0] )
        S44.start(  [c0] )
        S45.start(  [c0] )
        S46.start(  [c0] )
        S47.start(  [c0] )
        S48.start(  [c0] )
        S49.start(  [c0] )
        S50.start(  [c0] )
        S51.start(  [c0] )
        S52.start(  [c0] )
        S53.start(  [c0] )
        S54.start(  [c0] )
        S55.start(  [c0] )
        S56.start(  [c0] )
        S57.start(  [c0] )
        S58.start(  [c0] )
        S59.start(  [c0] )
        S60.start(  [c0] )
        S61.start(  [c0] )
        S62.start(  [c0] )
        S63.start(  [c0] )
        S64.start(  [c0] )
        S65.start(  [c0] )
        S66.start(  [c0] )
        S67.start(  [c0] )
        S68.start(  [c0] )
        S69.start(  [c0] )
        S70.start(  [c0] )
        


        #print "*** Running CLI"

        #CLI( net )



        #print "*** Stopping network"

        #net.stop()



if __name__ == '__main__':

    setLogLevel( 'info' )

    topology()

    #Topology Graph

    G.add_edges_from([(1, 3), (1, 4), (1, 5), (1, 8), (1, 11), (1, 16), (1, 57), (1, 28), (2, 65), (2, 3), (2, 6), (2, 7), (2, 9), (2, 23), (2, 14), (2, 17), (2, 19), (2, 55), (2, 39), (2, 26), (3, 4), (3, 69), (3, 22), (3, 28), (4, 32), (4, 34), (4, 5), (4, 33), (4, 8), (4, 42), (4, 12), (4, 15), (4, 31), (5, 6), (5, 8), (5, 11), (5, 49), (5, 26), (6, 35), (6, 7), (6, 10), (6, 12), (6, 20), (7, 19), (7, 34), (7, 13), (7, 51), (7, 23), (7, 61), (8, 9), (8, 10), (8, 13), (8, 48), (8, 36), (9, 49), (9, 14), (11, 66), (11, 67), (11, 15), (11, 16), (11, 35), (11, 52), (11, 29), (12, 20), (12, 18), (12, 22), (13, 51), (13, 52), (13, 14), (14, 38), (14, 43), (14, 45), (14, 17), (14, 21), (14, 25), (15, 66), (15, 40), (15, 21), (15, 54), (16, 19), (16, 24), (16, 25), (17, 18), (17, 53), (18, 33), (18, 70), (18, 50), (18, 53), (18, 27), (19, 62), (20, 59), (20, 46), (21, 47), (21, 31), (22, 57), (23, 41), (23, 56), (23, 24), (23, 29), (24, 42), (24, 27), (24, 30), (25, 62), (25, 44), (25, 46), (26, 36), (26, 63), (27, 37), (27, 58), (27, 59), (27, 30), (28, 63), (29, 32), (29, 40), (30, 50), (30, 60), (30, 47), (32, 56), (33, 38), (34, 44), (34, 43), (35, 37), (35, 39), (36, 64), (36, 48), (37, 68), (37, 45), (38, 54), (38, 41), (42, 60), (45, 55), (46, 67), (46, 57), (47, 65), (51, 58), (58, 61), (58, 70), (60, 69), (63, 64), (67, 68)])


    Nodes= nx.nodes(G)

    Edges= nx.edges(G)

    print 'The nodes are', Nodes

    print 'The edges are', Edges



    #Dictionary of switches to return --> e.g.  Link (1,2) --> (s1, s2)

    Switches_Dictionary = { (1): 's1', (2): 's2', (3): 's3',(4): 's4', (5): 's5', (6): 's6',
                           (7): 's7', (8): 's8', (9): 's9', (10): 's10', (11): 's11', (12): 's12', (13): 's13', (14): 's14',
                           (15): 's15', (16): 's16', (17): 's17', (18): 's18', (18): 's18', (19): 's19', (20): 's20', (21): 's21',
                           (22): 's22', (23): 's23', (24): 's24', (25): 's25', (26): 's26', (27): 's27', (28): 's28', (29): 's29',
                           (30): 's30', (31): 's31' , (32): 's32', (33): 's33', (34): 's34', (35): 's35', (36): 's36', (37): 's37',
                           (38): 's38', (39): 's39', (40): 's40', (41): 's41', (42): 's42', (43): 's43', (44): 's44', (45): 's45',
                           (46): 's46', (47): 's47', (48): 's48', (49): 's49', (50): 's50', (51): 's51',
                           (52): 's52', (53): 's53', (54): 's54', (55): 's55', (56): 's56', (57): 's57', (58): 's58',(59): 's59',
                           (60): 's60' , (61): 's61' , (62): 's62' , (63): 's63' , (64): 's64' , (65): 's65', (66): 's66',
                           (67): 's67', (68): 's68', (69): 's69', (70): 's70'}

    #Link's Length Dictionary

    Links_Lengths_Dictionary = {(1, 3) : 233 ,(1, 4) : 402 ,(1, 5) : 208 ,(1, 8) : 270 ,(1, 11) : 167 ,(1, 16) : 336 ,(1, 57) : 476 ,
(1, 28) : 468 ,(2, 65) : 589 ,(2, 3) : 522 ,(2, 6) : 430 ,(2, 7) : 432 ,(2, 9) : 151 ,(2, 23) : 179 ,(2, 14) : 264 ,(2, 17) : 49 ,
(2, 19) : 141 ,(2, 55) : 123 ,(2, 39) : 544 ,(2, 26) : 230 ,(3, 4) : 434 ,(3, 69) : 503 ,(3, 22) : 722 ,(3, 28) : 541 ,(4, 32) : 550 ,(4, 34) : 301 ,(4, 5) : 217 ,(4, 33) : 242 ,(4, 8) : 133 ,(4, 42) : 486 ,(4, 12) : 356 ,(4, 15) : 260 ,(4, 31) : 454 ,
(5, 6) : 499 ,(5, 8) : 94 ,(5, 11) : 292 ,(5, 49) : 464 ,(5, 26) : 205 ,(6, 35) : 565 ,(6, 7) : 184 ,(6, 10) : 1099 ,(6, 12) : 131 ,
(6, 20) : 294 ,(7, 19) : 565 ,(7, 34) : 41 ,(7, 13) : 145 ,(7, 51) : 161 ,(7, 23) : 283 ,(7, 61) : 538 ,(8, 9) : 197 ,(8, 10) : 681 ,
(8, 13) : 205 ,(8, 48) : 282 ,(8, 36) : 548 ,(9, 49) : 747 ,(9, 14) : 232 ,(11, 66) : 53 ,(11, 67) : 188 ,(11, 15) : 249 ,(11, 16) : 175 ,(11, 35) : 513 ,(11, 52) : 74 ,(11, 29) : 268 ,(12, 20) : 163 ,(12, 18) : 521 ,(12, 22) : 506 ,(13, 51) : 53 ,(13, 52) : 579 ,
(13, 14) : 187 ,(14, 38) : 165 ,(14, 43) : 416 ,(14, 45) : 658 ,(14, 17) : 298 ,(14, 21) : 794 ,(14, 25) : 26 ,(15, 66) : 208 ,(15, 40) : 484 ,(15, 21) : 419 ,(15, 54) : 348 ,(16, 19) : 937 ,(16, 24) : 863 ,(16, 25) : 881 ,(17, 18) : 243 ,(17, 53) : 104 ,(18, 33) : 442 ,(18, 70) : 335 ,(18, 50) : 743 ,(18, 53) : 187 ,(18, 27) : 140 ,(19, 62) : 420 ,(20, 59) : 98 ,(20, 46) : 368 ,(21, 47) : 468 ,(21, 31) : 176 ,(22, 57) : 96 ,(23, 41) : 15 ,(23, 56) : 231 ,(23, 24) : 538 ,(23, 29) : 490 ,(24, 42) : 94 ,(24, 27) : 101 ,
(24, 30) : 129 ,(25, 62) : 48 ,(25, 44) : 19 ,(25, 46) : 175 ,(26, 36) : 653 ,(26, 63) : 403 ,(27, 37) : 270 ,(27, 58) : 326 ,(27, 59) : 533 ,(27, 30) : 188 ,(28, 63) : 441 ,(29, 32) : 284 ,(29, 40) : 336 ,(30, 50) : 815 ,(30, 60) : 375 ,(30, 47) : 699 ,(32, 56) : 489 ,(33, 38) : 76 ,(34, 44) : 214 ,(34, 43) : 329 ,(35, 37) : 288 ,(35, 39) : 505 ,(36, 64) : 153 ,(36, 48) : 410 ,(37, 68) : 248 ,(37, 45) : 393 ,(38, 54) : 760 ,(38, 41) : 221 ,(42, 60) : 412 ,(45, 55) : 357 ,(46, 67) : 494 ,(46, 57) : 361 ,(47, 65) : 252 ,
(51, 58) : 368 ,(58, 61) : 132 ,(58, 70) : 360 ,(60, 69) : 361 ,(63, 64) : 349 ,(67, 68) : 488}

    #-------------------------------------------------------------------------------------------------------------
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

        L[i].Next_Failure = round(TTF) + 1 # To avoid zeros at the begining, we add (+1) to the TTF



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

           if TTF2 == 0:    # To avoid zeros
              TTF2 =1

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

             if TTF2 == 0:    # To avoid zeros
                TTF2 =1

             L[link_return].Next_Failure = round(TTF2)

             q.push(L[link_return].Name, L[link_return].Next_Failure)

             print 'The new Next_Failure of link', L[link_return].ID, 'is :', round(TTF2)



    #------------------------------------------------------------------------------

    def Send_To_Controller(lnk, lnk_prob):

        context = zmq.Context()

        socket = context.socket(zmq.REQ)

        #global socket

        socket.connect("tcp://localhost:5556")

        x = str(lnk)
        y= float(lnk_prob)

        LinkPrediction = {"type": "LinkFailure", "link": x, "probability": y}

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

        global X_param
        #sp.random.seed(123345)

        csv1 = open(TP, "a")


        if q.isEmpty() != True:

           F_Flag = True  #indicator
           Z_Flag = True  #indicator

           x = q.pop()

           L[x].Link_state = False      # Change link state to false as an indicator that link is going to fail


           L[x].P_Failure = (float(L[x].F_Count) / float(Global_Failure_Counter)) * 100

           print 'Link ', L[x].ID , 'will pop out from the Q with Next time to failure =', L[x].Next_Failure

           print 'The probability of failure to the link', L[x].ID, 'is ', L[x].P_Failure, '%'

           if (L[x].P_Failure >= 0.25):  #The threshold T_omega condition is valid

                    Z_Flag = False
                    print 'The link', L[x].ID, 'Has a failure probability over the threshould'
                    Dicision_1 = sp.random.uniform(low=0.1,high=0.3,size=1)   # Anticipated failure distribution
                    Dicision = float(Dicision_1 - Dicision_1 % 0.01)
                    

                    if Dicision < 0.2 :  #Means the controller will receive a notification and its a true positive TP
                           
                           L[x].F_Count+=1              # Increment the failure counter of the current link
                           Global_Failure_Counter+= 1   # Increment the global failure counter
                           k = L[x].ID
                           print "The link that will fail and put in F_set file is :", k
                           row1 = "\"" + str(k) + "\"" + "," + "TP_FN" +"\n"
                           csv1.write(row1)
                           csv1.close() 

                           if ((L[x].Next_Failure) > 2):

                               wt = (L[x].Next_Failure) - 2

                               print 'The controller will receive a notification after wt', wt, 'mins'

                               scheduler.enter(wt*60, 1, Send_To_Controller, (L[x].ID, L[x].P_Failure,)) #send a notification

                                                #about the link who will fail after two mins (i.e. wt * 60)

                           else:  
                                  
                                  print "The time window is too short to send a notificatoin about the true alarm"
 
                    else:                # Means the controller will receive a false positive alarm FP
                         L[x].Link_state = True      # Change link state to True as an indicator
                         F_Flag = False
                         if ((L[x].Next_Failure) > 2):
                            wt2 = (L[x].Next_Failure) - 2
                            print 'The controller will receive a notification after wt2', wt2, 'mins'
                            scheduler.enter(wt2*60, 1, Send_To_Controller, (L[x].ID, L[x].P_Failure,)) #send a notification 
                         else:
                             print "The time window is too short to send a notification about false alarm"

           else:

                print 'The link', L[x].ID, 'Has a failure probability below the threshould'

           if (F_Flag==True and Z_Flag==True):
               
               L[x].F_Count+=1              # Increment the failure counter of the current link
               Global_Failure_Counter+= 1   # Increment the global failure counter
               k = L[x].ID
               print "The link that will fail and put in F_set file is :", k
               row1 = "\"" + str(k) + "\"" + "," + "TP_FN" +"\n"
               csv1.write(row1)
               csv1.close() 
           moderator = sp.random.uniform(low=0.1,high=0.9,size=1)
           scheduler.enter((L[x].Next_Failure)*60 + moderator, 1, schedule, (L[x].Name,)) # Next_Failure *60 --> in minutes

        else:

               print 'The Q is empty ... '

        scheduler.run() #running the schedular
        

    #------------------------------------------------------------------------------

    print '**************************************'

    print 'START TIME:', time.time(), '-->', now

    print '**************************************'

    time.sleep(120) # Wait up to 2 mins then start the event failure simulation

    get_out()



