DROP TABLE IF EXISTS `bluetooth`.`bt_user`;
CREATE TABLE  `bluetooth`.`bt_user` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `firstname` varchar(45) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;