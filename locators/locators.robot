*** Variables ***
${LOGIN}    link=Login
${EMAIL_BOX}        xpath=//input[@name='email']
${PASSWORD_BOX}     xpath=//input[@name='password']
${LOGIN_BUTTON}     xpath=//input[@value='Log in']

${BROWSER}   chrome
${SELSPEED}  0.000s
${URL}    https://finviz.com/
${Tilte}    FINVIZ.com - Stock Screener

${xml}    ${CURDIR}\\credin.xml
