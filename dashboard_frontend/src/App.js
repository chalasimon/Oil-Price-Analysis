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
    <div style={{ background: '#f7f9fa', minHeight: '100vh', padding: '32px' }}>
      <div style={{ maxWidth: 800, margin: '0 auto', background: '#fff', borderRadius: 12, boxShadow: '0 2px 8px rgba(0,0,0,0.07)', padding: '32px' }}>
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
            {events.map((event, idx) => {
              // Generate a color for each event
              const colors = [
                '#d32f2f', '#1976d2', '#388e3c', '#fbc02d', '#7b1fa2', '#0288d1', '#c2185b', '#ffa000', '#689f38', '#303f9f'
              ];
              const color = colors[idx % colors.length];
              return (
                <ReferenceLine
                  key={event.Start_Date || event.start_date}
                  x={event.Start_Date ? event.Start_Date.split('T')[0] : event.start_date}
                  stroke={color}
                  label={null}
                />
              );
            })}
          </LineChart>
        </ResponsiveContainer>
        {/* Event legend below chart */}
        <div style={{ marginTop: 24 }}>
          <h3 style={{ fontSize: 16, color: '#0c0a7e', marginBottom: 8 }}>Event Legend</h3>
          <ul style={{ listStyle: 'none', padding: 0 }}>
            {events.map((event, idx) => {
              const colors = [
                '#d32f2f', '#1976d2', '#388e3c', '#fbc02d', '#7b1fa2', '#0288d1', '#c2185b', '#ffa000', '#689f38', '#303f9f'
              ];
              const color = colors[idx % colors.length];
              return (
                <li key={event.Start_Date || event.start_date} style={{ display: 'flex', alignItems: 'center', marginBottom: 6 }}>
                  <span style={{ width: 16, height: 16, background: color, borderRadius: '50%', display: 'inline-block', marginRight: 8 }}></span>
                  <span style={{ color: '#333', fontSize: 14 }}>{event.Description || event.description}</span>
                </li>
              );
            })}
          </ul>
        </div>
      </div>
    </div>
  );
}

export default App;