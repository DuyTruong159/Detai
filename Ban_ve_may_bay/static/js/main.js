function showPrice(sp) {
    document.getElementById('price').innerHTML = sp;
}

function t1() {
    var mysql = require('mysql');

    var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "phamduytruong",
    database: "detai"
    });

    con.connect(function(err) {
        if (err) throw err;
        con.query("SELECT Vechuenbay.gia FROM Vechuyenbay WHERE NgayDk BETWEEN '1-1' AND '1-31'", function(err, result) {
            if (err) throw err;
            document.getElementById('1').innerHTML = sum(result.chuyenbay_id = 1);
            document.getElementById('2').innerHTML = sum(result.chuyenbay_id = 2);
            document.getElementById('3').innerHTML = sum(result.chuyenbay_id = 3);
            document.getElementById('4').innerHTML = sum(result.chuyenbay_id = 4);
            document.getElementById('5').innerHTML = sum(result.chuyenbay_id = 5);
        });
    });
}

function t2() {
    var mysql = require('mysql');

    var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "phamduytruong",
    database: "detai"
    });

    con.connect(function(err) {
        if (err) throw err;
        con.query("SELECT Vechuenbay.gia FROM Vechuyenbay WHERE NgayDk BETWEEN '2-1' AND '2-29'", function(err, result) {
            if (err) throw err;
            document.getElementById('1').innerHTML = sum(result.chuyenbay_id = 1);
            document.getElementById('2').innerHTML = sum(result.chuyenbay_id = 2);
            document.getElementById('3').innerHTML = sum(result.chuyenbay_id = 3);
            document.getElementById('4').innerHTML = sum(result.chuyenbay_id = 4);
            document.getElementById('5').innerHTML = sum(result.chuyenbay_id = 5);
        });
    });
}

function t3() {
    var mysql = require('mysql');

    var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "phamduytruong",
    database: "detai"
    });

    con.connect(function(err) {
        if (err) throw err;
        con.query("SELECT Vechuenbay.gia FROM Vechuyenbay WHERE NgayDk BETWEEN '3-1' AND '3-31'", function(err, result) {
            if (err) throw err;
            document.getElementById('1').innerHTML = sum(result.chuyenbay_id = 1);
            document.getElementById('2').innerHTML = sum(result.chuyenbay_id = 2);
            document.getElementById('3').innerHTML = sum(result.chuyenbay_id = 3);
            document.getElementById('4').innerHTML = sum(result.chuyenbay_id = 4);
            document.getElementById('5').innerHTML = sum(result.chuyenbay_id = 5);
        });
    });
}

function t4() {
    var mysql = require('mysql');

    var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "phamduytruong",
    database: "detai"
    });

    con.connect(function(err) {
        if (err) throw err;
        con.query("SELECT Vechuenbay.gia FROM Vechuyenbay WHERE NgayDk BETWEEN '4-1' AND '4-30'", function(err, result) {
            if (err) throw err;
            document.getElementById('1').innerHTML = sum(result.chuyenbay_id = 1);
            document.getElementById('2').innerHTML = sum(result.chuyenbay_id = 2);
            document.getElementById('3').innerHTML = sum(result.chuyenbay_id = 3);
            document.getElementById('4').innerHTML = sum(result.chuyenbay_id = 4);
            document.getElementById('5').innerHTML = sum(result.chuyenbay_id = 5);
        });
    });
}

function t5() {
    var mysql = require('mysql');

    var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "phamduytruong",
    database: "detai"
    });

    con.connect(function(err) {
        if (err) throw err;
        con.query("SELECT Vechuenbay.gia FROM Vechuyenbay WHERE NgayDk BETWEEN '5-1' AND '5-31'", function(err, result) {
            if (err) throw err;
            document.getElementById('1').innerHTML = sum(result.chuyenbay_id = 1);
            document.getElementById('2').innerHTML = sum(result.chuyenbay_id = 2);
            document.getElementById('3').innerHTML = sum(result.chuyenbay_id = 3);
            document.getElementById('4').innerHTML = sum(result.chuyenbay_id = 4);
            document.getElementById('5').innerHTML = sum(result.chuyenbay_id = 5);
        });
    });
}

function t6() {
    var mysql = require('mysql');

    var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "phamduytruong",
    database: "detai"
    });

    con.connect(function(err) {
        if (err) throw err;
        con.query("SELECT Vechuenbay.gia FROM Vechuyenbay WHERE NgayDk BETWEEN '6-1' AND '6-30'", function(err, result) {
            if (err) throw err;
            document.getElementById('1').innerHTML = sum(result.chuyenbay_id = 1);
            document.getElementById('2').innerHTML = sum(result.chuyenbay_id = 2);
            document.getElementById('3').innerHTML = sum(result.chuyenbay_id = 3);
            document.getElementById('4').innerHTML = sum(result.chuyenbay_id = 4);
            document.getElementById('5').innerHTML = sum(result.chuyenbay_id = 5);
        });
    });
}

