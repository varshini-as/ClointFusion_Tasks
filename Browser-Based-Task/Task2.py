import ClointFusion as cf
import webbrowser
from ClointFusion.ClointFusion import message_counter_down_timer


def search_snip(img_path):
    x,y,w,h = cf.mouse_search_snip_return_coordinates_box(img=img_path)
    cf.mouse_click(x=x,y=y)


# Registering Chrome and launching website using Chrome browser
#chromedir = r"C:\Users\your\chrome\path\Chrome.exe"
#webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chromedir))
#webbrowser.open_new_tab(url="https:/www.flipkart.com")

# Launching website using default browser
webbrowser.open("https://www.flipkart.com")

cf.message_counter_down_timer(strMsg="Waiting for page to load...",start_value=10)

# Close popups 
#close_popup = r"C:\Test\close.PNG"
#search_snip(close_popup)

# Locate search bar and type the product name
search_bar = r"C:\Test\search.PNG"
search_snip(search_bar)
cf.key_write_enter(strMsg="boAt airdopes 131 bluetooth headset")
cf.search_highlight_tab_enter_open(searchText="Bestseller")

# Locate add/go-to-cart button and click
add_to_cart = r"C:\Test\addtocart.PNG"
search_snip(add_to_cart)

# Search for the second product, add to cart and proceed to place order
search_snip(search_bar)
cf.key_write_enter(strMsg="boAt airdopes 402 bluetooth headset")
cf.search_highlight_tab_enter_open(searchText="Bestseller")
search_snip(add_to_cart)
place_order = r"C:\Test\placeorder.PNG"
search_snip(place_order)


cf.window_close_windows("Chrome")
