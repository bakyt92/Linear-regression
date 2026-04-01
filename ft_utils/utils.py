import sys
class Reader_files:
	def __init__(self):
		self.data = []
		return 

	def Read_file(self, link_file):
		try:
			with open(link_file, mode="r", encoding="utf-8") as file:
				content = file.read()
				self.data = content
			# raw_data = Process_Data(content)
		except Exception as e:
			print(f"Exception: {e}")
		return

    # def Process_Data(self, content):
		
    #     return