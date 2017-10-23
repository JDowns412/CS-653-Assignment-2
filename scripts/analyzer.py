import os

# if readJson:
#         # run more analysis on an existing data set
#         location = '../results/exp%s/results.json' % experiment

#     else:

# experiment = 1
#     directory = '../traces/exp%s' % experiment

#     def run(data):
#     # go to the experiment's data record file directory
#     os.chdir('../results/exp%s' % experiment)

import json, pprint

def Main():

    traceFile = '../results/exp3/results5EarlyCBR.json'

    with open(traceFile, 'r') as f:
        values = json.load(f)
        # print(Values['Vegas - 99%']['1.0 to 2.0']['0.1 0\n +']['event'])
        # listForItr= list(range(100))
        rec = set()

        for key,val in values.items():
            rec.add(key)
            # for key2,val2 in val.items():
                # rec.add(key2)
                # for key3,val3 in val2.items():
                    # rec.add(key3)
                    # rec.add(val3['pktType'])

        pprint.pprint(rec)
            #item=item+1
        #for item in Values:
            #if (item=='Event'):
        #print(Values['Vegas - 99%']['1.0 to 2.0']['0.1 0\n +'])
        #for item in StringVal:
            #if (stri=='"event": "+",'):
        #print(Values['Vegas - 99%']['1.0 to 2.0']['event'])
    
if __name__ == "__main__":
    Main()