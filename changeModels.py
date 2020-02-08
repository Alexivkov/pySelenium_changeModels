from selenium import webdriver
import time


browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

def textChange(mypath, model):
    s = mypath.text
    mypath.clear()
    line =  s[:s.find("htc")-1] + model
    mypath.send_keys(line)

def fx(xpath):
    return browser.find_element_by_xpath("/" + xpath)

try:
    browser.get("https://remtel66.ru/iladmin/?route=iladmin")
    browser.implicitly_wait(3)
    # Enter Account
    # input('Enter login and password')
    login = 'd'
    password = ''
    browser.find_element_by_xpath('//html/body/div[2]/div/form/table/tbody/tr[2]/td[1]/input').send_keys(login)
    browser.find_element_by_xpath('//html/body/div[2]/div/form/table/tbody/tr[2]/td[2]/input').send_keys(password)
    browser.find_element_by_xpath('/html/body/div[2]/div/form/table/tbody/tr[2]/td[3]/input').click()
    time.sleep(2)
    myDict = {
        "Honor 6C":"344",
        "6X": "347",
        "6": "349",
        "8S": "350"
    }
    for key in myDict:
        model = key
        browser.get("https://remtel66.ru/iladmin/goods.php?c_id=" + myDict[key])

        listOfTd = browser.find_elements_by_tag_name("tr")
        myList = []
        for i in listOfTd:
                 if "".join(filter(str.isdigit, i.text)):
                    myList.append("".join(filter(str.isdigit, i.text)))


        for j in myList:
            link = 'https://remtel66.ru/iladmin/goods.php?edits=' + j
            browser.get(link)
            time.sleep(2)


            modelTire = "-".join(model.split(" "))
            textChange(browser.find_element_by_xpath('//html/body/div[3]/div/div/form[1]/table/tbody/tr[2]/td[2]/textarea'), modelTire)
            s = browser.find_element_by_xpath('//html/body/div[3]/div/div/form[1]/table/tbody/tr[2]/td[2]/textarea').text
            line = s[:s.find("htc")] + modelTire
            browser.find_element_by_xpath('//html/body/div[3]/div/div/form[1]/table/tbody/tr[2]/td[2]/textarea').clear()
            browser.find_element_by_xpath('//html/body/div[3]/div/div/form[1]/table/tbody/tr[2]/td[2]/textarea').send_keys(line)
            browser.find_element_by_xpath("//html/body/div[3]/div/div/form[1]/table/tbody/tr[8]/td[2]/textarea").clear()
            browser.find_element_by_xpath("//html/body/div[3]/div/div/form[1]/table/tbody/tr[8]/td[2]/textarea").send_keys("Huawei")
            browser.find_element_by_xpath("//html/body/div[3]/div/div/form[1]/table/tbody/tr[9]/td[2]/textarea").clear()
            browser.find_element_by_xpath("//html/body/div[3]/div/div/form[1]/table/tbody/tr[10]/td[2]/textarea").clear()
            browser.find_element_by_xpath("//html/body/div[3]/div/div/form[1]/table/tbody/tr[10]/td[2]/textarea").send_keys(
                model)

# change h1
            s = fx("/html/body/div[3]/div/div/form[1]/table/tbody/tr[18]/td[2]/textarea").text
            fx("/html/body/div[3]/div/div/form[1]/table/tbody/tr[18]/td[2]/textarea").clear()
            line = line =  s[:s.find("HTC")] + model
            fx("/html/body/div[3]/div/div/form[1]/table/tbody/tr[18]/td[2]/textarea").send_keys(line)

            fx("/html/body/div[3]/div/div/form[1]/table/tbody/tr[19]/td[2]/textarea").clear()
            fx('/html/body/div[3]/div/div/form[1]/table/tbody/tr[19]/td[2]/textarea').send_keys(line)

            fx("/html/body/div[3]/div/div/form[1]/table/tbody/tr[21]/td[2]/textarea").clear()
            fx("/html/body/div[3]/div/div/form[1]/table/tbody/tr[21]/td[2]/textarea").send_keys(line)
# change description
            fx("/html/body/div[3]/div/div/form[1]/table/tbody/tr[20]/td[2]/textarea").clear()
            fx("/html/body/div[3]/div/div/form[1]/table/tbody/tr[20]/td[2]/textarea").send_keys("Евросервис - " + line + " - сервисный центр в Екатеринбурге, ремонт от 490 руб, гарантия до 12 месяцев, срок ремонта - 20 минут")

            fx('/*[@id="submit"]').click()
            print(link, "ok")

finally:

    browser.quit()
