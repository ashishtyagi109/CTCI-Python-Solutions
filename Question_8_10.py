def paintFill(screen, point, newColor):
	row, col = point
	if (screen[row][col] == newColor):
		return False
	return paintFillHelper(screen, point, newColor, origColor)

def paintFillHelper(screen, point, newColor, origColor):
	row, col = point
	rMax, cMax = screen.shape
	if ((row < 0) or (row >= rMax) or (col < 0) or (col >= cMax)):
		return False

	if (screen[row][col] == origColor):
		screen[row][col] = newColor
		paintFillHelper(screen, (row-1, col), newColor, origColor)
		paintFillHelper(screen, (row+1, col), newColor, origColor)
		paintFillHelper(screen, (row, col-1), newColor, origColor)
		paintFillHelper(screen, (row, col+1), newColor, origColor)

	return True
	