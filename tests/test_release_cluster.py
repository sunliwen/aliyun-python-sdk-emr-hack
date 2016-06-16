# pip install aliyun-python-sdk-emr-hack

import json

from os import getenv
from aliyunsdkcore.client import AcsClient
from aliyunsdkemr.request.v20160408 import ListClustersRequest, CreateClusterRequest

print(getenv('ALIYUN_ACCESS_KEY_ID'))
print(getenv('ALIYUN_ACCESS_KEY_SECRET'))
client = AcsClient(ak=getenv('ALIYUN_ACCESS_KEY_ID'),
                   secret=getenv('ALIYUN_ACCESS_KEY_SECRET'),
                   region_id='cn-hangzhou')

create_cluster_body = [
    {
        "NodeCount": 1,
        "NodeType": "MASTER",
        "InstanceType": "ecs.n1.large",
        "DiskType": "CLOUD_EFFICIENCY",
        "DiskCapacity": 80,
        "DiskCount": 1,
        "Index": 1
    },
    {
        "NodeCount": 1,
        "NodeType": "CORE",
        "InstanceType": "ecs.n1.large",
        "DiskType": "CLOUD_EFFICIENCY",
        "DiskCapacity": 80,
        "DiskCount": 1,
        "Index": 2

    }
]

req = CreateClusterRequest.CreateClusterRequest()

req.set_accept_format("JSON")

req.set_RegionId('cn-hangzhou')
req.set_Name('test-liwen-cluster')

req.set_SecurityGroupId('sg-23oe84n4q')

req.set_AutoRenew(False)
req.set_ChargeType('PostPaid')
req.set_ClusterType('HADOOP')
req.set_EmrVer("EMR-1.2.0")
req.set_IsOpenPublicIp(True)
req.set_LogEnable(True)
req.set_LogPath('oss://dell-liwen-test-log/test_liwen_cluster')
req.set_MasterPwdEnable(True)
req.set_MasterPwd('Aa1234567890')
req.set_ZoneId('cn-hangzhou-b')

req.set_EcsOrder(create_cluster_body)


status, headers, body = client.get_response(req)
if status == 200:
    result = json.loads(body)
    print(result)
else:
    print('Unexpected errors: status=%d, error=%s' % (status, body))
