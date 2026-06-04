#coding=utf8
import os,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree


def save_with_selenium(url, save_name="page_selenium.html"):
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
    html = driver.page_source
    driver.quit()
    selector=etree.HTML(html)
    res=selector.xpath('//div[@id="cctable"]//a/text()')
    print(res)
    print(len(res))
    wanted=res[1:len(res)]
    for n in range(0,10):
        print(wanted[5*n],wanted[5*n+1])


"""
    with open(save_name, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ 保存成功：{save_name}")
"""


if __name__=='__main__':
#    url='https://fundf10.eastmoney.com/ccmx_009776.html'
    url=input('please input the url:')
    save_with_selenium(url)
