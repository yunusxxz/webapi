from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import  Column, String, Integer, Float, ForeignKey, DateTime
from datetime import datetime

Base = declarative_base()


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)
    products = relationship('Product', back_populates='category')


class Brand(Base):
    __tablename__ = "brands"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)
    products = relationship('Product', back_populates='brand')


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(160), nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float)
    discountPercentage = Column(Float, nullable=False, default=0)
    stock = Column(Integer, nullable=False, default=0)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='products')
    brand_id = Column(Integer, ForeignKey('brands.id'))
    brand = relationship('Brand', back_populates='products')
    tags = relationship('Tag', back_populates='product')


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship('Product', back_populates='tags')



class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, autoincrement=True, primary_key=True)
    comment = Column(String(25), nullable=False)
    rating = Column(Integer, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    reviewerName = Column(String, nullable=False)
    reviewerEmail = Column(String, nullable=False)
    name = Column(String(25), nullable=False, unique=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship('Product', back_populates='reviews')
