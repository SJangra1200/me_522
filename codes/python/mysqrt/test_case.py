<<<<<<< HEAD
def test_case_1():
	from numpy import sqrt 
	from mysqrt import sqrt2
	small = 1.0e-14
	xvalues = [2,100,10000,0.0001,1e8,0]
	
	for x in xvalues:
		s = sqrt2(x)
		s_num= sqrt(x)
		print(f"for x = {x}, s = {s} and s_num = {s_num}")
		assert (s-s_num)<small, f"square root disagrees with numpy square root for x = {x}"
	
def test_case_2():
	from numpy import sqrt 
	from mysqrt import sqrt2
	small = 1.0e-14
	xvalues = [25,100,625,144,121]
	
	for x in xvalues:
		s = sqrt2(x)
		s_num= sqrt(x)
		print(f"for x = {x}, s = {s} and s_num = {s_num}")
		assert (s-s_num)<small, f"square root disagrees with numpy square root for x = {x}"
=======
def test_1():
	from numpy import sqrt
	from mysqrt import sqrt2
	small=1.0e-14
	
	xvalues=[2,100,10000,0.0001,0,1e8]
	for x in xvalues:
		s=sqrt2(x)
		s_numpy=sqrt(x)
		print(f"for x={x}, s={s} and s_numpy={s_numpy}")
		assert (s-s_numpy)<small, f"square root disagrees with numpy square root for x={x}"
	
def test_2():
	from numpy import sqrt
	from mysqrt import sqrt2
	small=1.0e-14
	
	xvalues=[3,6,"10"]
	for x in xvalues:
		s=sqrt2(x)
		s_numpy=sqrt(x)
		print(f"for x={x}, s={s} and s_numpy={s_numpy}")
		assert (s-s_numpy)<small, f"square root disagrees with numpy square root for x={x}"
>>>>>>> 931a67a (The fortran code and the hpc data has been added)
	
