
import sys
import math
from time import time
import numpy as np
import pickle

def AkcCont(free, beta,L,D,LK,DK,V):
	akc=free
	param=[L,D,LK,DK,V]
	for i,j in zip(beta,param):
		akc=akc+i*j
	return np.clip(akc,-40,40)

def KorCont(beta,L,D,LK,DK,V):
	akc=0
	param=[L,D,LK,DK,V]
	for i,j in zip(beta,param):
		akc=akc+i*j
	return np.clip(akc,-90,90)




def main():
	


	
	#a1,a2,a3,a4,a5,a6, k1,k2,k3,k4,k5=list(np.load("Parametri.npy"))

	
	
	start=time()
	while True:
		input_str = input() # lnIn - procitaj ulaze sa standardnog ulaza

		(L,D,LK,DK,V,S, W, H, pos_x, pos_y) = [int(s) for s in input_str.split(" ") if s.isdigit()] # tu je kraj rjesen
		
		input_str = input() # lnIn - procitaj ulaze sa standardnog ulaza

		(a1,a2,a3,a4,a5,a6, k1,k2,k3,k4,k5) = [float(s) for s in input_str.split(" ") ]
		betaA=[a1,a2,a3,a4,a5]
		betaK=[k1,k2,k3,k4,k5]
		akcel =int(AkcCont(a6, list(betaA),L,D,LK,DK,V))
		
		#print(akcel, file=sys.stderr)

		kormilo =  int(KorCont(list(betaK),L,D,LK,DK,V))
	


		#np.save("Output.npy",np.array([pos_x, pos_y, W, H, time()-start]))

		print(akcel, kormilo)
		sys.stdout.flush();


if __name__ == '__main__':
	main()