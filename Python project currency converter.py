import tkinter as tk
from tkinter import ttk, messagebox

# Dictionary of currency codes and their values in INR (Indian Rupees)
exchange_rates_to_inr = {
    "AFN": 1.16, "AMD": 0.21, "AZN": 49.00, "BDT": 0.76, "KHR": 0.021, "CNY": 11.50,
    "GEL": 31.14, "HKD": 10.63, "IDR": 0.0051, "JPY": 0.54, "KZT": 0.19, "LAK": 0.0039,
    "MYR": 17.43, "KRW": 0.061, "LKR": 0.28, "MVR": 5.39, "PKR": 0.30, "PHP": 1.45,
    "THB": 2.25, "TWD": 2.56, "VND": 0.0033, "BHD": 220.96, "AED": 22.68, "SAR": 22.21,
    "OMR": 216.38, "ILS": 22.15, "IND": 1.00, "IQD": 0.064, "IRR": 0.0020, "JOD": 117.52,
    "KWD": 270.41, "LBP": 0.00093, "QAR": 22.88, "LYD": 17.15, "BAM": 45.61, "EUR": 89.04,
    "BGN": 45.57, "CZK": 3.53, "HRK": 11.83, "DKK": 11.94, "HUF": 0.23, "ISK": 0.59,
    "MDL": 4.66, "MKD": 1.45, "NOK": 7.63, "PLN": 20.61, "RON": 17.89, "RSD": 0.76,
    "RUB": 0.90, "SEK": 7.68, "CHF": 91.17, "TRY": 2.56, "UAH": 2.12, "GBP": 103.60,
    "USD": 83.30, "CAD": 60.91, "AWG": 46.28, "BBD": 41.49, "BMD": 83.30, "BSD": 83.73,
    "DOP": 1.42, "JMD": 0.54, "MXN": 4.91, "ZAR": 4.36, "EGP": 1.73, "GHS": 6.21,
    "GMD": 1.23, "KES": 0.64, "MAD": 8.26, "MUR": 1.80, "NAD": 4.35, "NGN": 0.066,
    "SCR": 6.05, "TND": 26.40, "UGX": 0.022, "XAF": 0.14, "AUD": 54.19, "FJD": 36.32,
    "NZD": 49.45, "XPF": 0.74
}

# List of countries with their currency codes
countries = {
    "Afghanistan": "AFN", "Armenia": "AMD", "Azerbaijan": "AZN", "Bangladesh": "BDT",
    "Cambodia": "KHR", "China": "CNY", "Georgia": "GEL", "Hong Kong": "HKD",
    "Indonesia": "IDR", "Japan": "JPY", "Kazakhstan": "KZT", "Laos": "LAK",
    "Malaysia": "MYR", "South Korea": "KRW", "Sri Lanka": "LKR", "Maldives": "MVR",
    "Pakistan": "PKR", "Philippines": "PHP", "Thailand": "THB", "Taiwan": "TWD",
    "Vietnam": "VND", "Bahrain": "BHD", "United Arab Emirates": "AED", "Saudi Arabia": "SAR",
    "Oman": "OMR", "Israel": "ILS", "India": "IND", "Iraq": "IQD", "Iran": "IRR",
    "Jordan": "JOD", "Kuwait": "KWD", "Lebanon": "LBP", "Qatar": "QAR", "Libya": "LYD",
    "Bosnia": "BAM", "European Union": "EUR", "Bulgaria": "BGN", "Czech Republic": "CZK",
    "Croatia": "HRK", "Denmark": "DKK", "Hungary": "HUF", "Iceland": "ISK", "Moldova": "MDL",
    "Macedonia": "MKD", "Norway": "NOK", "Poland": "PLN", "Romania": "RON", "Serbia": "RSD",
    "Russia": "RUB", "Sweden": "SEK", "Switzerland": "CHF", "Turkey": "TRY", "Ukraine": "UAH",
    "United Kingdom": "GBP", "United States": "USD", "Canada": "CAD", "Aruba": "AWG",
    "Barbados": "BBD", "Bermuda": "BMD", "Bahamas": "BSD", "Dominica": "DOP",
    "Jamaica": "JMD", "Mexico": "MXN", "South Africa": "ZAR", "Egypt": "EGP", "Ghana": "GHS",
    "Gambia": "GMD", "Kenya": "KES", "Morocco": "MAD", "Mauritius": "MUR", "Namibia": "NAD",
    "Nigeria": "NGN", "Seychelles": "SCR", "Tunisia": "TND", "Uganda": "UGX",
    "Central Africa": "XAF", "Australia": "AUD", "Fiji": "FJD", "New Zealand": "NZD",
    "CPF": "XPF"
}

# Function to convert between two currencies
def convert_currency(amount, from_currency, to_currency):
    if from_currency in exchange_rates_to_inr:
        amount_in_inr = amount * exchange_rates_to_inr[from_currency]
    else:
        return None

    if to_currency in exchange_rates_to_inr:
        converted_amount = amount_in_inr / exchange_rates_to_inr[to_currency]
        return converted_amount
    else:
        return None

# Function to perform currency conversion when the button is clicked
def perform_conversion():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combobox.get().upper()  # Normalize to uppercase
        to_currency = to_currency_combobox.get().upper()      # Normalize to uppercase

        if from_currency and to_currency and amount > 0:
            converted_amount = convert_currency(amount, from_currency, to_currency)
            if converted_amount is not None:
                result_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.4f} {to_currency}")
            else:
                messagebox.showerror("Error", "Currency conversion failed. Please check your input.")
        else:
            messagebox.showwarning("Warning", "Please enter a valid amount and select currencies.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric amount.")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x400")
root.configure(bg="#e9ecef")

# Title Label
title_label = tk.Label(root, text="Currency Converter", font=("Helvetica", 18, "bold"), bg="#e9ecef", fg="#007BFF")
title_label.pack(pady=20)

# Create input field for the amount
amount_label = tk.Label(root, text="Amount to Convert:", bg="#e9ecef", font=("Helvetica", 12))
amount_label.pack(pady=5)

amount_entry = tk.Entry(root, font=("Helvetica", 12), bd=2, relief=tk.SUNKEN)
amount_entry.pack(pady=5, padx=20, fill=tk.X)

# Create dropdown for 'From' currency
from_currency_label = tk.Label(root, text="From Currency:", bg="#e9ecef", font=("Helvetica", 12))
from_currency_label.pack(pady=5)

from_currency_combobox = ttk.Combobox(root, values=list(countries.values()), font=("Helvetica", 12))
from_currency_combobox.pack(pady=5, padx=20, fill=tk.X)

# Create dropdown for 'To' currency
to_currency_label = tk.Label(root, text="To Currency:", bg="#e9ecef", font=("Helvetica", 12))
to_currency_label.pack(pady=5)

to_currency_combobox = ttk.Combobox(root, values=list(countries.values()), font=("Helvetica", 12))
to_currency_combobox.pack(pady=5, padx=20, fill=tk.X)

# Create button to perform conversion
convert_button = tk.Button(root, text="Convert", command=perform_conversion, bg="#007BFF", fg="white", font=("Helvetica", 12))
convert_button.pack(pady=20)

# Label to display the result
result_label = tk.Label(root, text="", bg="#e9ecef", font=("Helvetica", 12))
result_label.pack(pady=5)

# Run the application
root.mainloop()
