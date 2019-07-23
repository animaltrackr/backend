# SETUP AWS
echo "***** Transfering files to ec2 instance *****\n"
scp -r -v -o "StrictHostKeyChecking no" ~/repo ${DEPLOY_USER}@${DEPLOY_LOCATION}:~/tmp

echo "***** SSHing into ec2 instance for setup *****\n"
ssh -tt -o "StrictHostKeyChecking no" ${DEPLOY_USER}@${DEPLOY_LOCATION} << HERE
    killall screen
    rm -rf ~/api
    mv ~/tmp ~/api
    source ./api/.circleci/aws-tags.sh
    ls -la
    cd api
    pip3 install -r requirements.txt --user # <- I know this isn't ideal. Andy: Changed to --user to fix psycopg2.
    python3 ./manage.py migrate
    screen -dm python3 ./manage.py runserver
    exit
HERE
