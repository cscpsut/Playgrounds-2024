sudo docker rm -f xsisi
sudo docker rmi -f xsisi
sudo docker build -t xsisi .
sudo docker run --rm --name xsisi -p 80:80 -e FLAG=PlaygroundsCTF{FAKE_FLAG_FOR_TESTING} xsisi
