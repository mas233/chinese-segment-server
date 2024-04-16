docker stop segment | true
docker rmi chinese-segment | true
docker rm segment | true
docker build -t chinese-segment .
docker run -d --name segment -p 5050:5050 chinese-segment
