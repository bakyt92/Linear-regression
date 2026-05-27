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
		theta0_index = headers.index("theta0")
		theta0_plot = float(data[0][theta0_index])
		theta1_index = headers.index("theta1")
		theta1_plot = float(data[0][theta1_index])
		Reader_bonus.Read_file(input_file)
		data.clear()
		headers.clear()
		headers, data = Reader_bonus.get_data()
		kms_list = [float(row[headers.index('km')]) for row in data]
		print(f"list: {kms_list}")
		#prices_list = [float(row[headers.index('price')]) for row in data]
		maximum_km = max(kms_list) / 1000
		print(f"Max KMs are: {maximum_km}")
		y_max = theta0_plot + theta1_plot * maximum_km
		minimum_km = min(kms_list) / 1000
		print(f"Min KMs are: {minimum_km}")
		y_min = theta0_plot + theta1_plot * minimum_km
		x1 = [minimum_km, maximum_km]
		y1 = [y_min, y_max]
		plt.plot(x1, y1, color = "blue", label = "Linear Regression price / mileage")
		plt.title("Simple line plot")
		plt.legend(["LR progression"])
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
			trainer = Training()
			trainer.ft_training(headers, data)
		elif args.command == "estimate":
			file_link = args.result_file
			Reader = Reader_files()
			Reader.Read_file(file_link)
			headers, data = Reader.get_data()
			Estimation = Estimate()
			entered_km = 0
			while entered_km >= 0:
				entered_km = input(f"Please enter kms for price estimate: ")
				entered_km = float(entered_km)
				entered_km /= 1000
				estimate_price = Estimation.ft_estimate(entered_km, headers, data)
				print(f"Estimate price is: {estimate_price}")
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
