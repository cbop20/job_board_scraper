import React from 'react';
import FilterBar from './components/filterBar';
import JobCards from './components/jobCards';
import Button from '@mui/material/Button';
import './styles/App.css';

function App() {
  const [data, setData] = React.useState([]);
  const call=()=>{
    fetch('http://localhost:8080/opportunities')
    .then(response => response.json())
    .then(json=>setData(json))
    .catch(er=>console.log(er))
 }
  const func= ()=> {
    fetch('https://localhost:5000/')
    .then(response => response.json())
    .then(ret=>console.log(ret))
    .catch(er=>console.log(er))
  };

  React.useEffect(()=>{
    call()
  },[])

  return (
    <div className="page">
      <Button onClick={()=>func()}>Scrape</Button>
      <FilterBar/>
      <JobCards {...data}/>
    </div>
  );
}

export default App;
