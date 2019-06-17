import boto3

client = boto3.client('elb')
#Get Elb Name
lb = client.describe_load_balancers()
name = lb["LoadBalancerDescriptions"][0]["LoadBalancerName"]
l = []
ec2 = boto3.resource('ec2')
for i in ec2.instances.all():
	for tag in i.tags:
		if tag['Key'] == 'Name':
			if "k8s" in tag['Value']: 
				#print tag['Value']
				#print(i.id)
				dict = {'InstanceId':i.id}
				#print dict
				l.append(dict)

#print l
response = client.register_instances_with_load_balancer(
    LoadBalancerName=name,
    Instances=l
)
