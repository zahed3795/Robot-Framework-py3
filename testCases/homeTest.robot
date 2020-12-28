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
Resource   ../Keywords/user_Keywords.robot
Resource    ../Keywords/web_Keyword.robot
Resource    ../locators/locators.robot
Suite Setup    Log To Console    Test Started  
Test Setup      key Launch driver 
Test Teardown      Close Browser
Suite Teardown    Log To Console    Test done
*** Test Cases ***  
Untitled Test Case  
    [Tags]    smoke    foundBug
    Key Verify Title    ${Tilte}
    User Log In
    
Untitled Test Case2  
    Key Verify Title    ${Tilte}
    User Log In using Encrypt

costom Test Case
    zahed_costom_keyword
    Cover Element   xpath://a[contains(text(),'News')]


  
    
