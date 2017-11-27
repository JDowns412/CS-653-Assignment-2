import json, pprint
import numpy as np
import matplotlib.pyplot as plt

def Main():

	TraceFile= open('C:/Users/user/Documents/assignment2/results3.json').read()
	Values=json.loads(TraceFile)
	Results={'latency':{}, 'throughput':{}}
	LatencyListRenoDropTail=[]
	LatencyListRenoRED=[]
	LatencyListSackDropTail=[]
	LatencyListSackRED=[]
	TimeStampRenoDropTail=[]
	TimeStampRenoRED=[]
	TimeStampSackDropTail=[]
	TimeStampSackRED=[]
	t2=0
	t1=0
	for key,val in Values.items():
		listOFPacketIds={}
		largestpktid=0
		latencysum=0
		countReceived=0
		for key1,val1 in val.items():
			for key2,val2 in val1.items():
				if(val2['pktType']=='tcp'):
					if(val2['pktId']>largestpktid):
						largestpktid=val2['pktId']
					if val2['pktId'] not in listOFPacketIds:
						listOFPacketIds[val2['pktId']]={}
						countReceived=countReceived+1
						listOFPacketIds[val2['pktId']]['type'] = val2['pktType']
						if(val2['event']=='+'):
							listOFPacketIds[val2['pktId']]['t1'] = val2['time']
					if (val2['event']=='r'):
						listOFPacketIds[val2['pktId']]['t2'] = val2['time']
		for key3, val3 in listOFPacketIds.items():
			t1=val3['t1']
			if ('t2' in val3):
				t2=val3['t2']
				latencysum=latencysum+t2-t1
			if (key=='Reno_DropTail - 75%'):
				if t2 not in TimeStampRenoDropTail:
					LatencyListRenoDropTail.append(t2-t1)
					TimeStampRenoDropTail.append(t2)
			if(key=='SACK_RED - 75%'):
				if t2 not in TimeStampSackRED:
					LatencyListSackRED.append(t2-t1)
					TimeStampSackRED.append(t2)
			if(key=='Reno_RED - 75%'):
				if t2 not in TimeStampRenoRED:
					LatencyListRenoRED.append(t2-t1)
					TimeStampRenoRED.append(t2)
			if(key=='SACK_DropTail - 75%'):
				if t2 not in TimeStampSackDropTail:
					LatencyListSackDropTail.append(t2-t1)
					TimeStampSackDropTail.append(t2)
		latency=(latencysum/countReceived)
		Results['latency'][key]=latency

	plt.figure(4, figsize=(7,5))  
	plt.ylim(0.03, 0.05)
	
	plt.plot(TimeStampRenoRED, LatencyListRenoRED)
	plt.plot(TimeStampSackDropTail, LatencyListSackDropTail)
	plt.plot(TimeStampSackRED, LatencyListSackRED)
	plt.plot(TimeStampRenoDropTail, LatencyListRenoDropTail)

	labels=['RenoRED', 'SackDropTail', 'SackRED', 'RenoDropTail']
	plt.legend(labels,loc="best", shadow=True, title="Variant Type", fancybox=True)
	plt.grid(True) 
	plt.ylabel("Latency")
	plt.xlabel("Time") l
	plt.title("Time vs Latency for RenoDropTail") 
	plt.savefig("Latencyplotrenodroptail.png")
	plt.clf()				
	
	ThroughputListRenoDropTail=[]
	ThroughputListRenoRED=[]
	ThroughputListSackDropTail=[]
	ThroughputListSackRED=[]
	TimeStampRenoDropTail=[]
	TimeStampRenoRED=[]
	TimeStampSackDropTail=[]
	TimeStampSackRED=[]
	t2=0
	t1=0

	for key,val in Values.items():
		listofSeqNos={}
		timestamp=0
		SeqNo=0
		for key1,val1 in val.items():
			for key2,val2 in val1.items():
				if(val2['pktType']!='cbr'):
					if val2['pktId'] not in listofSeqNos:
						listofSeqNos[val2['pktId']]={}
						listofSeqNos[val2['pktId']]['seqNo']=val2['seqNum']
						listofSeqNos[val2['pktId']]['t1']=val2['time']
						if (val2['seqNum']>SeqNo):
							SeqNo=val2['seqNum']
						if (val2['time']>timestamp):
							timestamp= val2['time']
		throughput=SeqNo/timestamp
		Results['throughput'][key]=throughput
		for key3, val3 in listofSeqNos.items():
			t1=val3['t1']
			if (key=='Reno_DropTail - 75%'):
				if t1 not in TimeStampRenoDropTail:
					ThroughputListRenoDropTail.append(val3['seqNo'])
					TimeStampRenoDropTail.append(t1)
			if(key=='SACK_RED - 75%'):
				if t1 not in TimeStampSackRED:
					ThroughputListSackRED.append(val3['seqNo'])
					TimeStampSackRED.append(t1)
			if(key=='Reno_RED - 75%'):

				if t1 not in TimeStampRenoRED:
					ThroughputListRenoRED.append(val3['seqNo'])
					TimeStampRenoRED.append(t1)
			if(key=='SACK_DropTail - 75%'):
				if t1 not in TimeStampSackDropTail:
					ThroughputListSackDropTail.append(val3['seqNo'])
					TimeStampSackDropTail.append(t1)
	
	
	
	plt.figure(4, figsize=(7,5))  
	plt.plot(TimeStampRenoRED, ThroughputListRenoRED)
	plt.plot(TimeStampSackDropTail, ThroughputListSackDropTail)
	plt.plot(TimeStampSackRED, ThroughputListSackRED)
	plt.plot(TimeStampRenoDropTail, ThroughputListRenoDropTail)
	labels=['RenoRED', 'SackDropTail', 'SackRED', 'RenoDropTail']
	plt.legend(labels,loc="best", shadow=True, title="Variant Type", fancybox=True)
	plt.grid(True) 
	plt.ylabel("Throughput") 
	plt.xlabel("Time") 
	plt.title("Time vs Throughput") 

	plt.savefig("ThroughputDropTailRED.png")
	plt.clf()				
	
	pprint.pprint(Results)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
if __name__=="__main__":
	Main()