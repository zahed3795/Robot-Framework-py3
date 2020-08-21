*** Settings ***
Library    SeleniumLibrary  
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




*** Keywords ***
User Log In       
    ${user_name}    Key Get XML Value    username 
    ${password}     Key Get XML Value    password
    Key Click element    ${LOGIN}
    Key Send keys        ${EMAIL_BOX}    ${user_name}
    Key send password     ${PASSWORD_BOX}    ${password}
    Key Click element    ${LOGIN_BUTTON}






