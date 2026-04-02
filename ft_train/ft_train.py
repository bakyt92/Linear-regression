import sys
from ..ft_utils import utils

class Training:
	def __init__(self):
		self.bias = 0
		self.slope = 0
		return
	
	def ft_train(self, link_file):
		try:
			Reader = utils.Reader_files()
			Reader.Read_file(link_file)
			
		except Exception as e:
			print(f"Exception: {e}")
			sys.exit(1)


	def ft_mean(self, headers: list[str], data: list[float]) -> list[float]:
		res = []
		size = len(headers)
		counter = 0
		while counter < size:
			for rows in data:
				res[counter] += rows[counter]
			res[counter] /= len(data)
			counter += 1
		return res

	
	def ft_msq(self, headers: list[str], data: list[float]) -> float:
		try:
			res = 0
			mean_val = self.ft_mean(headers, data)
			size = len(headers)
			if size != 2:
				raise(ValueError)
			index = headers.index("price")
			for rows in data:
				res = (rows[index] - mean_val[index]) ** 2 + res
			res /= len(data)
			return res
		except Exception as e:
			print(f"Exception: {e}")
			sys.exit(1)
