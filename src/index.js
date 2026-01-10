require('dotenv').config();
const express = require('express');

const app = express();
const PORT = process.env.PORT || 3000;
const DB_HOST = process.env.DB_HOST || 'localhost';

// Simulate DB Connection (Mock)
console.log(`Successfully connected to database at ${DB_HOST}`);

app.get('/health', (req, res) => {
    res.json({ status: 'ok', db: 'connected' });
});

app.get('/data', (req, res) => {
    res.json({
        data: [1, 2, 3],
        source: DB_HOST
    });
});

// INTENTIONAL SYNTAX ERROR: Missing closing brace for app.listen
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
