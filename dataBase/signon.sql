/*
 Navicat Premium Data Transfer

 Source Server         : aliMySQL
 Source Server Type    : MySQL
 Source Server Version : 80016
 Source Host           : rm-2ze61i7u6d7a3fwp9yo.mysql.rds.aliyuncs.com:3306
 Source Schema         : pidata

 Target Server Type    : MySQL
 Target Server Version : 80016
 File Encoding         : 65001

 Date: 14/05/2020 21:05:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for signon
-- ----------------------------
DROP TABLE IF EXISTS `signon`;
CREATE TABLE `signon`  (
  `username` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`username`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of signon
-- ----------------------------
INSERT INTO `signon` VALUES ('123', 'pbkdf2:sha256:150000$0bRh9FH6$25bfd72f85c7abb847ec98bc6f2df9ac7ed05f4ce02c81e4af81a3b9f569c517');
INSERT INTO `signon` VALUES ('321', 'pbkdf2:sha256:150000$K7d6hUuk$e5c220c0594d3aa466179b77fda85bb078d86b758e142b297762108a22376b93');
INSERT INTO `signon` VALUES ('cwj', 'pbkdf2:sha256:150000$UEhkEUhH$044da24daaa25640b2778fb05727c5e80cf46e95f15896d0981201b1d85d6875');
INSERT INTO `signon` VALUES ('hhh', 'pbkdf2:sha256:150000$6B7F3WMU$e545d97c343ce809281e6918ade69686d6a2e62b38bf1daebdf52b08f3f86a01');
INSERT INTO `signon` VALUES ('hhhh', 'pbkdf2:sha256:150000$T1dnZkUb$8f1bf5eec4f1f176549b634233281eccded767df832968ed307321e2fb74a393');
INSERT INTO `signon` VALUES ('hjr', 'pbkdf2:sha256:150000$cNY14t4s$70c343984465cefe00d6124c13d9e20d1b32d13a6769dabd280201d860055cb7');
INSERT INTO `signon` VALUES ('wfy', 'pbkdf2:sha256:150000$uNQfPc1o$c3650533c9d066fcac278ea9e10e116846bd96cc01072d2e151caca1432df9d6');
INSERT INTO `signon` VALUES ('zgy', 'pbkdf2:sha256:150000$anEZLEoO$634a021538ed177e05ee6855debd50e861aaa6822effbaf68e77435a7a7157e0');
INSERT INTO `signon` VALUES ('zlj', 'pbkdf2:sha256:150000$J1DD9nWP$6a9a95c0338a58e0aa204cf726d54296d51242af5d836a1c240c6c63a9c923c1');

SET FOREIGN_KEY_CHECKS = 1;
