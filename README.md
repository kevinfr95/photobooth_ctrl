# Photobooth_ctrl
This python script to control the lights and the power of DIY photobooth.


## Requirements 
Copy all the files in /opt/photobooth_ctrl/ folder and install the requirements

```
sudo pip3 install RPi.GPIO
sudo pip3 install gpiozero
```

## Create the service
To run the script automatically at the startup copy the systemd folder:
```
sudo cp photobooth.service /etc/systemd/system/photobooth.service
````

And activate it:
```
sudo systemctl daemon-reload
sudo systemctl enable photobooth.service
sudo systemctl start photobooth.service
```
