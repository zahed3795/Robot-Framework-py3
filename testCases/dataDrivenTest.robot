*** Settings ***
Library    SeleniumLibrary    plugins=CryptoLibrary.Plugin
Library    DataDriver    DataDriven.xls
Library    Collections    
Library    DateTime    
Library    Dialogs    
Library    OperatingSystem    
Library    Process    
Library    Screenshot    
Library    String    
Library    Telnet    
Library    XML
Library    BuiltIn
Library    DataDriver    file=DataDriven.xls
Resource   ../robotframework/rfswarm/Robot_Resources/perftest.resource
Resource   ../Keywords/user_Keywords.robot
Resource    ../Keywords/web_Keyword.robot
Resource    ../locators/locators.robot
Suite Setup    Log To Console    Test Started  
Test Setup      key Launch driver 
Test Teardown      Close Browser
Suite Teardown    Log To Console    Test done
Test Template   User Log In Using XL
*** Comments ***
    Data driven test with xls files
*** Test Cases ***  
Login with user '${userName}' and password '${password}' for finviz
    
*** Keywords ***
User Log In Using XL
    [Arguments]        ${userName}        ${password}
    Key Click element    ${LOGIN}
    Key Send keys        ${EMAIL_BOX}    ${userName}
    Key send password     ${PASSWORD_BOX}    ${password}
    Key Click element    ${LOGIN_BUTTON}
  
    
