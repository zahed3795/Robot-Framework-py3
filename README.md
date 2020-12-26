# Raper Robot-Framework by Zahed Khan


<h2>Need to run advanced_execution/install_environment.bat in CMD or terminal for installation and this step is must: 🚀</h2>

[install_environment.bat](https://github.com/zahed3795/Robot-Framework-py3/blob/master/advanced_execution/install_environment.bat)

```bash
git clone https://github.com/zahed3795/Robot-Framework-py3.git
cd Robot-Framework-py3
@ECHO OFF
pip install robotframework-pabot
pip install webdrivermanager
pip install robotframework-datadriver
pip install robotframework-requests
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
cd..
pip install -U robotframework-datadriver[XLS]
```

Framework can download web-drivers 

```bash
webdrivermanager firefox chrome opera edge 
 or 
webdrivermanager firefox chrome opera edge --linkpath (Your prefarable path)
```
# Selenium raper keywords
Helps to improve selenium keywords
```robotframework
Key Click element
    [Arguments]    ${locator}
    
Key Send keys
    [Arguments]    ${locator}     ${text}   
       
Key Verify Title
    [Arguments]    ${title}  

Key send password 
    [Arguments]    ${locator}    ${text}
    
Key send Encrypt password 
    [Arguments]    ${locator}    ${text}
```
#### Use `python -m CryptoLibrary` and `python -m CryptoClient`
for encryption 

### You can add your own selenium keywork from selenium 

More read me will be added soon


