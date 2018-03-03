-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: hdb_data
-- ------------------------------------------------------
-- Server version	5.7.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `blocks`
--

DROP TABLE IF EXISTS `blocks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blocks` (
  `postal_code` int(10) unsigned NOT NULL,
  `block_number` varchar(15) NOT NULL,
  `project_name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  PRIMARY KEY (`postal_code`),
  KEY `project_name_idx` (`project_name`),
  CONSTRAINT `project_name` FOREIGN KEY (`project_name`) REFERENCES `project` (`town`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blocks`
--

LOCK TABLES `blocks` WRITE;
/*!40000 ALTER TABLE `blocks` DISABLE KEYS */;
/*!40000 ALTER TABLE `blocks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project` (
  `idproject` int(11) NOT NULL AUTO_INCREMENT,
  `town` varchar(255) NOT NULL,
  `project_name` varchar(255) NOT NULL,
  `room_type` varchar(255) NOT NULL,
  `last_updated` date DEFAULT NULL,
  `units_offered` int(11) NOT NULL,
  `hyperlink` varchar(999) DEFAULT NULL,
  PRIMARY KEY (`idproject`),
  KEY `town_name_idx` (`town`),
  KEY `project_hx` (`project_name`,`room_type`),
  CONSTRAINT `town_name` FOREIGN KEY (`town`) REFERENCES `town` (`town`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_hx_data`
--

DROP TABLE IF EXISTS `project_hx_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project_hx_data` (
  `idproject_hx_data` int(11) NOT NULL AUTO_INCREMENT,
  `project_name` varchar(255) NOT NULL,
  `room_type` varchar(255) NOT NULL,
  `units_available` int(11) NOT NULL,
  `chinese_quota` int(11) NOT NULL,
  `malay_quota` int(11) NOT NULL,
  `others_quota` int(11) NOT NULL,
  PRIMARY KEY (`idproject_hx_data`),
  KEY `fk_to_project_idx` (`project_name`,`room_type`),
  CONSTRAINT `fk_to_project` FOREIGN KEY (`project_name`, `room_type`) REFERENCES `project` (`project_name`, `room_type`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_hx_data`
--

LOCK TABLES `project_hx_data` WRITE;
/*!40000 ALTER TABLE `project_hx_data` DISABLE KEYS */;
/*!40000 ALTER TABLE `project_hx_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `town`
--

DROP TABLE IF EXISTS `town`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `town` (
  `town` varchar(255) NOT NULL,
  `entry_date` date DEFAULT NULL,
  PRIMARY KEY (`town`),
  UNIQUE KEY `TOWN` (`town`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `town`
--

LOCK TABLES `town` WRITE;
/*!40000 ALTER TABLE `town` DISABLE KEYS */;
INSERT INTO `town` VALUES ('Bukit Batok','2018-03-03'),('Geylang','2018-03-03'),('Punggol','2018-03-03'),('Sengkang','2018-03-03'),('Tampines','2018-03-03');
/*!40000 ALTER TABLE `town` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `units`
--

DROP TABLE IF EXISTS `units`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `units` (
  `postal_code` int(10) unsigned NOT NULL,
  `floor` int(11) NOT NULL,
  `unit` int(11) NOT NULL,
  `isTaken` int(11) DEFAULT NULL,
  `date_taken` date DEFAULT NULL,
  `date_updated` date DEFAULT NULL,
  PRIMARY KEY (`floor`,`unit`,`postal_code`),
  KEY `postal_code_idx` (`postal_code`),
  CONSTRAINT `postal_code` FOREIGN KEY (`postal_code`) REFERENCES `blocks` (`postal_code`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `units`
--

LOCK TABLES `units` WRITE;
/*!40000 ALTER TABLE `units` DISABLE KEYS */;
/*!40000 ALTER TABLE `units` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-04  0:44:30
