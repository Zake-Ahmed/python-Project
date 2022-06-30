#! /bin/bash

sudo cp /home/zake3/python-Project/app.service /tmp/app.service
sudo cp /tmp/app.service /etc/systemd/system/app.service
sudo systemctl daemon-reload
sudo systemctl start app