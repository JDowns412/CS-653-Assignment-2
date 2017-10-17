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



# we will loop through congestion values with this for/switch combination
# for {set i 1} {$i < 10} {incr i} {
#temporary replacement for the above for loop until coding this experiment is done
set i 1

switch -exact -- $i {
            1 {set percent 0.1}
            2 {set percent 0.25}
            3 {set percent 0.50}
            4 {set percent 0.75}
            5 {set percent 0.80}
            6 {set percent 0.85}
            7 {set percent 0.90}
            8 {set percent 0.95}
            9 {set percent 0.99}
            default {percent 0.00}
}

# we will loop through TCP agent types with this for/switch combination (Tahoe, Reno, NewReno, and Vegas)
# for {set k 1} {$k < 5} {incr k} {
#temporary replacement for the above for loop until coding this experiment is done
set k 1
switch -exact -- $k {
		#set to tahoe, the default
        1 {set tcp [new Agent/TCP]}
        #set to reno
        2 {set tcp [new Agent/TCP/Reno]}
        #set to newReno
        3 {set tcp [new Agent/TCP/Newreno]}
        #set to vegas
        4 {set tcp [new Agent/TCP/Vegas]}
        default {set tcp [new Agent/TCP]}
}

#Create a simulator object
set ns [new Simulator]

#used to create the trace file below, 
# such that we know which results correspond to which experiment
set filename [expr $percent + $k]

#Open the trace file (before you start the experiment!)
set tf [open $filename w]
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
# TCP agent selection is done above in the switch
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
$cbr set packet_size_ 500
#change the rate for generalizable results, using the same switch tactic from before
switch -exact -- $i {
            1 {$cbr set rate_ 1Mb}
            2 {$cbr set rate_ 2.5Mb}
            3 {$cbr set rate_ 5.0Mb}
            4 {$cbr set rate_ 7.5Mb}
            5 {$cbr set rate_ 8.0Mb}
            6 {$cbr set rate_ 8.5Mb}
            7 {$cbr set rate_ 9.0Mb}
            8 {$cbr set rate_ 9.5Mb}
            9 {$cbr set rate_ 9.9Mb}
            default {$cbr set rate_ 0.0Mb}
}

# the below is a flag indicating whether or not to introduce random "noise" in 
# the schedules transmission times. It is "off" by default, 
# and can be set to be "on" by typing "set random_ 1"
# Using this to generalize more to the outside world
$cbr set random_ 1


#Schedule events for the CBR and FTP agents
#  maybe change this for generalizing th experiment?
# starting at 30 seconds to keep the data low, maybe change later
$ns at 0.1 "$cbr start"
$ns at 1 "$tcp start"
$ns at 31 "$cbr stop"
$ns at 31 "$tcp stop"

#Call the finish procedure after 5 seconds of simulation time
$ns at 32 "finish"

#Print CBR packet size and interval
puts "CBR packet size = [$cbr set packet_size_]"
puts "CBR interval = [$cbr set interval_]"

#Run the simulation
$ns run

# }
