from sqlalchemy import create_engine, text
import streamlit as st

# Database connection
DATABASE_URL = "postgresql://user:password@db:5432/mydb"
engine = create_engine(DATABASE_URL)

st.title("User Management")

# Button to load users
if st.button("Load Users"):
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM users"))
        users = [dict(row._mapping) for row in result]  # Use row._mapping for conversion
        st.write(users)
