def open_left(x, alpha, beta):
	if x <= alpha:
		return 1 

	elif alpha < x < beta:
		return (beta - x)/ (beta - alpha)

	else:
		return 0

x = int(input('Enter your x value: '))
result = open_left(x, 30, 50)

print(f"open_left membership value for {x}: {result}")
