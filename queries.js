const Pool = require('pg').Pool;
require('dotenv').config();
const pool = new Pool({
    user: process.env.DB_USER,
    host: process.env.DB_HOST,
    database: process.env.DB_NAME,
    password: process.env.DB_PASSWORD,
    port: process.env.DB_PORT
});

const getNumEntries = (request, response) => {
    pool.query('SELECT Count(*) FROM opportunities', (error, results) => {
        if (error) {
            response.status(500).send(error);
        } else {
            response.status(200).send(results.rows[0].count);
        }
    });
};

module.exports = {getNumEntries};