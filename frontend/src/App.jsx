import React from 'react';
import FilterBar from './components/filterBar';
import JobCards from './components/jobCards';
import './styles/App.css';

function App() {
  const [data, setData] = React.useState([]);
  const call=()=>{
    fetch('http://localhost:8080/opportunities')
    .then(response => response.json())
    .then(json=>setData(json))
    .catch(er=>console.log(er))
 }

  React.useEffect(()=>{
    call()
  },[])

  return (
    <div className="page" style={{}}>
      <FilterBar/>
      <JobCards {...data}/>
    </div>
  );
}

export default App;
