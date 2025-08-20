import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer, ReferenceLine } from 'recharts';

function App() {
  const [health, setHealth] = useState(null);
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [volatility, setVolatility] = useState([]);

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

    fetch('/api/volatility')
      .then(res => res.json())
      .then(data => setVolatility(data));
  }, []);

  const filteredPrices = prices.filter(p => {
    if (!startDate && !endDate) return true;
    const d = new Date(p.date);
    return (!startDate || d >= new Date(startDate)) && (!endDate || d <= new Date(endDate));
  });

  // Merge volatility data with filteredPrices by date
  const mergedData = filteredPrices.map(p => {
    const v = volatility.find(v => v.date === p.date);
    return { ...p, volatility: v ? v.volatility : null };
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
        <LineChart data={mergedData}>
          <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="volatility" stroke="#0c0a7eff" />
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