"""
Helpful reference information:
x-axis = length of neck
y-axis = width of neck
z-axis = arbitrary third dimension for depth purposes

for website matrices: Bottom number is the COLUMN, top number is the ROW

The p_guitar value should be defined within each fret function
The homography matrix will likely need to be recalculated for each frame in the feed
"""
#use actual coordinate addresses (these definitions are for sample purposes)
#each of these should ideally be an ordered pair or 3-d coordinate
#p1 = node1_topright
#p2 = node2_bottomright
#p3 = node1_topleft
#p4 = node2_bottomleft

#begin defining internal arrays for matrix
#x value array:
x_vals = [p2x-p1x, p3x-p1x, p1x]
#y value array:
y_vals = [p2y-p1y, p3y-p1y, p1y]
#arbitrary z value array:
z_vals = [0, 0, 1]

homography_matrix = [x_vals, y_vals, z_vals]

#length = neck length
#width = neck width
#fret_length = length distance to fret from p1
#fret_width = width distance to fret from p1
###width could potentially be constant since it only looks at string distance###
p_guitar = [fret_legth/length, fret_width/width, 1]

###Begin creating coordinate for fret indicator overlay
#first index is the row (xyz), second index is the column
p_screenx = (homography_matrix[0][0]*p_guitar[0]) + (homography_matrix[0][1]*p_guitar[1]) + homography_matrix[0][2]
p_screeny = (homography_matrix[1][0]*p_guitar[0]) + (homography_matrix[1][1]*p_guitar[1]) + homography_matrix[1][2]
p_screenz = (homography_matrix[2][0]*p_guitar[0]) + (homography_matrix[2][1]*p_guitar[1]) + homography_matrix[2][2]
#p_screenz will always be [0, 0, 1], so this final calculation may not be neccessary

fret_coord = [p_screenx, p_screeny, p_screenz]

#input this array into arkit for dot overlay, may need to convert to an ordered pair since p_screenz will always be "1", arkit might only need a 2-d value
