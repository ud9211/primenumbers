# primenumbers

This project extracts specific data from the HPRERA Public Dashboard using Selenium and pandas.

## Features

- Extracts full table data for specified entries
- Cleans and organizes data into a pandas DataFrame
- Allows user to set the range of data to be extracted

## Requirements

- Python 3.9+
- Google Chrome browser
- Chromedriver compatible with your Chrome version

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/ud9211/primenumbers.git
    cd hprera-data-extractor
    ```

2. **Set up a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Download and set up Chromedriver:**

    - Download the Chromedriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) that matches your Chrome browser version.
    - Place the `chromedriver` executable in the project directory or in a directory that is included in your system's `PATH`.

## Usage

1. **Set the range of data to be extracted:**

    Edit the `n` variable in the `test.py` script to the desired range of data entries you want to extract:

    ```python
    n = 6  # Replace this with the desired range
    ```

2. **Run the script:**

    ```sh
    python main.py
    ```

3. **View the extracted data:**

    The extracted data will be printed to the console and can be further processed or saved as needed.

## Example

Here is an example of the output DataFrame:

```plaintext
                                  Name          GSTIN No.     PAN No.                                  Permanent Address
0                     MANAVINDER SINGH             -NA-  ACLPS2284H  Villette Kothi, Khalini, Shimla, Khalini, Shimla
1                     MANAVINDER SINGH             -NA-  ACLPS2284H  Villette Kothi, Khalini, Shimla, Khalini, Shimla
2                     MANAVINDER SINGH             -NA-  ACLPS2284H  Villette Kothi, Khalini, Shimla, Khalini, Shimla
3              UMA BAGOLIA AND D KONDA  GSTN01234567891  AFDPB7079J  C/o Shiv Kumar Bagolia, House No. 1155, Sector
4                      MS URBAN GREENS  00AAAAA0000AAAA  AAGFU9110M  C/o Solutions, Near Grand Plaza Shopping Complex
5  M/S. JANTA LAND PROMOTERS PVT. LTD.  GSTIN0123456789  AABCJ3450D  SCO39-42,SECTOR -82, SAS NAGAR MOHALI, Mohali
