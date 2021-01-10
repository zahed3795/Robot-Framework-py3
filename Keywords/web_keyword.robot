*** Settings ***
Library    SeleniumLibrary    plugins=CryptoLibrary.Plugin
Library    Collections    
Library    DateTime    
Library    Dialogs    
Library    OperatingSystem    
Library    Process    
Library    Screenshot    
Library    String    
Library    Telnet    
Library    XML  
Resource   user_Keywords.robot
Resource    ../locators/locators.robot
Library    DataDriver    file=DataDriven.xls


*** Keywords ***
User Log In
    ${user_name}    Key Get XML Value    username
    Key Standard Think Time
    ${password}     Key Get XML Value    password
    Click Element    ${LOGIN}
    Key Send keys        ${EMAIL_BOX}    ${user_name}
    Key send password     ${PASSWORD_BOX}    ${password}
    Click Element    ${LOGIN_BUTTON}

User Log In using Encrypt
    ${user_name}    Key Get XML Value    username
    ${password}     Key Get XML Value    password
    Key Click element    ${LOGIN}
    Key Send keys        ${EMAIL_BOX}    ${user_name}
    Key send Encrypt password     ${PASSWORD_BOX}    ${password}
    Key Click element    ${LOGIN_BUTTON}



