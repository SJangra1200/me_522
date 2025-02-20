<<<<<<< HEAD
def sqrt2(x, debug=False):
    from numpy import nan
    if x==0:
    	return 0
    elif x<0:
    	return nan
    s=1.0
    kmax=1000
    tol = 1.0e-14
    for k in range(kmax):
        s0=s
        s = 0.5*(s + x/s)
        if debug:
            print(f"At iteration {k+1}, the value s={s}")
        delta_s = s-s0
        if(abs(delta_s/x)<tol):
            break
    if debug:
        print(f"The final value is s={s}")
    return s    
=======
<<<<<<< HEAD
x = int(input("Enter the number which square root you want to calculate :"))
s = int(input("Enter a random number :"))
#x=1000000.0
#s=1.0
kmax=1000
tol = 1.0e-14
for k in range(kmax):
    s0=s
    s = 0.5*(s + x/s)
    print(f"At iteration {k+1}, the value s={s}")
    delta_s = s-s0
    if(abs(delta_s)<tol):
        break
print(f"The final value is s={s}")    
=======
def sqrt2(x, debug=False):
	from numpy import nan
	if x==0:
		return 0
	elif x<0:
		return nan
	s=1.0
	kmax=100
	tol=1.0e-14
	for k in range(kmax):
		if debug:
			print(f"At iteration {k} the value of s={s:20.15f}")
		s0 = s
		s = 0.5 * (s + (x/s))
		delta_s = s-s0
		if(abs(delta_s/x) < tol):
			break
	if debug:
		print(f"Finally, the value of s={s:20.15f}")
	return s
	
if __name__=="__main__":
	import test_case
	print("In main, executing test_1() in test_case.py")
	test_case.test_1()
	
>>>>>>> upstream/main
>>>>>>> 931a67a (The fortran code and the hpc data has been added)
