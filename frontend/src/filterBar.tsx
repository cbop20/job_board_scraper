import TextField from '@mui/material/TextField'
import SearchIcon from '@mui/icons-material/Search'
import IconButton from '@mui/material/IconButton'
export default function FilterBar() {
    const call=()=>{
    
       fetch('http://localhost:8080/opportunities')
       .then(response => response.json())
       .then(jsno=>console.log(jsno))
       .catch(er=>console.log(er))
    }
    return(
        <div style={{padding:'5px',display:'flex',justifyContent:'center'}}>
            <form style={{display:'flex',justifyContent:'center'}}>
                <label>
                    <input 
                        style={{width:'50vw', height:'35px',fontSize:'25px', border: '1px solid #ccc', outline:'1px solid #333333', transition: 'outline 0.1s ease', borderRadius:'5px',color:'#555555'}} 
                        onFocus={(e)=>{e.target.style.outline= '2px solid #3498db'}}
                        onBlur={(e) => (e.target.style.outline='1px solid #333333')} // Change border color on blur
                        type="text"/>
                </label>
                <IconButton sx={{marginLeft:'5px', color:'#3498db',
                '& .MuiTouchRipple-root': {
                    color:'#3498db'
                },
                '&:hover':{
                    color:'#2980b9',
                    background:'none'
                }}}
                onClick={()=>call()}
                >

                    <SearchIcon/>
                </IconButton>
            </form>
        </div>
    )
}