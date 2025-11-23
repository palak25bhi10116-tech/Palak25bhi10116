# 🏦 Project title: INR Currency Converter

## 1. Problem Statement

In today's globalized economy, accurate and real-time (or near-real-time) currency conversion is a necessity for many users. The Indian Rupee (INR) is a critical currency for trade, tourism, and remittances. Manual conversion is inefficient, error-prone, and often relies on outdated, static rates.
The core problem is the lack of a **simple, reliable, and accessible tool** that allows users to quickly calculate the equivalent value of a given INR amount into major international currencies (USD, EUR, GBP, JPY, etc.) directly on their local machine.

## 2. Scope of the Project

The scope of this project is to implement a console-based application using Python that meets the following criteria:

* **Focus Currency:** Conversion must be performed *from* the Indian Rupee (INR) as the base currency.
* **Rate Source:** Utilizes a predefined, fixed dictionary of current exchange rates as a reliable, non-API-dependent **Data Module** for simplicity. (Future scope involves API integration).
* **Output:** Provides the final converted amount formatted correctly to two decimal places.
* **Core Feature:** Implements a clear, dedicated **Core Conversion Logic Module**.

**Out of Scope:**
* Live API integration (using a fixed dictionary for rates).
* Graphical User Interface (GUI).
* Historical data analysis or prediction features.

## 3. Target Users 

The target users for this application are primarily those who require quick, transactional conversion checks:

1.  **Students/Academics:** Need to convert costs for foreign courses, books, or online services.
2.  **Small Business Owners:** Requiring fast conversion for pricing local goods for international sale.
3.  **Casual Travelers:** Need to budget and estimate foreign currency needs for a trip.
4.  **Remittance Senders:** Checking the equivalent value of INR before sending money abroad.

## 4. High-Level Features 

The application provides three primary high-level features, corresponding to the required functional modules

1.  **Rate Management:** The application defines and manages the list of supported currency codes and their corresponding exchange rates through a dedicated **Data Module** (`get_exchange_rates_data`).
2.  **Validated Input:** The system accepts and validates user input for both the amount (must be a positive number) and the target currency code (must be supported) within the **Main/Interface Module** (`run_converter_interface`).

3.  **Accurate Conversion:** The dedicated **Core Logic Module** (`convert_currency`) performs the exchange rate multiplication accurately and returns the converted amount.
