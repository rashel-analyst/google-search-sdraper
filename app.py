import streamlit as st
from googlesearch import search

# Function to perform Google search
def get_google_results(query, num_results=30):
    results = list(search(query, num_results=num_results))
    
    # Split results into pages (10 per page)
    pages = [results[i:i + 10] for i in range(0, len(results), 10)]
    return pages

# Streamlit UI
st.title("Google Search Scraper")

# Input field
query = st.text_input("Enter search query:")

# Submit button
if st.button("Search"):
    if query:
        st.write(f"**Searching for:** {query}")
        results = get_google_results(query)

        # Display results in a table
        for i, links in enumerate(results, start=1):
            st.subheader(f"Page {i} Results")
            st.table({"Links": links})
    else:
        st.warning("Please enter a search query.")
