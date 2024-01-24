const Pool = require('pg').Pool;;
const pool = new Pool({
    user: process.env.POSTGRES_USER,
    host: 'postgres',
    database: process.env.POSTGRES_DB,
    password: process.env.POSTGRES_PASSWORD,
    port: parseInt(process.env.POSTGRES_PORT),
});
const getOpportunities = async (request, response) => {
    await pool.query('SELECT * FROM opportunities', (error, results) => {
        if (error) {
            response.status(500).send(error);
        } else {
            response.status(200).send(results.rows);
        }
    });
};

module.exports = {getOpportunities};