function t7() {
    var mysql = require('mysql');

    var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "phamduytruong",
    database: "detai"
    });

    con.connect(function(err) {
        if (err) throw err;
        con.query("SELECT Vechuenbay.gia FROM Vechuyenbay WHERE NgayDk BETWEEN '7-1' AND '4-31'", function(err, result) {
            if (err) throw err;
            document.getElementById('1').innerHTML = sum(result.chuyenbay_id = 1);
            document.getElementById('2').innerHTML = sum(result.chuyenbay_id = 2);
            document.getElementById('3').innerHTML = sum(result.chuyenbay_id = 3);
            document.getElementById('4').innerHTML = sum(result.chuyenbay_id = 4);
            document.getElementById('5').innerHTML = sum(result.chuyenbay_id = 5);
        });
    });
}

function t8() {
    var mysql = require('mysql');

    var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "phamduytruong",
    database: "detai"
    });

    con.connect(function(err) {
        if (err) throw err;
        con.query("SELECT Vechuenbay.gia FROM Vechuyenbay WHERE NgayDk BETWEEN '8-1' AND '8-31'", function(err, result) {
            if (err) throw err;
            document.getElementById('1').innerHTML = sum(result.chuyenbay_id = 1);
            document.getElementById('2').innerHTML = sum(result.chuyenbay_id = 2);
            document.getElementById('3').innerHTML = sum(result.chuyenbay_id = 3);
            document.getElementById('4').innerHTML = sum(result.chuyenbay_id = 4);
            document.getElementById('5').innerHTML = sum(result.chuyenbay_id = 5);
        });
    });
}

function t9() {
    var mysql = require('mysql');

    var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "phamduytruong",
    database: "detai"
    });

    con.connect(function(err) {
        if (err) throw err;
        con.query("SELECT Vechuenbay.gia FROM Vechuyenbay WHERE NgayDk BETWEEN '9-1' AND '9-30'", function(err, result) {
            if (err) throw err;
            document.getElementById('1').innerHTML = sum(result.chuyenbay_id = 1);
            document.getElementById('2').innerHTML = sum(result.chuyenbay_id = 2);
            document.getElementById('3').innerHTML = sum(result.chuyenbay_id = 3);
            document.getElementById('4').innerHTML = sum(result.chuyenbay_id = 4);
            document.getElementById('5').innerHTML = sum(result.chuyenbay_id = 5);
        });
    });
}

function t10() {
    var mysql = require('mysql');

    var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "phamduytruong",
    database: "detai"
    });

    con.connect(function(err) {
        if (err) throw err;
        con.query("SELECT Vechuenbay.gia FROM Vechuyenbay WHERE NgayDk BETWEEN '10-1' AND '10-31'", function(err, result) {
            if (err) throw err;
            document.getElementById('1').innerHTML = sum(result.chuyenbay_id = 1);
            document.getElementById('2').innerHTML = sum(result.chuyenbay_id = 2);
            document.getElementById('3').innerHTML = sum(result.chuyenbay_id = 3);
            document.getElementById('4').innerHTML = sum(result.chuyenbay_id = 4);
            document.getElementById('5').innerHTML = sum(result.chuyenbay_id = 5);
        });
    });
}

function t11() {
    var mysql = require('mysql');

    var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "phamduytruong",
    database: "detai"
    });

    con.connect(function(err) {
        if (err) throw err;
        con.query("SELECT Vechuenbay.gia FROM Vechuyenbay WHERE NgayDk BETWEEN '11-1' AND '11-30'", function(err, result) {
            if (err) throw err;
            document.getElementById('1').innerHTML = sum(result.chuyenbay_id = 1);
            document.getElementById('2').innerHTML = sum(result.chuyenbay_id = 2);
            document.getElementById('3').innerHTML = sum(result.chuyenbay_id = 3);
            document.getElementById('4').innerHTML = sum(result.chuyenbay_id = 4);
            document.getElementById('5').innerHTML = sum(result.chuyenbay_id = 5);
        });
    });
}

function t12() {
    var mysql = require('mysql');

    var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "phamduytruong",
    database: "detai"
    });

    con.connect(function(err) {
        if (err) throw err;
        con.query("SELECT Vechuenbay.gia FROM Vechuyenbay WHERE NgayDk BETWEEN '12-1' AND '12-31'", function(err, result) {
            if (err) throw err;
            document.getElementById('1').innerHTML = sum(result.chuyenbay_id = 1);
            document.getElementById('2').innerHTML = sum(result.chuyenbay_id = 2);
            document.getElementById('3').innerHTML = sum(result.chuyenbay_id = 3);
            document.getElementById('4').innerHTML = sum(result.chuyenbay_id = 4);
            document.getElementById('5').innerHTML = sum(result.chuyenbay_id = 5);
        });
    });
}