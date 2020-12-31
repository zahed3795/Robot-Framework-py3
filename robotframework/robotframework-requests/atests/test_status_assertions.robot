*** Settings ***
Library  ../src/RequestsLibrary/RequestsKeywords.py
Resource  res_setup.robot

Suite Setup     Setup Flask Http Server
Suite Teardown  Teardown Flask Http Server And Sessions


*** Test Cases ***

Request And Status Should Be Different
    [Tags]  get  status
    ${resp}=  Get Request  ${GLOBAL_LOCAL_SESSION}  /status/404
    Run Keyword And Expect Error  Url: http://localhost:5000/status/404 Expected status: 404 != 201  Status Should Be  201  ${resp}

Request And Status Should Be Equal
    [Tags]  get  status
    ${resp}=  Get Request  ${GLOBAL_LOCAL_SESSION}  /status/404
    Status Should Be  404  ${resp}

Request And Status Should Be A Named Status Code
    [Tags]  get  status
    ${resp}=  Get Request  ${GLOBAL_LOCAL_SESSION}  /status/418
    Status Should Be  I am a teapot  ${resp}

Request And Status Should Be An Invalid Named Status
    [Tags]  get  status
    ${resp}=  Get Request  ${GLOBAL_LOCAL_SESSION}  /status/418
    Run Keyword And Expect Error    UnknownStatusError: i am an alien    Status Should Be  i am an alien  ${resp}

Invalid Response
    [Tags]  get  status
    Run Keyword And Expect Error  InvalidResponse: this-is-not-a-request*
    ...  Status Should Be  123   this-is-not-a-request

Request And Status Should Be With A Message
    [Tags]  get  status
    ${resp}=  Get Request  ${GLOBAL_LOCAL_SESSION}  /status/418
    Run Keyword And Expect Error  He should be a teapot! Url: http://localhost:5000/status/418 Expected status: 418 != 200
    ...   Status Should Be  OK  ${resp}  He should be a teapot!

Request Should Be Successful
    [Tags]  get  status
    ${resp}=  Get Request  ${GLOBAL_LOCAL_SESSION}  /status/200
    Request Should Be Successful  ${resp}

Request Should Not Be Successful
    [Tags]  get  status
    ${resp}=  Get Request  ${GLOBAL_LOCAL_SESSION}  /status/500
    Run Keyword And Expect Error  HTTPError: 500*  Request Should Be Successful  ${resp}
