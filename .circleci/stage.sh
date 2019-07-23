# SETUP AWS
echo "***** Transfering files to ec2 instance *****\n"
scp -r -v -o "StrictHostKeyChecking no" ~/repo ${DEPLOY_USER}@${DEPLOY_LOCATION}:~/tmp

echo "***** SSHing into ec2 instance for setup *****\n"
ssh -tt -o "StrictHostKeyChecking no" ${DEPLOY_USER}@${DEPLOY_LOCATION} << HERE
    aws ec2 describe-tags > awstags.json
    numtags="$(jq -r '.[]| length' awstags.json)"
    echo $numtags
    i=0
    while [ $i -lt $numtags ]
    do
        Key="$(jq -r '.Tags['$i'] | [.Key] | join("/")' awstags.json)"
        Value="$(jq -r '.Tags['$i'] | [.Value] | join("/")' awstags.json)"
        echo $Key
        echo $Value
        export $Key=$Value
        ((i++))
    done
    killall screen
    rm -rf ~/api
    mv ~/tmp ~/api
    cd api
    pip3 install -r requirements.txt --user # <- I know this isn't ideal. Andy: Changed to --user to fix psycopg2.
    rm /home/ec2-user/api/trackr_server/settings.py
    ln -s /home/ec2-user/settings.py /home/ec2-user/api/trackr_server/settings.py
    python3 ./manage.py migrate
    screen -dm python3 ./manage.py runserver
    exit
HERE
