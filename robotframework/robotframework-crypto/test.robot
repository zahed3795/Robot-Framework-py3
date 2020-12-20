*** Settings ***
Library    SeleniumLibrary    plugins=CryptoLibrary.Plugin


*** Variables ***
${Admins-Password}=    crypt:u63G+YYrmlTxt6PvYzJ9x8KGNcvcyEXCi1egVLK/Qlnm1oJ4j14ufnJiyuV/CqTlfng75phbNg==


*** Test Cases ***
Decrypt as Plugin
    Open Browser      http://www.keyword-driven.de  chrome
    Input Text        input_username    admin
    Input Password    input_password    ${Admins-Password}