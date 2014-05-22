#PLEASE TRY TO KEEP THIS CODE AS CLEAN AND CONSISE AS POSSIBLE. USE CONSISTENT VARIABLES, CLEAN FORMATTING, AND GET TO THE POINT.
# Just defining pi and importing sys libraries, nothing to see here...
from math import pi
import sys

# Title, Version Number, and Help
print """Trevor McKay's Geometry Calculator 

"""

print """Press the enter key to continue or type 'close' to exit the program.

"""

print """Type 'help' for a list of figures, abbreviations and correct syntax.

"""

print """Version Alpha 1.2.0 (type 'changelog' to view patch and release notes) 

"""

raw_input()

# Makes calculator run until broken or terminated
x = 1
while True:
	
	# Ask user for function
	function = raw_input("If you are looking for a value, type what is given. If you are looking for an equation, type the equation. > ")

	# close program
	closeprogram = function == "close"
	if closeprogram is True:
		sys.exit()
	
	# help
	askforhelp = function == 'help'
	if askforhelp is True:
		
		print """
		SYNTAX
		To find an equation: eq <find> <figure>
		To find a value: <given> <given 2 if it applies> <figure>
	
		SUPPORTED FIGURES
		Spheres
		Cylinders (Partially)
	
		ABBREVIATIONS
		h = height
		vol = volume
		sa = surface area
		rad = radius
		b = area of a base
		la = lateral area
		ta = total area
		"""
		raw_input()
		
	# changelog
	openchangelog = function == "cl"
	if openchangelog is True:
		
		print """
		NOTE: Old versions are not available for download or use.
		
		Version Alpha 1.0.0
		- Added values of spheres
		
		Version Alpha 1.1.0
		- Added equations of spheres
		- Improved help
		- Added changelog
		- Updated syntax
		- Minor optimizations
			Known Issues
		- Some values for spheres return only as 0.0
		
		Version Alpha 1.2.0
		- Fixed issues from version 1.1
		- Added cylinders
		- Optimized and trimmed code
		- Calculator now asks for given instead of what is to be found
		- Minor formatting changes
		"""
		raw_input()
		
#VALUES REGARDING SPHERES
		
	# given volume of sphere
	givenvolsphere = function == "vol sphere"
	if givenvolsphere is True:
		volume = raw_input("What is the volume? > ")
		isnumber = volume.isdigit()
		if isnumber is False:
			print "Invalid number, the program will now close. "
			raw_input()
			sys.exit()
		if isnumber is True:
			rad = pow(0.2387 * int(volume), 0.33333)
			sa = pow(pi, 0.3333) * pow(6 * int(volume), 0.6666)
			print "The radius is approximately " + str(rad) + " units."
			print "The surface area is approximately " + str(sa) + " square units."
			raw_input()
			
	# given surface area of sphere
	givensasphere = function == "sa sphere"
	if givensasphere is True:
		sa = raw_input("What is the surface area? > ")
		isnumber = sa.isdigit()
		if isnumber is False:
			print "Invalid number, the program will now close. "
			raw_input()
			sys.exit()
		if isnumber is True:
			rad = 0.5 * pow(int(sa) / pi, 0.5)
			vol = 4 * pi * (int(rad), 3)
			print "The radius is approximately " + str(rad) + " units."
			print "The volume is approximately " + str(vol) + " units cubed."
			raw_input()
	
	# given radius of sphere
	givenradsphere = function == "rad sphere"
	if givenradsphere is True:
		rad = raw_input("What is the radius? > ")
		isnumber = rad.isdigit()
		if isnumber is False:
			print "Invalid number, the program will now close. "
			raw_input()
			sys.exit()
		if isnumber is True:
			vol = 1.3333 * pi * int(rad) ** 3
			sa = 4 * pi * int(rad) ** 2
			print "The volume is approximately " + str(vol) + " units cubed."
			print "The surface area is approximately " + str(sa) + " square units."
			raw_input()
					
# EQUATIONS REGARDING SPHERES

	# Volume of a sphere
	askeqvolsphere = function == "eq vol sphere"
	if askeqvolsphere is True:
		print "The equation for volume of a sphere is 4/3(pi)r^3. "
		raw_input()
	
	# Surface area of a sphere
	askeqsasphere = function == "eq sa sphere"
	if askeqsasphere is True:
		print "The equation for surface area of a sphere is 4(pi)r^2. "
		raw_input()
		
# VALUES OF CYLINDERS
	
	# Given radius and height
	givenradhcyl1 = function == "rad h cyl"
	givenradhcyl2 = function == "h rad cyl"
	if givenradhcyl1 is True or givenradhcyl2 is True:
		rad = raw_input("What is the radius? > ")
		h = raw_input("What is the height? > ")
		vol = pi * pow(int(rad), 2) * int(h)
		la = 2 * pi * int(rad) * int(h)
		b = pi * pow(int(rad), 2)
		ta = 2* int(b) + int(la)
		print "The volume is " + str(vol) + " cubic units."
		print "The lateral area is " + str(la) + " square units."
		print "The area of a base is " + str(b) + " square units."
		print "The total surface area is " + str(ta) + " square units."
		raw_input()

	# Given radius and volume
	givenradvolcyl1 = function == "rad vol cyl"
	givenradvolcyl2 = function == "vol rad cyl"
	if givenradvolcyl1 is True or givenradvolcyl2 is True:
		rad = raw_input("What is the radius? > ")
		vol = raw_input("What is the volume? > ")
		h = int(vol) / pi * pow(int(rad), 2)
		la = 2 * int(vol) / int(rad)
		ba = pi * pow(int(rad), 2)
		ta = int(la) + int(ba)
		print "The height is " + str(h) + " units."
		print "The lateral area is " + str(la) + " square units."
		print "The area of a base is " + str(ba) + " square units."
		print "The total area is " + str(ta) + " square units."
		raw_input()
		
	# Given radius and lateral area
	givenradlacyl1 = function == "rad la cyl"
	givenradlacyl2 = function == "la rad cyl"
	if givenradlacyl1 is True or givenradlacyl2 is True:
		rad = raw_input("
		la = raw_input("
		h =
		ba =
		ta =
		vol =
