CREATE DATABASE Finances;
DROP TABLE if EXISTS Administrator;
CREATE Table Administrator(
    name VARCHAR(255) NOT NULL,
    adminID VARCHAR(255) NOT NULL,
    password VARCHAR(255),
    PRIMARY KEY (adminID)
)ENGINE=INNODB DEFAULT CHARSET=UTF8;

DROP TABLE if EXISTS employee;
CREATE TABLE Employee(
    name VARCHAR(255) NOT NULL,
    empID VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    addr VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (empID)
)ENGINE=INNODB DEFAULT CHARSET=UTF8;

DROP TABLE if EXISTS audit;
CREATE TABLE Audit(
    name VARCHAR(255) NOT NULL,
    auditID VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    addr VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (auditID)
)ENGINE=INNODB DEFAULT CHARSET=UTF8;

DROP TABLE if EXISTS bills;
CREATE TABLE bills(
    billno INT NOT NULL AUTO_INCREMENT,
    user VARCHAR(255) NOT NULL,
    amount VARCHAR(255) NOT NULL,
    reason VARCHAR(255) NOT NULL,
    time DATETIME NOT NULL,
    PRIMARY KEY (billno),
    FOREIGN KEY (user) REFERENCES employee(empID)
)ENGINE=INNODB DEFAULT CHARSET=UTF8;

INSERT INTO Administrator
VALUES
    (
        '宣恩允',
        '1911501',
        '201028'
    );

INSERT INTO administrator
VALUES
    (
        '朱浩泽',
        '1911530',
        '1911530'
    ),
    (
        '赵一林',
        '1910874',
        '1910874'
    ),
    (
        '马轻飏',
        '1911450',
        '1911450'
    ),
    (
        '何坤彬',
        '1911417',
        '1911417'
    );


INSERT INTO employee
VALUES
    (
        '宣恩允',
        '440881200011230419',
        '17320262903',
        '广东省湛江市廉江市',
        '201028'
    );

INSERT INTO audit
VALUES
    (
        '宣恩允',
        '440881200011230419',
        '17320262903',
        '广东省湛江市廉江市',
        '201028'
    );

INSERT INTO bills
VALUES
    (
        1,
        '440881200011230419',
        '1234.123',
        '出差',
        NOW()
    );

INSERT INTO bills(user, amount, reason, time)
VALUES
    ('440881200011230419', '1091.63', '交学费', NOW()),
    ('440881200011230419', '643.81', '交学费', NOW()),
    ('440881200011230419', '1860.88', '交学费', NOW()),
    ('440881200011230419', '1324.35', '交学费', NOW()),
    ('440881200011230419', '1979.2', '交学费', NOW()),
    ('440881200011230419', '8.51', '交学费', NOW()),
    ('440881200011230419', '1929.2', '交学费', NOW()),
    ('440881200011230419', '679.69', '交学费', NOW()),
    ('440881200011230419', '390.45', '交学费', NOW()),
    ('440881200011230419', '1715.52', '交学费', NOW()),
    ('440881200011230419', '1164.59', '交学费', NOW()),
    ('440881200011230419', '53.77', '交学费', NOW()),
    ('440881200011230419', '1536.85', '交学费', NOW()),
    ('440881200011230419', '437.82', '交学费', NOW()),
    ('440881200011230419', '1064.46', '交学费', NOW()),
    ('440881200011230419', '1788.60', '交学费', NOW()),
    ('440881200011230419', '566.62', '交学费', NOW()),
    ('440881200011230419', '500.22', '交学费', NOW()),
    ('440881200011230419', '500.97', '交学费', NOW()),
    ('440881200011230419', '477.32', '交学费', NOW());
    