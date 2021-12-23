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

 Date: 14/05/2020 21:05:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `username` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `identity` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `phonenum` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `dorm` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `room` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `campus` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `rpiname` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT '',
  PRIMARY KEY (`username`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('123', 'costumer', '13323755686', '123', '123', '', NULL);
INSERT INTO `user` VALUES ('321', 'costumer', '+8613323755686', '321', '321', '', NULL);
INSERT INTO `user` VALUES ('cwj', 'costumer', '+8615243657949', '123', '123', '', 'raspberrypi');
INSERT INTO `user` VALUES ('hhh', 'costumer', '18091903321', '123', '123', '', NULL);
INSERT INTO `user` VALUES ('hhhh', 'costumer', '15808192311', '123', '123', '', NULL);
INSERT INTO `user` VALUES ('hjr', 'costumer', '18091903369', '123', '123', '', NULL);
INSERT INTO `user` VALUES ('wfy', 'costumer', '15808018765', '123', '123', '', NULL);
INSERT INTO `user` VALUES ('zgy', 'costumer', '+8618091903369', '123', '123', '', 'raspberrypi');
INSERT INTO `user` VALUES ('zlj', 'costumer', '+861836819600', '123', '123', '', NULL);

SET FOREIGN_KEY_CHECKS = 1;
