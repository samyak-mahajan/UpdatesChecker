
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
    lines=formtext.teAfxt.split("\n")
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
"""Add the moodle course links and other forum links in this dictionary by logging into moodle,opening the course page and copying the url in this dictioonary.
For detailed instructions see the configurations file(Though I doubt I could tell you more than this ;).
I am from batch B so I am putting links for Batch B"""
#right now I am just creating the logic so I am using only one link. rest others can be similarly done easily once I create the full logic
Courses_website_dict={"2002-ELL101":"https://moodle.iitd.ac.in/course/view.php?id=11053"}
import pickle



##driver.close()

 
