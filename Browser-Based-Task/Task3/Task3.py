import ClointFusion as cf


file_path = "C:/Test/Task3Excel.xlsx"
region_header = r"C:\Test\Capture.PNG"
search_filter = r"C:\Test\search_filter.PNG"
total_header = r"C:\Test\total_header.PNG"

# Selects and copies the entire table, opens a new sheet and pastes the copied data.
def copy_paste_table():
    cf.key_press("shift+space")
    cf.key_press("ctrl+shift+down")
    cf.key_press("ctrl+c")
    cf.key_press("alt+shift+f1")
    cf.key_press("ctrl+v")

# Presses the shortcut keys for opening the filter dropdown
def column_filter():
    cf.key_press("ctrl + shift + l")
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Test\dropdown.PNG"))

# Navigates through conditional formatting menu
def conditional_format():
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Test\format.PNG"))
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Test\color_scale.PNG"))
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Test\green-to-red.PNG"))
    cf.key_hit_enter()

def find_snip(img_path):
    cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(img_path))       


# Opens the given excel file
cf.launch_any_exe_bat_application(file_path)

# Shortcut keys to reach the 'Region' header 
cf.key_press("right,right")
cf.key_press("ctrl + down")

# Copy the entire table to a new sheet and filter by 'Region' column (Filter out "Central")
copy_paste_table()
find_snip(region_header)
column_filter()
find_snip(search_filter)
cf.key_write_enter("Central")
cf.key_hit_enter()

# Copy the modified table and paste into another sheet.
# Filter the new table from smallest to largest using the 'Total' column.
find_snip(region_header)
copy_paste_table()
find_snip(total_header)
column_filter()
cf.mouse_click(*cf.mouse_search_snip_return_coordinates_x_y(r"C:\Test\sort.PNG"))

# Conditional format 'Total' column 
find_snip(total_header)
cf.key_press("ctrl + shift + down")
conditional_format()
cf.key_press("alt + h + b + a")
find_snip(r"C:/Test/order_date.PNG")
cf.key_press("ctrl+shift+right")
cf.key_press("ctrl+1")
find_snip("C:/Test/fill_border.PNG")
find_snip("C:/Test/black_bg.PNG")
find_snip(r"C:/Test/font.PNG")
find_snip(r"C:/Test/font_dropdown.PNG")
find_snip(r"C:/Test/yellow_font.PNG")
find_snip(r"C:/Test/OK.PNG")

# Save
cf.key_press("ctrl+s")