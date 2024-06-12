lines=[]
objects=[]

f = open("table.txt","r")

for textline in f:
	lines.append(textline.replace("\n",""))
f.close()

for item in lines:
	# Split the string by whitespace
	words = item.split()
	# Ensure there are exactly two words
	if len(words) == 2:
		# Create a dictionary with the first and second word
		word_dict = {'ip': words[0], 'asn': int(words[1])}
		objects.append(word_dict)

problematicASN = 32934
nameOfAddressSet = "Facebook"

for bloc in objects:
	if bloc["asn"] == problematicASN:
		print("set security address-book global address " + bloc["ip"] + " " + bloc["ip"] + ' description "' + nameOfAddressSet + '"')
		print("set security address-book global address-set " + nameOfAddressSet + " address " + bloc["ip"])





#print(objects)
