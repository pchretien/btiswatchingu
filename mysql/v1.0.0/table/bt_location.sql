DROP TABLE IF EXISTS `bluetooth`.`bt_location`;
CREATE TABLE  `bluetooth`.`bt_location` (
  `name` varchar(45) NOT NULL,
  `google` text,
  `created` datetime NOT NULL,
  `createdby` varchar(45) NOT NULL,
  PRIMARY KEY  (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;