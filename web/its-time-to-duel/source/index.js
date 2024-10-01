var express = require('express');
var session = require('express-session');
var bodyParser = require("body-parser");
var routes = require('./routes');
var flash = require('connect-flash');
var path = require('path');

var app = express();

app.use(session({
        secret: require("crypto").randomBytes(64).toString("hex"),
        resave: true,
        saveUninitialized: false,
        cookie: { sameSite: 'strict', maxAge: 240000 }
}));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(flash());
app.use(express.static(path.join(__dirname + '/public')));
app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');

app.use(routes);

app.listen(3000, '0.0.0.0', () => {
  console.log('Server running at http://0.0.0.0:3000/');
});