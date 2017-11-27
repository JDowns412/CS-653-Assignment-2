import json, pprint
import numpy as np
import matplotlib.pyplot as plt

def Main():
	TraceFile= open('C:/Users/user/Documents/assignment2/results1Shreya.json').read()
	Values=json.loads(TraceFile)
	Results={'latency':{}, 'throughput':{}, 'packetdrops':{}}
	for key,val in Values.items():
		listOFPacketIds={}
		largestpktid=0
		latencysum=0
		countReceived=0
		for key1,val1 in val.items():
			for key2,val2 in val1.items():
				if(val2['pktType']!='cbr'):
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
			#print(countReceived)
		for key3, val3 in listOFPacketIds.items():
			t1=val3['t1']
			if ('t2' in val3):
				t2=val3['t2']
				latencysum=latencysum+t2-t1
		latency=(latencysum/countReceived)*3
		SeqNo=0
		timestamp=0
		Results['latency'][key]=latency
		
	#print ("\n ")
	#####################Throughput################################
	ThroughPutResults={}
	for key,val in Values.items():
		listofSeqNos={}
		for key1,val1 in val.items():
			for key2,val2 in val1.items():
				if(val2['pktType']!='cbr'):

					if val2['pktType'] not in listofSeqNos:
						if val2['pktType']=='tcp':
							listofSeqNos[val2['pktType']]={}
						if (val2['seqNum']>SeqNo):
							SeqNo=val2['seqNum']
						if (val2['time']>timestamp):
							timestamp= val2['time']
		#print(listofSeqNos)			
		#print("seqno is ", SeqNo)
		#print("timestamp is ", timestamp)
		throughput=SeqNo/timestamp
		Results['throughput'][key]=throughput
	#pprint.pprint(Results)
	
	#################################Drops################################
	DropResults={}
	listofPacketDrops={}
	
	for key,val in Values.items():
		CountOfDrops=0
		for key1,val1 in val.items():
			for key2,val2 in val1.items():
		#if val['pktType'] not in listofSeqNos:
			#if (val['pktType']=='cbr'):
			#listOFPacketIds[val['pktType']]={}
				#print(val2['event']=='d')
				if (val2['event']=='d'):
					CountOfDrops= CountOfDrops+1
					#print(" Encountered packet drop at ", key, " ", key1, " ", key2)
					#print (" drop count now ", CountOfDrops)
		Results['packetdrops'][key]= CountOfDrops
	pprint.pprint(Results)

	print("Writing output JSON to results.json")
	with open('Analysis.json', 'w') as f:
		json.dump(Results, f, indent=4)
		
		
	AverageResultsLatencyTahoe=[]
	AverageResultsLatencyReno=[]
	AverageResultsLatencyNewReno=[]
	AverageResultsLatencyVegas=[]
	for key, val in Results['latency'].items():
		temp= key.split(" ")
		if (temp[0]=='Tahoe'):
			AverageResultsLatencyTahoe.append(val)
		if (temp[0]=='Reno'):
			AverageResultsLatencyReno.append(val)
		if (temp[0]=='NewReno'):
			AverageResultsLatencyNewReno.append(val)
		if (temp[0]=='Vegas'):
			AverageResultsLatencyVegas.append(val)
			
	#pprint.pprint(AverageResultsLatencyTahoe)
	#pprint.pprint(AverageResultsLatencyReno)
	#pprint.pprint(AverageResultsLatencyNewReno)
	#pprint.pprint(AverageResultsLatencyVegas)
	
	FinalTahoeLatency=0
	for item in AverageResultsLatencyTahoe:
		FinalTahoeLatency+=item
	FinalRenoLatency=0
	for item in AverageResultsLatencyReno:
		FinalRenoLatency+=item
	FinalNewRenoLatency=0
	for item in AverageResultsLatencyNewReno:
		FinalNewRenoLatency+=item
	FinalVegasLatency =0
	for item in AverageResultsLatencyVegas:
		FinalVegasLatency+=item
		
	#print("Final latency Tahoe ", FinalTahoeLatency)
	#print(" final latency Reno ", FinalRenoLatency)
	#print("Final latency NewReno ", FinalNewRenoLatency)
	#print("final latency Vegas ", FinalVegasLatency)
	
	####################averagethroughputs####################
	AverageResultsThroughputTahoe=[]
	AverageResultsThroughputReno=[]
	AverageResultsThroughputNewReno=[]
	AverageResultsThroughputVegas=[]
	for key, val in Results['throughput'].items():
		temp= key.split(" ")
		if (temp[0]=='Tahoe'):
			AverageResultsThroughputTahoe.append(val)
		if (temp[0]=='Reno'):
			AverageResultsThroughputReno.append(val)
		if (temp[0]=='NewReno'):
			AverageResultsThroughputNewReno.append(val)
		if (temp[0]=='Vegas'):
			AverageResultsThroughputVegas.append(val)
			
	
	FinalThroughputTahoe=0
	FinalThroughputReno=0
	FinalThroughputNewReno=0
	FinalThroughputVegas=0
	
	for item in AverageResultsThroughputTahoe:
		FinalThroughputTahoe+=item
		
	for item in AverageResultsThroughputReno:
		FinalThroughputReno+=item
		
	for item in AverageResultsThroughputNewReno:
		FinalThroughputNewReno+=item
	for item in AverageResultsLatencyVegas:
		FinalThroughputVegas+=item
		
	#print("Final Throughput Tahoe ", FinalThroughputTahoe)
	#print("Final Throughput Reno ", FinalThroughputReno)
	#print("Final Throughput NewReno ", FinalThroughputNewReno)
	#print("Final Throughput Vegas ", FinalThroughputVegas)
	
	AveragepacketdropsTahoe=[]
	AveragepacketdropsReno=[]
	AveragepacketdropsNewReno=[]
	AveragePacketDropsVegas=[]
	
	for key, val in Results['packetdrops'].items():
		temp= key.split(" ")
		if (temp[0]=='Tahoe'):
			AveragepacketdropsTahoe.append(val)
		if (temp[0]=='Reno'):
			AveragepacketdropsReno.append(val)
		if (temp[0]=='NewReno'):
			AveragepacketdropsNewReno.append(val)
		if (temp[0]=='Vegas'):
			AveragePacketDropsVegas.append(val)
			
	FinalPacketDropTahoe=0
	FinalPacketDropReno=0
	FinalPacketDropNewReno=0
	FinalPacketDropVegas=0
	
	for item in AveragepacketdropsTahoe:
		FinalPacketDropTahoe+=item
	
	for item in AveragepacketdropsReno:
		FinalPacketDropReno+=item
		
	for item in AveragepacketdropsNewReno:
		FinalPacketDropNewReno+=item
		
	for item in AveragePacketDropsVegas:
		FinalPacketDropVegas+=item
		
	#print("Final PacketDrop Tahoe ", FinalPacketDropTahoe)
	#print("Final PacketDrop Reno ", FinalPacketDropReno)
	#print("Final PacketDrop NewReno ", FinalPacketDropNewReno)
	#print("Final PacketDrop Vegas ", FinalPacketDropVegas)

if __name__=="__main__":
	Main()