import os, re #importazione modulo regular expression

dirToProcess = '/Users/alessandrocascino/Desktop/XREVERSE_TOOL/DATA' #directory da processare
fileExt = [".yaml",".yml",".YAML",".unity"] #estensioni da processare
ignoredDir = os.sep + 'target' + os.sep 
makeBackup = False #backup del file esistente

#pattern di replace
patternStr = r"(GameObject)_((\d+)_ID(\d+))"
patternStr2 = r"(MonoBehaviour)_((\d+)_ID(\d+))"
#stringa di replace
#repStr = "\\5_\\1:"

def containsPattern(filePath): #ricerca del pattern che stiamo cercando
	inputFile = open(filePath)
	fContent = inputFile.read()
	containsPattern = re.search(patternStr, fContent)
	if containsPattern:
		inputFile.close()
		return True
	else:
		inputFile.close()
		return False

def replaceStringInFile(filePath): #lettura del codice sorgente e chiusura dello stream input
	readFile = open(filePath)
	fContent = readFile.read()
	readFile.close()

# 	replacedText = re.sub(patternStr, repStr, fContent)

	count_go = len(re.findall(patternStr, fContent))
	count_mb = len(re.findall(patternStr2, fContent))

	oriFile = open(filePath, 'w')
	oriFile.write(str(count_go))
	oriFile.write(str(count_mb))
	oriFile.write(fContent)
	oriFile.close()

	if makeBackup:
		backupName = filePath+'.rep_backup'
		backupFile = open(backupName,'w')	
		backupFile.write(replacedText)
		backupFile.close()

	print("processed {}".format(filePath))
	print(count_go)
	print(count_mb)

#cerca nella directory il file a cui sono interessato (che contiene il pattern) e processalo 
def walkThroughDirAndProcess(dir):
	for subdir, dirs, files in os.walk(dir):
	    for file in files:
	        filepath = subdir + os.sep + file
	        if filepath.endswith(tuple(fileExt)) and containsPattern(filepath) and not ignoredDir in subdir:
	            replaceStringInFile(filepath)

walkThroughDirAndProcess(dirToProcess)