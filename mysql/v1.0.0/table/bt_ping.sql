DROP TABLE IF EXISTS `bluetooth`.`bt_ping`;
CREATE TABLE  `bluetooth`.`bt_ping` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `address` varchar(45) NOT NULL,
  `location` varchar(45) NOT NULL,
  `created` datetime NOT NULL,
  `createdby` varchar(45) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=153 DEFAULT CHARSET=latin1;