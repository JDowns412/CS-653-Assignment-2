# Writing a procedure called "test"
proc test {} {
    set a 43
    set b 27
    set c [expr $a + $b]
    set d [expr [expr $a - $b] * $c]
    for {set k 0} {$k < 10} {incr k} {
	if {$k < 5} {
	    puts "k < 5, pow = [expr pow($d, $k)]"
	} else {
	    puts "k >= 5, mod = [expr $d % $k]"
	}
    }
    set test "[expr 2+2]"
    puts "hello"
    puts $test

    for {set i 1} {$i <= 3} {incr i} {

        switch -exact -- $i {
            1 {
                set t 0.95
                # puts "running on [$t]"
            }
            2 {puts "two"}
            3 {
                puts "three"
            }
            default {puts "nope"}
        }
    }

    set ns [new Simulator]
    set j 1
    set l 20
    set test [expr $j + $l]
    set tf [open $test w]
    $ns trace-all $tf
    close $tf

}

proc two {} {
    exit 0
}


# Calling the "test" procedure created above
test
two