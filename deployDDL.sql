  

CREATE DATABASE IF NOT EXISTS projShell;

USE projShell;


  CREATE TABLE  `projShell`.`user` (
  `userID` int(11) NOT NULL AUTO_INCREMENT,

  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `username` varchar(200) NOT NULL,

  PRIMARY KEY (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=29484 DEFAULT CHARSET=utf8;




  CREATE TABLE  `projShell`.`tagDate` (
  `tagDateId` int(10) NOT NULL
  `tagId` int(10) NOT NULL,
  `month` ,
  `year` ,

/*
  `TerritoryID` int(11) DEFAULT NULL,
  `CustomerType` varchar(1) NOT NULL,
  `rowguid` varbinary(16) NOT NULL,
  `ModifiedDate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
*/
  PRIMARY KEY (`tagDateId`)
) ENGINE=InnoDB AUTO_INCREMENT=29484 DEFAULT CHARSET=utf8;