import sys

def main():
	try:
		question1 = input("Would you like Estimate Price (write EP) or Train Model (TM)? ")
		if question1 == "EP":
			est_res = ft_estimate()
		else if question1 == "TM":
			train_res = ft_train()
	except Exception as e:
		print("Error {e}")
		sys.exit(1)


if __name__ == "__main__":
	main()
