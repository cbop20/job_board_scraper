import React from 'react';
import FilterBar from './filterBar';
import JobCards from './jobCards';
import './App.css';

function App() {

  return (
    <div className="page" style={{}}>
      <FilterBar/>
      <JobCards/>
    </div>
  );
}

export default App;
