import sys
from ft_est_price.ft_estimate import Estimate
from ft_train.ft_train import Training
from ft_utils.utils import Reader_files
import matplotlib.pyplot as plt
import argparse

def ft_bonus(input_file, result_file):
	theta0_plot = 0 
	theta1_plot = 0
	try:
		Reader_bonus = Reader_files()
		Reader_bonus.Read_file(result_file)
		headers, data = Reader_bonus.get_data()
		if "theta0" not in headers or "theta1" not in headers:
			raise Exception("Entered file does not contain results theta1 / theta0 - i.e. no result file")
		theta0_index = headers.index("theta0")
		theta0_plot = float(data[0][theta0_index])
		theta1_index = headers.index("theta1")
		theta1_plot = float(data[0][theta1_index])
		data.clear()
		headers.clear()
		Reader_bonus.Read_file(input_file)
		headers, data = Reader_bonus.get_data()
		if "price" not in headers or "km" not in headers:
			raise Exception("Entered file does not contain kms and prices - i.e. no data file")
		kms_list = [float(row[headers.index('km')]) / 1000 for row in data]
		#print(f"list: {kms_list}")
		prices_list = [float(row[headers.index('price')]) for row in data]
		#print(f"list prices: {prices_list}")
		plt.scatter(kms_list, prices_list, color="red", label = "Real Data from CSV")
		maximum_km = max(kms_list)
		print(f"Max KMs are: {maximum_km}")
		y_max = theta0_plot + theta1_plot * maximum_km
		minimum_km = min(kms_list)
		print(f"Min KMs are: {minimum_km}")
		y_min = theta0_plot + theta1_plot * minimum_km
		x1 = [minimum_km, maximum_km]
		y1 = [y_min, y_max]
		plt.plot(x1, y1, color = "blue", label = "Linear Regression price / mileage")
		plt.xlabel("kms x 1000", fontsize=12)
		plt.ylabel("price in USD", fontsize=12)
		plt.title("Comparison of calculated and real data")
		plt.legend(["Real Data", "Calculated LR progression"])
		plt.grid(True)
		plt.show()
	except Exception as e:
		print(f"Exception in Bonus: {e}")
	return

def main():
	try:
		parser = argparse.ArgumentParser(description="Linear Regression")
		subparser = parser.add_subparsers(dest="command")
		train_mode = subparser.add_parser("train", help="Train model and generate CSV result file")
		train_mode.add_argument("input_file", help="CSV file for training model")
		estimate_mode = subparser.add_parser("estimate", help="Estimate price of voiture based on mileage")
		estimate_mode.add_argument("result_file", help="CSV result file for estimation")
		bonus_mode = subparser.add_parser("bonus", help="Run bonus mode, create a plot")
		bonus_mode.add_argument("input_file", help="CSV file for training model")
		bonus_mode.add_argument("result_file", help="CSV result file for estimation")
		args = parser.parse_args()
		if args.command == "train":
			Reader = Reader_files()
			try:
				file_link = args.input_file
				Reader.Read_file(file_link)
			except Exception as e:
				print(f"Error: {e}")
				sys.exit(1)
			headers, data = Reader.get_data()
			if "price" not in headers or "km" not in headers:
				raise Exception("Entered file does not contain kms and prices - i.e. no data file")
			trainer = Training()
			trainer.ft_training(headers, data)
		elif args.command == "estimate":
			file_link = args.result_file
			Reader = Reader_files()
			Reader.Read_file(file_link)
			headers, data = Reader.get_data()
			if "theta0" not in headers or "theta1" not in headers:
				raise Exception("Entered file does not contain results theta1 / theta0 - i.e. no result file")
			Estimation = Estimate()
			entered_km = 0
			while True:
				entered_km = input(f"Please enter kms for price estimate (above 1 km. Type exit for exit): ")
				if entered_km == "exit":
					print(f"You've entered EXIT command. Good Luck!")
					break
				try: 
					enter_km = float(entered_km)
				except ValueError:
					print(f"Entered km is not float or int")
					continue
				if enter_km <= 1:
					print(f"Value is small. Number should be above 1 km.")
					continue
				enter_km /= 1000
				estimate_price = Estimation.ft_estimate(enter_km, headers, data)
				if estimate_price < 0:
					print(f"Expected price of car is 0 / no value")
					continue
				print(f"Estimate price is: {estimate_price:.2f}")
		elif args.command == "bonus":
			ft_bonus(args.input_file, args.result_file)
		else:
			raise ValueError("wrong input. Please use --help command")
	except Exception as e:
		print(f"Error {e}")
		sys.exit(1)
	return


if __name__ == "__main__":
	main()
