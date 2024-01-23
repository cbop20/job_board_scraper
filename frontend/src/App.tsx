import React from 'react';
import FilterBar from './components/filterBar';
import JobCards from './components/jobCards';
import './styles/App.css';

function App() {

  return (
    <div className="page" style={{}}>
      <FilterBar/>
      <JobCards/>
    </div>
  );
}

export default App;
