# Product Filter Script

This script filters products from an input CSV file based on specified price and category criteria, then saves the filtered results to an output CSV file.

## Requirements

- Must Installed Python 3
- A CSV file containing product data with the following columns:
  - `product_id`, `name`, `category`, `price`

## Parameters

- **input_file**: The path to the CSV file containing the original product data.
- **output_file**: The path to the CSV file where the filtered data will be saved.
- **min_price** and **max_price**: Define the price range for filtering products.
- **category_filter**: Specifies the product category to filter by.

## Filtering Process

1. The input CSV file (`input_file`) is opened in read mode.
2. Each row is read and checked to see if it meets the criteria:
   - Price is between `min_price` and `max_price`.
   - The product category matches `category_filter`.
3. Rows that meet these criteria are stored in a list called `filtered_products`.

## Output File

- The output CSV file (`output_file`) is opened in write mode.
- The `csv.DictWriter` is used to write the filtered rows into this file with field names (`product_id`, `name`, `category`, `price`).
- A header row is written first, followed by each filtered product.
  
After writing to `output_file`, a message confirms that the filtered products were saved successfully.

## How to Run

### 1. **Download and Extract the ZIP File**
   - Download the ZIP file containing the project code and CSV file.
   - Extract the contents of the ZIP file to a folder on your computer.

### 2. **Install Python (if not already installed)**
   - Ensure **Python 3.x** is installed on your computer. You can download it from [here](https://www.python.org/downloads/).

### 3. **Open a Terminal or Command Prompt**
   - Open the terminal (Linux/Mac) or command prompt (Windows).

### 4. **Navigate to the Extracted Folder**
   - Use the `cd` command to navigate to the folder where you extracted the ZIP file. For example:
     ```bash
     cd path/to/extracted/folder
     ```

### 5. **Check the Folder Contents**
   - Verify that the folder contains both the Python script (e.g., `filter_products.py`) and the `products.csv` file.

### 6. **Run the Program**
   - Once you are in the correct folder, run the Python script with the following command:
     ```bash
     python filter_products.py
     ```


## Instructions to Run the Script

1. **Prepare the CSV File**: 
   - Create a CSV file named `products.csv` (or use another name, but make sure to update `input_file` if you change it).
   - The file should contain columns in this order: `product_id`, `name`, `category`, and `price`.
   - Example content for `products.csv`:
     ```csv
     product_id,name,category,price
     1,Pencil,Stationery,10
     2,Eraser,Stationery,5
     3,Notebook,Stationery,15
     4,Scissors,Office Supplies,12
     ```

2. **Set Up the Code**:
   - Copy the code into a Python file, e.g., `filter_products.py`.

3. **Update Parameters**:
   - Modify the `input_file`, `output_file`, `min_price`, `max_price`, and `category_filter` variables in the code:
     ```python
     input_file = 'products.csv'             # Path to the original CSV file
     output_file = 'filtered_products.csv'   # Path for the output CSV file
     min_price = 5                           # Minimum price for filtering
     max_price = 20                          # Maximum price for filtering
     category_filter = 'Stationery'          # Desired category to filter by
     ```

4. **Check the Output**:
   - After running the script, you should see the following message:
     ```
     Filtered products saved to filtered_products.csv
     ```
   - Open `filtered_products.csv` to view the filtered products.

## Example Output

If your input file contains the sample data above and you filter for `category_filter = 'Stationery'` with `min_price = 5` and `max_price = 20`, `filtered_products.csv` might look like this:

```csv
product_id,name,category,price
1,Pencil,Stationery,10
2,Eraser,Stationery,5
3,Notebook,Stationery,15
