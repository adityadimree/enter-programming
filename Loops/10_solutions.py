import time

attempts = 0
max_attempts = 5
wait_time = 1

while attempts < max_attempts:
    print("Attempts:", attempts+1, "- Before the next try wait for", wait_time, "seconds.")
    #sleep pehle karana zaroori hai varna pehle attempt ka sleep time lelega
    time.sleep(wait_time)
    attempts += 1
    wait_time *= 2


