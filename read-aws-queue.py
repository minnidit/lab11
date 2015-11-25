import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2

# Get the keys from a specific url and then use them to connect to AWS Service
url= sys.argv[1]
req = urllib2.Request(url)
response = urllib2.urlopen(req)
key = response.read()

access_key_id, secret_access_key = key.split(':')

name = sys.argv[2]

# Set up a connection to the AWS service.
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)



rs = conn.get_all_queues()
for q in rs:
        if q.id == name:
                response = conn.receive_message(q)
		msg=response[0]
                print "Message: "+ msg.get_body()
		q.delete_message(msg)
