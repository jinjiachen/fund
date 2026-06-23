#coding=utf8
import os,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree


def save_with_selenium(url, save_name="page_selenium.html",ptf="NO"):
    """Selenium 真实浏览器抓取（支持动态JS）"""
    print(f"[2] 正在用 Selenium 抓取：{url}")
    
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # 后台运行，不弹出浏览器
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(3)
    html = driver.page_source#渲染后的网页源代码
    driver.quit()
    selector=etree.HTML(html)#转换成lxml的对象
    res=selector.xpath('//div[@id="cctable"]//a/text()')
    wanted=res[1:len(res)]#股票名称和代码
    span=selector.xpath('//div[@id="cctable"]//span/text()')#涨跌幅信息
    if ptf=='YES':
        print(res)
        print(span)
        #print(len(res))
    for n in range(0,10):
        print(wanted[5*n],wanted[5*n+1],span[2*n],span[2*n+1])#通过规律观察,输出想要的参数


'''
    with open(save_name, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ 保存成功：{save_name}")
'''


if __name__=='__main__':
    code=input('please input the url:')
    url=f'https://fundf10.eastmoney.com/ccmx_{code}.html'
    save_with_selenium(url)
