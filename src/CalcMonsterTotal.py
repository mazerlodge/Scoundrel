#!/usr/bin/python3

# calc total monster value in deck where clubs and spades are monsters, j, q, k, A = 11, 12, 13, 14

tot = 0

for x in range(14,1,-1): 
	tot += x 
	
print(f"Total value of monsters is {tot}")

