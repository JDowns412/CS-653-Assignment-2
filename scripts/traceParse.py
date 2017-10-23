# things we need to analyze: 
# exp1:
# average throughput (rate that data is successfully delivered over a TCP connection: just the seq number )
# average latency (the time required for a packet to travel across a network. Can be RTT or 1-way)
# dropped packets
# overall best

# exp2:
# "fairness", so a cumulative measurement of the above statistics
# probably look at retransmissions and total average throughput/drops

# exp3:
# "fair" bandwidth, just like exp2
# end-to-end latency like before
# reaction of TCP to CBR flow

# in a "meta" section, 
# first sort out the types of communications (1 to 2, 4 to 6)
# then sort out what types of communication's are detested between those nodes (CBR, tcp, ack)
# additional statistics required here?

# main database part:
	# inside of the two above categories, 


	# need to utilize the flow id better

import sys, os, decimal, json

def parseFile(file, out, experiment):

    debug = set()

    # out = {}
    # parse the TCP agent from the filename
    tcpAgent = ""
    if (experiment == '1'):
        if file[0] == '1':
            tcpAgent = "Tahoe"
        if file[0] == '2':
            tcpAgent = "Reno"
        if file[0] == '3':
            tcpAgent = "NewReno"
        if file[0] == '4':
            tcpAgent = "Vegas"
    elif (experiment == '2'):
        if file[0] == '1':
            tcpAgent = "Reno_Reno"
        if file[0] == '2':
            tcpAgent = "NewReno_Reno"
        if file[0] == '3':
            tcpAgent = "Vegas_Vegas"
        if file[0] == '4':
            tcpAgent = "NewReno_Vegas"
    elif (experiment == '3'):
        if file[1] == '1':
            tcpAgent = "Reno"
            if file[0] == '1':
                tcpAgent += "_DropTail"
            else:
                tcpAgent += "_RED"
        if file[1] == '2':
            tcpAgent = "SACK"
            if file[0] == '2':
                tcpAgent += "_DropTail"
            else:
                tcpAgent += "_RED"

    # parse the CBD bandwidth usage from the filename
    cbrBand = int(round(float(file[2:]), 2)*100)

    experiment = "%s - %d%%" % (tcpAgent, cbrBand)
    # this is where we will store the data from the experiment
    # this will keep the overall dictionary (results) organized
    out[experiment] = {}

    print("parsing ", experiment)

    # parse in the whole trace file
    with open(file, 'r') as f:
        # each line is the trace of a single packet
        for line in f:
            # an example line looks like this:
            # + 5.278795 1 2 tcp 1040 ------- 1 0.0 3.0 1301 3885

            splitLine = line.split(" ")
            event = splitLine[0]
            time = splitLine[1]
            fromNode = splitLine[2]
            toNode = splitLine[3]
            pktType = splitLine[4]
            pktSize = splitLine[5]
            flags = splitLine[6]
            flowId = splitLine[7]
            srcAddr = splitLine[8]
            dstAddr = splitLine[9]
            seqNum = splitLine[10]
            pktId = splitLine[11]

            path = "%s to %s" % (srcAddr, dstAddr)
            # if we have initialized the path sub-dictionary already
            if path not in out[experiment]:
                out[experiment][path] = {}

            # make a unique identifier for this packet record
            pId = "%s %s %s" % (time, pktId, event)

            # I'm not 100% that this pId will always be unique... 
            # checking with an assert statement
            assert pId not in out[experiment][path]
            
            # add this unique packet record to the database
            out[experiment][path][pId] = {}

            #populate the packet record
            out[experiment][path][pId]["event"] = event
            out[experiment][path][pId]["time"] = float(time)
            out[experiment][path][pId]["fromNode"] = int(fromNode)
            out[experiment][path][pId]["toNode"] = int(toNode)
            out[experiment][path][pId]["pktType"] = pktType
            out[experiment][path][pId]["pktSize"] = int(pktSize)
            out[experiment][path][pId]["flags"] = flags
            out[experiment][path][pId]["flowId"] = int(flowId)
            out[experiment][path][pId]["srcAddr"] = srcAddr
            out[experiment][path][pId]["dstAddr"] = dstAddr
            out[experiment][path][pId]["seqNum"] = int(seqNum)
            out[experiment][path][pId]["pktId"] = int(pktId)

    return out



def makeDic(experiment):
    results = {}

    # go to the experiment's trace file directory
    os.chdir('../traces/exp%s' % experiment)
    # iterate over all the files in the directory
    for file in os.listdir():
        if file.split(".")[-1] == "py":
            # ignore the file, since we don't want to evaluate on a python file
            pass
        else: #it is a file we want to parse in to our experiment results
            # we build the results dictionary as we go, file by file
            results = parseFile(file, results, experiment)

    # go to where we are keeping our results
    os.chdir('../../results/exp%s' % experiment)

    print("Writing output JSON to results%s.json" % experiment)
    with open('results%s.json' % experiment, 'w') as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    experiment = sys.argv[1]
    makeDic(experiment)

    #TODO
    # add in compression of the JSON to push it to github, though we'll probably just do this manually