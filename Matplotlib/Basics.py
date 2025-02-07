import matplotlib.pyplot as plt
import numpy as np
# xpoint=[33,34,35,36,37]
# ypoint=[200,240,260,290,320]
# plt.plot(xpoint,ypoint)
# plt.show()

# # using array
# xpoint=np.array([33,34,35,36,37])
# ypoint=np.array([200,240,260,290,320])
# plt.plot(xpoint,ypoint)
# plt.show()


# #If we only want the markings then we can give 
# #string notation parameter'o' which means rings
# xpoint=np.array([33,34,35,36,37])
# ypoint=np.array([200,240,260,290,320])
# plt.plot(xpoint,ypoint,'o')
# plt.show()


#Marking with a Proper Joinings

# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(xpoints, ypoints,marker='o')
# plt.show()
#some more marker to write in place of 'o'

# 'o'	Circle	
# '*'	Star	
# '.'	Point	
# ','	Pixel	
# 'x'	X	
# 'X'	X (filled)	
# '+'	Plus	
# 'P'	Plus (filled)	
# 's'	Square	
# 'D'	Diamond	
# 'd'	Diamond (thin)	
# 'p'	Pentagon	
# 'H'	Hexagon	
# 'h'	Hexagon	
# 'v'	Triangle Down	
# '^'	Triangle Up	
# '<'	Triangle Left	
# '>'	Triangle Right	
# '1'	Tri Down	
# '2'	Tri Up	
# '3'	Tri Left	
# '4'	Tri Right	
# '|'	Vline	
# '_'	Hline



# marker:line:color,default line is --

# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, 'o:r')
# plt.show()


#marker size ms=xx
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()
#also mec=color,give color to marker edge
#mfc=color,give color markers face
