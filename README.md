# Genetic algorithm project
Bot learns to navigate a boat through the canal using a genetic algorithm. 

Input is the velocity of the boat, left and the right distance from shore at angle 90 and 45 degrees. 

An output is two numbers, one is acceleration and other is the steering angle. Each output number is the linear combination of input parameters where coefficients are found by the genetic algorithm. 

**main.py** starts training in parallel on 4 threads and coefficients are saved in txt.
