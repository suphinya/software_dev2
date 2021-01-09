#ref : https://medium.com/botnoi-classroom/web-scraping-%E0%B8%89%E0%B8%9A%E0%B8%B1%E0%B8%9A%E0%B8%84%E0%B8%99%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B8%94%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%99%E0%B8%B5%E0%B9%89%E0%B9%80%E0%B8%A5%E0%B8%A2%E0%B8%81%E0%B9%87%E0%B8%AA%E0%B8%B2%E0%B8%A1%E0%B8%B2%E0%B8%A3%E0%B8%96%E0%B8%97%E0%B8%B3%E0%B9%84%E0%B8%94%E0%B9%89-by-botnoi-student-ba7febad3527
# : https://medium.com/equinox-blog/%E0%B8%A5%E0%B8%AD%E0%B8%87%E0%B8%97%E0%B8%B3-web-scraping-%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-beautifulsoup-%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B9%80%E0%B8%96%E0%B8%AD%E0%B8%B0-b58dc0e1775a
# : https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import bs4
import requests

# ---------- ดึงข้อมูลจากเว็บที่ต้องการ(ใส่web) ----------
website = requests.get("https://www.bbc.com/news")
print(website)             # ถ้าขึ้นต้นเลข 2 แสดงว่าดึงข้อมูลสำเร็จ

# ---------- check ข้อมูลในหน้าเว็บทั้งหมด ----------
#print(website.text)        

# ---------- แปลงเป็น type bs4.BeautifulSoup เพื่อใช้คำสั่งของ BeautifulSoup ----------
soup = bs4.BeautifulSoup(website.text , 'html.parser')
#print(soup)                # ดูข้อมูลที่ได้
#print(type(soup))          # check type
#print(soup.prettify())     # ทำให้ Source code ที่ได้มาถูกทำให้อยู่ในแบบที่ดูง่ายขึ้น(คล้ายF12)

# ---------- เอาข้อมูลมา (soup.find_all('div', {'class': 'product'})) ----------
trend = soup.find_all('a',{'class' : 'gs-c-promo-heading nw-o-link gs-o-bullet__text gs-o-faux-block-link__overlay-link gel-pica-bold gs-u-pl-@xs'})
for i in range(len(trend)):
    info = trend[i].getText()       # เฉพาะข้อความ
    link = trend[i].get('href')     # เฉพาะ URL
    print(i+1,info + "\nhttps://www.bbc.com" + link)
