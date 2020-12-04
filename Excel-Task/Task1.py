import ClointFusion as cf
file_path = "C:/Test/Excel.xlsx"

# To get all the header columns of given excel file
headers = cf.excel_get_all_header_columns(file_path)
print("\nList of header columns:",headers)

# To get row and column count
row, col = cf.excel_get_row_column_count(file_path)
print("\nRows in given excel file:",row)
print("Columns in given excel file:",col)


# To get all sheet names
sheet_names = cf.excel_get_all_sheet_names(file_path)
print("\nList of sheet names:",sheet_names)

# To remove duplicates
cf.excel_remove_duplicates(excel_path=file_path,columnName="ID")
new_row,new_col = cf.excel_get_row_column_count(excel_path=file_path,sheet_name="Sheet1",header=0)
print("\nNumber of rows after removing duplicate ID:",new_row)

# Sort rows by date
cf.excel_sort_columns(excel_path=file_path,firstColumnToBeSorted="OrderDate")

# drop column
cf.excel_drop_columns(excel_path=file_path, sheet_name='Sheet1', header=0, columnsToBeDropped = "Region")

# Create a dictionary with product ID as key and Units as the value
units_dictionary = {}
for i in range(new_row-1):
    id_num = cf.excel_get_single_cell(excel_path=file_path,sheet_name="Sheet1",columnName="ID",cellNumber=i)
    units = cf.excel_get_single_cell(excel_path=file_path,sheet_name="Sheet1",header=0,columnName="Units",cellNumber=i)
    units_dictionary[id_num] = units   

print("Product ID with Units:\n",units_dictionary)    
