import os
import numpy as np
from tqdm import tqdm
import copy
import pickle
from time import time
from multiprocessing.dummy import Pool as ThreadPool 


class genom():

	Akc1=0
	Akc2=0
	Akc3=0
	Akc4=0
	Akc5=0
	Kor1=0
	Kor2=0
	Kor3=0
	Kor4=0
	Kor5=0
	fitnes=0
	low=-0.15
	high=0.15
	low_k=-0.7
	high_k=0.7
	low_free=-10
	high_free=25
	
	def __init__(self):
		
		self.Akc1=np.random.uniform(self.low, self.high)
		self.Akc2=np.random.uniform(self.low, self.high)
		self.Akc3=np.random.uniform(self.low, self.high)
		self.Akc4=np.random.uniform(self.low, self.high)
		self.Akc5=np.random.uniform(self.low, self.high)
		self.Akc6=np.random.uniform(self.low_free, self.high_free)
		
		self.Kor1=np.random.uniform(self.low_k, self.high_k)
		self.Kor2=np.random.uniform(self.low_k, self.high_k)
		self.Kor3=np.random.uniform(self.low_k, self.high_k)
		self.Kor4=np.random.uniform(self.low_k, self.high_k)
		self.Kor5=np.random.uniform(self.low_k, self.high_k)
	def crossover(self,p2):
		'''
		self.Akc1=(self.Akc1+p2.Akc1)/2
		self.Akc2=(self.Akc2+p2.Akc2)/2
		self.Akc3=(self.Akc3+p2.Akc3)/2
		self.Akc4=(self.Akc4+p2.Akc4)/2
		self.Akc5=(self.Akc5+p2.Akc5)/2
		self.Akc6=(self.Akc6+p2.Akc6)/2

		self.Kor1=(self.Kor1+p2.Kor1)/2
		self.Kor2=(self.Kor2+p2.Kor2)/2
		self.Kor3=(self.Kor3+p2.Kor3)/2
		self.Kor4=(self.Kor4+p2.Kor4)/2
		self.Kor5=(self.Kor5+p2.Kor5)/2
		'''
		self.Akc3=p2.Akc3
		self.Akc4=p2.Akc4
		self.Akc5=(self.Akc5+p2.Akc5)/2
		self.Akc6=(self.Akc6+p2.Akc6)/2
		
		self.Kor3=p2.Kor3
		self.Kor4=p2.Kor4
		self.Kor5=(self.Kor5+p2.Kor5)/2



	def mutate(self, p=0.01):
		
		if np.random.uniform()<p:
			self.Akc1=np.random.uniform(self.low, self.high)
		if np.random.uniform()<p:
			self.Akc2=np.random.uniform(self.low, self.high)
		if np.random.uniform()<p:
			self.Akc3=np.random.uniform(self.low, self.high)
		if np.random.uniform()<p:
			self.Akc4=np.random.uniform(self.low, self.high)
		if np.random.uniform()<p:
			self.Akc5=np.random.uniform(self.low, self.high)
		if np.random.uniform()<p:
			self.Akc6=np.random.uniform(self.low_free, self.high_free)
		if np.random.uniform()<p:
			self.Kor1=np.random.uniform(self.low_k, self.high_k)
		if np.random.uniform()<p:
			self.Kor2=np.random.uniform(self.low_k, self.high_k)
		if np.random.uniform()<p:
			self.Kor3=np.random.uniform(self.low_k, self.high_k)
		if np.random.uniform()<p:
			self.Kor4=np.random.uniform(self.low_k, self.high_k)
		if np.random.uniform()<p:
			self.Kor5=np.random.uniform(self.low_k, self.high_k)



	def fit_help(self,percent, t):
		
		temp = percent**4*(1 + 100 * (percent/100)**4/t**2)
		
		self.fitnes=temp

	def cal_fitnes(self):

		GUI=np.random.choice(np.arange(3))
		send=str(GUI) + " " + str(self.Akc1) + " " + str(self.Akc2) + " " + str(self.Akc3) + " " + str(self.Akc4) + " " + str(self.Akc5) + " " + str(self.Akc6) \
														 + " " + str(self.Kor1) + " " + str(self.Kor2) + " " + str(self.Kor3) + " " + str(self.Kor4) + " " + str(self.Kor5)
		start = time()
		percent = os.system("java -jar Simulator.jar " + send)
		t = time()-start
		
		

		self.fit_help(percent, t)

		return self.fitnes



def get_best_parents(fitnes):

	fitnes = np.array(fitnes)
	fit_norma=fitnes/sum(fitnes)

	idx1=np.random.choice(np.arange(len(fit_norma)),p=fit_norma)
	idx2=np.random.choice(np.arange(len(fit_norma)),p=fit_norma)

	return idx1, idx2

def get_worst_parents(fitnes):

	temp=1/np.array(fitnes)

	p=temp/sum(temp)
	return np.random.choice(np.arange(len(p)),p=p)

def mutil_fitnes(genom):
	
	return genom.cal_fitnes()
	
if __name__ == '__main__':

	pool = ThreadPool(4) 
	n_population=20
	n_generation=20000
	
	population=[]
	
		
	for i in range(n_population):

		population.append(genom())

	fitnes = pool.map(mutil_fitnes, population)	
	'''	
	fitnes=[0]*n_population
	for j in tqdm(range(n_population)):

		fitnes[j]=population[j].cal_fitnes()
	'''
	for i in tqdm(range(n_generation)):

		childs = []
		bad = []
		for i in range(4):
			idx1, idx2 =get_best_parents(fitnes)		
			child =copy.deepcopy(population[idx1])		
			child.crossover(population[idx2])
			child.mutate()
			childs.append(child)
			idx= get_worst_parents(fitnes)
			bad.append(idx)
		
		fitnes_childs=pool.map(mutil_fitnes, childs)
		
		for k, child_f,child in zip(bad,fitnes_childs,childs):
			fitnes[k]=child_f
			population[k]=copy.deepcopy(child)
		
		if i%100==0:
			pickle.dump(population, open( "populacija.p", "wb" ) )

