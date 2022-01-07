yum list installed | grep -i python3
sudo yum install python3 -y
python3 -m venv my_app/env
source ~/my_app/env/bin/activate

pip install pip --upgrade
pip install boto3

python

import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
exit()

echo "source ${HOME}/my_app/env/bin/activate" >> ${HOME}/.bashrc