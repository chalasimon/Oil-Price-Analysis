import React, { useEffect, useState } from 'react';

function App() {
  const [health, setHealth] = useState(null);

  useEffect(() => {
    fetch('/api/health')
      .then(res => res.json())
      .then(data => setHealth(data));
  }, []);

  return (
    <div>
      <h1>Oil Price Dashboard</h1>
      <p>Backend status: {health ? health.message : 'Checking...'}</p>
    </div>
  );
}

export default App;