# To conduct this experiment in a generalized manner, we will:
#     1. Set up the network topology that is specified in the writeup
#     2. Start both TCP variant flows. To generalize here, we will:
#     ○   Vary the starting times of the two flows. (There will be a lot of permutations here,
#         so we will need to see how many variations of start times that we need to do
#         when actually running the experiments)
#     ○    Change which order the flows are started in. For example, we need to compare
#         Reno vs NewReno. We will run experiments that:
#             ■ Start Reno 5 seconds before, 1 second before, 50 RTT before, 25 RTT
#             before, and 10 RTT before, along with starting the same time as the
#             NewReno connection.
#             ■ We will then repeat this with the NewReno connection first
    # 3. We will also try adding in the CBR flow to see if certain variants behave more or less
    # fairly under congestion rates. When adding in a CBR flow to introduce congestion, we
    # will start the CBR before either of the TCP flows, and also:
    # ○       Vary the CBR bandwidth at 25%, 50%, 75%, 90%, 95%, and 99% of the link’s
    # total capacity
    # 4. (Optional) we could also try introducing in CBR congestion after the TCP flows have
    # matured, but this might be time consuming and not helpful.



#parse in command line arguments, this script will be called externally, many times
if { [expr $argc % 3] != 0 } {
    puts stderr "ERROR! ns called with wrong number of arguments!($argc)"
    exit 1
} else {
    set i [lindex $argv 0]
    set j [lindex $argv 1]
    set k [lindex $argv 2]
}

# we will set the congestion value with this switch statement
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
        10 {set percent 1.00}
        11 {set percent 1.05}
        12 {set percent 1.10}
        13 {set percent 1.25}
        14 {set percent 1.50}
        default {set percent 0.00}
}


#Create a simulator object
set ns [new Simulator]

#used to create the trace file below, 
# such that we know which results correspond to which experiment
set filename [expr $percent + $j]
# set namfile [expr $filename * -1]

#Open the trace file (before you start the experiment!)
set tf [open $filename w]
$ns trace-all $tf

#Open the NAM trace file
# set nf [open namfile w]
# $ns namtrace-all $nf

puts $filename
# puts $namfile
#Define a 'finish' procedure
proc finish {} {
        global ns tf
        $ns flush-trace
        
        # Close the trace file (after you finish the experiment!)
        close $tf
        #Close the NAM trace file
        # close $nf
        #Execute NAM on the trace file
        # exec nam out.nam &
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

#Give node position (for NAM)
$ns duplex-link-op $n1 $n2 orient right-down
$ns duplex-link-op $n5 $n2 orient right-up
$ns duplex-link-op $n2 $n3 orient right
$ns duplex-link-op $n3 $n4 orient right-up
$ns duplex-link-op $n3 $n6 orient right-down

#Setup the first TCP connection
switch -exact -- $j {
        10 {set tcp [new Agent/TCP/Reno]}
        20 {set tcp [new Agent/TCP/Newreno]}
        30 {set tcp [new Agent/TCP/Vegas]}
        40 {set tcp [new Agent/TCP/Newreno]}
        default {set tcp [new Agent/TCP]}
}

# TCP agent selection is done above in the switch
$tcp set class_ 1
$tcp set fid_ 1
$ns attach-agent $n1 $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n4 $sink
$ns connect $tcp $sink

#Setup a FTP over th first TCP connection
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP

#Setup the second TCP connection
switch -exact -- $k {
        100 {set tcp2 [new Agent/TCP]}
        200 {set tcp2 [new Agent/TCP/Reno]}
        300 {set tcp2 [new Agent/TCP/Newreno]}
        400 {set tcp2 [new Agent/TCP/Vegas]}
        default {set tcp2 [new Agent/TCP]}
}

# TCP agent selection is done above in the switch
$tcp2 set class_ 2
$tcp2 set fid_ 2
$ns attach-agent $n5 $tcp2
set sink2 [new Agent/TCPSink]
$ns attach-agent $n6 $sink2
$ns connect $tcp2 $sink2

#Setup a FTP over the second TCP connection
set ftp2 [new Application/FTP]
$ftp2 attach-agent $tcp2
$ftp2 set type_ FTP

#Setup a UDP connection
set udp [new Agent/UDP]
$udp set fid_ 3
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
            10 {$cbr set rate_ 10Mb}
            11 {$cbr set rate_ 10.5Mb}
            12 {$cbr set rate_ 11Mb}
            13 {$cbr set rate_ 12.5Mb}
            14 {$cbr set rate_ 15Mb}
            default {$cbr set rate_ 0.0Mb}
}

# the below is a flag indicating whether or not to introduce random "noise" in 
# the schedules transmission times. It is "off" by default, 
# and can be set to be "on" by typing "set random_ 1"
# Using this to generalize more to the outside world
$cbr set random_ 1


#Schedule events for the CBR and FTP agents
#  maybe change this for generalizing the experiment?
# starting at 30 seconds to keep the data low, maybe change later
$ns at 2 "$cbr start"
$ns at 1 "$ftp start"
$ns at 1 "$ftp2 start"
$ns at 5 "$cbr stop"
$ns at 5 "$ftp stop"
$ns at 5 "$ftp2 stop"

#Call the finish procedure after 5 seconds of simulation time
$ns at 6 "finish"

#Print CBR packet size and interval
# puts "CBR packet size = [$cbr set packet_size_]"
# puts "CBR interval = [$cbr set interval_]"

#Run the simulation
$ns run