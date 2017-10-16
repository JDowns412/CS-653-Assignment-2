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

