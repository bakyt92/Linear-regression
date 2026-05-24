import sys
from ft_est_price.ft_estimate import ft_estimate
from ft_train.ft_train import ft_train
from ft_utils.utils import Reader_files


def main():
	try:
		question1 = input("Would you like Estimate Price (write EP) or Train Model (TM)? ")
		if question1 == "EP":
			est_res = ft_estimate()
		elif question1 == "TM":
			Reader = Reader_files()
			try:
				Reader.Read_file(sys.argv[1])
			except Exception as e:
				print(f"Error: {e}")
				sys.exit(1)
			headers, data = Reader.get_data()
			train_res = ft_train(headers, data)
		else:
			raise ValueError("wrong input")
	except Exception as e:
		print("Error {e}")
		sys.exit(1)


	print("PRINT CONTENTS OF SYS.ARGV: Res.data")
	print(Reader.raw_data)
	# print("PRINT CONTENTS OF SYS.ARGV: Res.data1")
	# print(Reader.raw_data[0])
	# print("PRINT CONTENTS OF SYS.ARGV: Res.HEADER")
	# print(Reader.header)


	return


if __name__ == "__main__":
	main()
