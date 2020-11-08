def application(environ, start_response):
	status = '200 ok'
	output = b'Hello World'
	
	response_headers = [('Content-type', 'text/plain'), ('Content-length', str(len(output)))]
	start_response(status, response_headers)
	return [output]


