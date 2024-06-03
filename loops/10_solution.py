import time

wait_time = 1
max_retries = 5
attempes = 0

while attempes < max_retries:
  print("Attempts " , attempes + 1 , "wait_time " , wait_time )
  time.sleep(wait_time)
  wait_time *= 2
  attempes += 1