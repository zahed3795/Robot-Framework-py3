@ECHO OFF
pip install robotframework-pabot
pip install webdrivermanager
pip install robotframework-datadriver
pip install robotframework-requests
webdrivermanager firefox chrome opera edge --linkpath C:\Users\bakul\AppData\Local\Programs\Python\Python38
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
cd..
pip install -U robotframework-datadriver[XLS]
