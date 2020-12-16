# Raper Robot-Framework by Zahed Khan


<h2>Need to run advanced_execution/install_environment.bat in CMD or terminal for installation and this step is must: 🚀</h2>

[install_environment.bat](https://github.com/zahed3795/Robot-Framework-py3/blob/master/advanced_execution/install_environment.bat)

```bash
git clone https://github.com/zahed3795/Robot-Framework-py3.git
cd Robot-Framework-py3
pip install robotframework
pip install robotframework-seleniumlibrary
pip install robotframework-pabot
pip install webdrivermanager
pip install robotframework-crypto
pip install robotframework-excal
pip install robotframework-datadriver
pip install robotframework-requests
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
```
#### Use `python -m CryptoLibrary` and `python -m CryptoClient`
for encryption 

More read me will be added soon


