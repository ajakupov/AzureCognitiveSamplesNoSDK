# AzureCognitiveSamplesNoSDK

This repository contains Azure Cognitive Services usage samples using only standard python libraries, no special SDKs. 
Some examples require creating environmant variables. To create a variable:

Linux:
```
export NAME=VALUE


Windows:
```
$env:NAME = 'Value'

To run the solution on your environment:
1. Install Python virtual environment
```
pip install virtualenv
```
2. Go to the project folder (where you have your README.md file)
3. Create your virtual environment
```
python3 -m venv bertvent
```
4. Access to venv virtual environment
```
source bertvent/bin/activate
```
5. Install project dependencies
```
pip install -r requirements.txt
```
6. Install other packages and update your requirements with the following command
```
pip freeze>requirements.txt
```
