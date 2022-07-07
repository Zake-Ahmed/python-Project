CREATE TABLE IF NOT EXISTS user
             (
                          id         INTEGER NOT NULL AUTO_INCREMENT,
                          first_name VARCHAR(30) NOT NULL,
                          last_name  VARCHAR(30) NOT NULL,
                          email      VARCHAR(150) NOT NULL,
                          PRIMARY KEY (id),
                          UNIQUE (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

create table if not exists users(
id int not null auto_increment,
firstName varchar(20) ,
lastName varchar(20) ,
userName varchar(200) ,
primary key(id))ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

create table if not exists posts(
id int not null auto_increment,
userId int not null,
message varchar(280),
likes int default(0),
primary key(id),
foreign key(userId) references users(id)  ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Ben','Hesketh','test@test7.com'),(2,'Luke','Benson','test@test.com'),(3,'Matt','Hunt','test4@test.com');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;