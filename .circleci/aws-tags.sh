aws ec2 describe-tags > awstags.json
numtags="$(jq -r '.[]| length' awstags.json)"
i=0
while [ $i -lt $numtags ]
do
    Key="$(jq -r '.Tags['$i'] | [.Key] | join("/")' awstags.json)"
    Value="$(jq -r '.Tags['$i'] | [.Value] | join("/")' awstags.json)"
    export $Key=$Value
    ((i++))
done
