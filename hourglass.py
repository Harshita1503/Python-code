
"""
Given a 2D Array, B, we define an hourglass in to be a subset of values
with indices falling in this pattern in A's graphical representation:
a b c
  d
e f g
There are hourglasses in B, and an hourglass sum is the sum of an hourglass' values.
"""

B = []
for arr_i in range(6):
	arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
	B.append(arr_t)

smax = -9 * 7

for row in range(len(B) - 2):
	for column in range(len(B[row]) - 2):
		tl = B[row][column]
		tc = B[row][column + 1]
		tr = B[row][column + 2]
		mc = B[row + 1][column + 1]
		bl = B[row + 2][column]
		bc = B[row + 2][column + 1]
		br = B[row + 2][column + 2]
		s = tl + tc + tr + mc + bl + bc + br
		smax = max(s, smax)

print(smax)
