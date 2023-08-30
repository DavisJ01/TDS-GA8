import streamlit as st

def find_largest_number(a, b, c):
    return max(a, b, c)

def main():
    st.title("Find the Largest Number")
    
    st.write("Enter three numbers:")
    a = st.number_input("Number 1:", step=1)
    b = st.number_input("Number 2:", step=1)
    c = st.number_input("Number 3:", step=1)
    
    if st.button("Find Largest"):
        largest_number = find_largest_number(a, b, c)
        st.write(f"The largest number is: {largest_number}")

if __name__ == "__main__":
    main()
