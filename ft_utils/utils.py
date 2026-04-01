import sys
class Reader_files:
	def __init__(self):
		self.data = []
		return 

	def Read_file(self, link_file):
		try:
			with open(link_file, mode="r", encoding="utf-8") as file:
				content = file.read()
			raw_data = Process_Data(content)
		except Exception as e:
			print(f"Exception: {e}")
			sys.exit(1)
		return

	def Process_Data(self, content):
		try:
			header = []
			raw_data = []
			for x in content[0]:
				if isinstance(x, str):
					header.append(x)
			for rows in content:
				if all(isinstance(x, (int, float)) for x in rows):
					raw_data.append(rows)
				else: 
					continue



		except Exception as e:
			print(f"Exception: {e}")
			sys.exit(1)
		return