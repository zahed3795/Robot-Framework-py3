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
    Key Click element   xpath://a[contains(text(),'News')]

Test User Log In Using XL
    User Log In Using XL    ${password}
  
    
