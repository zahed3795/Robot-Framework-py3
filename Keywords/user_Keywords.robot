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
Resource    ../locators/locators.robot
Resource    ../Keywords/user_Keywords.robot
Resource    ../Keywords/web_Keyword.robot
*** Keywords ***
Key Click element
    [Arguments]    ${locator}
    Wait Until Element Is Visible    ${locator}
    Wait Until Element Is Enabled    ${locator}    
    Click Element    ${locator}      
    
Key Verify Title
    [Arguments]    ${title}
    ${realTitle}    Get Title
    Convert To String    ${realTitle}
    Strip String    ${realTitle}  
    Strip String    ${title} 
    Should Be Equal As Strings    ${realTitle}    ${title}    
    Title Should Be    ${title}    
    
    
Key user name text 
    [Arguments]    ${locator}    ${text}
    Wait Until Element Is Visible    ${locator}   
    Wait Until Element Is Enabled    ${locator}
    Clear Element Text    ${locator}
    Input Text    ${locator}    ${text}    
    

Key user send password 
    [Arguments]    ${locator}    ${text}
    Wait Until Element Is Visible    ${locator}   
    Wait Until Element Is Enabled    ${locator}
    Clear Element Text    ${locator}
    Input Password    ${locator}    ${text}  

key Launch driver
    ${browser}    Key Get Browser    browser
    Run Keywords  Open Browser  ${URL}    ${browser}
    ...    AND    Maximize Browser Window
    ...    AND   Set Selenium Speed  ${SELSPEED}
    ...    AND     Delete All Cookies
Key Get Browser 
    [Arguments]    ${arg}
    ${value}=    Parse Xml    ${xml}    
    ${browser}    Get Element Text    ${value}    ${arg}
    [Return]    ${browser}  
    
Key Get Username 
    [Arguments]    ${arg}
    ${value}=    Parse Xml    ${xml}    
    ${username}    Get Element Text    ${value}    ${arg}
    [Return]    ${username} 

Key Get Password 
    [Arguments]    ${arg}
    ${value}=    Parse Xml    ${xml}    
    ${password}    Get Element Text    ${value}    ${arg}
    [Return]    ${password} 
    
Key Get XML Value
    ${value}=    Parse Xml    ${xml}   
    FOR    ${value}    IN      @{value}    
    ${dict}    Create Dictionary    ${value.tag}      ${value.text}
    ${b}    Get Dictionary Values    ${dict}    browser  
    Log To Console     ${b}
    END 
      
    
    #[Return]    ${value}

    
    





 
  