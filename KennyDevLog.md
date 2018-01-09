## My Develop Logs
With SunFounder Smart Video Car Kit V2.0

Quick Links:

 * [1/8/2018](#1_8_2018)
 * [Contact me](#contact_me)

----------------------------------------------
<a id="1_8_2018"></a>
### 1/8/2018: Auto start server, auto send the IP address by email
#### IP address
If the Pi using DHCP, then the IP address may change from time to time. Here are some solutions:
1. Using static IP address in Pi.
1. On the wireless router, bind the IP address to MAC address of Pi
1. When Pi boot up, send email to notify you. Refer to:
    1. [Send email on PI](https://www.sbprojects.com/projects/raspberrypi/exim4.php)
    1. In /etc/rc.local, add commands to get current IP and call mail client to send email.
* ToDo: Try to discover the PI with mobile app.

#### Auto start the remote control server
In /etc/rc.local, add the following two lines before the "exit 0" to run the remote control server in the back ground:
* cd /home/pi/SunFounder_PiCar-V/remotecontrol
* ./start &

#### Problem found
On the web UI, cannot use the buttons to control the car. Seems that the JS functions are not triggered. Tested on Chrome/Win and all web browsers on my Mac.
* ToDo: Use jQuery to replace the current JS in /SunFounder_PiCar-V/remote_control/remote_control/templates/templates/run.html
* ToDo: Get an ANDROID app for remote control.


----------------------------------------------
<a id="contact_me"></a>
### Contact me:
* Email: he.scu2013@gmail.com
* http://kennyhe.com/
