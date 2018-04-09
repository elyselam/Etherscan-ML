import csv, json, sys
#if you are not using utf-8 files, remove the next line
#sys.setdefaultencoding("UTF-8") #set the encode to utf8
#check if you pass the input file and output file
if sys.argv[1] is not None and sys.argv[2] is not None:
    fileInput = sys.argv[1]
    fileOutput = sys.argv[2]
    inputFile = open(fileInput) #open json file
    outputFile = open(fileOutput, 'w') #load csv file
    data = json.load(inputFile) #load json content
    inputFile.close() #close the input file
    output = csv.writer(outputFile) #create a csv.write
    output.writerow(data[0].keys())  # header row
    for row in data:
        output.writerow(row.values()) #values row
