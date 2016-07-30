import requests


for x in xrange(21):
	query = str(x+1) 
	if(x <= 8):
		res = requests.get('http://www.facweb.iitkgp.ernet.in/~sourav/Lecture-0' + query + '.pdf')
		pdf = open('Lec-0'+query,'wb')
	else :
		res = requests.get('http://www.facweb.iitkgp.ernet.in/~sourav/Lecture-' + query + '.pdf')
		pdf = open('Lec-'+query,'wb')
	res.raise_for_status()
	

	for chunk in res.iter_content(1000000):
		pdf.write(chunk)

	pdf.close()		
