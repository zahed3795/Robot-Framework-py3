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
Library    BuiltIn
Resource   ../Keywords/user_Keywords.robot
Resource    ../Keywords/web_Keyword.robot
Resource    ../locators/locators.robot
Suite Setup    Log To Console    Test Started
Test Teardown      Close Browser
Suite Teardown    Log To Console    Test done
*** Test Cases ***
Example of running a python script
    ${result}=  run process      python   gui_test_runner.py
    log to console  ${result}


