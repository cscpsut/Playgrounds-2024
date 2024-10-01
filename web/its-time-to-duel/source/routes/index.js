var express = require('express');
var router = express.Router();
var mysql = require('mysql'); /* Upgraded deprecated mysqljs */
var flash = require('connect-flash');
var db = require('../config/db.js');
var connection = mysql.createConnection(db.db)

router.get('/', function(req, res) {
	res.render('index');
});

router.get('/login', function(req, res) {
	res.render('login', { logged : req.flash('error') });
});

router.get('/register', function(req, res) {
	res.render('register', { registered : req.flash('error') });
});

router.get('/reset', function(req, res) {
	res.render('reset', { reset : req.flash('error') });
});

router.use('/401', function(req,res){
    res.render('401');
});

router.use('/500', function(req,res){
    res.render('500');
});

router.use('/404', function(req,res){
    res.render('404');
});

router.get('/logout', function(req, res) {
	if (req.session) {
	    req.session.destroy(err => {
	      if (err) {
	        res.redirect('/500');
	      } else {
	        res.redirect('/login');
	      }
	    });
	  } else {
	    res.redirect('/login');
	  }
});

router.post('/api/register', function(req, res) {
	req.flash('error', 'Currently not available!');
	res.redirect('/register');
});

router.post('/api/reset', function(req, res) {
	req.flash('error', 'Currently not available!');
	res.redirect('/reset');
});

router.post('/api/login', function(req, res) {
	let username = req.body.username;
	let password = req.body.password;
	if (username && password) {
		connection.query('SELECT * FROM accounts WHERE username = ? AND password = ?', [username, password], function(error, results, fields) {
			if (error) throw error;
			if (results.length > 0) {
				req.session.loggedin = true;
				req.session.username = username;
				req.flash('success', 'Succesfully logged in!');
				res.redirect('/admin');
			} else {
				req.flash('error', 'Wrong credentials! Try Again!');
				res.redirect('/login');
			}			
			res.end();
		});
	} else {
		res.redirect('/login');
	}
});

router.get('/admin', function(req, res) {
	if (req.session.loggedin) {
		res.render('admin');
	} else {
		res.redirect('/login');
	}
	res.end();
});

router.get('/notes', function(req, res) {
	if (req.session.loggedin) {
		res.render('notes');
	} else {
		res.redirect('/401');
	}
	res.end();
});

router.get('/charts', function(req, res) {
	if (req.session.loggedin) {
		res.render('charts');
	} else {
		res.redirect('/401');
	}
	res.end();
});

router.get('/tables', function(req, res) {
	if (req.session.loggedin) {
		res.render('tables');
	} else {
		res.redirect('/401');
	}
	res.end();
});

router.all('*', (req, res) => {
	res.status(404);		
	res.redirect('/404');
});

module.exports = router;