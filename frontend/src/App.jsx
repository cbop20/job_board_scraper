import {React, useEffect, useState} from 'react';
import FilterBar from './components/filterBar';
import JobCards from './components/jobCards';
import Button from '@mui/material/Button';
import './styles/App.css';
import debounce from 'lodash/debounce';

function App() {
  const [data, setData] = useState([]);
  const [searchedJobs, setSearchedJobs] = useState([]);
  const [searchValue, setSearchValue] = useState('');
  const [scrapeButton, setScrapeButton] = useState(false);

  const getJobs=()=>{
    fetch('http://localhost:8080/opportunities')
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json()
    })
    .then(json=>{
      if(json){
        setData(json)
        setSearchedJobs(json)
      }
    })
    .catch(er=>console.log(er))
 }

  const scrape= async ()=> {
    setScrapeButton(true)
    await fetch('http://localhost:5000/get_opportunities',{
      method: 'GET',
    })
    .then(response => {
      setScrapeButton(false)
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
    })
    .then(()=>{
      getJobs()
    })
  
    .catch(er=>{
      setScrapeButton(false)
      console.log(er)})
  };

  useEffect(() => {
    getJobs();
  }, []);

  const search = () => {
    const filteredItems = data.filter((job) =>
    job.title.toLowerCase().includes(searchValue.toLowerCase())
    );
    setSearchedJobs(filteredItems);
  }

  useEffect(() => {
    if (searchValue!= ''){
      search()
    }
  },[searchValue]);


  return (
    <div className="page">
      <div className="options">
        <Button centerRipple className='scrape-button' onClick={()=>scrape()} disabled={scrapeButton}>Scrape</Button>
        <FilterBar searchValue={searchValue} setSearchValue={setSearchValue} search={search} />
      </div>
      <JobCards {...searchedJobs}/>
    </div>
  );
}

export default App;
