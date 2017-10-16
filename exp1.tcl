# To conduct this experiment in a generalized manner, we will:
# 1. Set up the network topology that is specified in the writeup
# 2. Add in and start the CBR flow and treat it as the independent variable in the experiment
# ○     We will vary the bandwidth of this CBR flow in multiple runs of the experiment.
# ○      We are considering running the CBR at 25%, 50%, 75%, 90%, 95%, and 99% of
#       the link’s total capacity
# 3. Start whichever TCP variant’s flow
# ○     (we will do this for every specified variant)
# 4. We will also try initializing the CBR flow after the TCP flow has matured and left
# slow-start, in order to see if there is any different behavior observed. We will vary these
# CBR flows as discussed above to generalize. (as specified above)


#Create a simulator object
set ns [new Simulator]

#Open the trace file (before you start the experiment!)
set tf [open first_output.tr w]
$ns trace-all $tf

#Define a 'finish' procedure
proc finish {} {
        global ns tf
        $ns flush-trace

        # Close the trace file (after you finish the experiment!)
        close $tf
        exit 0
}

#Create six nodes, according to the writeup
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]

# $ns_ duplex-link <node1> <node2> <bw> <delay> <qtype> <args>
#Create links between the nodes
$ns duplex-link $n1 $n2 10Mb 10ms DropTail
$ns duplex-link $n5 $n2 10Mb 10ms DropTail
$ns duplex-link $n2 $n3 10Mb 10ms DropTail
$ns duplex-link $n3 $n4 10Mb 10ms DropTail
$ns duplex-link $n3 $n6 10Mb 10ms DropTail


#Setup the TCP connection
set tcp [new Agent/TCP]
# not sure what this class statement is, don't even know if we need it. 
# I think it's for MAN, which we don't need
$tcp set class_ 1
$ns attach-agent $n1 $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n4 $sink
$ns connect $tcp $sink


#Setup a UDP connection
set udp [new Agent/UDP]
$ns attach-agent $n2 $udp
set null [new Agent/Null]
$ns attach-agent $n3 $null
$ns connect $udp $null

#Setup a CBR over UDP connection
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set type_ CBR
$cbr set packet_size_ 1000
#change the rate for generalizable results
$cbr set rate_ 1mb
#the below is a flag indicating whether or not to introduce random "noise" in the schedules transmission times. It is "off" by default, and can be set to be "on" by typing "set random_ 1"
$cbr set random_ false


#Schedule events for the CBR and FTP agents
$ns at 0.1 "$cbr start"
$ns at 4.5 "$cbr stop"

#Detach tcp and sink agents (not really necessary)
$ns at 4.5 "$ns detach-agent $n0 $tcp ; $ns detach-agent $n3 $sink"

#Call the finish procedure after 5 seconds of simulation time
$ns at 1000.0 "finish"

#Print CBR packet size and interval
puts "CBR packet size = [$cbr set packet_size_]"
puts "CBR interval = [$cbr set interval_]"

#Run the simulation
$ns run

