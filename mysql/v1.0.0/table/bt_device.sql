DROP TABLE IF EXISTS `bluetooth`.`bt_device`;
CREATE TABLE  `bluetooth`.`bt_device` (
  `address` varchar(30) NOT NULL COMMENT 'the address of the bluetooth device',
  `createdby` varchar(45) NOT NULL COMMENT 'the line has been added by this user',
  `created` datetime NOT NULL,
  PRIMARY KEY  (`address`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;