
"""DEVNOTES::::PUT ALL THE LOGIN PORTION IN A FUNCTION CALLED MOODLE LOGIN AND ALL THE PART OF CHECKING UPDATES IN A FUNCTION CALLED MOODLE_CHECK(IT CAN BE IN LOWERCASE!!!)"""
def moodle_login():
    ID="ID"#put your moodle id here for example ph1200xx
    PWD="password"#put your password here 
    driver.get("https://moodle.iitd.ac.in/login/index.php")  
    """finding username tbox,clicking on it,typing id,same with pwd"""
    username_textbox = driver.find_element_by_id("username")
    username_textbox.click()
    username_textbox.send_keys(ID)
    password_textbox = driver.find_element_by_id("password")
    password_textbox.click()
    password_textbox.send_keys(PWD)

    formtext=driver.find_element_by_xpath('//*[@id="login"]')
    """print(formtext.text)
    gives output
    Username / email
    Password
    Remember username
    Please subtract 56 - 84 =
    Forgotten your username or password?
    """
    lines=formtext.text.split("\n")
    """print(lines) gives output
    ['Username / email', 'Password', 'Remember username', 'Please enter first value 85 , 92 =', 'Forgotten your username or password?']
    so we need to check for the element at index 3"""
    condition=lines[3]
    """now checking for one of the four possibilities:add,subtract,find first elem,find second elem
    and for that we need to use regular expressions using re module"""
    import re
    from selenium.webdriver.common.keys import Keys#guess i can't press backspace using strings ;)
    i_aint_a_bot_test_box = driver.find_element_by_id("valuepkg3")
    i_aint_a_bot_test_box.click()
    i_aint_a_bot_test_box.send_keys(Keys.BACK_SPACE)
    if re.search("Please enter first value",condition):
        val=condition.split()[4]
    elif re.search("Please enter second value",condition):
        val=condition.split()[6]
    elif re.search("Please add",condition):
        val=int(condition.split()[2])+int(condition.split()[4])
    else:
        val=int(condition.split()[2])-int(condition.split()[4]) 
    i_aint_a_bot_test_box.send_keys(str(val))

    loginbutton=driver.find_element_by_id("loginbtn")
    loginbutton.click()
    """YAAYYYYY!!!!! """





##driver.close()

 
