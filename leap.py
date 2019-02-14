ry=int(input())
if ry%4==0:
	if ry%100==0:
		if ry%400==0:
			print("yes")
		else:
			print("no")
	else:
		print("yes")
else:
	print("no")
		
