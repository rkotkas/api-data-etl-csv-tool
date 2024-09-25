# ETL Tool for Fetching and Transforming Data

This project is a Python-based ETL (Extract, Transform, Load) tool that demonstrates the ability to perform data extraction from an API, transform the data into a structured format, and save it for further use. It uses the `requests` library for fetching data, `pandas` for data transformation, and `re` for text processing. The script is equipped with unit tests to validate the functionality of each component, showcasing a test-driven development approach.

## Features

- **Data Extraction**: Fetches data from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/posts), a free online REST API for testing and prototyping.
- **Data Transformation**:
  - Converts JSON data into a structured Pandas DataFrame.
  - Adds a new column `body_length` that calculates the number of characters in the `body` field of each record, excluding special characters and spaces.
- **Data Loading**: Saves the transformed DataFrame as a CSV file (`final_data.csv`).
- **Unit Testing**: Contains unit tests to ensure the accuracy of the main functions used in the ETL process.

## Project Structure

```
├── etl_script.py # Main ETL script 
├── README.md # Project documentation 
└── final_data.csv # Output file generated after running the script
```

## Prerequisites

- Python 3.7+
- `requests` library
- `pandas` library

Install dependencies using:

  ```bash
  pip install requests pandas
  ```

## Usage

1. Clone the repository and navigate to the project directory.

2. Run the ETL script using:

    ```bash
    python etl_script.py
    ```

3. The script will perform the following steps:
    - Fetch data from the API.
    - Transform the data into a Pandas DataFrame.
    - Add a `body_length` column containing the character count of the `body` field.
    - Save the DataFrame to `final_data.csv`.

4. The final CSV file will be saved in the project directory.

## Code Overview

### ETL Functions

- `get_data(input_url)`: Fetches JSON data from the given URL and returns it as a Python dictionary.
- `transform_data_into_df(data)`: Converts the fetched data into a Pandas DataFrame.
- `count_chars(text)`: Calculates the number of alphanumeric characters in a given text, excluding special characters and spaces.
- `find_field_from_df(data, field, index)`: Retrieves a specific field value from the DataFrame at the given index.

### Main Function

- `main()`: Coordinates the ETL process by calling the extraction, transformation, and loading functions in sequence.

### Unit Tests

- `test_find_field_from_df()`: Validates that the correct field value is retrieved from the DataFrame.
- `test_count_chars()`: Confirms that the character count function works as expected.
- `test_transform_data_into_df()`: Ensures that the JSON data is correctly transformed into a Pandas DataFrame.

## Output

- The script generates a CSV file (`final_data.csv`) containing the original data along with an additional column `body_length` that contains the length of each post's `body` content.

## Demonstrated Skills

- **API Integration**: Fetching data from an external REST API using Python.
- **Data Transformation**: Using `pandas` for transforming JSON data into a structured format.
- **Text Processing**: Implementing custom functions to clean and analyze text data.
- **Testing**: Writing unit tests to validate individual components of the ETL process.

## Future Enhancements

- Add error handling for network failures or API changes.
- Implement parallel data fetching to handle large datasets efficiently.
- Extend the tool to support different data sources and transformation logic.

## License

This project is open-source and free to use under the MIT license.
