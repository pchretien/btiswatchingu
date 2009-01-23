DROP TABLE IF EXISTS `bluetooth`.`bt_device_name`;
CREATE TABLE  `bluetooth`.`bt_device_name` (
  `address` varchar(20) NOT NULL COMMENT 'the address of the bluetooth device',
  `name` varchar(45) NOT NULL COMMENT 'the name of the bluetooth device',
  `createdby` varchar(45) NOT NULL COMMENT 'this line has been added by this user',
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  PRIMARY KEY  (`address`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
