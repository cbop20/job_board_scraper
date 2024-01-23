const express = require('express');
const cors = require('cors');
const db = require('./routes/queries');
const app = express();

app.get('/', cors(), (req,res)=>{
    res.json('Hello World')
});
app.get('/opportunities', cors(), db.getNumEntries);
const port = 8080;
app.listen(port, ()=> console.log(`Server running on port ${port}`));
