import TextField from '@mui/material/TextField'
import SearchIcon from '@mui/icons-material/Search'
import IconButton from '@mui/material/IconButton'
import Button from '@mui/material/Button'
import '../styles/filterBar.css'
export default function FilterBar() {
    return(
        <div className="filter-bar-wrapper">
            <form>
                <label>
                    <input 
                        className='filter-bar'
                        type="text"/>
                </label>
                <IconButton className='search-button'>
                    <SearchIcon/>
                </IconButton>
            </form>
        </div>
    )
}