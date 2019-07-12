# SETUP AWS
# aws configure set $ACCESS_KEY_ID $SECRET_ACCESS_KEY;
echo "***** Transfering files to ec2 instance *****\n"
scp -r -v -o "StrictHostKeyChecking no" ~/repo ${DEPLOY_USER}@${DEPLOY_LOCATION}:~/tmp

echo "***** SSHing into ec2 instance for setup *****\n"
ssh -tt -o "StrictHostKeyChecking no" ${DEPLOY_USER}@${DEPLOY_LOCATION} << HERE
    killall screen
    rm -rf ~/api
    mv ~/tmp ~/api
    cd api
    sudo pip3 install -r requirements.txt # <- I know this isn't ideal
    screen -dm python3 ./manage.py runserver
    exit
HERE
