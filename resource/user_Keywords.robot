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

*** Variables ***
${BROWSER}   chrome
${SELSPEED}  0.500s

*** Keywords ***
Key Click element
    [Arguments]    ${locator}
    Wait Until Element Is Visible    ${locator}
    Click Element    ${locator}      
    
Key Verify Title
    [Arguments]    ${title}
    ${realTitle}    Get Title
    Convert To String    ${realTitle}
    Strip String    ${realTitle}  
    Strip String    ${title} 
    Should Be Equal As Strings    ${realTitle}    ${title}    
    Title Should Be    ${title}    
    
    

  