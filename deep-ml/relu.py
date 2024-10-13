def relu(z: float):
    # could also do 
    # 	if z > 0:
	# 	return z 
	# else: return 0
    return max(0, z)