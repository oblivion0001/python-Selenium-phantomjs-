# coding:utf-8
from selenium import webdriver
import time

# 新建session

host = "http://kmzs.qian-baobei.com"
driver = webdriver.PhantomJS(executable_path = "C:/Users/newone/Desktop/test/phantomjs/bin/phantomjs.exe")
list_href = {}


def get_cookies():
    # u'启动selenium获取浏览器cookies'
    driver.get(host + "/User/login.aspx")
    driver.find_element_by_xpath('//*[@id="TxtAlipayUser"]').send_keys("罗俊")
    driver.find_element_by_xpath('//*[@id="TxtAlipayPass"]').send_keys("123456")
    driver.find_element_by_xpath('//*[@id="IbtnAlipayLogin"]').click()
    time.sleep(3)


def get_all_data():
    driver.get(host + "/User/Loan/MyLoanClient.aspx")
    num = driver.find_element_by_xpath('//table/tbody/tr[23]/td/span[3]').text
    _list = range(1, int(num))
    for _ in _list:
        name = driver.find_elements_by_xpath('//table/tbody/tr/td[2]')
        sex = driver.find_elements_by_xpath('//*[@id="EgvUser"]/tbody/tr/td[3]')
        local = driver.find_elements_by_xpath('//*[@id="EgvUser"]/tbody/tr/td[7]')
        money = driver.find_elements_by_xpath('//*[@id="EgvUser"]/tbody/tr/td[9]')
        state = driver.find_elements_by_xpath('//*[@id="EgvUser"]/tbody/tr/td[10]')
        review = driver.find_elements_by_xpath('//*[@id="EgvUser"]/tbody/tr/td[13]')
        for j in range(0, name.__len__()):
            print(name[j].text + "-" + sex[j].text + "-" + local[j].text + "-" +
                  money[j].text + "-" + state[j].text + "-" + review[j].text)
        driver.find_element_by_xpath('//table/tbody/tr[23]/td/a[3]').click()


def get_my_data():
    driver.get(host + "/User/Loan/MyLoanClient.aspx")
    num = driver.find_element_by_xpath('//table/tbody/tr[23]/td/span[3]').text
    _list = range(1, int(num))
    myFile = open('my.txt', 'w')
    print("---start---")
    for _ in _list:
        # //*table/tbody/tr/td[2]
        name = driver.find_elements_by_xpath('//table/tbody/tr/td[2]')
        sex = driver.find_elements_by_xpath('//table/tbody/tr/td[3]')
        age = driver.find_elements_by_xpath('//table/tbody/tr/td[4]')
        phone = driver.find_elements_by_xpath('//table/tbody/tr/td[5]')
        point = driver.find_elements_by_xpath('//table/tbody/tr/td[6]')
        local = driver.find_elements_by_xpath('//table/tbody/tr/td[7]')
        s_time = driver.find_elements_by_xpath('//table/tbody/tr/td[8]')
        money = driver.find_elements_by_xpath('//table/tbody/tr/td[9]')
        state = driver.find_elements_by_xpath('//table/tbody/tr/td[12]')
        review = driver.find_elements_by_xpath('//table/tbody/tr/td[13]')
        r_time = driver.find_elements_by_xpath('//table/tbody/tr/td[14]')
        tip = driver.find_elements_by_xpath('//table/tbody/tr/td[15]')
        href = driver.find_elements_by_xpath('//table/tbody/tr/td[16]/a[1]')
        for j in range(0, name.__len__() - 1):
            txt = "姓名：" + name[j].text + \
                  "-性别：" + sex[j].text + \
                  "-年龄：" + age[j].text + \
                  "-电话：" + phone[j].text + \
                  "-芝麻分：" + point[j].text + \
                  "-地址：" + local[j].text + \
                  "-申请：" + s_time[j].text + \
                  "-借款：" + money[j].text + \
                  "-状态：" + state[j].text + \
                  "-审核人：" + review[j].text + \
                  "-审核：" + r_time[j].text + \
                  "-备注：" + tip[j].text + "\n"
            str_href = href[j].get_attribute("href")
            list_href.update({"0" + str(j) + name[j].text: str_href})
            myFile.write(txt)
            print(txt)
        driver.find_element_by_xpath('//table/tbody/tr[23]/td/a[3]').click()
    myFile.close()


def get_one_data():
    for i in list_href:
        print("one_start")
        one_file = open(i + '.txt', 'w')
        driver.get(list_href.get(i))
        url_i = driver.find_element_by_xpath('//*[@id="linkViewBQS"]').get_attribute("href")
        driver.get(url_i)
        try:
            phone_list = driver.find_elements_by_xpath('//*[@id="main"]//*/table/tbody/tr[1]/td[2]/p/span[1]')
            phone = phone_list[1].text
        except Exception:
            phone = ""
        try:
            msg_list = driver.find_elements_by_xpath('//*[@id="main"]//*/table/tbody/tr[2]/td[2]/p/span[1]')
            msg = msg_list[1].text
        except Exception:
            msg = ""

        call_one_list = driver.find_elements_by_xpath('//*[@id="main"]//*/table/tbody/tr[3]/td/p[1]/span[1]')
        try:
            call_one = call_one_list[2].text
        except Exception:
            call_one = ""

        try:
            call_two = driver.find_element_by_xpath('//*[@id="main"]//*/table/tbody/tr[4]/td/p[1]/span[1]').text
        except Exception:
            call_two = ""

        txt = "电话：" + phone + "\n" + \
              "实名信息：" + msg + "\n" + \
              "紧急联系人:" + call_one + \
              "---：" + call_two + "\n" + \
              "近六个月常用联系人" + "\n"
        one_file.write(txt)
        call_list = driver.find_elements_by_xpath('//*[@id="main"]//div[@class="items detail"]/table/tbody//span')
        count_list = driver.find_elements_by_xpath('//*[@id="main"]//div[@class="items detail"]/table/tbody//td[6]')
        for j in range(0, call_list.__len__() - 1):
            txt_j = "--------" + call_list[j].text + "呼叫次数：" + count_list[j].text + "\n"
            one_file.write(txt_j)
        one_file.close()
        print("one_end")


if __name__ == '__main__':
    get_cookies()
    get_my_data()
    get_one_data()
    print("---end---")
    driver.quit()
