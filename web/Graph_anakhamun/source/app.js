const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { buildSchema } = require('graphql');
const path = require('path');
const fs = require('fs');

const schema = buildSchema(`
  type User {
    id: Int
    username: String
    email: String
  }

  type Hints {
    id: Int
    message: String
  }

  type Secret {
    password : String
    hidden: String
  }

  type Query {
    users: [User]
    hints(id: Int!): Hints 
    secret(password: String!) : Secret
  
  }

`);

const data = JSON.parse(fs.readFileSync(path.join(__dirname, '/users.json'), 'utf-8'));

const root = {
  users: () => data.users,
  hints: ({ id }) => data.hints.find(hints => hints.id === id),
  // secret: ({ password }) => data.secret.find(secret => (secret.password == password)),
  secret: ({ password }) => {
    const compare = data.secret.find(secret => secret.password === password);
    if (compare) {
        return { hidden: compare.hidden };
    } else {
        return { hidden: "Wrong password, try again." };
    }
  
}
};

const app = express();

app.get('/Maybe', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/Maybe.html')); 
});

app.use(express.static(path.join(__dirname, '/public')));

app.use('/graph2', graphqlHTTP({
  schema: schema,
  rootValue: root,
  graphiql: true 
}));

app.listen(4000, () => console.log('Server running on http://localhost:4000'));
