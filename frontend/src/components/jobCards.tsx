import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
export default function JobCards(){
    const data = [1,2,3,4,5,6,7]
    return(
        <Box display="flex" flexDirection="row" flexWrap="wrap" justifyContent={'center'}>
        {data.map((item) => (
          <Card sx={{height:'300px',width:'300px',margin:'5px',outline:'1px solid #333333'}}>
            <CardContent>
              <h1>{item}</h1>
            </CardContent>
          </Card>
        ))}
      </Box>
    )
}