import React, { useState, useEffect } from 'react';

function DataScreen() {
  const [timestamp, setTimestamp] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/data') 
      .then(response => response.json())
      .then(data => {
        if (data && data.timestamp) {
          setTimestamp(data.timestamp);
        }
      })
      .catch(error => {
        console.error('Error fetching timestamp:', error);
      });
  }, []);

  const formatDate = (timestamp) => {
    const date = new Date(timestamp * 1000);
    return date.toLocaleString('en-US');
  }

  return (
    <div>
      <h2>Data Screen</h2>
      <p>Timestamp: {timestamp ? formatDate(timestamp) : 'Loading...'}</p>
    </div>
  );
}

export default DataScreen;
