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

 Date: 14/05/2020 21:06:21
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for vercode
-- ----------------------------
DROP TABLE IF EXISTS `vercode`;
CREATE TABLE `vercode`  (
  `user` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `time` datetime(0) DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0)
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of vercode
-- ----------------------------
INSERT INTO `vercode` VALUES ('321', 'k49c', '2020-05-08 22:22:40');

SET FOREIGN_KEY_CHECKS = 1;
