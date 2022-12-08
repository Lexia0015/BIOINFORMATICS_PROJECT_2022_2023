# def check_attributes(feature, att, i):
# 	elements = list_attributes(att)
# 	if elements == []:
# 		print_error('i', 'The list of attributes has the wrong syntax')
# 		return False
# 	if len(elements) < 2:
# 		print_error(i, 'Missing attributes, needded at least 2')
# 		return False	
# 	if elements[0][0] != 'gene_id':
# 		print_error(i, 'The first attribute (' + str(elements[0][0]) + ') must be "gene_id"')
# 		return False
# 	if elements[1][0] != 'transcript_id':
# 		print_error(i, 'The second attribute (' + str(elements[1][0]) + ') must be "Transcript_it"')
# 		return False
# 	if(feature in ['inter', 'inter_CNS'] and (elements[0][1] != '' or elements[1][1] != '')):
# 		print_error(i, 'gene_id and transcript_id must be equal to '' for features: inter and inter_CNS')
# 		return False
# 	return True

# define a function
# for transcription
def transcript(x) :
	
	# convert string into list
	l = list(x)

	for i in range(len(x)):

		if(l[i]=='G'):
			l[i]='C'

		elif(l[i]=='C'):
			l[i]='G'

		elif (l[i] == 'T'):
			l[i] = 'A'

		elif (l[i] == 'A'):
			l[i] = 'U'

		else:
			print('Invalid Input')					
			
	print("Translated DNA : ",end="")	
	for char in l:
		print(char,end="")

# Driver code
if __name__ == "__main__":
	
	x = "GCTAA"
	# function calling
	transcript(x)
