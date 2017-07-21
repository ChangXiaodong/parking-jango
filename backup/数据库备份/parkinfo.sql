/*
Navicat MySQL Data Transfer

Source Server         : aliyun
Source Server Version : 50628
Source Host           : 121.42.213.241:3306
Source Database       : parkinfo

Target Server Type    : MYSQL
Target Server Version : 50628
File Encoding         : 65001

Date: 2017-05-04 12:18:25
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add park data', '7', 'add_parkdata');
INSERT INTO `auth_permission` VALUES ('20', 'Can change park data', '7', 'change_parkdata');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete park data', '7', 'delete_parkdata');
INSERT INTO `auth_permission` VALUES ('22', 'Can add park data history', '8', 'add_parkdatahistory');
INSERT INTO `auth_permission` VALUES ('23', 'Can change park data history', '8', 'change_parkdatahistory');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete park data history', '8', 'delete_parkdatahistory');
INSERT INTO `auth_permission` VALUES ('25', 'Can add manhole data', '9', 'add_manholedata');
INSERT INTO `auth_permission` VALUES ('26', 'Can change manhole data', '9', 'change_manholedata');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete manhole data', '9', 'delete_manholedata');
INSERT INTO `auth_permission` VALUES ('28', 'Can add manhole data history', '10', 'add_manholedatahistory');
INSERT INTO `auth_permission` VALUES ('29', 'Can change manhole data history', '10', 'change_manholedatahistory');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete manhole data history', '10', 'delete_manholedatahistory');
INSERT INTO `auth_permission` VALUES ('31', 'Can add bill board data', '11', 'add_billboarddata');
INSERT INTO `auth_permission` VALUES ('32', 'Can change bill board data', '11', 'change_billboarddata');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete bill board data', '11', 'delete_billboarddata');
INSERT INTO `auth_permission` VALUES ('34', 'Can add sensor', '12', 'add_sensor');
INSERT INTO `auth_permission` VALUES ('35', 'Can change sensor', '12', 'change_sensor');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete sensor', '12', 'delete_sensor');
INSERT INTO `auth_permission` VALUES ('37', 'Can add data', '13', 'add_data');
INSERT INTO `auth_permission` VALUES ('38', 'Can change data', '13', 'change_data');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete data', '13', 'delete_data');
INSERT INTO `auth_permission` VALUES ('40', 'Can add configure', '14', 'add_configure');
INSERT INTO `auth_permission` VALUES ('41', 'Can change configure', '14', 'change_configure');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete configure', '14', 'delete_configure');
INSERT INTO `auth_permission` VALUES ('46', 'Can add ip tables', '16', 'add_iptables');
INSERT INTO `auth_permission` VALUES ('47', 'Can change ip tables', '16', 'change_iptables');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete ip tables', '16', 'delete_iptables');
INSERT INTO `auth_permission` VALUES ('49', 'Can add pre configure', '17', 'add_preconfigure');
INSERT INTO `auth_permission` VALUES ('50', 'Can change pre configure', '17', 'change_preconfigure');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete pre configure', '17', 'delete_preconfigure');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('11', 'info', 'billboarddata');
INSERT INTO `django_content_type` VALUES ('9', 'info', 'manholedata');
INSERT INTO `django_content_type` VALUES ('10', 'info', 'manholedatahistory');
INSERT INTO `django_content_type` VALUES ('7', 'info', 'parkdata');
INSERT INTO `django_content_type` VALUES ('8', 'info', 'parkdatahistory');
INSERT INTO `django_content_type` VALUES ('14', 'manhole_database', 'configure');
INSERT INTO `django_content_type` VALUES ('13', 'manhole_database', 'data');
INSERT INTO `django_content_type` VALUES ('16', 'manhole_database', 'iptables');
INSERT INTO `django_content_type` VALUES ('17', 'manhole_database', 'preconfigure');
INSERT INTO `django_content_type` VALUES ('12', 'manhole_database', 'sensor');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2017-05-01 19:37:03');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2017-05-01 19:37:04');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2017-05-01 19:37:04');
INSERT INTO `django_migrations` VALUES ('4', 'contenttypes', '0002_remove_content_type_name', '2017-05-01 19:37:04');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0002_alter_permission_name_max_length', '2017-05-01 19:37:05');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0003_alter_user_email_max_length', '2017-05-01 19:37:05');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0004_alter_user_username_opts', '2017-05-01 19:37:05');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0005_alter_user_last_login_null', '2017-05-01 19:37:05');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0006_require_contenttypes_0002', '2017-05-01 19:37:05');
INSERT INTO `django_migrations` VALUES ('10', 'manhole_database', '0001_initial', '2017-05-01 19:37:05');
INSERT INTO `django_migrations` VALUES ('11', 'manhole_database', '0002_auto_20170501_1612', '2017-05-01 19:37:05');
INSERT INTO `django_migrations` VALUES ('12', 'manhole_database', '0003_auto_20170501_1615', '2017-05-01 19:37:06');
INSERT INTO `django_migrations` VALUES ('13', 'manhole_database', '0004_delete_sensordata', '2017-05-01 19:37:06');
INSERT INTO `django_migrations` VALUES ('14', 'sessions', '0001_initial', '2017-05-01 19:37:06');
INSERT INTO `django_migrations` VALUES ('15', 'manhole_database', '0005_auto_20170502_1058', '2017-05-02 10:58:31');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for info_billboarddata
-- ----------------------------
DROP TABLE IF EXISTS `info_billboarddata`;
CREATE TABLE `info_billboarddata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `update_time` datetime NOT NULL,
  `nodeid` varchar(30) DEFAULT NULL,
  `x` varchar(30) DEFAULT NULL,
  `y` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of info_billboarddata
-- ----------------------------

-- ----------------------------
-- Table structure for info_manholedata
-- ----------------------------
DROP TABLE IF EXISTS `info_manholedata`;
CREATE TABLE `info_manholedata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `update_time` datetime NOT NULL,
  `changed_time` datetime NOT NULL,
  `areaid` varchar(5) DEFAULT NULL,
  `address` bigint(20) DEFAULT NULL,
  `command` varchar(5) DEFAULT NULL,
  `TMR_data` varchar(5) DEFAULT NULL,
  `threshold` varchar(5) DEFAULT NULL,
  `reed_data` varchar(5) DEFAULT NULL,
  `rssi_data` varchar(5) DEFAULT NULL,
  `snr_data` varchar(5) DEFAULT NULL,
  `battery_data` varchar(5) DEFAULT NULL,
  `last_disable_time` datetime NOT NULL,
  `administrator` varchar(20) DEFAULT NULL,
  `remarks` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of info_manholedata
-- ----------------------------
INSERT INTO `info_manholedata` VALUES ('1', '2016-06-25 15:01:51', '2016-06-03 14:29:23', '0', '1', '2', '1574', '1574', '9', '0', '0', '0', '2016-04-07 10:58:41', 'xiaoxiami', '');
INSERT INTO `info_manholedata` VALUES ('2', '2016-06-03 14:29:23', '2016-06-03 14:29:23', '0', '2', '0', '0', '0', '0', '0', '0', '0', '2016-04-07 10:58:41', 'xiaoxiami', '');
INSERT INTO `info_manholedata` VALUES ('3', '2016-06-03 14:29:23', '2016-06-03 14:29:23', '0', '3', '0', '0', '0', '0', '0', '0', '0', '2016-04-07 10:58:41', 'xiaoxiami', '');
INSERT INTO `info_manholedata` VALUES ('4', '2016-06-03 14:29:23', '2016-06-03 14:29:23', '0', '4', '0', '0', '0', '0', '0', '0', '0', '2016-04-07 10:58:41', 'xiaoxiami', '');
INSERT INTO `info_manholedata` VALUES ('5', '2016-06-03 14:29:23', '2016-06-03 14:29:23', '0', '5', '0', '0', '0', '0', '0', '0', '0', '2016-04-07 10:58:41', 'xiaoxiami', '');
INSERT INTO `info_manholedata` VALUES ('6', '2016-06-03 14:29:23', '2016-06-03 14:29:23', '0', '6', '0', '0', '0', '0', '0', '0', '0', '2016-04-07 10:58:41', 'xiaoxiami', '');
INSERT INTO `info_manholedata` VALUES ('7', '2016-06-03 14:29:23', '2016-06-03 14:29:23', '0', '7', '0', '0', '0', '0', '0', '0', '0', '2016-04-07 10:58:41', 'xiaoxiami', '');
INSERT INTO `info_manholedata` VALUES ('8', '2016-06-03 14:29:23', '2016-06-03 14:29:23', '0', '8', '0', '0', '0', '0', '0', '0', '0', '2016-04-07 10:58:41', 'xiaoxiami', '');
INSERT INTO `info_manholedata` VALUES ('9', '2016-06-03 14:29:23', '2016-06-03 14:29:23', '0', '9', '0', '0', '0', '0', '0', '0', '0', '2016-04-07 10:58:41', 'xiaoxiami', '');
INSERT INTO `info_manholedata` VALUES ('10', '2017-05-01 14:24:13', '2017-05-01 14:24:13', '0', '14', '0', '0', '0', '0', '0', '0', '0', '2016-04-07 10:58:41', 'xiaoxiami', '');

-- ----------------------------
-- Table structure for info_manholedatahistory
-- ----------------------------
DROP TABLE IF EXISTS `info_manholedatahistory`;
CREATE TABLE `info_manholedatahistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `update_time` datetime NOT NULL,
  `last_disable_time` datetime NOT NULL,
  `address` bigint(20) DEFAULT NULL,
  `data` varchar(5) DEFAULT NULL,
  `data_type` varchar(3) DEFAULT NULL,
  `administrator` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of info_manholedatahistory
-- ----------------------------

-- ----------------------------
-- Table structure for info_parkdata
-- ----------------------------
DROP TABLE IF EXISTS `info_parkdata`;
CREATE TABLE `info_parkdata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime NOT NULL,
  `changed_time` datetime NOT NULL,
  `relayid` varchar(30) DEFAULT NULL,
  `nodeid` varchar(30) DEFAULT NULL,
  `data` varchar(30) DEFAULT NULL,
  `parkid` varchar(5) DEFAULT NULL,
  `command` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=236 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of info_parkdata
-- ----------------------------
INSERT INTO `info_parkdata` VALUES ('186', '2017-02-24 10:59:07', '2017-02-24 10:58:53', '0086-110108-00022105-01', '0086-110108-00022105-0001', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('187', '2017-02-24 11:01:36', '2017-02-24 10:54:25', '0086-110108-00022105-01', '0086-110108-00022105-0002', '1', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('188', '2017-02-24 10:59:13', '2017-02-24 10:58:37', '0086-110108-00022105-01', '0086-110108-00022105-0003', '1', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('189', '2017-02-22 15:13:09', '2017-02-22 15:13:09', '0086-110108-00022105-01', '0086-110108-00022105-0004', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('190', '2016-09-19 14:25:32', '2016-06-01 14:14:05', '0086-110108-00022105-02', '0086-110108-00022105-0005', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('191', '2016-09-19 14:25:32', '2016-06-01 14:14:05', '0086-110108-00022105-02', '0086-110108-00022105-0006', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('192', '2016-09-19 14:25:32', '2016-06-01 14:14:05', '0086-110108-00022105-02', '0086-110108-00022105-0007', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('193', '2016-09-19 14:25:32', '2016-06-01 14:14:05', '0086-110108-00022105-02', '0086-110108-00022105-0008', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('194', '2016-09-19 14:25:32', '2016-06-01 14:14:05', '0086-110108-00022105-02', '0086-110108-00022105-0009', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('195', '2016-09-19 14:25:32', '2016-06-01 14:14:05', '0086-110108-00022105-02', '0086-110108-00022105-0010', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('196', '2016-09-19 14:25:32', '2016-06-01 14:14:05', '0086-110108-00022105-02', '0086-110108-00022105-0011', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('197', '2016-09-19 14:25:32', '2016-06-01 14:14:05', '0086-110108-00022105-02', '0086-110108-00022105-0012', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('198', '2016-09-19 14:25:32', '2016-06-01 14:14:05', '0086-110108-00022105-02', '0086-110108-00022105-0013', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('199', '2016-09-19 14:25:32', '2016-06-01 14:14:05', '0086-110108-00022105-02', '0086-110108-00022105-0014', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('200', '2016-09-19 14:25:32', '2016-06-01 14:14:05', '0086-110108-00022105-02', '0086-110108-00022105-0015', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('201', '2016-09-19 14:25:32', '2016-06-01 14:14:05', '0086-110108-00022105-02', '0086-110108-00022105-0016', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('202', '2016-09-19 14:25:32', '2016-06-01 14:14:05', '0086-110108-00022105-02', '0086-110108-00022105-0017', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('203', '2016-09-19 14:25:32', '2016-06-01 14:14:05', '0086-110108-00022105-02', '0086-110108-00022105-0018', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('204', '2016-09-19 14:25:32', '2016-06-01 14:14:05', '0086-110108-00022105-02', '0086-110108-00022105-0019', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('205', '2016-09-19 14:25:32', '2016-06-01 14:14:05', '0086-110108-00022105-02', '0086-110108-00022105-0020', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('206', '2016-09-19 14:25:32', '2016-06-01 14:14:05', '0086-110108-00022105-02', '0086-110108-00022105-0021', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('207', '2016-04-18 19:53:49', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0022', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('208', '2016-05-03 04:12:43', '2016-05-02 21:10:05', '0086-110108-00022105-01', '0086-110108-00022105-0023', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('209', '2016-04-18 19:53:49', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0024', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('210', '2016-04-18 19:53:49', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0025', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('211', '2016-04-18 19:53:49', '2016-04-08 19:19:37', '0086-110108-00022105-01', '0086-110108-00022105-0026', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('212', '2016-04-18 19:53:49', '2016-04-18 12:36:38', '0086-110108-00022105-01', '0086-110108-00022105-0027', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('213', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0028', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('214', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0029', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('215', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0030', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('216', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0031', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('217', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0032', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('218', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0033', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('219', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0034', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('220', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0035', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('221', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0036', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('222', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0037', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('223', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0038', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('224', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0039', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('225', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0040', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('226', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0041', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('227', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0042', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('228', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0043', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('229', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0044', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('230', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0045', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('231', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0046', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('232', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0047', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('233', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0048', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('234', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0049', '0', '22105', '0');
INSERT INTO `info_parkdata` VALUES ('235', '2015-12-24 10:30:53', '2016-04-07 10:58:41', '0086-110108-00022105-01', '0086-110108-00022105-0050', '0', '22105', '0');

-- ----------------------------
-- Table structure for info_parkdatahistory
-- ----------------------------
DROP TABLE IF EXISTS `info_parkdatahistory`;
CREATE TABLE `info_parkdatahistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime NOT NULL,
  `relayid` varchar(30) DEFAULT NULL,
  `record` longtext,
  `data` longtext,
  `parkid` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of info_parkdatahistory
-- ----------------------------

-- ----------------------------
-- Table structure for manhole_database_configure
-- ----------------------------
DROP TABLE IF EXISTS `manhole_database_configure`;
CREATE TABLE `manhole_database_configure` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `relayid` varchar(30) DEFAULT NULL,
  `sensorid` varchar(10) NOT NULL,
  `update_time` datetime NOT NULL,
  `acc_scale` int(11) NOT NULL,
  `acc_fchoice` int(11) NOT NULL,
  `acc_dlpf` int(11) NOT NULL,
  `gyo_scale` int(11) NOT NULL,
  `gyo_fchoice` int(11) NOT NULL,
  `gyo_dlpf` int(11) NOT NULL,
  `split_data_VAR_LEN` int(11) NOT NULL,
  `split_data_MEAN_WIDTH_1` int(11) NOT NULL,
  `split_data_MEAN_WIDTH_2` int(11) NOT NULL,
  `get_valid_data_WIDTH` int(11) NOT NULL,
  `split_data_WIDTH` int(11) NOT NULL,
  `update_middlevalue_cnt` int(11) NOT NULL,
  `listened_data_STABLECNT` int(11) NOT NULL,
  `listened_data_SLOP` int(11) NOT NULL,
  `listened_data_COUNT` int(11) NOT NULL,
  `open_angle_threshold` int(11) NOT NULL,
  `open_angle_cnt` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of manhole_database_configure
-- ----------------------------
INSERT INTO `manhole_database_configure` VALUES ('1', '1', '1', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('2', '1', '2', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('3', '1', '3', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('4', '1', '4', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('5', '1', '5', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('6', '1', '6', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('7', '1', '7', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('8', '1', '8', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('9', '1', '9', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('10', '1', '10', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('11', '2', '11', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('12', '2', '12', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('13', '2', '13', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('14', '2', '14', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('15', '2', '15', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('16', '2', '16', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('17', '2', '17', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('18', '2', '18', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('19', '2', '19', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('20', '2', '20', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('21', '3', '21', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('22', '3', '22', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('23', '3', '23', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('24', '3', '24', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('25', '3', '25', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('26', '3', '26', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('27', '3', '27', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('28', '3', '28', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('29', '3', '29', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_configure` VALUES ('30', '3', '30', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');

-- ----------------------------
-- Table structure for manhole_database_data
-- ----------------------------
DROP TABLE IF EXISTS `manhole_database_data`;
CREATE TABLE `manhole_database_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `relayid` varchar(30) NOT NULL,
  `sensorid` varchar(10) NOT NULL,
  `update_time` datetime NOT NULL,
  `processed_status` int(11) NOT NULL,
  `start_index` int(11) NOT NULL,
  `end_index` int(11) NOT NULL,
  `index_len` int(11) NOT NULL,
  `width` int(11) NOT NULL,
  `peakvalue` int(11) NOT NULL,
  `other_peak` int(11) NOT NULL,
  `other_var` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=129 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of manhole_database_data
-- ----------------------------
INSERT INTO `manhole_database_data` VALUES ('1', '1', '1', '2017-05-04 11:16:26', '0', '95', '276', '2', '94', '24291', '65294', '2724');
INSERT INTO `manhole_database_data` VALUES ('2', '1', '1', '2017-05-04 11:16:31', '0', '97', '252', '2', '99', '8852', '8618', '1105');
INSERT INTO `manhole_database_data` VALUES ('3', '1', '1', '2017-05-04 11:16:36', '0', '95', '391', '2', '184', '51364', '65535', '4133');
INSERT INTO `manhole_database_data` VALUES ('4', '1', '1', '2017-05-04 11:16:41', '0', '95', '799', '3', '609', '64249', '65535', '4144');
INSERT INTO `manhole_database_data` VALUES ('5', '1', '1', '2017-05-04 11:16:46', '0', '95', '313', '2', '102', '27197', '65535', '3164');
INSERT INTO `manhole_database_data` VALUES ('6', '1', '1', '2017-05-04 11:16:51', '0', '94', '249', '2', '108', '10729', '7731', '1049');
INSERT INTO `manhole_database_data` VALUES ('7', '1', '1', '2017-05-04 11:16:56', '0', '96', '308', '2', '79', '19872', '23689', '2154');
INSERT INTO `manhole_database_data` VALUES ('8', '1', '1', '2017-05-04 11:17:01', '0', '95', '647', '3', '451', '28759', '57753', '2306');
INSERT INTO `manhole_database_data` VALUES ('9', '1', '1', '2017-05-04 11:17:06', '0', '97', '255', '2', '101', '8312', '7669', '901');
INSERT INTO `manhole_database_data` VALUES ('10', '1', '1', '2017-05-04 11:17:11', '0', '95', '222', '2', '93', '2778', '986', '221');
INSERT INTO `manhole_database_data` VALUES ('11', '1', '1', '2017-05-04 11:17:16', '0', '96', '303', '2', '113', '20612', '43070', '1821');
INSERT INTO `manhole_database_data` VALUES ('12', '1', '1', '2017-05-04 11:17:21', '0', '96', '247', '2', '56', '13513', '24578', '1290');
INSERT INTO `manhole_database_data` VALUES ('13', '1', '1', '2017-05-04 11:17:26', '0', '95', '320', '2', '76', '37899', '65535', '3458');
INSERT INTO `manhole_database_data` VALUES ('14', '1', '1', '2017-05-04 11:17:31', '0', '95', '319', '2', '114', '21435', '18831', '1563');
INSERT INTO `manhole_database_data` VALUES ('15', '1', '1', '2017-05-04 11:17:36', '0', '97', '167', '2', '31', '2348', '980', '213');
INSERT INTO `manhole_database_data` VALUES ('16', '1', '1', '2017-05-04 11:17:41', '0', '95', '562', '3', '336', '23916', '51265', '1947');
INSERT INTO `manhole_database_data` VALUES ('17', '1', '1', '2017-05-04 11:17:46', '0', '80', '210', '2', '115', '2536', '1012', '256');
INSERT INTO `manhole_database_data` VALUES ('18', '1', '1', '2017-05-04 11:17:51', '0', '95', '296', '2', '102', '29231', '65535', '4350');
INSERT INTO `manhole_database_data` VALUES ('19', '1', '1', '2017-05-04 11:17:56', '0', '96', '272', '2', '65', '14665', '11719', '1168');
INSERT INTO `manhole_database_data` VALUES ('20', '1', '1', '2017-05-04 11:18:01', '0', '94', '266', '2', '117', '8402', '4016', '801');
INSERT INTO `manhole_database_data` VALUES ('21', '1', '1', '2017-05-04 11:18:06', '0', '95', '277', '2', '113', '21461', '65535', '2183');
INSERT INTO `manhole_database_data` VALUES ('22', '1', '1', '2017-05-04 11:18:11', '0', '94', '252', '2', '128', '3360', '918', '200');
INSERT INTO `manhole_database_data` VALUES ('23', '1', '1', '2017-05-04 11:18:16', '0', '95', '317', '2', '104', '36226', '65535', '3140');
INSERT INTO `manhole_database_data` VALUES ('24', '1', '1', '2017-05-04 11:18:21', '0', '96', '340', '2', '116', '16083', '26924', '1616');
INSERT INTO `manhole_database_data` VALUES ('25', '1', '1', '2017-05-04 11:18:26', '0', '96', '778', '2', '578', '49059', '65535', '3358');
INSERT INTO `manhole_database_data` VALUES ('26', '1', '1', '2017-05-04 11:18:31', '0', '96', '240', '2', '105', '8894', '10605', '1080');
INSERT INTO `manhole_database_data` VALUES ('27', '1', '1', '2017-05-04 11:18:36', '0', '95', '351', '2', '130', '28530', '58559', '2721');
INSERT INTO `manhole_database_data` VALUES ('28', '1', '1', '2017-05-04 11:18:41', '0', '96', '291', '2', '115', '27867', '65535', '3394');
INSERT INTO `manhole_database_data` VALUES ('29', '1', '1', '2017-05-04 11:18:46', '0', '95', '272', '2', '88', '35100', '40517', '2936');
INSERT INTO `manhole_database_data` VALUES ('30', '1', '1', '2017-05-04 11:18:51', '0', '95', '310', '2', '115', '22520', '14733', '1475');
INSERT INTO `manhole_database_data` VALUES ('31', '1', '1', '2017-05-04 11:18:56', '0', '95', '256', '2', '100', '4624', '1140', '321');
INSERT INTO `manhole_database_data` VALUES ('32', '1', '1', '2017-05-04 11:19:01', '0', '95', '312', '2', '101', '15511', '15571', '1281');
INSERT INTO `manhole_database_data` VALUES ('33', '1', '1', '2017-05-04 11:19:06', '0', '95', '662', '3', '471', '15621', '9921', '1056');
INSERT INTO `manhole_database_data` VALUES ('34', '1', '1', '2017-05-04 11:19:11', '0', '96', '302', '2', '117', '16523', '25971', '1505');
INSERT INTO `manhole_database_data` VALUES ('35', '1', '1', '2017-05-04 11:19:16', '0', '95', '272', '2', '126', '2960', '936', '226');
INSERT INTO `manhole_database_data` VALUES ('36', '1', '1', '2017-05-04 11:19:21', '0', '95', '305', '2', '122', '22249', '46269', '1802');
INSERT INTO `manhole_database_data` VALUES ('37', '1', '1', '2017-05-04 11:19:26', '0', '95', '315', '2', '109', '27303', '65535', '3772');
INSERT INTO `manhole_database_data` VALUES ('38', '1', '1', '2017-05-04 11:19:31', '0', '95', '286', '2', '100', '27671', '65535', '4297');
INSERT INTO `manhole_database_data` VALUES ('39', '1', '1', '2017-05-04 11:19:36', '0', '95', '307', '2', '104', '22434', '24312', '1560');
INSERT INTO `manhole_database_data` VALUES ('40', '1', '1', '2017-05-04 11:19:41', '0', '95', '312', '2', '90', '37840', '65491', '3089');
INSERT INTO `manhole_database_data` VALUES ('41', '1', '1', '2017-05-04 11:19:46', '0', '95', '471', '2', '251', '21772', '65535', '1754');
INSERT INTO `manhole_database_data` VALUES ('42', '1', '1', '2017-05-04 11:19:51', '0', '95', '333', '2', '128', '17732', '21315', '1535');
INSERT INTO `manhole_database_data` VALUES ('43', '1', '1', '2017-05-04 11:19:56', '0', '94', '436', '2', '197', '48178', '65535', '6552');
INSERT INTO `manhole_database_data` VALUES ('44', '1', '1', '2017-05-04 11:20:01', '0', '95', '293', '2', '102', '30200', '58647', '2936');
INSERT INTO `manhole_database_data` VALUES ('45', '1', '1', '2017-05-04 11:20:07', '0', '95', '285', '2', '83', '31702', '65535', '5102');
INSERT INTO `manhole_database_data` VALUES ('46', '1', '1', '2017-05-04 11:20:12', '0', '95', '295', '2', '94', '18613', '40330', '1927');
INSERT INTO `manhole_database_data` VALUES ('47', '1', '1', '2017-05-04 11:20:17', '0', '95', '301', '2', '102', '14007', '24071', '1435');
INSERT INTO `manhole_database_data` VALUES ('48', '1', '1', '2017-05-04 11:20:22', '0', '95', '320', '2', '171', '4241', '958', '276');
INSERT INTO `manhole_database_data` VALUES ('49', '1', '1', '2017-05-04 11:20:27', '0', '96', '295', '2', '104', '24585', '65302', '2652');
INSERT INTO `manhole_database_data` VALUES ('50', '1', '1', '2017-05-04 11:20:32', '0', '96', '326', '2', '104', '27871', '49658', '2370');
INSERT INTO `manhole_database_data` VALUES ('51', '1', '1', '2017-05-04 11:20:37', '0', '96', '325', '3', '106', '33126', '47671', '2925');
INSERT INTO `manhole_database_data` VALUES ('52', '1', '1', '2017-05-04 11:20:42', '0', '95', '294', '2', '63', '35035', '60895', '2593');
INSERT INTO `manhole_database_data` VALUES ('53', '1', '1', '2017-05-04 11:20:47', '0', '93', '422', '2', '220', '62711', '65535', '3960');
INSERT INTO `manhole_database_data` VALUES ('54', '1', '1', '2017-05-04 11:20:52', '0', '94', '299', '2', '101', '31850', '65535', '3120');
INSERT INTO `manhole_database_data` VALUES ('55', '1', '1', '2017-05-04 11:20:57', '0', '95', '309', '2', '81', '17267', '29844', '1667');
INSERT INTO `manhole_database_data` VALUES ('56', '1', '1', '2017-05-04 11:21:02', '0', '96', '332', '2', '100', '23643', '63619', '2710');
INSERT INTO `manhole_database_data` VALUES ('57', '1', '1', '2017-05-04 11:21:07', '0', '87', '286', '2', '109', '5322', '2993', '435');
INSERT INTO `manhole_database_data` VALUES ('58', '1', '1', '2017-05-04 11:21:12', '0', '96', '603', '4', '368', '55899', '65535', '5946');
INSERT INTO `manhole_database_data` VALUES ('59', '1', '1', '2017-05-04 11:21:17', '0', '95', '282', '2', '65', '33487', '65535', '3694');
INSERT INTO `manhole_database_data` VALUES ('60', '1', '1', '2017-05-04 11:21:22', '0', '95', '299', '2', '85', '22129', '65535', '3403');
INSERT INTO `manhole_database_data` VALUES ('61', '1', '1', '2017-05-04 11:24:47', '0', '97', '338', '2', '142', '12470', '22218', '1330');
INSERT INTO `manhole_database_data` VALUES ('62', '1', '1', '2017-05-04 11:24:52', '0', '95', '334', '2', '110', '16515', '23867', '1455');
INSERT INTO `manhole_database_data` VALUES ('63', '1', '1', '2017-05-04 11:24:57', '0', '95', '334', '2', '115', '17835', '62941', '3572');
INSERT INTO `manhole_database_data` VALUES ('64', '1', '1', '2017-05-04 11:25:02', '0', '95', '306', '2', '107', '16604', '31808', '1685');
INSERT INTO `manhole_database_data` VALUES ('65', '1', '1', '2017-05-04 11:25:07', '0', '96', '284', '2', '93', '29937', '65535', '3177');
INSERT INTO `manhole_database_data` VALUES ('66', '1', '1', '2017-05-04 11:25:12', '0', '96', '274', '2', '70', '23989', '57518', '3178');
INSERT INTO `manhole_database_data` VALUES ('67', '1', '1', '2017-05-04 11:25:17', '0', '95', '274', '2', '80', '11715', '12200', '1123');
INSERT INTO `manhole_database_data` VALUES ('68', '1', '1', '2017-05-04 11:25:22', '0', '96', '310', '2', '107', '24199', '65535', '2844');
INSERT INTO `manhole_database_data` VALUES ('69', '1', '1', '2017-05-04 11:25:27', '0', '95', '309', '2', '93', '35152', '62229', '2759');
INSERT INTO `manhole_database_data` VALUES ('70', '1', '1', '2017-05-04 11:25:33', '0', '95', '353', '2', '109', '26917', '65535', '3004');
INSERT INTO `manhole_database_data` VALUES ('71', '1', '1', '2017-05-04 11:25:38', '0', '95', '313', '2', '127', '40274', '65535', '4338');
INSERT INTO `manhole_database_data` VALUES ('72', '1', '1', '2017-05-04 11:25:43', '0', '95', '275', '2', '83', '33442', '65359', '3649');
INSERT INTO `manhole_database_data` VALUES ('73', '1', '1', '2017-05-04 11:25:48', '0', '96', '338', '2', '125', '10361', '13185', '1079');
INSERT INTO `manhole_database_data` VALUES ('74', '1', '1', '2017-05-04 11:25:53', '0', '96', '681', '3', '451', '34289', '65535', '3580');
INSERT INTO `manhole_database_data` VALUES ('75', '1', '1', '2017-05-04 11:25:58', '0', '94', '300', '2', '97', '22895', '55072', '2567');
INSERT INTO `manhole_database_data` VALUES ('76', '1', '1', '2017-05-04 11:26:03', '0', '94', '307', '2', '96', '21834', '53697', '2331');
INSERT INTO `manhole_database_data` VALUES ('77', '1', '1', '2017-05-04 11:26:08', '0', '95', '335', '2', '130', '23182', '39057', '2121');
INSERT INTO `manhole_database_data` VALUES ('78', '1', '1', '2017-05-04 11:26:13', '0', '95', '323', '2', '101', '34875', '38517', '2521');
INSERT INTO `manhole_database_data` VALUES ('79', '1', '1', '2017-05-04 11:26:18', '0', '95', '292', '2', '87', '36086', '65535', '5006');
INSERT INTO `manhole_database_data` VALUES ('80', '1', '1', '2017-05-04 11:26:23', '0', '94', '458', '2', '195', '53706', '65535', '5874');
INSERT INTO `manhole_database_data` VALUES ('81', '1', '1', '2017-05-04 11:26:28', '0', '95', '225', '2', '76', '4414', '961', '216');
INSERT INTO `manhole_database_data` VALUES ('82', '1', '1', '2017-05-04 11:26:33', '0', '96', '281', '2', '76', '25645', '56130', '2601');
INSERT INTO `manhole_database_data` VALUES ('83', '1', '1', '2017-05-04 11:26:38', '0', '95', '324', '2', '100', '24947', '44358', '2579');
INSERT INTO `manhole_database_data` VALUES ('84', '1', '1', '2017-05-04 11:26:43', '0', '95', '333', '2', '141', '12598', '14312', '1108');
INSERT INTO `manhole_database_data` VALUES ('85', '1', '1', '2017-05-04 11:26:48', '0', '80', '218', '2', '87', '3393', '955', '165');
INSERT INTO `manhole_database_data` VALUES ('86', '1', '1', '2017-05-04 11:26:53', '0', '95', '317', '2', '104', '29544', '65535', '3144');
INSERT INTO `manhole_database_data` VALUES ('87', '1', '1', '2017-05-04 11:26:58', '0', '96', '468', '2', '266', '40184', '65535', '2722');
INSERT INTO `manhole_database_data` VALUES ('88', '1', '1', '2017-05-04 11:27:03', '0', '95', '306', '2', '120', '21511', '35979', '2060');
INSERT INTO `manhole_database_data` VALUES ('89', '1', '1', '2017-05-04 11:27:08', '0', '85', '632', '3', '523', '3835', '993', '302');
INSERT INTO `manhole_database_data` VALUES ('90', '1', '1', '2017-05-04 11:27:13', '0', '96', '298', '2', '119', '25328', '65535', '2933');
INSERT INTO `manhole_database_data` VALUES ('91', '1', '1', '2017-05-04 11:27:18', '0', '96', '293', '2', '89', '31380', '65535', '3833');
INSERT INTO `manhole_database_data` VALUES ('92', '1', '1', '2017-05-04 11:27:23', '0', '96', '311', '2', '114', '25869', '65535', '2575');
INSERT INTO `manhole_database_data` VALUES ('93', '1', '1', '2017-05-04 11:27:28', '0', '95', '321', '2', '114', '16486', '20016', '1607');
INSERT INTO `manhole_database_data` VALUES ('94', '1', '1', '2017-05-04 11:27:33', '0', '95', '301', '2', '128', '28488', '59730', '2685');
INSERT INTO `manhole_database_data` VALUES ('95', '1', '1', '2017-05-04 11:27:38', '0', '95', '309', '2', '115', '24872', '36346', '2254');
INSERT INTO `manhole_database_data` VALUES ('96', '1', '1', '2017-05-04 11:27:43', '0', '95', '299', '2', '123', '23431', '65339', '2431');
INSERT INTO `manhole_database_data` VALUES ('97', '1', '1', '2017-05-04 11:27:48', '0', '95', '309', '2', '108', '16735', '11948', '1320');
INSERT INTO `manhole_database_data` VALUES ('98', '1', '1', '2017-05-04 11:27:53', '0', '95', '304', '2', '124', '25499', '31321', '1987');
INSERT INTO `manhole_database_data` VALUES ('99', '1', '1', '2017-05-04 11:27:58', '0', '95', '798', '5', '603', '39792', '65535', '3460');
INSERT INTO `manhole_database_data` VALUES ('100', '1', '1', '2017-05-04 11:28:03', '0', '96', '798', '4', '623', '32563', '65535', '3542');
INSERT INTO `manhole_database_data` VALUES ('101', '1', '1', '2017-05-04 11:28:08', '0', '97', '213', '2', '91', '2514', '899', '77');
INSERT INTO `manhole_database_data` VALUES ('102', '1', '1', '2017-05-04 11:28:13', '0', '95', '241', '2', '67', '11188', '13399', '1088');
INSERT INTO `manhole_database_data` VALUES ('103', '1', '1', '2017-05-04 11:28:18', '0', '96', '310', '2', '127', '17568', '22777', '1391');
INSERT INTO `manhole_database_data` VALUES ('104', '1', '1', '2017-05-04 11:28:23', '0', '95', '270', '2', '94', '12970', '15289', '1305');
INSERT INTO `manhole_database_data` VALUES ('105', '1', '1', '2017-05-04 11:28:28', '0', '96', '326', '2', '132', '37482', '65535', '3688');
INSERT INTO `manhole_database_data` VALUES ('106', '1', '1', '2017-05-04 11:28:33', '0', '94', '218', '2', '79', '2988', '965', '139');
INSERT INTO `manhole_database_data` VALUES ('107', '1', '1', '2017-05-04 11:28:38', '0', '94', '302', '2', '106', '19727', '60442', '2450');
INSERT INTO `manhole_database_data` VALUES ('108', '1', '1', '2017-05-04 11:28:43', '0', '95', '322', '2', '138', '37383', '52499', '4710');
INSERT INTO `manhole_database_data` VALUES ('109', '1', '1', '2017-05-04 11:28:48', '0', '96', '404', '2', '206', '26093', '65535', '3291');
INSERT INTO `manhole_database_data` VALUES ('110', '1', '1', '2017-05-04 11:28:53', '0', '95', '325', '3', '149', '24335', '65535', '3319');
INSERT INTO `manhole_database_data` VALUES ('111', '1', '1', '2017-05-04 11:28:58', '0', '95', '315', '2', '88', '32833', '55184', '2728');
INSERT INTO `manhole_database_data` VALUES ('112', '1', '1', '2017-05-04 11:29:03', '0', '94', '329', '2', '97', '29657', '65535', '3684');
INSERT INTO `manhole_database_data` VALUES ('113', '1', '1', '2017-05-04 11:29:08', '0', '95', '770', '2', '556', '30685', '65535', '3867');
INSERT INTO `manhole_database_data` VALUES ('114', '1', '1', '2017-05-04 11:29:13', '0', '95', '241', '2', '66', '5808', '5428', '572');
INSERT INTO `manhole_database_data` VALUES ('115', '1', '1', '2017-05-04 11:29:18', '0', '95', '289', '2', '50', '21148', '27075', '2037');
INSERT INTO `manhole_database_data` VALUES ('116', '1', '1', '2017-05-04 11:29:23', '0', '95', '455', '2', '275', '12553', '10550', '1042');
INSERT INTO `manhole_database_data` VALUES ('117', '1', '1', '2017-05-04 11:29:28', '0', '95', '309', '2', '106', '13210', '15832', '1270');
INSERT INTO `manhole_database_data` VALUES ('118', '1', '1', '2017-05-04 11:29:33', '0', '95', '332', '2', '99', '29105', '65535', '3636');
INSERT INTO `manhole_database_data` VALUES ('119', '1', '1', '2017-05-04 11:29:38', '0', '95', '261', '2', '85', '37100', '65535', '3787');
INSERT INTO `manhole_database_data` VALUES ('120', '1', '1', '2017-05-04 11:29:43', '0', '94', '458', '2', '235', '41410', '65535', '4017');
INSERT INTO `manhole_database_data` VALUES ('121', '1', '1', '2017-05-04 11:29:48', '0', '96', '310', '2', '98', '36580', '58879', '3288');
INSERT INTO `manhole_database_data` VALUES ('122', '1', '1', '2017-05-04 11:29:53', '0', '96', '302', '2', '109', '30477', '65535', '3783');
INSERT INTO `manhole_database_data` VALUES ('123', '1', '1', '2017-05-04 11:29:58', '0', '95', '647', '2', '103', '21906', '41655', '2386');
INSERT INTO `manhole_database_data` VALUES ('124', '1', '1', '2017-05-04 11:30:03', '0', '96', '315', '2', '136', '43443', '65535', '3688');
INSERT INTO `manhole_database_data` VALUES ('125', '1', '1', '2017-05-04 11:30:08', '0', '95', '249', '2', '92', '4771', '1379', '300');
INSERT INTO `manhole_database_data` VALUES ('126', '1', '1', '2017-05-04 11:30:13', '0', '95', '253', '2', '105', '3407', '1243', '303');
INSERT INTO `manhole_database_data` VALUES ('127', '1', '1', '2017-05-04 11:30:18', '0', '96', '333', '2', '102', '15856', '15779', '1255');
INSERT INTO `manhole_database_data` VALUES ('128', '1', '1', '2017-05-04 11:30:23', '0', '96', '312', '2', '126', '15796', '13982', '1352');

-- ----------------------------
-- Table structure for manhole_database_iptables
-- ----------------------------
DROP TABLE IF EXISTS `manhole_database_iptables`;
CREATE TABLE `manhole_database_iptables` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `relayid` varchar(30) DEFAULT NULL,
  `sensorid` varchar(10) NOT NULL,
  `net_address` varchar(6) DEFAULT NULL,
  `channel` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of manhole_database_iptables
-- ----------------------------
INSERT INTO `manhole_database_iptables` VALUES ('1', '1', '1', '1', '0');
INSERT INTO `manhole_database_iptables` VALUES ('2', '1', '2', '2', '0');
INSERT INTO `manhole_database_iptables` VALUES ('3', '1', '3', '3', '0');
INSERT INTO `manhole_database_iptables` VALUES ('4', '1', '4', '4', '0');
INSERT INTO `manhole_database_iptables` VALUES ('5', '1', '5', '5', '0');
INSERT INTO `manhole_database_iptables` VALUES ('6', '1', '6', '6', '0');
INSERT INTO `manhole_database_iptables` VALUES ('7', '1', '7', '7', '0');
INSERT INTO `manhole_database_iptables` VALUES ('8', '1', '8', '8', '0');
INSERT INTO `manhole_database_iptables` VALUES ('9', '1', '9', '9', '0');
INSERT INTO `manhole_database_iptables` VALUES ('10', '1', '10', '10', '0');
INSERT INTO `manhole_database_iptables` VALUES ('11', '2', '11', '1', '5');
INSERT INTO `manhole_database_iptables` VALUES ('12', '2', '12', '2', '5');
INSERT INTO `manhole_database_iptables` VALUES ('13', '2', '13', '3', '5');
INSERT INTO `manhole_database_iptables` VALUES ('14', '2', '14', '4', '5');
INSERT INTO `manhole_database_iptables` VALUES ('15', '2', '15', '5', '5');
INSERT INTO `manhole_database_iptables` VALUES ('16', '2', '16', '6', '5');
INSERT INTO `manhole_database_iptables` VALUES ('17', '2', '17', '7', '5');
INSERT INTO `manhole_database_iptables` VALUES ('18', '2', '18', '8', '5');
INSERT INTO `manhole_database_iptables` VALUES ('19', '2', '19', '9', '5');
INSERT INTO `manhole_database_iptables` VALUES ('20', '2', '20', '10', '5');
INSERT INTO `manhole_database_iptables` VALUES ('21', '3', '21', '1', '10');
INSERT INTO `manhole_database_iptables` VALUES ('22', '3', '22', '2', '10');
INSERT INTO `manhole_database_iptables` VALUES ('23', '3', '23', '3', '10');
INSERT INTO `manhole_database_iptables` VALUES ('24', '3', '24', '4', '10');
INSERT INTO `manhole_database_iptables` VALUES ('25', '3', '25', '5', '10');
INSERT INTO `manhole_database_iptables` VALUES ('26', '3', '26', '6', '10');
INSERT INTO `manhole_database_iptables` VALUES ('27', '3', '27', '7', '10');
INSERT INTO `manhole_database_iptables` VALUES ('28', '3', '28', '8', '10');
INSERT INTO `manhole_database_iptables` VALUES ('29', '3', '29', '9', '10');
INSERT INTO `manhole_database_iptables` VALUES ('30', '3', '30', '10', '10');

-- ----------------------------
-- Table structure for manhole_database_preconfigure
-- ----------------------------
DROP TABLE IF EXISTS `manhole_database_preconfigure`;
CREATE TABLE `manhole_database_preconfigure` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `relayid` varchar(30) DEFAULT NULL,
  `sensorid` varchar(10) NOT NULL,
  `update_time` datetime NOT NULL,
  `acc_scale` int(11) NOT NULL,
  `acc_fchoice` int(11) NOT NULL,
  `acc_dlpf` int(11) NOT NULL,
  `gyo_scale` int(11) NOT NULL,
  `gyo_fchoice` int(11) NOT NULL,
  `gyo_dlpf` int(11) NOT NULL,
  `split_data_VAR_LEN` int(11) NOT NULL,
  `split_data_MEAN_WIDTH_1` int(11) NOT NULL,
  `split_data_MEAN_WIDTH_2` int(11) NOT NULL,
  `get_valid_data_WIDTH` int(11) NOT NULL,
  `split_data_WIDTH` int(11) NOT NULL,
  `update_middlevalue_cnt` int(11) NOT NULL,
  `listened_data_STABLECNT` int(11) NOT NULL,
  `listened_data_SLOP` int(11) NOT NULL,
  `listened_data_COUNT` int(11) NOT NULL,
  `open_angle_threshold` int(11) NOT NULL,
  `open_angle_cnt` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of manhole_database_preconfigure
-- ----------------------------
INSERT INTO `manhole_database_preconfigure` VALUES ('1', '1', '1', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('2', '1', '2', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('3', '1', '3', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('4', '1', '4', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('5', '1', '5', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('6', '1', '6', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('7', '1', '7', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('8', '1', '8', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('9', '1', '9', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('10', '1', '10', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('11', '2', '11', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('12', '2', '12', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('13', '2', '13', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('14', '2', '14', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('15', '2', '15', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('16', '2', '16', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('17', '2', '17', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('18', '2', '18', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('19', '2', '19', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('20', '2', '20', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('21', '3', '21', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('22', '3', '22', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('23', '3', '23', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('24', '3', '24', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('25', '3', '25', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('26', '3', '26', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('27', '3', '27', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('28', '3', '28', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('29', '3', '29', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');
INSERT INTO `manhole_database_preconfigure` VALUES ('30', '3', '30', '2017-05-02 10:31:48', '0', '0', '5', '2', '1', '6', '2', '20', '10', '2', '20', '5000', '300', '400', '700', '30', '500');

-- ----------------------------
-- Table structure for manhole_database_sensor
-- ----------------------------
DROP TABLE IF EXISTS `manhole_database_sensor`;
CREATE TABLE `manhole_database_sensor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `relayid` varchar(30) DEFAULT NULL,
  `sensorid` varchar(30) NOT NULL,
  `update_time` datetime NOT NULL,
  `new` tinyint(1) NOT NULL,
  `open_time` datetime NOT NULL,
  `close_time` datetime NOT NULL,
  `status` varchar(10) NOT NULL,
  `period` varchar(10) NOT NULL,
  `working_mode` varchar(10) NOT NULL,
  `install_time` datetime NOT NULL,
  `max_speed` int(11) NOT NULL,
  `heavy_vehicle_p` int(11) NOT NULL,
  `light_vehicle_p` int(11) NOT NULL,
  `manhole_material` varchar(10) NOT NULL,
  `manhole_used_time` int(11) NOT NULL,
  `estimate_status` varchar(10) NOT NULL,
  `identified_status` double DEFAULT NULL,
  `heavy_vehicle_cnt` bigint(20) DEFAULT NULL,
  `middle_vehicle_cnt` bigint(20) DEFAULT NULL,
  `light_vehicle_cnt` bigint(20) DEFAULT NULL,
  `total_vehicle_cnt` bigint(20) DEFAULT NULL,
  `average_speed` int(11) DEFAULT NULL,
  `battery` double DEFAULT NULL,
  `open_status` varchar(10) DEFAULT NULL,
  `loss_status` varchar(10) DEFAULT NULL,
  `remarks` longtext,
  `error` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of manhole_database_sensor
-- ----------------------------
INSERT INTO `manhole_database_sensor` VALUES ('1', '1', '1', '2017-05-01 19:35:17', '1', '2017-05-04 12:00:00', '2017-05-04 13:00:00', 'open', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('2', '1', '2', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('3', '1', '3', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('4', '1', '4', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('5', '1', '5', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('6', '1', '6', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('7', '1', '7', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('8', '1', '8', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('9', '1', '9', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('10', '1', '10', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('11', '2', '11', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('12', '2', '12', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('13', '2', '13', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('14', '2', '14', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('15', '2', '15', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('16', '2', '16', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('17', '2', '17', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('18', '2', '18', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('19', '2', '19', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('20', '2', '20', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('21', '3', '21', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('22', '3', '22', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('23', '3', '23', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('24', '3', '24', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('25', '3', '25', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('26', '3', '26', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('27', '3', '27', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('28', '3', '28', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('29', '3', '29', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `manhole_database_sensor` VALUES ('30', '3', '30', '2017-05-01 19:35:17', '1', '2017-05-01 19:35:19', '2017-05-01 19:35:22', 'close', '120', 'mannual', '2017-05-01 19:35:34', '60', '1', '0', 'steel', '365', 'low', null, null, null, null, null, null, null, null, null, null, null);
