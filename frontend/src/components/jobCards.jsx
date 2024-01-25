import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardHeader from '@mui/material/CardHeader';
import Button from '@mui/material/Button';
import CardActions from '@mui/material/CardActions';
import Typography from '@mui/material/Typography';
import '../styles/jobCards.css'
export default function JobCards(data){
    return(
        <Box className='job-card-box'>
        {Object.values(data).map((item) => (
          <Card key={item.id} className='job-card'>
            <CardHeader className='card-header' title={item.title} subheader={item.company_name} />
            <CardContent className='card-content'>
              <Typography className='text'>{item.info.join('\n')}</Typography>
            </CardContent>
            <CardActions className='card-actions'>
              <Button className='apply-button'>
                <Typography sx={{textTransform:'none'}}>Apply</Typography>
                  </Button>
            </CardActions>
          </Card>
        ))}
      </Box>
    )
}