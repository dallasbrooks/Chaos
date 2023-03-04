import matplotlib.pyplot as plt
import random

DEF_N = 100 # grid size
DEF_M = 5000 # number of points

def main(n, m):
	targets = ((0, 0), (n/2, n), (n, 0))
	count = len(targets)
	plt.figure()
	last = (targets[0])
	for i in range(count):
		t = targets[random.randrange(count)]
		x = (last[0] + t[0]) / 2.0
		y = (last[1] + t[1]) / 2.0
		plt.plot(x, y, marker='.', markersize=1)
		last = (x, y)
	plt.show()

if __name__ == '__main__':
	main(DEF_N, DEF_M)