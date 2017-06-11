import numpy as np 

#This code will generate the same test set as long as you 
# 1. You use same seed value for shuffle
# 2. The dataset does not change.

def split_train_test(data, test_ratio, seed_value=42):
	np.random.seed(seed_value)
	shuffled_indices = np.random.permutation(len(data))
	test_set_size = int(len(data) * test_ratio)
	test_indices = shuffled_indices[:test_set_size]
	train_indices = shuffled_indices[test_set_size:]
	return data.iloc[train_indices], data.iloc[test_indices]

