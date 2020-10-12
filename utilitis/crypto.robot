*** Settings ***
Library    SeleniumLibrary
Library     CryptoLibrary    %{private_key_password}    variable_decryption=False
#private key which should be secret, should also be protected by a password
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
Resource   ../Keywords/user_Keywords.robot
Resource    ../Keywords/web_Keyword.robot
Resource    ../locators/locators.robot
Suite Setup    Log To Console    Test Started  
Test Setup      key Launch driver 
Test Teardown      Close Browser
Suite Teardown    Log To Console    Test done 

*** Variables ***
${secret}=     KILL ALL HUMANS!!!
${enc_user}=   crypt:nkpEPOVKfOko3t04XxOupA+F/ANTEuR9aQuPaPeMBGBQenwYf6UNESEl9MWRKGuj60ZWd10=
${enc_pwd}=    crypt:TVpamLXCtrzRsl8UAgD0YuoY+lSJNV73+bTYhOP51zM1GQihgyCvSZ2CoGoKsUHLFjokyJLHxFzPEB4=

*** Test Cases ***
Valid Logi                                #disable Robot Framework logging
    ${var}=    set Variable   ${secret}
    Log To Console  ${var}                               #enable Robot Framework logging
    ${user}=    Get Decrypted Text    ${enc_user}     #decrypts cipher text and returns plain text
    Log To Console    ${user}    
    ${password}=    Get Decrypted Text    ${enc_pwd}  #decrypts cipher text and returns plain text
    Log To Console    ${password}    
