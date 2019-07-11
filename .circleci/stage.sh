# SETUP AWS
# aws configure set $ACCESS_KEY_ID $SECRET_ACCESS_KEY;
echo "Transfering files to ec2 instance"
echo ${DEPLOY_USER}@${DEPLOY_LOCATION}
scp -r -o "StrictHostKeyChecking no" ~/repo ${DEPLOY_USER}@${DEPLOY_LOCATION}:~/tmp

ssh -o "StrictHostKeyChecking no" ${DEPLOY_USER}@${DEPLOY_LOCATION} << HERE
    pwd
    ls -la
    ls ./tmp -la
    ls ./tmp/repo -la
    ls ./tmp/repo/trackr_server -la
    ls ./tmp/repo/backend -la
HERE
