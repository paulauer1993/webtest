*** Settings ***
Library    webtest.py

Test Setup    SETUP
Test Teardown    TEARDOWN

*** Keywords ***
SETUP
    OPEN BROWSER

TEARDOWN
    CLOSE BROWSER

*** Test Cases ***
TEST WEB APP
    SIGN IN
    CREATE ACCOUNT
    CHECK ADDRESS
    SIGN OUT
    Sleep    10
