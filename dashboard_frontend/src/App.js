import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer, ReferenceLine } from 'recharts';

function App() {
  const [health, setHealth] = useState(null);
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  useEffect(() => {
    fetch('/api/health')
      .then(res => res.json())
      .then(data => setHealth(data));

    fetch('/api/prices')
      .then(res => res.json())
      .then(data => setPrices(data));

    fetch('/api/events')
      .then(res => res.json())
      .then(data => setEvents(data));
  }, []);

  const filteredPrices = prices.filter(p => {
    if (!startDate && !endDate) return true;
    const d = new Date(p.date);
    return (!startDate || d >= new Date(startDate)) && (!endDate || d <= new Date(endDate));
  });
  

  return (
    <div>
      <h1>Oil Price Dashboard</h1>
      <p>Backend status: {health ? health.message : 'Checking...'}</p>
      <h2>Brent Oil Prices</h2>
      <label>
        Start Date:
        <input type="date" value={startDate} onChange={e => setStartDate(e.target.value)} />
      </label>
      <label>
        End Date:
        <input type="date" value={endDate} onChange={e => setEndDate(e.target.value)} />
      </label>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={filteredPrices}>
          <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="price" stroke="#8884d8" />
          {events.map(event => (
            <ReferenceLine
              key={event.Start_Date}
              x={event.Start_Date ? event.Start_Date.split('T')[0] : event.start_date}
              stroke="red"
              label={event.Description || event.description}
            />
          ))}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default App;