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
Resource   ../resource/user_Keywords.robot

*** Variables ***
${BROWSER}   chrome
${SELSPEED}  0.0s
${URL}    https://finviz.com/
${Tilte}    FINVIZ.com - Stock Screener



${LOGIN}    link=Screener



*** Test Cases ***
Untitled Test Case
    [Setup]  Run Keywords  Open Browser  ${URL}  ${BROWSER}
    ...    AND    Maximize Browser Window
    ...    AND   Set Selenium Speed  ${SELSPEED}
    Key Verify Title    ${Tilte}
    Key Click element      ${LOGIN}  
    Log To Console    test done    
    #[Teardown]  Close Browser