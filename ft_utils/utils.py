import sys
import re
class Reader_files:
	def __init__(self):
		self.header = []
		self.raw_data = []
		return 

	def Read_file(self, link_file):
		try:
			with open(link_file, mode="r") as file:
				for index, line in enumerate(file):
					line_split = line.split(",")
					line_split = [re.sub("\n", "", val) for val in line_split]
					if index == 0:
						self.header = line_split
						header_size = len(self.header)
					else:
						if all(self.isfloat(x) for x in line_split) and header_size == len(line_split):
							line_split = [float(x) for x in line_split]
							self.raw_data.append(line_split)
						# self.raw_data.append(line_split)
						else:
							continue
		except Exception as e:
			print(f"Exception: {e}")
			sys.exit(1)
		return

	def isfloat(self, num):
		try:
			float(num)
			return True
		except ValueError:
			return False

