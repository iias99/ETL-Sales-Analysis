import pandas as pd
files_names={"sales": "Sales.csv",
             "customers": "Customers.csv",
             "employees" : "Employees.csv" ,
             "products" : "Products.csv" ,
             "egions" : "Regions.csv" ,
             "stores" : "Stores.csv"

}
for name ,file in files_names.items():
    print(f"\n--{name.upper()}  MISSING VALUES --")
    print(f"\n--{name.upper()}  is cleaning --")
    data=pd.read_csv(file)
    for col in data.select_dtypes(include='object').columns :
      mode_value=data[col].mode()[0]
      data[col].fillna(mode_value)
    for col in data.select_dtypes(include=["Int64",'float64']).columns:
       mean_value=data[col].mean() 
       data[col].fillna(mean_value)
print(data.isnull().sum())
clean_name = f"cleaned_{file}"
data.to_csv(clean_name, index=False)
print("-" * 50)

sales_df= pd.read_csv("Sales.csv")
customer_df =pd.read_csv("Customers.csv")
merged_df=pd.merge(sales_df,customer_df , on="customer_id" , how="left")
print (merged_df.head())
unique_customers =merged_df["customer_id"].nunique()
print("num of uniqe customers",unique_customers)
total_sales =merged_df["unit_price"].sum()
print("Total of sales",total_sales)
top_customer =merged_df["customer_name"].value_counts().idxmax()
print(top_customer)
average_price =merged_df["unit_price"].mean()
print(average_price)
sales_by_gendersales_by_gender=merged_df.groupby("gender")["unit_price"].sum()
print(sales_by_gendersales_by_gender)

import  matplotlib.pyplot  as plt 
sales_by_gendersales_by_gender.plot(kind='bar',color=['skyblue', 'salmon'])
plt.title("Sales by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

import pandas as pd
sales_by_product =merged_df.groupby("product_id")["unit_price"].sum()
print(sales_by_product)
sales_by_store =merged_df.groupby("store_id")["unit_price"].sum()
print("Sales by Store:")
print (sales_by_store)
print("-" * 50)
sales_by_date= merged_df.groupby("date")["unit_price"].sum()
print ("Sales by Date:")
print (sales_by_date)
print("-" * 50)
sales_by_product.plot(kind='bar', color='skyblue')
plt.title("Sales by Product")
plt.xlabel("Product ID")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
sales_by_store.plot(kind='bar', color='lightgreen')
plt.title("Sales by stor")
plt.xlabel("stor ID")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
sales_by_date.plot(kind='line', marker='o',color='orange')
plt.title("Sales by Date")
plt.xlabel('date')
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



