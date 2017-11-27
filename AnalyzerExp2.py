import json, pprint
import numpy as np
import matplotlib.pyplot as plt

def Main():
	TraceFile= open('C:/Users/user/Documents/assignment2/results2Shreya(LateCBR).json').read()
	Values=json.loads(TraceFile)
	Results={'latency':{1:{'Reno1':{},'Reno2':{}},
						2:{'NewReno1':{}, 'Reno2':{}},
						3:{'Vegas1':{}, 'Vegas2':{}},
						4:{'NewReno1':{}, 'Vegas2':{}}}, 
			'throughput':{1:{'Reno1':{},'Reno2':{}},
						2:{'NewReno1':{}, 'Reno2':{}},
						3:{'Vegas1':{}, 'Vegas2':{}},
						4:{'NewReno1':{}, 'Vegas2':{}}}, 
			'packetdrops':{1:{'Reno1':{},'Reno2':{}},
						2:{'NewReno1':{}, 'Reno2':{}},
						3:{'Vegas1':{}, 'Vegas2':{}},
						4:{'NewReno1':{}, 'Vegas2':{}}
			}}
	LatencyReno1pair1=[]
	LatencyReno2pair1=[]
	LatencyNewReno1pair2=[]
	LatencyReno2pair2=[]
	LatencyVegas1pair3=[]
	LatencyVegas2pair3=[]
	LatencyNewReno1pair4=[]
	LatencyVegas2pair4=[]
	i=1
	LatencyByPercent={}
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	for key,val in Values.items():
		listOFPacketIds1={}
		listOFPacketIds2={}
		largestpktid1=0
		largestpktid2=0
		latencysum1=0
		countReceived1=0
		latencysum2=0
		countReceived2=0
		for key1,val1 in val.items():
			for key2,val2 in val1.items():
				if (val2['flowId']==1):
					if(val2['pktId']>largestpktid1):
						largestpktid1=val2['pktId']
					if val2['pktId'] not in listOFPacketIds1:
						listOFPacketIds1[val2['pktId']]={}
						countReceived1=countReceived1+1

					listOFPacketIds1[val2['pktId']]['type'] = val2['pktType']
					if(val2['event']=='+'):
						listOFPacketIds1[val2['pktId']]['t1'] = val2['time']
					if (val2['event']=='r'):
						listOFPacketIds1[val2['pktId']]['t2'] = val2['time']
				if (val2['flowId']==2):
				
					if(val2['pktId']>largestpktid2):
						largestpktid2=val2['pktId']
					if val2['pktId'] not in listOFPacketIds2:
						listOFPacketIds2[val2['pktId']]={}
						countReceived2=countReceived2+1
					listOFPacketIds2[val2['pktId']]['type'] = val2['pktType']
					if(val2['event']=='+'):
						listOFPacketIds2[val2['pktId']]['t1'] = val2['time']
					if (val2['event']=='r'):
						listOFPacketIds2[val2['pktId']]['t2'] = val2['time']
		#pprint.pprint(listOFPacketIds1)
		for key3, val3 in listOFPacketIds1.items():
			t1=val3['t1']
			if ('t2' in val3):
				t2=val3['t2']
				latencysum1=latencysum1+t2-t1
				#print(latencysum1)
		latency1=(latencysum1/countReceived1)*3
		#print(countReceived2)

		for key3, val3 in listOFPacketIds2.items():
			t1=val3['t1']
			if ('t2' in val3):
				t2=val3['t2']
				latencysum2=latencysum2+t2-t1
		latency2=(latencysum2/countReceived2)*3
		temp=key.split(" ")
		tempnew=temp[0].split("_")
		if (temp[0]=='Reno_Reno'):
			if key not in LatencyByPercent:
				LatencyByPercent[key]={}
				if ('%s%i'%(tempnew[0],1)) not in LatencyByPercent[key]: 
					#print('%s%i'%(tempnew[0],1))
					LatencyByPercent[key]['%s%i'%(tempnew[0],1)]= {}
			LatencyByPercent[key]['%s%i'%(tempnew[0],1)]=latency1
			Results['latency'][1]['%s%i'%(tempnew[0],1)]=latency1
			if ('%s%i'%(tempnew[1],2)) not in LatencyByPercent[key]: 
					LatencyByPercent[key]['%s%i'%(tempnew[1],2)]= {}
			LatencyByPercent[key]['%s%i'%(tempnew[1],2)]=latency2
			Results['latency'][1]['%s%i'%(tempnew[1],2)]=latency2
		if (temp[0]=='NewReno_Reno'):
			if key not in LatencyByPercent:
				LatencyByPercent[key]={}
				if ('%s%i'%(tempnew[0],1)) not in LatencyByPercent[key]: 
					#print('%s%i'%(tempnew[0],1))
					LatencyByPercent[key]['%s%i'%(tempnew[0],1)]= {}
			LatencyByPercent[key]['%s%i'%(tempnew[0],1)]=latency1
			Results['latency'][2]['%s%i'%(tempnew[0],1)]=latency1
			if ('%s%i'%(tempnew[1],2)) not in LatencyByPercent[key]: 
					LatencyByPercent[key]['%s%i'%(tempnew[1],2)]= {}
			LatencyByPercent[key]['%s%i'%(tempnew[1],2)]=latency2
			Results['latency'][2]['%s%i'%(tempnew[1],2)]=latency2
		if (temp[0]=='Vegas_Vegas'):
			if key not in LatencyByPercent:
				LatencyByPercent[key]={}
				if ('%s%i'%(tempnew[0],1)) not in LatencyByPercent[key]: 
					#print('%s%i'%(tempnew[0],1))
					LatencyByPercent[key]['%s%i'%(tempnew[0],1)]= {}
			LatencyByPercent[key]['%s%i'%(tempnew[0],1)]=latency1
			Results['latency'][3]['%s%i'%(tempnew[0],1)]=latency1
			if ('%s%i'%(tempnew[1],2)) not in LatencyByPercent[key]: 
					LatencyByPercent[key]['%s%i'%(tempnew[1],2)]= {}
			LatencyByPercent[key]['%s%i'%(tempnew[1],2)]=latency2
			Results['latency'][3]['%s%i'%(tempnew[1],2)]=latency2
		if (temp[0]=='NewReno_Vegas'):
			if key not in LatencyByPercent:
				LatencyByPercent[key]={}
				if ('%s%i'%(tempnew[0],1)) not in LatencyByPercent[key]: 
					#print('%s%i'%(tempnew[0],1))
					LatencyByPercent[key]['%s%i'%(tempnew[0],1)]= {}
			LatencyByPercent[key]['%s%i'%(tempnew[0],1)]=latency1
			Results['latency'][4]['%s%i'%(tempnew[0],1)]=latency1
			if ('%s%i'%(tempnew[1],2)) not in LatencyByPercent[key]: 
					LatencyByPercent[key]['%s%i'%(tempnew[1],2)]= {}
			LatencyByPercent[key]['%s%i'%(tempnew[1],2)]=latency2
			Results['latency'][4]['%s%i'%(tempnew[1],2)]=latency2
			
	#pprint.pprint(LatencyByPercent)
	#####################Throughput################################
	SeqNo1=0
	SeqNo2=0
	timestamp1=0
	timestamp2=0
	ThroughPutResults={}
	ThroughputByPercent={}
	for key,val in Values.items():
		listofSeqNos1={}
		listofSeqNos2={}
		for key1,val1 in val.items():
			for key2,val2 in val1.items():
				if (val2['flowId']==1):
					if val2['pktType'] not in listofSeqNos1:
						if val2['pktType']=='tcp':
							listofSeqNos1[val2['pktType']]={}
						if (val2['seqNum']>SeqNo1):
							SeqNo1=val2['seqNum']
						if (val2['time']>timestamp1):
							timestamp1= val2['time']
				if (val2['flowId']==2):
					if val2['pktType'] not in listofSeqNos2:
						if val2['pktType']=='tcp':
							listofSeqNos2[val2['pktType']]={}
						if (val2['seqNum']>SeqNo2):
							SeqNo2=val2['seqNum']
						if (val2['time']>timestamp2):
							timestamp2= val2['time']
		throughput1=SeqNo1/timestamp1
		
		throughput2=SeqNo2/timestamp2
		
		temp=key.split(" ")
		tempnew=temp[0].split("_")
		if (temp[0]=='Reno_Reno'):
			if key not in ThroughputByPercent:
				ThroughputByPercent[key]={}
				if ('%s%i'%(tempnew[0],1)) not in ThroughputByPercent[key]: 
					ThroughputByPercent[key]['%s%i'%(tempnew[0],1)]= {}
			ThroughputByPercent[key]['%s%i'%(tempnew[0],1)]=throughput1
			Results['throughput'][1]['%s%i'%(tempnew[0],1)]=throughput1
			if ('%s%i'%(tempnew[1],2)) not in ThroughputByPercent[key]: 
					ThroughputByPercent[key]['%s%i'%(tempnew[1],2)]= {}
			ThroughputByPercent[key]['%s%i'%(tempnew[1],2)]=throughput2
			Results['throughput'][1]['%s%i'%(tempnew[1],2)]=throughput2
		if (temp[0]=='NewReno_Reno'):
			#print(temp[0])
			#tempnew=temp[0].split("_")
			#print(tempnew[0])
			#print(tempnew[1])
			if key not in ThroughputByPercent:
				ThroughputByPercent[key]={}
				if ('%s%i'%(tempnew[0],1)) not in ThroughputByPercent[key]: 
					#print('%s%i'%(tempnew[0],1))
					ThroughputByPercent[key]['%s%i'%(tempnew[0],1)]= {}
			ThroughputByPercent[key]['%s%i'%(tempnew[0],1)]=throughput1
			Results['throughput'][2]['%s%i'%(tempnew[0],1)]=throughput1
			if ('%s%i'%(tempnew[1],2)) not in ThroughputByPercent[key]: 
					#print('%s%i'%(tempnew[0],2))
					ThroughputByPercent[key]['%s%i'%(tempnew[1],2)]= {}
			ThroughputByPercent[key]['%s%i'%(tempnew[1],2)]=throughput2
			Results['throughput'][2]['%s%i'%(tempnew[1],2)]=throughput2
		if (temp[0]=='Vegas_Vegas'):
			if key not in ThroughputByPercent:
				ThroughputByPercent[key]={}
				if ('%s%i'%(tempnew[0],1)) not in ThroughputByPercent[key]: 
					ThroughputByPercent[key]['%s%i'%(tempnew[0],1)]= {}
			ThroughputByPercent[key]['%s%i'%(tempnew[0],1)]=throughput1
			Results['throughput'][3]['%s%i'%(tempnew[0],1)]=throughput1
			if ('%s%i'%(tempnew[1],2)) not in ThroughputByPercent[key]: 
					ThroughputByPercent[key]['%s%i'%(tempnew[1],2)]= {}
			ThroughputByPercent[key]['%s%i'%(tempnew[1],2)]=throughput2
			Results['throughput'][3]['%s%i'%(tempnew[1],2)]=throughput2
		if (temp[0]=='NewReno_Vegas'):
			if key not in ThroughputByPercent:
				ThroughputByPercent[key]={}
				if ('%s%i'%(tempnew[0],1)) not in ThroughputByPercent[key]: 
					ThroughputByPercent[key]['%s%i'%(tempnew[0],1)]= {}
			ThroughputByPercent[key]['%s%i'%(tempnew[0],1)]=throughput1
			Results['throughput'][4]['%s%i'%(tempnew[0],1)]=throughput1
			if ('%s%i'%(tempnew[1],2)) not in ThroughputByPercent[key]: 
				ThroughputByPercent[key]['%s%i'%(tempnew[1],2)]= {}
			ThroughputByPercent[key]['%s%i'%(tempnew[1],2)]=throughput2
			Results['throughput'][4]['%s%i'%(tempnew[1],2)]=throughput2
	#pprint.pprint(Results)
	#pprint.pprint(ThroughputByPercent)
	#################################Drops################################
	DropResults={}
	listofPacketDrops={}
	PacketDropsByPercent={}
	for key,val in Values.items():
		CountOfDrops1=0
		CountOfDrops2=0
		for key1,val1 in val.items():
			for key2,val2 in val1.items():
		#if val['pktType'] not in listofSeqNos:
			#if (val['pktType']=='cbr'):
			#listOFPacketIds[val['pktType']]={}
				#print(val2['event']=='d')
				if (val2['event']=='d'):
					if (val2['flowId']==1):
						CountOfDrops1= CountOfDrops1+1
						#print(" Encountered packet drop at ", key, " ", key1, " ", key2)
						#print (" drop count now ", CountOfDrops)
					if (val2['flowId']==2):
						CountOfDrops2= CountOfDrops2+1
		#print(CountOfDrops1)
		#print(CountOfDrops2)
		temp=key.split(" ")
		tempnew=temp[0].split("_")
		if (temp[0]=='Reno_Reno'):
			if key not in PacketDropsByPercent:
				PacketDropsByPercent[key]={}
				if ('%s%i'%(tempnew[0],1)) not in PacketDropsByPercent[key]: 
					PacketDropsByPercent[key]['%s%i'%(tempnew[0],1)]= {}
			PacketDropsByPercent[key]['%s%i'%(tempnew[0],1)]=CountOfDrops1
			Results['packetdrops'][1]['%s%i'%(tempnew[0],1)]=CountOfDrops1
			if ('%s%i'%(tempnew[1],2)) not in PacketDropsByPercent[key]: 
				PacketDropsByPercent[key]['%s%i'%(tempnew[1],2)]= {}
			PacketDropsByPercent[key]['%s%i'%(tempnew[1],2)]=CountOfDrops2
			Results['packetdrops'][1]['%s%i'%(tempnew[1],2)]=CountOfDrops2
		if (temp[0]=='NewReno_Reno'):
			if key not in PacketDropsByPercent:
				PacketDropsByPercent[key]={}
				if ('%s%i'%(tempnew[0],1)) not in PacketDropsByPercent[key]: 
					PacketDropsByPercent[key]['%s%i'%(tempnew[0],1)]= {}
			PacketDropsByPercent[key]['%s%i'%(tempnew[0],1)]=CountOfDrops1
			Results['packetdrops'][2]['%s%i'%(tempnew[0],1)]=CountOfDrops1
			if ('%s%i'%(tempnew[1],2)) not in PacketDropsByPercent[key]: 
				PacketDropsByPercent[key]['%s%i'%(tempnew[1],2)]= {}
			PacketDropsByPercent[key]['%s%i'%(tempnew[1],2)]=CountOfDrops2
			Results['packetdrops'][2]['%s%i'%(tempnew[1],2)]=CountOfDrops2
		if (temp[0]=='Vegas_Vegas'):
			if key not in PacketDropsByPercent:
				PacketDropsByPercent[key]={}
				if ('%s%i'%(tempnew[0],1)) not in PacketDropsByPercent[key]: 
					PacketDropsByPercent[key]['%s%i'%(tempnew[0],1)]= {}
			PacketDropsByPercent[key]['%s%i'%(tempnew[0],1)]=CountOfDrops1
			Results['packetdrops'][3]['%s%i'%(tempnew[0],1)]=CountOfDrops1
			if ('%s%i'%(tempnew[1],2)) not in PacketDropsByPercent[key]: 
				PacketDropsByPercent[key]['%s%i'%(tempnew[1],2)]= {}
			PacketDropsByPercent[key]['%s%i'%(tempnew[1],2)]=CountOfDrops2
			Results['packetdrops'][3]['%s%i'%(tempnew[1],2)]=CountOfDrops2
		if (temp[0]=='NewReno_Vegas'):
			if key not in PacketDropsByPercent:
				PacketDropsByPercent[key]={}
				if ('%s%i'%(tempnew[0],1)) not in PacketDropsByPercent[key]: 
					PacketDropsByPercent[key]['%s%i'%(tempnew[0],1)]= {}
			PacketDropsByPercent[key]['%s%i'%(tempnew[0],1)]=CountOfDrops1
			Results['packetdrops'][4]['%s%i'%(tempnew[0],1)]=CountOfDrops1
			if('%s%i'%(tempnew[1],2)) not in PacketDropsByPercent[key]: 
				PacketDropsByPercent[key]['%s%i'%(tempnew[1],2)]= {}
			PacketDropsByPercent[key]['%s%i'%(tempnew[1],2)]=CountOfDrops2
			Results['packetdrops'][4]['%s%i'%(tempnew[1],2)]=CountOfDrops2
	#pprint.pprint(Results)	#print("Writing output JSON to results.json")
	#pprint.pprint(Results)
	pprint.pprint(PacketDropsByPercent)
	pprint.pprint(ThroughputByPercent)
	pprint.pprint(LatencyByPercent)
	
	######################FinalValuesForPlot#############################################
	
	FinalLatencyPair1Reno1=Results['latency'][1]['Reno1']
	FinalLatencyPair1Reno2=Results['latency'][1]['Reno2']
	FinalLatencyPair2NewReno1=Results['latency'][2]['NewReno1']
	FinalLatencyPair2Reno2=Results['latency'][2]['Reno2']
	FinalLatencyPair3Vegas1=Results['latency'][3]['Vegas1']
	FinalLatencyPair3Vegas2=Results['latency'][3]['Vegas2']
	FinalLatencyPair4NewReno1=Results['latency'][4]['NewReno1']
	FinalLatencyPair4Vegas2=Results['latency'][4]['Vegas2']

	FinalThroughputPair1Reno1=Results['throughput'][1]['Reno1']
	FinalThroughputPair1Reno2=Results['throughput'][1]['Reno2']
	FinalThroughputPair2NewReno1=Results['throughput'][2]['NewReno1']
	FinalThroughputPair2Reno2=Results['throughput'][2]['Reno2']
	FinalThroughputPair3Vegas1=Results['throughput'][3]['Vegas1']
	FinalThroughputPair3Vegas2=Results['throughput'][3]['Vegas2']
	FinalThroughputPair4NewReno1=Results['throughput'][4]['NewReno1']
	FinalThroughputPair4Vegas2=Results['throughput'][4]['Vegas2']
	
	FinalPDPair1Reno1=Results['packetdrops'][1]['Reno1']
	FinalPDPair1Reno2=Results['packetdrops'][1]['Reno2']
	FinalPDPair2NewReno1=Results['packetdrops'][2]['NewReno1']
	FinalPDPair2Reno2=Results['packetdrops'][2]['Reno2']
	FinalPDPair3Vegas1=Results['packetdrops'][3]['Vegas1']
	FinalPDPair3Vegas2=Results['packetdrops'][3]['Vegas2']
	FinalPDPair4NewReno1=Results['packetdrops'][4]['NewReno1']
	FinalPDPair4Vegas2=Results['packetdrops'][4]['Vegas2']

	with open('AnalysisExp2.json', 'w') as f:
		json.dump(Results, f, indent=4)
		
		
		
if __name__=="__main__":
	Main()