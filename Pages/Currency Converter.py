import streamlit as st
from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount

def main():
    st.title("Currency Converter")

    amount = st.number_input("Enter amount:", min_value=0.01, step=0.01)
    from_currency = st.text_input("From currency (3-letter code):")
    to_currency = st.text_input("To currency (3-letter code):")

    if st.button("Convert"):
        if amount and from_currency and to_currency:
            try:
                converted_amount = convert_currency(amount, from_currency, to_currency)
                st.success(f"{amount} {from_currency} = {converted_amount} {to_currency}")
            except:
                st.error("Conversion failed. Please check the currency codes.")

if __name__ == "__main__":
    main()
