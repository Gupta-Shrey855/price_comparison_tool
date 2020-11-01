from tkinter import *
window=Tk()
window.geometry("1000x1000")
no = 1

def Show(s):
    global no
    t.insert(END,s)
    no += 1

def Shown(s,v):
    global no
    t.insert(END,s)
    t.insert(END,v)
    no += 2

from bs4 import BeautifulSoup
import requests
import time
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

flipkart=''
ebay=''
croma=''
amazon=''
olx=''

def Flipkart(name):
    try:
        global flipkart
        name1 = name.replace(" ","+")
        flipkart=f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
        res = requests.get(f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',headers=headers)


        Show("\nSearching in flipkart....\n")
        soup = BeautifulSoup(res.text,'html.parser')
        flipkart_name = soup.select('._3wU53n')[0].getText().strip()
        flipkart_name = flipkart_name.upper()
        if name.upper() in flipkart_name:
            flipkart_price = soup.select('._2rQ-NK')[0].getText().strip()
            flipkart_name = soup.select('._3wU53n')[0].getText().strip()
            Show("Flipkart:")
            Show(flipkart_name)
            Show(flipkart_price)
            Show("----------\n")
        else:
            Show("Flipkart:No product found!\n")
            Show("----------\n")
            flipkart_price='0'
        return flipkart_price 
    except:
        Show("Flipkart:No product found!\n")  
        Show("-----------\n")
        flipkart_price= '0'
    return flipkart_price 
def Ebay(name):
    try:
        global ebay
        name1 = name.replace(" ","+")
        ebay=f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={name1}&_sacat=0'
        res = requests.get(f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={name1}&_sacat=0',headers=headers)
        Show("\nSearching in ebay.....\n")
        soup = BeautifulSoup(res.text,'html.parser')
        length = soup.select('.s-item__price')
        ebay_page_length=int(len(length))
        for i in range (0,ebay_page_length):
            info = soup.select('.SECONDARY_INFO')[i].getText().strip()
            info = info.upper()
            if info=='BRAND NEW':
                ebay_name = soup.select('.s-item__title')[i].getText().strip()
                name=name.upper()
                ebay_name=ebay_name.upper()
                if name in ebay_name[:25]:
                    ebay_price = soup.select('.s-item__price')[i].getText().strip()
                    ebay_name = soup.select('.s-item__title')[i].getText().strip()
                    Show("Ebay:")
                    Show(ebay_name)
                    Show(ebay_price.replace("INR","₹"))
                    Show(info)
                    Show("--------\n")
                    ebay_price=ebay_price[0:14]
                    break
                else:
                    i+=1
                    i=int(i)
                    if i==ebay_page_length:
                        Show("Ebay: No product Found!\n")
                        Show("--------\n")
                        ebay_price = '0'
                        break

        return ebay_price
    except:
        Show("Ebay: No product Found!\n")
        Show("-----------\n")
        ebay_price = '0'
    return ebay_price

def Croma(name):
    try:
        global croma
        name1 = name.replace(" ","+")
        croma=f'https://www.croma.com/search/?text={name1}'
        res = requests.get(f'https://www.croma.com/search/?text={name1}',headers=headers)
        Show("\nSearching in croma.....\n")
        soup = BeautifulSoup(res.text,'html.parser')
        croma_name = soup.select('h3')

        croma_page_length = int( len(croma_name))
        for i in range (0,croma_page_length):
            name = name.upper()
            croma_name = soup.select('h3')[i].getText().strip().upper()
            if name in croma_name.upper()[:25]:
                croma_name = soup.select('h3')[i].getText().strip().upper()
                croma_price = soup.select('.pdpPrice')[i].getText().strip()
                Show(croma_name)
                Show(croma_price)
                Show("------------\n")
                break
            else:
                i+=1
                i=int(i)
                if i==croma_page_length:
                    Show("Croma: No product Found!\n")
                    Show("----------\n")
                    croma_price = '0'
                    break
        return croma_price
    except:
        Show("Croma: No product Found!\n")
        Show("---------\n")
        croma_price = '0'
    return croma_price

def Amazon(name):
    try:
        global amazon
        name1 = name.replace(" ","-")
        name2 = name.replace(" ","+")
        amazon=f'https://www.amazon.in/{name1}/s?k={name2}'
        res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}',headers=headers)
        Show("\nSearching in amazon:.....\n")
        soup = BeautifulSoup(res.text,'html.parser')
        amazon_page = soup.select('.a-color-base.a-text-normal')
        amazon_page_length = int(len(amazon_page))
        for i in range(0,amazon_page_length):
            name = name.upper()
            amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
            if name in amazon_name[0:20]:
                amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
                amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()
                Show("Amazon:")
                Show(amazon_name)
                Show("₹"+amazon_price)
                Show("--------\n")
                break
            else:
                i+=1
                i=int(i)
                if i==amazon_page_length:
                    Show("amazon : No product found!\n")
                    Show("---------\n")
                    amazon_price = '0'
                    break
        return amazon_price
    except:
        Show("amazon: No product found!\n")
        Show("--------\n")
        amazon_price = '0'
    return amazon_price


def Olx(name):
    try:
        global olx
        name1 = name.replace(" ","-")
        olx=f'https://www.olx.in/items/q-{name1}?isSearchCall=true'
        res = requests.get(f'https://www.olx.in/items/q-{name1}?isSearchCall=true',headers=headers)
        Show("\nSearching in OLX......\n")
        soup = BeautifulSoup(res.text,'html.parser')
        olx_name = soup.select('._2tW1I')
        olx_page_length = len(olx_name)
        for i in range(0,olx_page_length):
            olx_name = soup.select('._2tW1I')[i].getText().strip()
            name = name.upper()
            olx_name = olx_name.upper()
            if name in olx_name:
                olx_price = soup.select('._89yzn')[i].getText().strip()
                olx_name = soup.select('._2tW1I')[i].getText().strip()
                olx_loc = soup.select('.tjgMj')[i].getText().strip()
                try:
                    label = soup.select('._2Vp0i span')[i].getText().strip()
                except:
                    label = "OLD"
                
                Show("Olx:")
                Show(label)
                Show(olx_name)
                Show(olx_price)
                Show(olx_loc)
                Show("---------\n")
                break
            else:
                i+=1
                i=int(i)
                if i==olx_page_length:
                    Show("Olx: No product Found!\n")
                    Show("-------------\n")
                    olx_price = '0'
                    break
        return olx_price
    except:
        Show("Olx: No product found!\n")
        Show("--------\n")
        olx_price = '0'
    return olx_price

def convert(a):
    b=a.replace(" ",'')
    c=b.replace("INR",'')
    d=c.replace(",",'')
    f=d.replace("₹",'')
    f=f.replace("$",'')
    f=f.replace("to",'')
    g=int(float(f))
    return g

def submit():
    name=product_entry.get()
    ebay_price=Ebay(name)
    flipkart_price=Flipkart(name)
    amazon_price=Amazon(name)
    croma_price=Croma(name)
    olx_price = Olx(name)
    Show("---------------\n")
    if ebay_price== '0':
        Show("\nNo Product found!\n")
        ebay_price = int(ebay_price)
    else:
        Shown("\nEbay price:",ebay_price)
        ebay_price = convert(ebay_price)*73.63
    if flipkart_price=='0':
        Show("\nNo product found!\n")
        flipkart_price = int(ebay_price)
    else:
        Shown("\nFLipkart Price:",flipkart_price)
        flipkart_price=convert(flipkart_price)
    if amazon_price=='0':
        Show("\nNo Product found!\n")
        amazon_price = int(amazon_price)
    else:
        Shown("\namazon price:₹",amazon_price)
        amazon_price=convert(amazon_price)
   
    if croma_price=='0':
        Show("\nNo product found!\n")
        croma_price = int(croma_price)
    else:
        Shown("\nCroma Price:",croma_price)
        croma_price=convert(croma_price)
    if olx_price =='0':
        Show("\nNo product found!")
        olx_price = int(olx_price)
    else:
        Shown("Olx Price:",olx_price)
        olx_price=convert(olx_price)

    time.sleep(2)

    lst = [ebay_price,flipkart_price,amazon_price,croma_price,olx_price]
    lst2=[]
    for j in range(0,len(lst)):
        if lst[j]>0:
            lst2.append(lst[j])
    min_price=min(lst2)

    Show("___________\n")
    Shown("\nMinimun Price: ₹",min_price)
    price = {
        f'{ebay_price}':f"{ebay}",
        f'{amazon_price}':f'{amazon}',
        f'{olx_price}':f"{olx}",
        f'{flipkart_price}':f'{flipkart}',
        f'{croma_price}':f'{croma}'
    }
    for key, value in price.items():
        if float(key)==float(min_price):
            Shown ('\nurl:', price[key])
    Show("\nUrls:\n")
    Show("\n-------------\n")
    Show(ebay)
    Show("\n-------------\n")
    Show(amazon)
    Show("\n-------------\n")
    Show(olx)
    Show("\n-------------\n")
    Show(flipkart) 
    Show("\n-------------\n")
    Show(croma)
    Show("\n--------------\n")

label1=Label(window,text=" PRICE COMPARISION SYSTEM ",font="times 28 bold")
label1.pack(pady=20)

item_listbox=StringVar(window)
input_lable = Label(window,text="ENTER THE PRODUCT YOU WANT TO SEARCH :",font = "Arial 10")
input_lable.pack(pady=5)

product_entry = Entry(window,width=23)
product_entry.pack(pady=5)

b1=Button(window,text="SEARCH",width=12,bg='gray',command=submit)
b1.pack(pady=5)

s=Scrollbar(window)
s.pack(side=BOTTOM,fill=X)
v=Scrollbar(window)
v.pack(side=RIGHT,fill=Y)
t= Text(window,width = 100, height = 100, wrap = NONE,yscrollcommand = v.set,xscrollcommand = s.set)
t.configure(yscrollcommand=v.set)
t.configure(xscrollcommand=s.set)
t.pack()
v.configure(command=t.yview)
s.configure(command=t.xview)

window.mainloop()