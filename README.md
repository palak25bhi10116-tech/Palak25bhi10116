#MODULAR INR CURRENCY CONVERTER

##Project Overview

This project is a simple, console-based Currency Converter implemented in Python. Its primary function is to convert a specified amount of Indian Rupees (INR) to major international currencies such as the US Dollar (USD), Euro (EUR), and Japanese Yen (JPY). The application is built with a strict adherence to modular programming principles, clearly separating its core functionality into three distinct components: a Data Management Module, a Core Logic Module, and a User Interface Module. The main objective of this project is to demonstrate proficiency in fundamental programming concepts, including the use of data structures (dictionaries), input/output operations, effective conditional logic, and robust error handling practices.

##Project Features

The converter includes several key features designed for reliability and ease of use:

INR Base Conversion: The system is dedicated to converting amounts specifically from the Indian Rupee (INR) to any other supported currency.

Modular Design: The entire application is structured with clear separation of concerns across three modules: Data Management (for rates), Core Logic (for calculation), and User Interface (for I/O).

Supported Currencies: Currently, the system supports conversions for USD, EUR, GBP, JPY, and AED, and its structure allows for easy expansion to include more currencies.

Input Validation: The application automatically detects and rejects invalid inputs, such as non-numeric amounts or unsupported currency codes, providing the user with clear and constructive error messages.

Formatted Output: The final converted value is presented along with the current exchange rate used, and the result is meticulously formatted to two decimal places for accurate financial clarity.

##Technologies and Tools Used

Primary Language: Python 3.x. This was chosen for its excellent readability, clean syntax, and strong features supporting structured and modular programming practices.

Data Structure: Python Dictionary. This is used for the efficient storage and instantaneous lookup of all currency exchange rates.

Version Control: Git and GitHub. These tools were utilized for tracking project history, managing changes across development iterations, and meeting the required submission guidelines for version control.

Environment: Command Line/Terminal. The application operates as a console-based script, which ensures maximum simplicity and low operational overhead.

##Steps to Install and Run the Project

This project uses standard Python features and does not require the installation of any external libraries, making it a standalone script.

Prerequisites

You must have Python 3.x installed on your operating system (Windows, macOS, or Linux).

##Installation and Execution Instructions

Clone the Repository:
Open your terminal and use the following command to download the project files:

git clone - https://github.com/palak25bhi10116-tech/Palak25bhi10116
cd modular-inr-converter # Replace with your actual repository name


##Run the Script:
Execute the main application file from your terminal using the Python interpreter:

python converter.py


Follow Prompts:
The running application will immediately prompt you for input. You will be asked to:

Enter the amount in INR (for example, typing '5000').

Enter the target currency code (for example, typing 'USD' or 'JPY').

##Instructions for Testing

To confirm the converter's reliability and robustness, you should execute the following test scenarios:

**Successful Conversion**: Input 100 INR and the target currency USD. The expected outcome is for the application to display the correct calculated USD amount (e.g., 1.20 USD).

**Self-Conversion Test**: Input 500 INR and the target currency INR. The expected outcome is the display of the same amount, 500.00 INR, confirming the calculation logic is sound.

**Invalid Amount (Text Input)**: Input text, like 'hello', for the amount, and USD for the currency. The expected outcome is a specific error message stating: "Invalid input. Please enter a valid number."

**Invalid Amount (Negative Value)**: Input a negative number, like -100, for the amount, and USD for the currency. The expected outcome is a specific error message stating: "Amount must be a positive number."

A folder named /screenshots is included in the repository and contains images of the application running successfully in the terminal for visual proof.
