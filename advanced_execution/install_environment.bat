@ECHO OFF
pip install webdrivermanager
webdrivermanager firefox chrome opera edge --linkpath C:\Users\zahed\AppData\Local\Programs\Python\Python38
cd..
cd robotframework
cd robotframework-crypto
python setup.py install
cd..
cd SeleniumLibrary
python setup.py install
pip install -r requirements.txt
cd..
cd robotframework
python setup.py install
cd..
cd rfswarm
python setup-agent.py install
python setup-gui.py install
cd..
cd robotframework-datadriver
python setup.py install
cd..
cd pabot
python setup.py install
pip install -r requirements.txt
cd..
cd robotframework-requests
python setup.py install
pip install -r requirements.txt
cd..
cd..
pip install -U robotframework-datadriver[XLS]
