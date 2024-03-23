import React, { useState, useEffect } from 'react';


function Photos() {
  const [images, setImages] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:5000/data');
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }
      const data = await response.json();
      console.log(data);
      setImages(data);
    }
    catch (e) {
      console.error("Error: ", e);
    }
  };

  return (
    <div>
      <h2>Data Screen</h2>
      
      <div className="image-container">
        {images.map((image, index) => (
          <img src={`data:image/jpg;base64,${image}`} className='image'/>
        ))}
      </div>
    </div>
  );
}

export default Photos;