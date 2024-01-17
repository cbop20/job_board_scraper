import {CardContent, Card, Grid} from '@mui/material';
import {useState,useMemo} from 'react';
import './home.css'
export default function CardGrid() {
    const [list,setList] = useState([1,2,3,4,5,6,7]);

    const cardList = useMemo( () => {
        return(list.map(index =>(
            <Card sx={{
                width: '500px'
            }} 
            key={index} 
            variant="outlined">
                <CardContent>
                    {index}
                </CardContent>
            </Card>
        )))
    },[list]);
    
    return(
        <Grid sx={{
            justifyContent: 'center'  
        }}
        container spacing={2} >
            {cardList}
        </Grid> 
    )
}