# lava points
## install python and screen
```
sudo apt-get update
sudo apt-get install python3.10
sudo apt install screen
sudo apt install git
```
```
sudo apt install python3-pip
```
```
git clone https://github.com/Theshaho/lava/
```
```
cd lava
```
## Change Starknet Main RPC
```
nano rpc.py
```
Ctrl+X / Y / Enter

### Run Starknet Mainnet
```
screen -S lava-stark-main
```
```
python3 starknet_main.py
```
CTRL + A + D
