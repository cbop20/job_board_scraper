import TextField from '@mui/material/TextField'
import SearchIcon from '@mui/icons-material/Search'
import IconButton from '@mui/material/IconButton'
import Button from '@mui/material/Button'
import '../styles/filterBar.css'
export default function FilterBar({searchValue, setSearchValue, search}) {
    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            search(searchValue)
        }
      };
    return(
        <div className="filter-bar-wrapper">
            <input 
                className='filter-bar'
                type="text"
                value={searchValue}
                onChange={(e)=>setSearchValue(e.target.value)}
                onKeyUp={(e)=>handleKeyPress(e)}/>
            <IconButton className='search-button' onClick={()=>search(searchValue)}>
                <SearchIcon/>
            </IconButton>
        </div>
    )
}