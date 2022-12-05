def check_attributes(feature, att, i):
	elements = list_attributes(att)
	if elements == []:
		print_error('i', 'The list of attributes has the wrong syntax')
		return False
	if len(elements) < 2:
		print_error(i, 'Missing attributes, needded at least 2')
		return False	
	if elements[0][0] != 'gene_id':
		print_error(i, 'The first attribute (' + str(elements[0][0]) + ') must be "gene_id"')
		return False
	if elements[1][0] != 'transcript_id':
		print_error(i, 'The second attribute (' + str(elements[1][0]) + ') must be "Transcript_it"')
		return False
	if(feature in ['inter', 'inter_CNS'] and (elements[0][1] != '' or elements[1][1] != '')):
		print_error(i, 'gene_id and transcript_id must be equal to '' for features: inter and inter_CNS')
		return False
	return True