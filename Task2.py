import ClointFusion as cf
import webbrowser

from ClointFusion.ClointFusion import message_counter_down_timer

def search_snip(img_path):
    x,y,w,h = cf.mouse_search_snip_return_coordinates_box(img=img_path)
    cf.mouse_click(x=x,y=y)



chromedir = r"C:\Users\BARSHINI AS\AppData\Local\Google\Chrome\Application\Chrome.exe"
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chromedir))
webbrowser.get('chrome').open("https://www.flipkart.com")
#webbrowser.open_new_tab(url="https:/www.flipkart.com")

cf.message_counter_down_timer(strMsg="Waiting for page to load...",start_value=10)
#close_popup = r"C:\Users\BARSHINI AS\Desktop\doubts\close.PNG"
#search_snip(close_popup)
search_bar = r"C:\Users\BARSHINI AS\Desktop\doubts\search.PNG"
search_snip(search_bar)
cf.key_write_enter(strMsg="boAt airdopes 131 bluetooth headset")
cf.search_highlight_tab_enter_open(searchText="Bestseller")
add_to_cart = r"C:\Users\BARSHINI AS\Desktop\doubts\addtocart.PNG"
search_snip(add_to_cart)
search_snip(search_bar)
cf.key_write_enter(strMsg="boAt airdopes 402 bluetooth headset")
cf.search_highlight_tab_enter_open(searchText="Bestseller")
search_snip(add_to_cart)
place_order = r"C:\Users\BARSHINI AS\Desktop\doubts\placeorder.PNG"
search_snip(place_order)
cf.window_close_windows("Chrome")
