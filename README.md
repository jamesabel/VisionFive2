# VisionFive2

My journey with the VisionFive 2 open source quad-core RISC-V dev board

# Bill of Materials

[VisionFive 2 open source quad-core RISC-V dev board](https://www.kickstarter.com/projects/starfive/visionfive-2)

[Geekworm Raspberry Pi Heatsink CPU Cooler 8PCS Copper Heatsinks with Thermal Conductive Adhesive](https://www.amazon.com/dp/B0B2CP1G23) 
(optional but highly recommended and these fit well)

[SanDisk 64GB Extreme microSDXC UHS-I Memory Card](https://www.amazon.com/dp/B09X7C7LL1) (you can pick a size to suit your application, 
but this size worked for me and was reasonably priced)

[M2.5 Black Nylon Screw, Nut and Standoff Set](https://www.amazon.com/dp/B07XJWF7HM) (I opted for nylon vs metal just to be safe, 
but you can use metal if you're comfortable with that)

[QILIPSU Junction Box with Mounting Plate 250x150x100mm, Clear Cover Plastic DIY Electrical Project Case IP67](https://www.amazon.com/dp/B07H5B9W5H) 
(or pick a box more appropriate for your setup)

[65W/61W USB C Power Adapter, WEGWANG Type C Power Delivery PD Wall Charger 65W](https://www.amazon.com/dp/B07KXGXBL6) 
(or equivalent)

[WEme CF Card Reader, Aluminum SuperSpeed Micro SD Card Converter with OTG Adapter for SanDisk CF TF SDHC SDXC MMC Card, USB 3.0 SD Card Reader Writer](https://www.amazon.com/dp/B06Y4BW487) 
(or equivalent)

[Kingston NV2 250G M.2 2280 NVMe Internal SSD](https://www.amazon.com/dp/B0BBWH7DBT) (optional, pick size to suit your application)

# The Board

![Vision Five 2 with heatsinks](vision_five_2_with_heatsinks.jpg "Vision Five 2 with heatsinks")
Vision Five 2 with heatsinks

![](vision_five_2_with_ssd.jpg "Vision Five 2 with SSD") 
Vision Five 2 with SSD installed

# Initial Setup

Mount the VisionFive 2 card in the proto box using the nylon standoffs. Drill holes in the proto box to allow for wires.

## Flash SD Card

Initially use the `55` StarFive Debian OS image: [starfive-jh7110-VF2-VF2_515_v2.3.0-55.img.bz2](https://drive.google.com/file/d/14RDGjyUkyUKsowP7zH8E55Ym6FpuE899) .

Use [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/) to flash the above Debian OS image to the SD card.
(The Balena Etcher did not work for me)

## Hardware connections

- Connect an ethernet cable to one of the board's ethernet connectors.
- Connect power to the USB-C connector.

Tip: use a power strip with an on/off switch to control power to the board. It doesn't have its own power switch.

![](vision_five_2_with_power_and_ethernet.jpg "Vision Five 2 with power and ethernet")

## Access via your local network

The board will appear on your network as `starfive`. Use [PuTTY](https://www.putty.org/) or similar to login to the board.

Note: you don't need to use the "serial port".

Also, the HDMI and mouse/keyboard don't work at this point.

## Login

Initial login:

```
Username: user
Password: starfive
```

Note that `root` login may not work yet. [Follow these directions to enable root](https://doc-en.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/enable_ssh_root_login.html).

After root is enabled, you can now also login as root:

```
Username: root
Password: starfive
```

## Python

First, [Install Python](https://cloudinfrastructureservices.co.uk/how-to-install-python-3-in-debian-11-10/). 
You probably only need to do this (as root):

```shell
apt update
apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
apt install python3 -y
apt install python3-venv
```

## Using the SSD

If you installed the SSD (recommended), perform the steps given at [StarFive VisionFive 2 Official Debian SSD Boot Guide](https://jamesachambers.com/starfive-visionfive-2-debian-ssd-boot-guide/) 
to enable it.

Note that your "disk" size will be whatever you started with when you booted from the SD card, which is probably smaller
than you'd like and uses only part of your SSD. One option (what I currently used) is to create a new partition on the 
SSD, format it, and mount it to some useful location (e.g., somewhere in your user directory). This way you can use 
the additional disk space without having to expand the partition while you're running.

I ended up with:

```shell
user@starfive:~/projects$ lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
mmcblk1     179:0    0  59.5G  0 disk
|-mmcblk1p1 179:1    0    16M  0 part
|-mmcblk1p2 179:2    0   100M  0 part
`-mmcblk1p3 179:3    0  14.5G  0 part
nvme0n1     259:0    0 232.9G  0 disk
|-nvme0n1p1 259:1    0    16M  0 part
|-nvme0n1p2 259:2    0   100M  0 part
|-nvme0n1p3 259:3    0  14.5G  0 part /
`-nvme0n1p4 259:4    0 218.2G  0 part /home/user/projects

user@starfive:~/projects$ df -h
Filesystem      Size  Used Avail Use% Mounted on
udev            1.7G     0  1.7G   0% /dev
tmpfs           390M  1.7M  388M   1% /run
/dev/nvme0n1p3   15G   12G  2.5G  83% /
tmpfs           2.0G     0  2.0G   0% /dev/shm
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
/dev/nvme0n1p4  214G   20M  203G   1% /home/user/projects
tmpfs           390M   28K  390M   1% /run/user/111
tmpfs           390M   20K  390M   1% /run/user/0
tmpfs           390M   24K  390M   1% /run/user/1000

```

While I used up 83% of my original "root" partition (e.g. for OS, etc.), I now have over 200GB ready for projects. 

Perhaps someone will create a utility that automatically does the repartition, but this works for now.

# References

## Websites

[StarFive VisionFive 2 High Performance RISC-V SBC Review by James Chambers](https://jamesachambers.com/starfive-visionfive2-review/)

## OSs

[Debian OS images](https://drive.google.com/drive/folders/1yhMVrB05wSjcqbrxgW2nXJNOeSC3ViRx)

[Main Debian StarFive page](https://debian.starfivetech.com/)
