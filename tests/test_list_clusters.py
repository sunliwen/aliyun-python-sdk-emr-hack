# pip install aliyun-python-sdk-emr-hack


import json

from os import getenv
from pprint import pprint
from aliyunsdkcore.client import AcsClient
from aliyunsdkemr.request.v20160408 import ListClustersRequest

print(getenv('ALIYUN_ACCESS_KEY_ID'))
print(getenv('ALIYUN_ACCESS_KEY_SECRET'))
client = AcsClient(ak=getenv('ALIYUN_ACCESS_KEY_ID'),
                   secret=getenv('ALIYUN_ACCESS_KEY_SECRET'),
                   region_id='cn-hangzhou')

req = ListClustersRequest.ListClustersRequest()
req.set_RegionId('cn-hangzhou')
req.set_StatusList(["CREATING", "RUNNING", "IDLE"])
req.set_accept_format("JSON")

status, headers, body = client.get_response(req)
if status == 200:
    regions = json.loads(body)
    pprint(regions)
    cluster = regions['Clusters']['ClusterInfo'][0]
    print(cluster['Name'])
else:
    print('Unexpected errors: status=%d, error=%s' % (status, body))

