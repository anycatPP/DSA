const express = require('express');
const cors = require('cors');
const app = express();
const monk = require('monk');
const Filter = require('bad-words');
const rateLimit = require('express-rate-limit');
const db = monk(process.env.MONGO_URI || 'localhost/meower');
const mews = db.get('mews');
const filter = new Filter();
app.use(cors());
app.use(express.json());
app.use(rateLimit({
    windowMs: 30 * 1000,
    max: 1
}));
app.get('/', (req, res) => {
    res.json({ message: 'shitt head' });
});
app.get('/mews', (req, res) => {
    mews
        .find()
        .then(mews => {
            res.json(mews);
        });
})

function isValidMew(mew) {
    return mew.name && mew.name.toString().trim() !== '' && mew.content && mew.content.toString().trim() !== '';
}
app.post('/mews', (req, res) => {
    if (isValidMew(req.body)) {
        //insert into db
        const mew = {
            name: filter.clean(req.body.name.toString()),
            content: filter.clean(req.body.content.toString()),
            created: new Date()
        };
        mews
            .insert(mew)
            .then(createdMew => {
                res.json(createdMew);
            });
    } else {
        res.status(422);
        res.json({
            message: 'hey name and content required'
        })
    }
});

app.listen(5000, () => {
    console.log('listening on http://localhost:5000');
})