import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer } from 'recharts';

function App() {
  const [health, setHealth] = useState(null);
  const [prices, setPrices] = useState([]);

  useEffect(() => {
    fetch('/api/health')
      .then(res => res.json())
      .then(data => setHealth(data));

    fetch('/api/prices')
      .then(res => res.json())
      .then(data => setPrices(data));
  }, []);

  return (
    <div>
      <h1>Oil Price Dashboard</h1>
      <p>Backend status: {health ? health.message : 'Checking...'}</p>
      <h2>Brent Oil Prices</h2>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={prices}>
          <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="price" stroke="#8884d8" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default App;