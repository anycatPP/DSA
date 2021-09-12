const feathers = require('@feathersjs/feathers');
const app = feathers();

class MesssageService {
    constructor() {
        this.messages = [];
    }
    async find() {
        return this.messages;
    }
    async create(data) {
        const message = {
            id: this.messages.length,
            text: data.text
        };
        this.messages.push(message);
        return message;
    }
}
app.use('messages', new MesssageService());

app.service('messages').on('created', (message) => {
    console.log('A new message has been created', message);
});

const main = async() => {
    await app.service('messages').create({
        text: 'hello feathers'
    });
    await app.service('messages').create({
        text: 'hello again'
    });
    const messages = await app.service('messages').find();
    console.log('all messages', message);
}
main();