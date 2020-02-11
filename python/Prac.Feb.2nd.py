# This program calculates whether Bolt or the cheetah is the winner
import math

finish = int(int(input()))
dis_Bolt = int(int(input()))
cheetahAcc = int(int(input()))
boltSpeed = int(int(input()))
time_bolt = (finish + dis_Bolt) / boltSpeed
print("the time bolt takes is {}", time_bolt)
time_cheetah = math.sqrt((dis_Bolt + finish)/(1/2 * cheetahAcc))
print("the time cheetah takes is {}", time_cheetah)

if time_bolt > time_cheetah and time_bolt != time_cheetah:
    print("Bolt is faster")
else:
    print("Cheetah is faster")
