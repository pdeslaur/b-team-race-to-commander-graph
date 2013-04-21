from tempfile import mkstemp
from shutil import move
from os import remove, close
import datetime

levels = { 1: 0, 2: 800, 3: 1900, 4: 3300, 5: 5300, 6: 7900, 7: 11100, 8: 14900, 9: 19300, 10: 24300, 11: 30100, 12: 36700, 13: 44100, 14: 52300, 15: 61300, 16: 71100, 17: 81700, 18: 93100, 19: 105300, 20: 118300, 21: 132100, 22: 146700, 23: 162100, 24: 178300, 25: 195300, 26: 213100, 27: 231700, 28: 251100, 29: 271300, 30: 292300, 31: 314100, 32: 337100, 33: 361300, 34: 386700, 35: 413300, 36: 441100, 37: 470100, 38: 500300, 39: 531700, 40: 564300, 41: 598100, 42: 633100, 43: 669300, 44: 706700, 45: 745300, 46: 785100, 47: 826100, 48: 868300, 49: 911700, 50: 956300, 51: 1002100, 52: 1049100, 53: 1097300, 54: 1146700, 55: 1197300, 56: 1249100 }

def replaceFirst(file_path, pattern, subst):
	#Create temp file
	hasBeenReplaced = False
	fh, abs_path = mkstemp()
	new_file = open(abs_path,'w')
	old_file = open(file_path)
	for line in old_file:
		replaced = line.replace(pattern, subst)

		if hasBeenReplaced:
			toWrite = line
		else:
			toWrite = replaced
		
		if replaced != line:
			hasBeenReplaced = True

		new_file.write(toWrite)
	#close temp file
	new_file.close()
	close(fh)
	old_file.close()
	#Remove original file
	remove(file_path)
	#Move new file
	move(abs_path, file_path)

while 1:
	level = 0
	xpneeded = 0
#	date = ""
#	try:
#		date=raw_input('Date: ')
#	except ValueError:
#		print "Not a number"
#		break
	
	try:
		level=int(raw_input('[Bdubs] Next level: '))
	except ValueError:
		print "Not a number"
		break

	try:
		xpneeded=int(raw_input('XP needed: '))
	except ValueError:
		print "Not a number"
		break

	bdoubleo100 = levels[level]-xpneeded

	try:
		level=int(raw_input('[Genny] Next level: '))
	except ValueError:
		print "Not a number"
		break

	try:
		xpneeded=int(raw_input('XP needed: '))
	except ValueError:
		print "Not a number"
		break

	generikb = levels[level]-xpneeded
	#replaceFirst("data.tsv", "genny", str(levels[level]-xpneeded))

	toWrite = "\n" + datetime.datetime.now().strftime("%Y%m%d") + "\t" + str(bdoubleo100) + "\t" + str(generikb)

	with open("data.tsv", "a") as myfile:
		myfile.write(toWrite)







