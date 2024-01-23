const Pool = require('pg').Pool;
require('dotenv').config();
const pool = new Pool({
    user: process.env.POSTGRES_USER,
    host: 'postgres',
    database: process.env.POSTGRES_DB,
    password: process.env.POSTGRES_PASSWORD,
    port: parseInt(process.env.POSTGRES_PORT),
});
console.log(process.env.POSTGRES_USER,process.env.POSTGRES_PASSWORD,process.env.POSTGRES_HOST,process.env.POSTGRES_PORT,process.env.POSTGRES_DB);
const connectToDB = async () => {
    try {
      await pool.connect();
    } catch (err) {
      console.log(err);
    }
  };
connectToDB();

const getNumEntries = async (request, response) => {
    await pool.query('SELECT Count(*) FROM opportunities', (error, results) => {
        if (error) {
            response.status(500).send(error);
        } else {
            response.status(200).send(results.rows[0].count);
        }
    });
};

module.exports = {getNumEntries};