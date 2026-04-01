import sys
# from ft_est_price.ft_estimate import ft_estimate
# from ft_train.ft_train import ft_train
from ft_utils.utils import Reader_files


def main():
	Reader = Reader_files()
	Reader.Read_file(sys.argv[1])
	print("PRINT CONTENTS OF SYS.ARGV: Res.data")
	print(Reader.data)
	# try:
	# 	question1 = input("Would you like Estimate Price (write EP) or Train Model (TM)? ")
	# 	if question1 == "EP":
	# 		est_res = ft_estimate()
	# 	elif question1 == "TM":
	# 		train_res = ft_train()
	# 	else:
	# 		raise ValueError("wrong input")
	# except Exception as e:
	# 	print("Error {e}")
	# 	sys.exit(1)
	
	return


if __name__ == "__main__":
	main()
