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
	S71 = net.addSwitch('s71')
	S72 = net.addSwitch('s72')
	S73 = net.addSwitch('s73')
	S74 = net.addSwitch('s74')
	S75 = net.addSwitch('s75')
	S76 = net.addSwitch('s76')
	S77 = net.addSwitch('s77')
	S78 = net.addSwitch('s78')
	S79 = net.addSwitch('s79')
	S80 = net.addSwitch('s80')
	S81 = net.addSwitch('s81')
	S82 = net.addSwitch('s82')
	S83 = net.addSwitch('s83')
	S84 = net.addSwitch('s84')
	S85 = net.addSwitch('s85')
	S86 = net.addSwitch('s86')
	S87 = net.addSwitch('s87')
	S88 = net.addSwitch('s88')
	S89 = net.addSwitch('s89')
	S90 = net.addSwitch('s90')
	S91 = net.addSwitch('s91')
	S92 = net.addSwitch('s92')
	S93 = net.addSwitch('s93')
	S94 = net.addSwitch('s94')
	S95 = net.addSwitch('s95')
	S96 = net.addSwitch('s96')
	S97 = net.addSwitch('s97')
	S98 = net.addSwitch('s98')
	S99 = net.addSwitch('s99')
	S100 = net.addSwitch('s100')

        c0 = net.addController( 'c0', controller=RemoteController, ip='127.0.0.1', port=6633 )

        # Adding 300 Links of the Brite_Topology 

        net.addLink (S1 ,S4 )
        net.addLink (S1 ,S5 )
	net.addLink (S1 ,S6 )
	net.addLink (S1 ,S71 )
	net.addLink (S1 ,S11 )
	net.addLink (S1 ,S13 )
	net.addLink (S1 ,S14 )
	net.addLink (S1 ,S82 )
	net.addLink (S1 ,S20 )
	net.addLink (S1 ,S85 )
	net.addLink (S1 ,S7 )
	net.addLink (S1 ,S68 )
	net.addLink (S1 ,S27 )
	net.addLink (S1 ,S29 )
	net.addLink (S1 ,S69 )
	net.addLink (S2 ,S65 )
	net.addLink (S2 ,S91 )
	net.addLink (S2 ,S4 )
	net.addLink (S2 ,S5 )
	net.addLink (S2 ,S7 )
	net.addLink (S2 ,S42 )
	net.addLink (S2 ,S43 )
	net.addLink (S2 ,S12 )
	net.addLink (S2 ,S45 )
	net.addLink (S2 ,S13 )
	net.addLink (S2 ,S18 )
	net.addLink (S2 ,S19 )
	net.addLink (S2 ,S21 )
	net.addLink (S2 ,S55 )
	net.addLink (S2 ,S15 )
	net.addLink (S3 ,S67 )
	net.addLink (S3 ,S4 )
	net.addLink (S3 ,S5 )
	net.addLink (S3 ,S8 )
	net.addLink (S3 ,S44 )
	net.addLink (S3 ,S14 )
	net.addLink (S3 ,S47 )
	net.addLink (S3 ,S83 )
	net.addLink (S3 ,S52 )
	net.addLink (S3 ,S94 )
	net.addLink (S3 ,S23 )
	net.addLink (S3 ,S91 )
	net.addLink (S3 ,S28 )
	net.addLink (S3 ,S30 )
	net.addLink (S4 ,S6 )
	net.addLink (S4 ,S7 )
	net.addLink (S4 ,S9 )
	net.addLink (S4 ,S12 )
	net.addLink (S4 ,S34 )
	net.addLink (S4 ,S80 )
	net.addLink (S4 ,S87 )
	net.addLink (S4 ,S91 )
	net.addLink (S5 ,S6 )
	net.addLink (S5 ,S8 )
	net.addLink (S5 ,S9 )
	net.addLink (S5 ,S10 )
	net.addLink (S5 ,S11 )
	net.addLink (S5 ,S13 )
	net.addLink (S5 ,S16 )
	net.addLink (S5 ,S43 )
	net.addLink (S5 ,S26 )
	net.addLink (S5 ,S59 )
	net.addLink (S6 ,S65 )
	net.addLink (S6 ,S8 )
	net.addLink (S6 ,S11 )
	net.addLink (S6 ,S12 )
	net.addLink (S6 ,S18 )
	net.addLink (S6 ,S14 )
	net.addLink (S6 ,S82 )
	net.addLink (S6 ,S21 )
	net.addLink (S6 ,S87 )
	net.addLink (S6 ,S88 )
	net.addLink (S6 ,S25 )
	net.addLink (S6 ,S90 )
	net.addLink (S7 ,S70 )
	net.addLink (S7 ,S38 )
	net.addLink (S7 ,S44 )
	net.addLink (S7 ,S24 )
	net.addLink (S7 ,S57 )
	net.addLink (S7 ,S27 )
	net.addLink (S8 ,S67 )
	net.addLink (S8 ,S9 )
	net.addLink (S8 ,S10 )
	net.addLink (S8 ,S75 )
	net.addLink (S8 ,S15 )
	net.addLink (S8 ,S35 )
	net.addLink (S8 ,S23 )
	net.addLink (S8 ,S26 )
	net.addLink (S9 ,S32 )
	net.addLink (S9 ,S10 )
	net.addLink (S10 ,S38 )
	net.addLink (S10 ,S44 )
	net.addLink (S10 ,S17 )
	net.addLink (S10 ,S18 )
	net.addLink (S10 ,S37 )
	net.addLink (S11 ,S45 )
	net.addLink (S11 ,S14 )
	net.addLink (S11 ,S16 )
	net.addLink (S11 ,S51 )
	net.addLink (S11 ,S87 )
	net.addLink (S11 ,S37 )
	net.addLink (S12 ,S32 )
	net.addLink (S12 ,S40 )
	net.addLink (S12 ,S78 )
	net.addLink (S12 ,S20 )
	net.addLink (S12 ,S60 )
	net.addLink (S13 ,S81 )
	net.addLink (S13 ,S33 )
	net.addLink (S13 ,S86 )
	net.addLink (S13 ,S15 )
	net.addLink (S13 ,S17 )
	net.addLink (S13 ,S54 )
	net.addLink (S13 ,S49 )
	net.addLink (S13 ,S28 )
	net.addLink (S14 ,S49 )
	net.addLink (S14 ,S45 )
	net.addLink (S14 ,S46 )
	net.addLink (S14 ,S17 )
	net.addLink (S14 ,S35 )
	net.addLink (S14 ,S20 )
	net.addLink (S14 ,S21 )
	net.addLink (S14 ,S29 )
	net.addLink (S15 ,S83 )
	net.addLink (S15 ,S47 )
	net.addLink (S15 ,S16 )
	net.addLink (S15 ,S19 )
	net.addLink (S15 ,S23 )
	net.addLink (S15 ,S26 )
	net.addLink (S16 ,S36 )
	net.addLink (S16 ,S50 )
	net.addLink (S16 ,S22 )
	net.addLink (S16 ,S56 )
	net.addLink (S16 ,S62 )
	net.addLink (S16 ,S31 )
	net.addLink (S17 ,S33 )
	net.addLink (S17 ,S34 )
	net.addLink (S17 ,S71 )
	net.addLink (S17 ,S39 )
	net.addLink (S17 ,S48 )
	net.addLink (S17 ,S54 )
	net.addLink (S17 ,S55 )
	net.addLink (S17 ,S89 )
	net.addLink (S17 ,S95 )
	net.addLink (S17 ,S61 )
	net.addLink (S17 ,S30 )
	net.addLink (S17 ,S31 )
	net.addLink (S18 ,S48 )
	net.addLink (S18 ,S19 )
	net.addLink (S18 ,S22 )
	net.addLink (S18 ,S28 )
	net.addLink (S18 ,S42 )
	net.addLink (S19 ,S31 )
	net.addLink (S19 ,S51 )
	net.addLink (S20 ,S37 )
	net.addLink (S20 ,S78 )
	net.addLink (S20 ,S84 )
	net.addLink (S20 ,S22 )
	net.addLink (S21 ,S32 )
	net.addLink (S21 ,S96 )
	net.addLink (S21 ,S70 )
	net.addLink (S21 ,S39 )
	net.addLink (S21 ,S24 )
	net.addLink (S21 ,S88 )
	net.addLink (S21 ,S25 )
	net.addLink (S21 ,S58 )
	net.addLink (S22 ,S64 )
	net.addLink (S22 ,S38 )
	net.addLink (S22 ,S39 )
	net.addLink (S22 ,S56 )
	net.addLink (S23 ,S74 )
	net.addLink (S23 ,S93 )
	net.addLink (S23 ,S24 )
	net.addLink (S23 ,S27 )
	net.addLink (S23 ,S61 )
	net.addLink (S24 ,S57 )
	net.addLink (S24 ,S25 )
	net.addLink (S24 ,S29 )
	net.addLink (S24 ,S95 )
	net.addLink (S25 ,S66 )
	net.addLink (S25 ,S98 )
	net.addLink (S25 ,S80 )
	net.addLink (S25 ,S53 )
	net.addLink (S26 ,S40 )
	net.addLink (S26 ,S64 )
	net.addLink (S27 ,S69 )
	net.addLink (S27 ,S97 )
	net.addLink (S27 ,S76 )
	net.addLink (S28 ,S33 )
	net.addLink (S28 ,S68 )
	net.addLink (S28 ,S41 )
	net.addLink (S28 ,S35 )
	net.addLink (S28 ,S30 )
	net.addLink (S29 ,S53 )
	net.addLink (S29 ,S73 )
	net.addLink (S30 ,S34 )
	net.addLink (S30 ,S41 )
	net.addLink (S30 ,S79 )
	net.addLink (S31 ,S36 )
	net.addLink (S31 ,S73 )
	net.addLink (S31 ,S50 )
	net.addLink (S31 ,S86 )
	net.addLink (S32 ,S94 )
	net.addLink (S32 ,S46 )
	net.addLink (S33 ,S41 )
	net.addLink (S33 ,S36 )
	net.addLink (S34 ,S49 )
	net.addLink (S34 ,S71 )
	net.addLink (S34 ,S72 )
	net.addLink (S34 ,S52 )
	net.addLink (S34 ,S53 )
	net.addLink (S34 ,S55 )
	net.addLink (S35 ,S43 )
	net.addLink (S35 ,S85 )
	net.addLink (S35 ,S60 )
	net.addLink (S36 ,S76 )
	net.addLink (S36 ,S51 )
	net.addLink (S36 ,S54 )
	net.addLink (S37 ,S40 )
	net.addLink (S37 ,S65 )
	net.addLink (S38 ,S56 )
	net.addLink (S38 ,S63 )
	net.addLink (S39 ,S64 )
	net.addLink (S39 ,S71 )
	net.addLink (S39 ,S42 )
	net.addLink (S39 ,S46 )
	net.addLink (S39 ,S93 )
	net.addLink (S40 ,S100 )
	net.addLink (S40 ,S70 )
	net.addLink (S40 ,S77 )
	net.addLink (S40 ,S45 )
	net.addLink (S41 ,S68 )
	net.addLink (S41 ,S48 )
	net.addLink (S41 ,S59 )
	net.addLink (S41 ,S62 )
	net.addLink (S42 ,S86 )
	net.addLink (S43 ,S74 )
	net.addLink (S43 ,S100 )
	net.addLink (S44 ,S47 )
	net.addLink (S45 ,S79 )
	net.addLink (S45 ,S81 )
	net.addLink (S45 ,S52 )
	net.addLink (S45 ,S94 )
	net.addLink (S46 ,S97 )
	net.addLink (S46 ,S98 )
	net.addLink (S46 ,S72 )
	net.addLink (S46 ,S80 )
	net.addLink (S46 ,S50 )
	net.addLink (S47 ,S77 )
	net.addLink (S47 ,S62 )
	net.addLink (S48 ,S55 )
	net.addLink (S48 ,S66 )
	net.addLink (S49 ,S75 )
	net.addLink (S49 ,S63 )
	net.addLink (S50 ,S96 )
	net.addLink (S50 ,S67 )
	net.addLink (S50 ,S76 )
	net.addLink (S50 ,S60 )
	net.addLink (S51 ,S59 )
	net.addLink (S51 ,S77 )
	net.addLink (S52 ,S83 )
	net.addLink (S52 ,S79 )
	net.addLink (S53 ,S58 )
	net.addLink (S54 ,S96 )
	net.addLink (S54 ,S98 )
	net.addLink (S54 ,S57 )
	net.addLink (S54 ,S89 )
	net.addLink (S55 ,S61 )
	net.addLink (S56 ,S58 )
	net.addLink (S57 ,S68 )
	net.addLink (S58 ,S72 )
	net.addLink (S59 ,S73 )
	net.addLink (S59 ,S90 )
	net.addLink (S59 ,S63 )
	net.addLink (S60 ,S67 )
	net.addLink (S60 ,S81 )
	net.addLink (S60 ,S92 )
	net.addLink (S61 ,S74 )
	net.addLink (S62 ,S69 )
	net.addLink (S64 ,S91 )
	net.addLink (S64 ,S66 )
	net.addLink (S65 ,S78 )
	net.addLink (S65 ,S82 )
	net.addLink (S65 ,S85 )
	net.addLink (S66 ,S84 )
	net.addLink (S66 ,S92 )
	net.addLink (S70 ,S95 )
	net.addLink (S72 ,S75 )
	net.addLink (S72 ,S84 )
	net.addLink (S72 ,S89 )
	net.addLink (S73 ,S93 )
	net.addLink (S78 ,S82 )
	net.addLink (S78 ,S99 )
	net.addLink (S79 ,S83 )
	net.addLink (S80 ,S88 )
	net.addLink (S82 ,S99 )
	net.addLink (S83 ,S90 )
	net.addLink (S84 ,S100 )
	net.addLink (S85 ,S92 )
	net.addLink (S87 ,S99 )
	net.addLink (S87 ,S97 )
        

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
        S71.start(  [c0] )
        S72.start(  [c0] )
        S73.start(  [c0] )
        S74.start(  [c0] )
        S75.start(  [c0] )
        S76.start(  [c0] )
        S77.start(  [c0] )
        S78.start(  [c0] )
        S79.start(  [c0] )
        S80.start(  [c0] )
        S81.start(  [c0] )
        S82.start(  [c0] )
        S83.start(  [c0] )
        S84.start(  [c0] )
        S85.start(  [c0] )
        S86.start(  [c0] )
        S87.start(  [c0] )
        S88.start(  [c0] )
        S89.start(  [c0] )
        S90.start(  [c0] )
        S91.start(  [c0] )
        S92.start(  [c0] )
        S93.start(  [c0] )
        S94.start(  [c0] )
        S95.start(  [c0] )
        S96.start(  [c0] )
        S97.start(  [c0] )
        S98.start(  [c0] )
        S99.start(  [c0] )
        S100.start(  [c0] )

        #print "*** Running CLI"
        #CLI( net )

        #print "*** Stopping network"
        #net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
    #Topology Graph
    G.add_edges_from([(1, 4), (1, 5), (1, 6), (1, 71), (1, 11), (1, 13), (1, 14), (1, 82), (1, 20), (1, 85), (1, 7), (1, 68), (1, 27),
                      (1, 29), (1, 69), (2, 65), (2, 91), (2, 4), (2, 5), (2, 7), (2, 42), (2, 43), (2, 12), (2, 45), (2, 13), (2, 18),
                      (2, 19), (2, 21), (2, 55), (2, 15), (3, 67), (3, 4), (3, 5), (3, 8), (3, 44), (3, 14), (3, 47), (3, 83), (3, 52),
                      (3, 94), (3, 23), (3, 91), (3, 28), (3, 30), (4, 6), (4, 7), (4, 9), (4, 12), (4, 34), (4, 80), (4, 87), (4, 91),
                      (5, 6), (5, 8), (5, 9), (5, 10), (5, 11), (5, 13), (5, 16), (5, 43), (5, 26), (5, 59), (6, 65), (6, 8), (6, 11),
                      (6, 12), (6, 18), (6, 14), (6, 82), (6, 21), (6, 87), (6, 88), (6, 25), (6, 90), (7, 70), (7, 38), (7, 44), 
                      (7, 24), (7, 57), (7, 27), (8, 67), (8, 9), (8, 10), (8, 75), (8, 15), (8, 35), (8, 23), (8, 26), (9, 32), 
                      (9, 10), (10, 38), (10, 44), (10, 17), (10, 18), (10, 37), (11, 45), (11, 14), (11, 16), (11, 51), (11, 87),    
                      (11, 37), (12, 32), (12, 40), (12, 78), (12, 20), (12, 60), (13, 81), (13, 33), (13, 86), (13, 15), (13, 17),
                      (13, 54), (13, 49), (13, 28), (14, 49), (14, 45), (14, 46), (14, 17), (14, 35), (14, 20), (14, 21), (14, 29),
                      (15, 83), (15, 47), (15, 16), (15, 19), (15, 23), (15, 26), (16, 36), (16, 50), (16, 22), (16, 56), (16, 62),
                      (16, 31), (17, 33), (17, 34), (17, 71), (17, 39), (17, 48), (17, 54), (17, 55), (17, 89), (17, 95), (17, 61),
                      (17, 30), (17, 31), (18, 48), (18, 19), (18, 22), (18, 28), (18, 42), (19, 31), (19, 51), (20, 37), (20, 78),
                      (20, 84), (20, 22), (21, 32), (21, 96), (21, 70), (21, 39), (21, 24), (21, 88), (21, 25), (21, 58), (22, 64),
                      (22, 38), (22, 39), (22, 56), (23, 74), (23, 93), (23, 24), (23, 27), (23, 61), (24, 57), (24, 25), (24, 29),
                      (24, 95), (25, 66), (25, 98), (25, 80), (25, 53), (26, 40), (26, 64), (27, 69), (27, 97), (27, 76), (28, 33),
                      (28, 68), (28, 41), (28, 35), (28, 30), (29, 53), (29, 73), (30, 34), (30, 41), (30, 79), (31, 36), (31, 73),
                      (31, 50), (31, 86), (32, 94), (32, 46), (33, 41), (33, 36), (34, 49), (34, 71), (34, 72), (34, 52), (34, 53),
                      (34, 55), (35, 43), (35, 85), (35, 60), (36, 76), (36, 51), (36, 54), (37, 40), (37, 65), (38, 56), (38, 63),
                      (39, 64), (39, 71), (39, 42), (39, 46), (39, 93), (40, 100), (40, 70), (40, 77), (40, 45), (41, 68), (41, 48),
                      (41, 59), (41, 62), (42, 86), (43, 74), (43, 100), (44, 47), (45, 79), (45, 81), (45, 52), (45, 94), (46, 97),
                      (46, 98), (46, 72), (46, 80), (46, 50), (47, 77), (47, 62), (48, 55), (48, 66), (49, 75), (49, 63), (50, 96),
                      (50, 67), (50, 76), (50, 60), (51, 59), (51, 77), (52, 83), (52, 79), (53, 58), (54, 96), (54, 98), (54, 57),
                      (54, 89), (55, 61), (56, 58), (57, 68), (58, 72), (59, 73), (59, 90), (59, 63), (60, 67), (60, 81), (60, 92),
                      (61, 74), (62, 69), (64, 91), (64, 66), (65, 78), (65, 82), (65, 85), (66, 84), (66, 92), (70, 95), (72, 75),
                      (72, 84), (72, 89), (73, 93), (78, 82), (78, 99), (79, 83), (80, 88), (82, 99), (83, 90), (84, 100), (85, 92),
                      (87, 99), (87, 97)])
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
                           (67): 's67', (68): 's68', (69): 's69', (70): 's70', (71): 's71', (72): 's72', (73): 's73', (74): 's74',
                           (75): 's75', (76): 's76', (77): 's77', (78): 's78', (79): 's79', (80): 's80', (81): 's81', (82): 's82',
                           (83): 's83', (84): 's84', (85): 's85', (86): 's86', (87): 's87', (88): 's88', (89): 's89', (90): 's90',
                           (91): 's91', (92): 's92', (93): 's93', (94): 's94', (95): 's95', (96): 's96', (97): 's97', (98): 's98',
                           (99): 's99', (100): 's100'}
    #Link's Length Dictionary
    Links_Lengths_Dictionary = {(1, 4) : 167 ,(1, 5) : 739 ,(1, 6) : 222 ,(1, 71) : 222 ,(1, 11) : 423 ,(1, 13) : 919 ,(1, 14) : 404 ,
                                (1, 82) : 110 ,(1, 20) : 42 ,(1, 85) : 481 ,(1, 7) : 403 ,(1, 68) : 469 ,(1, 27) : 259 ,(1, 29) : 183,
                                (1, 69) : 336 ,(2, 65) : 423 ,(2, 91) : 651 ,(2, 4) : 710 ,(2, 5) : 333 ,(2, 7) : 318 ,(2, 42) : 277,
                                (2, 43) : 399 ,(2, 12) : 821 ,(2, 45) : 391 ,(2, 13) : 307 ,(2, 18) : 359 ,(2, 19) : 313 ,(2, 21):451,
                                (2, 55) : 135 ,(2, 15) : 492 ,(3, 67) : 176 ,(3, 4) : 526 ,(3, 5) : 378 ,(3, 8) : 384 ,(3, 44) : 221 ,
                                (3, 14) : 524 ,(3, 47) : 128 ,(3, 83) : 356 ,(3, 52) : 634 ,(3, 94) : 422 ,(3, 23) : 95 ,(3, 91) : 470,
                                (3, 28) : 355 ,(3, 30) : 445 ,(4, 6) : 58 ,(4, 7) : 546 ,(4, 9) : 620 ,(4, 12) : 160 ,(4, 34) : 654 ,
                                (4, 80) : 569 ,(4, 87) : 97 ,(4, 91) : 160 ,(5, 6) : 753 ,(5, 8) : 219 ,(5, 9) : 464 ,(5, 10) : 415 ,
                                (5, 11) : 532 ,(5, 13) : 352 ,(5, 16) : 148 ,(5, 43) : 216 ,(5, 26) : 286 ,(5, 59) : 134 ,(6, 65) :367,
                                (6, 8) : 575 ,(6, 11) : 291 ,(6, 12) : 108 ,(6, 18) : 1015 ,(6, 14) : 244 ,(6, 82) : 202,(6, 21) : 436,
                                (6, 87) : 124 ,(6, 88) : 465 ,(6, 25) : 445 ,(6, 90) : 702 ,(7, 70) : 173 ,(7, 38) : 235 ,(7, 44) :217,
                                (7, 24) : 61 ,(7, 57) : 283 ,(7, 27) : 330 ,(8, 67) : 396 ,(8, 9) : 268 ,(8, 10) : 249 ,(8, 75) : 274 ,
                                (8, 15) : 87 ,(8, 35) : 107 ,(8, 23) : 473 ,(8, 26) : 104 ,(9, 32) : 167 ,(9, 10) : 371 ,(10, 38) :679,
                                (10, 44) : 527 ,(10, 17) : 502 ,(10, 18) : 689 ,(10, 37) : 297 ,(11, 45) : 270 ,(11, 14) : 66 ,
                                (11, 16) : 665 ,(11, 51) : 731 ,(11, 87) : 414 ,(11, 37) : 331 ,(12, 32) : 431 ,(12, 40) : 485 ,
                                (12, 78) : 291 ,(12, 20) : 353,(12, 60) : 668,(13, 81) : 292,(13, 33) : 42,(13, 86) : 122,(13, 15):641,
                                (13, 17) : 388 ,(13, 54) : 107 ,(13, 49) : 753 ,(13, 28) : 150 ,(14, 49) : 324 ,(14, 45) : 332 ,
                                (14, 46) : 420 ,(14, 17) : 721 ,(14, 35) : 282 ,(14, 20) : 405 ,(14, 21) : 547 ,(14, 29) : 488 ,
                                (15, 83) : 106 ,(15, 47) : 348 ,(15, 16) : 447 ,(15, 19) : 414 ,(15, 23) : 499 ,(15, 26) : 111 ,
                                (16, 36) : 188 ,(16, 50) : 159 ,(16, 22) : 640 ,(16, 56) : 742 ,(16, 62) : 214 ,(16, 31) : 184 ,
                                (17, 33) : 429 ,(17, 34) : 53 ,(17, 71) : 381 ,(17, 39) : 414 ,(17, 48) : 125 ,(17, 54) : 299 ,
                                (17, 55) : 106 ,(17, 89) : 164 ,(17, 95) : 301 ,(17, 61) : 121 ,(17, 30) : 495 ,(17, 31) : 221 ,
                                (18, 48) : 447 ,(18, 19) : 204 ,(18, 22) : 665 ,(18, 28) : 164 ,(18, 42) : 549 ,(19, 31) : 213 ,
                                (19, 51) : 115 ,(20, 37) : 104 ,(20, 78) : 64 ,(20, 84) : 211 ,(20, 22) : 576 ,(21, 32) : 743 ,
                                (21, 96) : 622 ,(21, 70) : 109 ,(21, 39) : 281 ,(21, 24) : 222 ,(21, 88) : 134 ,(21, 25) : 128 ,
                                (21, 58) : 241 ,(22, 64) : 628 ,(22, 38) : 17 ,(22, 39) : 236 ,(22, 56) : 134 ,(23, 74) : 242 ,
                                (23, 93) : 138 ,(23, 24) : 191 ,(23, 27) : 471 ,(23, 61) : 242 ,(24, 57) : 289 ,(24, 25) : 216 ,
                                (24, 29) : 608 ,(24, 95) : 524 ,(25, 66) : 315 ,(25, 98) : 696 ,(25, 80) : 218 ,(25, 53) : 187 ,
                                (26, 40) : 144 ,(26, 64) : 385 ,(27, 69) : 549 ,(27, 97) : 339 ,(27, 76) : 551 ,(28, 33) : 170 ,
                                (28, 68) : 325 ,(28, 41) : 277 ,(28, 35) : 505 ,(28, 30) : 227 ,(29, 53) : 279 ,(29, 73) : 767 ,
                                (30, 34) : 476 ,(30, 41) : 503 ,(30, 79) : 15 ,(31, 36) : 9 ,(31, 73) : 699 ,(31, 50) : 63 ,
                                (31, 86) : 101 ,(32, 94) : 345 ,(32, 46) : 578 ,(33, 41) : 293 ,(33, 36) : 245 ,(34, 49) : 679 ,
                                (34, 71) : 333 ,(34, 72) : 276 ,(34, 52) : 740 ,(34, 53) : 445 ,(34, 55) : 152 ,(35, 43) : 111 ,
                                (35, 85) : 242 ,(35, 60) : 192 ,(36, 76) : 421 ,(36, 51) : 306 ,(36, 54) : 175 ,(37, 40) : 475 ,
                                (37, 65) : 225 ,(38, 56) : 137 ,(38, 63) : 682 ,(39, 64) : 613 ,(39, 71) : 425 ,(39, 42) : 359 ,
                                (39, 46) : 452 ,(39, 93) : 366 ,(40, 100) : 557 ,(40, 70) : 516 ,(40, 77) : 203 ,(40, 45) : 174 ,
                                (41, 68) : 367 ,(41, 48) : 132 ,(41, 59) : 474 ,(41, 62) : 337 ,(42, 86) : 378 ,(43, 74) : 662 ,
                                (43, 100) : 524 ,(44, 47) : 267 ,(45, 79) : 341 ,(45, 81) : 383 ,(45, 52) : 347 ,(45, 94) : 144 ,
                                (46, 97) : 463 ,(46, 98) : 657 ,(46, 72) : 147 ,(46, 80) : 315 ,(46, 50) : 455 ,(47, 77) : 554 ,
                                (47, 62) : 69 ,(48, 55) : 73 ,(48, 66) : 664 ,(49, 75) : 242 ,(49, 63) : 264 ,(50, 96) : 35 ,
                                (50, 67) : 153 ,(50, 76) : 453 ,(50, 60) : 338 ,(51, 59) : 67 ,(51, 77) : 773 ,(52, 83) : 279 ,
                                (52, 79) : 399 ,(53, 58) : 350 ,(54, 96) : 100 ,(54, 98) : 163 ,(54, 57) : 253 ,(54, 89) : 449 ,
                                (55, 61) : 50 ,(56, 58) : 208 ,(57, 68) : 165 ,(58, 72) : 583 ,(59, 73) : 613 ,(59, 90) : 383 ,
                                (59, 63) : 382 ,(60, 67) : 294 ,(60, 81) : 254 ,(60, 92) : 572 ,(61, 74) : 293 ,(62, 69) : 414 ,
                                (64, 91) : 319 ,(64, 66) : 49 ,(65, 78) : 213 ,(65, 82) : 310 ,(65, 85) : 506 ,(66, 84) : 189 ,
                                (66, 92) : 250 ,(70, 95) : 617 ,(72, 75) : 315 ,(72, 84) : 187 ,(72, 89) : 406 ,(73, 93) : 839 ,
                                (78, 82) : 111 ,(78, 99) : 34 ,(79, 83) : 259 ,(80, 88) : 230 ,(82, 99) : 122 ,(83, 90) : 212 ,
                                (84, 100) : 167 ,(85, 92) : 205 ,(87, 99) : 206 ,(87, 97) : 93 }


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
    for i in range (len(Edges)):
        Length_Sum= Length_Sum + Links_Lengths_Dictionary[Edges[i]]
    #print 'The Total length is :', Length_Sum
    for i in range (len(Edges)):
        MTTR.append (round(float(Links_Lengths_Dictionary[Edges[i]]) / (float (Length_Sum)) *100))
    print 'The MTTR of each link: \n', MTTR
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

          def __init__(self, ID=None, Name=None, Length=None, MTBF=None, MTTR=None, Next_Failure=None,  F_Count=None, P_Failure=None,
                        Link_state=None):

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
           if (L[x].P_Failure >=50):
                    print 'The link', L[x].ID, 'Has a failure probability over the threshould'
                    Dicision = random.randint(0, 1)
                    if Dicision == 1 :  #Means the controller will receive a notification and its a true positive
                           if ((L[x].Next_Failure) > 2):
                              wt = (L[x].Next_Failure) - 2
                              print 'The controller will receive a notification after', wt, 'mins'
                              scheduler.enter(wt*60, 1, Send_To_Controller, (L[x].ID,)) #send a notification 
                                                #about the link who will fail after two mins (i.e. wt * 60)
                           else:
                                  scheduler.enter(2, 1, Send_To_Controller, (L[x].ID,)) #send a notification after 2 sec
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
