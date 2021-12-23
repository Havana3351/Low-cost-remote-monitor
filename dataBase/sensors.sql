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

 Date: 14/05/2020 21:05:11
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for sensors
-- ----------------------------
DROP TABLE IF EXISTS `sensors`;
CREATE TABLE `sensors`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data` json,
  `username` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 36 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sensors
-- ----------------------------
INSERT INTO `sensors` VALUES (1, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"32.46\"}]}', NULL);
INSERT INTO `sensors` VALUES (2, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"32.46\"}]}', NULL);
INSERT INTO `sensors` VALUES (3, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"32.46\"}]}', NULL);
INSERT INTO `sensors` VALUES (4, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"32.46\"}]}', NULL);
INSERT INTO `sensors` VALUES (5, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"32.46\"}]}', NULL);
INSERT INTO `sensors` VALUES (6, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"32.46\"}]}', NULL);
INSERT INTO `sensors` VALUES (7, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"32.46\"}]}', NULL);
INSERT INTO `sensors` VALUES (8, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"32.46\"}]}', NULL);
INSERT INTO `sensors` VALUES (9, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"32.46\"}]}', NULL);
INSERT INTO `sensors` VALUES (10, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"32.46\"}]}', NULL);
INSERT INTO `sensors` VALUES (11, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"32.46\"}]}', NULL);
INSERT INTO `sensors` VALUES (12, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"100\"}]}', NULL);
INSERT INTO `sensors` VALUES (13, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"100\"}]}', NULL);
INSERT INTO `sensors` VALUES (14, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"100\"}]}', NULL);
INSERT INTO `sensors` VALUES (15, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"100\"}]}', NULL);
INSERT INTO `sensors` VALUES (16, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `sensors` VALUES (17, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `sensors` VALUES (18, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `sensors` VALUES (19, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `sensors` VALUES (20, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `sensors` VALUES (21, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `sensors` VALUES (22, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `sensors` VALUES (23, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `sensors` VALUES (24, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `sensors` VALUES (25, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `sensors` VALUES (26, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `sensors` VALUES (27, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `sensors` VALUES (28, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `sensors` VALUES (29, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `sensors` VALUES (30, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `sensors` VALUES (31, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `sensors` VALUES (32, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', NULL);
INSERT INTO `sensors` VALUES (33, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', '123');
INSERT INTO `sensors` VALUES (34, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', '123');
INSERT INTO `sensors` VALUES (35, '{\"Humi\": [{\"Time\": 1579249151178, \"Value\": \"48\"}], \"Temp\": [{\"Time\": 1579249151178, \"Value\": \"50\"}]}', '123');

SET FOREIGN_KEY_CHECKS = 1;
