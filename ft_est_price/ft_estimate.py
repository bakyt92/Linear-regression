import sys

class Estimate:
	def __init__(self):
		self.theta0 = 0
		self.theta1 = 0

	def ft_estimate(self, entered_km, headers, data):
		print(f" HEADERS IS {headers}")
		print(f" DATA IS {data}")
		theta0_index = headers.index("theta0")
		self.theta0 = float(data[0][theta0_index])
		#print(f" DATA IS_Theta0 {data[0][theta0_index]}")
		theta1_index = headers.index("theta1")
		self.theta1 = float(data[0][theta1_index])
		#print(f" DATA IS_Theta1 {data[0][theta1_index]}")
		estimate_price = self.theta0 + self.theta1 * entered_km
		return estimate_price
