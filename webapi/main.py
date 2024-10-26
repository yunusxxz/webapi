import streamlit as st
from config import engine, get_session
from models import Base, Brand, Category, Product, Tag, Review
from repository import GenericRepository

Base.metadata.create_all(bind=engine)
session = get_session()
brand_repo = GenericRepository(Brand, session)
category_repo = GenericRepository(Category, session)
product_repo = GenericRepository(Product, session)
tag_repo = GenericRepository(Tag, session)
review_repo = GenericRepository(Review, session)


def main():
    session = get_session()
    brand_repo = GenericRepository(Brand, session)
    category_repo = GenericRepository(Category, session)
    product_repo = GenericRepository(Product, session)
    tag_repo = GenericRepository(Tag, session)
    review_repo = GenericRepository(Review, session)
    st.title("Product Management Dashboard")
    st.divider()
    option = st.sidebar.selectbox("Dashboard", ("Products0", "Brand", "Categories"))


def brand_section():
    st.title('Brands:')
    st.write("Hello from Brand Section!")


def category_section():
    st.title('Categories:')
    st.write("Hello from Categories Section!")


def product_section():
    st.title('Product:')
    st.write("Hello from Product Section!")


def tag_section():
    st.title('Tag:')
    st.write("Hello from Tag Section!")


def review_section():
    st.title('Review:')
    st.write("Hello from Review Section!")


st.sidebar.title("Menu")
if st.sidebar.button("Brands"):
    brand_section()

if st.sidebar.button("Categories"):
    category_section()

if st.sidebar.button("Rewievs"):
    review_section()

if st.sidebar.button("Tags"):
    tag_section()

if st.sidebar.button("Products"):
    product_section()



if __name__ == "__main__":
    main()
