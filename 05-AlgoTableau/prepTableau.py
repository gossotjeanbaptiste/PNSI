

import random

def tableau1():
	return [random.randint(1, 100000) for i in range(500)]

def tableau2():
	return sorted(tableau1())

tableau2()