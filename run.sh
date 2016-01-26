apt-get install curl
wget -qO- https://get.docker.com/ | sh
wget https://raw.githubusercontent.com/zh19970205/little_tools/master/Dockerfile
docker build -t tools .
docker run -d -p 80:80 -m 512m --name=tools --cpu-period=50000 --cpu-quota=25000 tools
while((1));do
	OK=NOT
	OK=$(curl -m 1 'http://localhost/python?run=print(%22OK%22)')
	if [ $OK != OK];then
		docker kill tools
		docker run -d -p 80:80 -m 512m --name=tools --cpu-period=50000 --cpu-quota=25000 tools
	fi
done;
