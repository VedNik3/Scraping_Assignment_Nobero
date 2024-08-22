import { useEffect, useState } from 'react';
import './App.css';
import axios from 'axios';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom'; // Import necessary components from react-router-dom
import ProductDetail from './ProductDetail'; // Import the ProductDetail component

function Navbar({ categories, onSelectCategory }) {
  return (
    <nav className="navbar">
      <ul>
        {categories.map((category, index) => (
          <li key={index} onClick={() => onSelectCategory(category)}>
            {category}
          </li>
        ))}
      </ul>
    </nav>
  );
}

function ProductList({ products, onViewDetails }) {
  return (
    <div className="product-list">
      {products.map((product) => (
        <div key={product.id} className="product-item">
          <h2>{product.title}</h2>
          <p>Category: {product.category}</p>
          <div className="sku-container">
            {product.available_skus.map((sku, index) => (
              <div key={index} className="product-sku">
                <img
                  src={`https:${product.image_url}`}  // Correctly format the image URL
                  alt={`Product ${index}`}
                />
              </div>
            ))}
            {/* <a href={product.url} target="_blank" rel="noopener noreferrer">
              View Product
            </a> */}
            <Link to={`/product/${product.id}`}>
              {/* <button> */}
                View Details
              {/* </button> */}
            </Link>
          </div>
        </div>
      ))}
    </div>
  );
}

function App() {
  const [products, setProducts] = useState([]);
  const [categories, setCategories] = useState([]);
  const [filteredProducts, setFilteredProducts] = useState([]);

  const API_URL = 'http://127.0.0.1:8000/api/products/';

  useEffect(() => {
    const getProducts = async () => {
      try {
        const response = await axios.get(API_URL);

        let productData;

        if (response.headers['content-type'].includes('application/json')) {
          productData = response.data;

          if (typeof productData === 'string') {
            productData = JSON.parse(productData);
          }

          if (Array.isArray(productData)) {
            setProducts(productData);
            setFilteredProducts(productData);

            // Extract unique categories from products
            const uniqueCategories = [...new Set(productData.map(product => product.category))];
            setCategories(uniqueCategories);
          } else {
            console.error("Unexpected response format:", productData);
          }
        } else {
          console.error("Unexpected content-type:", response.headers['content-type']);
        }
      } catch (error) {
        console.error("Error fetching products:", error);
      }
    };
    getProducts();
  }, []);

  const handleCategorySelect = (category) => {
    if (category === 'All') {
      setFilteredProducts(products);
    } else {
      const filtered = products.filter(product => product.category === category);
      setFilteredProducts(filtered);
    }
  };

  return (
    <Router>
      <div className="app-container">
        <Navbar categories={['All', ...categories]} onSelectCategory={handleCategorySelect} />
        
        <Routes>
          <Route
            path="/"
            element={<ProductList products={filteredProducts} />}
          />
          <Route
            path="/product/:productId"
            element={<ProductDetail products={products} />}
          />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
