from boto.s3.key import Key
from boto.s3.connection import S3Connection
from flask import Flask, request
import hashlib
import time
import os

#Create our application
app = Flask(__name__)

#Amazon S3
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', 'YOUR-ACCESS-KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', 'YOUR-SECRET-KEY')
S3_BUCKET_NAME = "mailgun-attachments"

def get_s3_bucket():
	conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
	return conn.create_bucket(S3_BUCKET_NAME)

@app.route('/')
def index():
	if request.method == "GET":
		return "Create a <a href='http://www.mailgun.com/'>Mailgun</a> route:<br/><br/>\
			<b>Filter Expression:</b> match_recipient(r'attach@you.mailgun.org')<br/> \
			<b>Action:</b> forward(r'http://%s/s3-attachment')<br/> \
			<b>Description:</b> Upload all attachments to Amazon S3<br/>" % request.headers['Host']

@app.route('/s3-attachment', methods=['POST'])
def store_attachments():
	if(len(request.files) > 0):
		bucket = get_s3_bucket()
		for attachment in request.files.values():
			data = attachment.stream.read()
			with open(attachment.filename, "w") as f:
				f.write(data)

			key = Key(bucket)

			#Include UNIX timestamp in object metadata
			key.set_metadata("timestamp", str(int(time.time())))

			#Set filename and upload
			key.key = attachment.filename
			key.set_contents_from_filename(attachment.filename)

	#Mailgun wants to see a HTTP 200 response
	return "200 OK"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
