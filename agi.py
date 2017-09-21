import time

envText = open("met_ch1.txt", "r").read().lower()  # all-text environment
envTime = 0

senText = ""  # envText sensor for
senTextRange = 10  # diameter for the sensor "eye", useful as a foundation for later sensors

# open agi mind from file


compTime = time.time() + 60 * 0.5  # for 30 seconds
while time.time() < compTime:  # compute agi for a given time
    # sensor 1 receive 1 character from envText on position
    senText = list(envText[envTime:+senTextRange])  # position of sensor in envText


    # compute agi mind
        # push senText info to lv0 nodes (level 0 nodes means "master" which processes the info

    # MEAT OF AGI:
    # find patterns in text
        # check for existing nodes
    ### MAKE RECURSIVE to find all combinations of groups to nodes
    try:
        for i in range(len(senText)):
            a, b = senText[i], senText[i + 1]
            print(a,b)
    except IndexError:
        pass


    # actuators send output to env


    # end behavior
    envTime += 1  # advance time in env

# save agi mind to file
