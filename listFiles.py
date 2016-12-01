def listFiles(dir):
	files=[];
	import os
	for name in os.listdir(dir):
		if os.path.isfile(os.path.join(dir, name)):
			files.append(name)
	return files 