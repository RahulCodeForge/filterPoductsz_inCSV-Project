import csv

def filter_products(input_file, output_file, min_price, max_price, category_filter):
    # Open the input CSV file for reading
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        
        # Filtered products will be stored in this list
        filtered_products = []
        
        # Iterate through each row in the input CSV
        for row in reader:
            # Convert price to a float for comparison
            price = float(row['price'])
            category = row['category']
            
            # Check if the product matches the specified criteria
            if min_price <= price <= max_price and category == category_filter:
                filtered_products.append(row)
    
    # Write the filtered products to the output CSV file
    with open(output_file, mode='w+', newline='') as outfile:
        # Use the same fieldnames as the input CSV
        fieldnames = ['product_id', 'name', 'category', 'price']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        # Write the header and filtered rows
        writer.writeheader()
        writer.writerows(filtered_products)

    print(f"Filtered products saved to {output_file}")

# Example usage
input_file = 'products.csv'        # Input CSV file with product data
output_file = 'filtered_products.csv'  # Output CSV file for filtered results
min_price = 150                     # Minimum price for filtering
max_price = 200000               # Maximum price for filtering
category_filter = 'Electronics'    #  category wise filtering

# Run the filter function
filter_products(input_file, output_file, min_price, max_price, category_filter)
