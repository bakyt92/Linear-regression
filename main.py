import sys
from ft_est_price.ft_estimate import Estimate
from ft_train.ft_train import Training
from ft_utils.utils import Reader_files


def main():
	try:
		question1 = input("Would you like Estimate Price (write EP) or Train Model (TM)? ")
		if question1 == "EP":
			file_link = input(f"Enter the name of input file: ")
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
		elif question1 == "TM":
			Reader = Reader_files()
			try:
				file_link = input(f"Enter the name of input file: ")
				Reader.Read_file(file_link)
			except Exception as e:
				print(f"Error: {e}")
				sys.exit(1)
			headers, data = Reader.get_data()
			trainer = Training()
			trainer.ft_training(headers, data)
		else:
			raise ValueError("wrong input")
	except Exception as e:
		print(f"Error {e}")
		sys.exit(1)
	print("PRINT CONTENTS OF SYS.ARGV: Res.data")
	print(Reader.raw_data)
	return


if __name__ == "__main__":
	main()
