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

 Date: 14/05/2020 21:04:54
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for sensorlist
-- ----------------------------
DROP TABLE IF EXISTS `sensorlist`;
CREATE TABLE `sensorlist`  (
  `username` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sensor` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`username`, `sensor`) USING BTREE,
  CONSTRAINT `username_fk` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sensorlist
-- ----------------------------
INSERT INTO `sensorlist` VALUES ('123', 'Humi');
INSERT INTO `sensorlist` VALUES ('123', 'Temp');

SET FOREIGN_KEY_CHECKS = 1;
