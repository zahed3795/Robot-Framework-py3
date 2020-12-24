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
Resource   ../robotframework/rfswarm/Robot_Resources/perftest.resource
Library    DataDriver    file=DataDriven.xls


*** Keywords ***
User Log In
    Standard Think Time
    ${user_name}    Key Get XML Value    username
    Standard Think Time
    ${password}     Key Get XML Value    password
    Standard Think Time
    Key Click element    ${LOGIN}
    Standard Think Time
    Key Send keys        ${EMAIL_BOX}    ${user_name}
    Standard Think Time
    Key send password     ${PASSWORD_BOX}    ${password}
    Standard Think Time
    Key Click element    ${LOGIN_BUTTON}
    Standard Think Time

User Log In using Encrypt
    ${user_name}    Key Get XML Value    username
    Standard Think Time
    ${password}     Key Get XML Value    password
    Standard Think Time
    Key Click element    ${LOGIN}
    Standard Think Time
    Key Send keys        ${EMAIL_BOX}    ${user_name}
    Standard Think Time
    Key send Encrypt password     ${PASSWORD_BOX}    ${password}
    Standard Think Time
    Key Click element    ${LOGIN_BUTTON}
    Standard Think Time


User Log In Using XL
    [Arguments]         ${password}
    ${user_name}    Key Get XML Value    username
    Key Click element    ${LOGIN}
    Key Send keys        ${EMAIL_BOX}    ${user_name}
    Key send password     ${PASSWORD_BOX}    ${password}
    Key Click element    ${LOGIN_BUTTON}


