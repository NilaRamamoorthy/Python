from sale_ops import sell_product, sales, buyers, products
from report_ops import generate_sales_report
from datetime import datetime

# Sample sales
sell_product("P001", "Alice", 2, datetime.now().strftime("%H:%M"))
sell_product("P002", "Bob", 5, datetime.now().strftime("%H:%M"))
sell_product("P003", "Charlie", 6, datetime.now().strftime("%H:%M"))

print("\nUnique Buyers:", buyers)
generate_sales_report(sales, products)
