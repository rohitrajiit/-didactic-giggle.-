#! python3
# countdown.py - A simple countdown script.

import time, subprocess

timeLeft = 5
while timeLeft > 0:
   print(timeLeft, end='')
   time.sleep(1)
   timeLeft = timeLeft - 1
   print('ticktick')

# TODO: At the end of the countdown, play a sound file.
mp3process = subprocess.Popen(['rhythmbox-client', '--play-uri=69.mp3'])
print(mp3process.poll())
#mp3process.wait()
print('good song')
fhandle = open('wakeup.txt','w')
fhandle.write('Wake UP')
fhandle.close()
mp3processs = subprocess.Popen(['see', 'wakeup.txt'])
time.sleep(10)
#mp3process.kill()
print('done')
