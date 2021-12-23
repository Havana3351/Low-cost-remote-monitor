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

 Date: 14/05/2020 21:06:34
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for warning
-- ----------------------------
DROP TABLE IF EXISTS `warning`;
CREATE TABLE `warning`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data` json,
  `username` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of warning
-- ----------------------------
INSERT INTO `warning` VALUES (1, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `warning` VALUES (2, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `warning` VALUES (3, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `warning` VALUES (4, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `warning` VALUES (5, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `warning` VALUES (6, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `warning` VALUES (7, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `warning` VALUES (8, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `warning` VALUES (9, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `warning` VALUES (10, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `warning` VALUES (11, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `warning` VALUES (12, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `warning` VALUES (13, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `warning` VALUES (14, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `warning` VALUES (15, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `warning` VALUES (16, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `warning` VALUES (17, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `warning` VALUES (18, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', '123');
INSERT INTO `warning` VALUES (19, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', '123');
INSERT INTO `warning` VALUES (20, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', '123');

SET FOREIGN_KEY_CHECKS = 1;
