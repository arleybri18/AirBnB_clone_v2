#!/usr/bin/env bash
# This script configure my server for webstatic

# validate if exists nginx
if [[ ! -x /usr/sbin/nginx ]]; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

# create directories and file
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
#create file for test
index_page="<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>"
echo -e "$index_page" | sudo tee /data/web_static/releases/test/index.html > /dev/null
# create symbolic links
symln=/data/web_static/current
if [ -L $symln ]
then
	sudo unlink /data/web_static/current
fi
sudo ln -snf /data/web_static/releases/test/ /data/web_static/current
# change user and group 
sudo  chown -R ubuntu:ubuntu /data/
# modify nginx configuration to server static content
location="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "37i\ $location" /etc/nginx/sites-available/default
sudo service nginx restart
