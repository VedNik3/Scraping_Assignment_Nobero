import React from 'react';
import { useParams } from 'react-router-dom';
import './product.css';

function ProductDetail({ products }) {
  const { productId } = useParams();
  const product = products.find(p => p.id === parseInt(productId));

  if (!product) {
    return <div>Product not found</div>;
  }

  return (
    <div className="product-detail">
      <img
        src={`https:${product.image_url}`}  // Correctly format the image URL
        alt={product.title}
        className="product-image"
      />
      <div className="product-info">
        <h2>{product.title}</h2>
        <div className='parent'>
        <p><span className="subtopic">Category:</span> <span className="detail">{product.category}</span></p>
        <p><span className="subtopic">Last 7 Days Sale:</span> <span className="detail">{product.last_7_day_sale}</span></p>
        <p><span className="subtopic">Fit:</span> <span className="detail">{product.fit}</span></p>
        <p><span className="subtopic">Fabric:</span> <span className="detail">{product.fabric}</span></p>
        <p><span className="subtopic">Neck:</span> <span className="detail">{product.neck}</span></p>
        <p><span className="subtopic">Sleeve:</span> <span className="detail">{product.sleeve}</span></p>
        <p><span className="subtopic">Pattern:</span> <span className="detail">{product.pattern}</span></p>
        <p><span className="subtopic">Length:</span> <span className="detail">{product.length}</span></p>
        <div className="sku-container">
          {product.available_skus.map((sku, index) => (
            <div key={index} className="product-sku">
              <p><span className="subtopic">Color:</span> <span class="detail">{sku.color}</span></p>
              <p><span className="subtopic">Sizes Available:</span> <span className="detail">{sku.size.filter(size => size).join(', ')}</span></p>
            </div>
          ))}
        </div>
        <p><span className="subtopic">Description:</span> <span className="detail">{product.description}</span></p>
        </div>

        <a href={product.url} target="_blank" rel="noopener noreferrer">
          View website
        </a>
      </div>
    </div>
  );
}

export default ProductDetail;
