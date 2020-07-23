import time
import random
import math
from multiprocessing import Process, Value, Lock, Pool

def main():
	start = time.time()
	# number process
	k=4
	# points per process
	n=25000

	cross=0
	nocross=0

	pool = Pool(k)

	results=[pool.apply_async(generate_data,args=(n,)) for i in range(k)]

	for result in results:
		result.wait()
		output = result.get()
		#print(output)
		nocross+=output[0]
		cross+=output[1]

	end = time.time()
	print('Random edges that cross: ' + str(cross))
	print('Random edges that do not cross: ' + str(nocross))
	print('Total time: ' + str(end-start))
	p=1.0/2*cross/(n*k)
	print('99% confidence interval for p: ' + str(p) + ' +/- ' +
		str(2.575*math.sqrt(p*(1-p)/n)))

def generate_data(n):
	cross=0
	nocross=0
	for i in range(n):
		if random_crossing()==0:
			nocross+=1
		else:
			cross+=1
	return [nocross,cross]
	

def generate_coords(len=4):
	pts=[]
	for i in range(len):
		pts.append(random.random())
	return pts

def random_crossing():
	x=generate_coords()
	y=generate_coords()
	z=generate_coords()
	#mathematica code to plot triangles
#	print('Graphics3D[{Red,Line[{{'+str(x[0])+','+str(y[0])+','+str(z[0])+'},{'
#		+str(x[1])+','+str(y[1])+','+str(z[1])+'},{'
#		+str(x[2])+','+str(y[2])+','+str(z[2])+'},{'
#		+str(x[0])+','+str(y[0])+','+str(z[0])+'}}],Blue,Line[{{'
#		+str(x[3])+','+str(y[3])+','+str(z[3])+'},{'
#		+str(x[4])+','+str(y[4])+','+str(z[4])+'},{'
#		+str(x[5])+','+str(y[5])+','+str(z[5])+'},{'
#		+str(x[3])+','+str(y[3])+','+str(z[3])+'}}]}]')

	crossing = check_crossing([x[0],y[0],z[0]],[x[1],y[1],z[1]],
				[x[2],y[2],z[2]],[x[3],y[3],z[3]])
#	print(str(crossings))
	return crossing


def check_crossing(p1,p2,q1,q2):
	# solve linear system for when two lines cross
	dxp = p2[0]-p1[0]
	dyp = p2[1]-p1[1]
	dxq = q2[0]-q1[0]
	dyq = q2[1]-q1[1]
	dxc = q1[0]-p1[0]
	dyc = q1[1]-p1[1]
	det=dyp*dxq-dxp*dyq
#	det=(p2[0]-p1[0])*(q1[1]-q2[1])-(q1[0]-q2[0])*(p2[1]-p1[1])
	t=( dxq*dyc-dyq*dxc ) / det
#	t=( (q1[1]-q2[1])*(q1[0]-p1[0])+(q2[0]-q1[0])*(q1[1]-p1[1]) ) / (
#		det )
	s=( dxp*dyc-dyp*dxc ) / det
#	s=( (p1[1]-p2[1])*(q1[0]-p1[0])+(p2[0]-p1[0])*(q1[1]-p1[1]) ) / (
#		det )

	# check if the lines cross inside the segments from p1 to p2 and q1 to q2
	if (0<t<1) and (0<s<1):
		# segments cross, find which is the over crossing
		if (p1[2] + t*(p2[2]-p1[2])) > (q1[2]+s*(q2[2]-q1[2])):
			overunder= 1
		else:
			overunder= -1
	else:
		overunder= 0

	# also check the possibility of numerical error
	#if abs((p1[2] + t*(p2[2]-p1[2])) - (q1[2]+s*(q2[2]-q1[2])))<0.0000000001:
	#	print('possible rounding error')

	# now determine sign of crossing
	if (det*overunder >0):
		return 1
	elif (det*overunder < 0):
		return -1
	else:
		return 0


if __name__ == "__main__":
	main()

##Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
##Type "help", "copyright", "credits" or "license()" for more information.
##>>> 
##= RESTART: C:\Users\kozai\OneDrive - Rose-Hulman Institute of Technology\research\reu2020\random_crossing.py
##Random edges that cross: 23149808
##Random edges that do not cross: 76850192
##Total time: 169.86428928375244
##99% confidence interval for p: 0.11574904 +/- 0.00016476072636037106
##>>> 

