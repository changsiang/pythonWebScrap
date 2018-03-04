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
  `period_id` int(11) DEFAULT NULL,
  `town` varchar(255) NOT NULL,
  `project_name` varchar(255) NOT NULL,
  `room_type` varchar(255) NOT NULL,
  `last_updated` datetime DEFAULT NULL,
  `units_offered` int(11) NOT NULL,
  `hyperlink` varchar(999) DEFAULT NULL,
  PRIMARY KEY (`town`,`project_name`,`room_type`),
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
INSERT INTO `project` VALUES (201708,'Bukit Batok','Sky Vista  @  Bukit Batok  /  West Scape  @  Bukit Batok','2-Room Flexi (Short Lease/99-Year Lease)','2018-03-04 12:45:23',627,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Bukit%20Batok&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=2-Room%20Flexi%20(Short%20Lease/99-Year%20Lease)&ViewOption=A&dteBallot=201708&projName='),(201708,'Bukit Batok','Sky Vista  @  Bukit Batok  /  West Scape  @  Bukit Batok','3-Room (income ceiling $6000)','2018-03-04 12:45:23',252,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Bukit%20Batok&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=3-Room%20(income%20ceiling%20$6,000)&ViewOption=A&dteBallot=201708&projName='),(201708,'Bukit Batok','West Scape  @  Bukit Batok','4-Room','2018-03-04 12:45:23',340,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Bukit%20Batok&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=4-Room&ViewOption=A&dteBallot=201708&projName='),(201708,'Bukit Batok','West Scape  @  Bukit Batok','5-Room','2018-03-04 12:45:23',178,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Bukit%20Batok&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=5-Room&ViewOption=A&dteBallot=201708&projName='),(201711,'Geylang','Eunos Court','4-Room','2018-03-04 12:45:22',538,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Geylang&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=4-Room&ViewOption=A&dteBallot=201711&projName='),(201711,'Punggol','Northshore Edge','4-Room','2018-03-04 12:45:22',192,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Punggol&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=4-Room&ViewOption=A&dteBallot=201711&projName='),(201711,'Punggol','Northshore Edge','5-Room','2018-03-04 12:45:23',196,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Punggol&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=5-Room&ViewOption=A&dteBallot=201711&projName='),(201711,'Sengkang','Anchorvale Village  /  Fernvale Glades','2-Room Flexi (Short Lease/99-Year Lease)','2018-03-04 12:45:23',637,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Sengkang&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=2-Room%20Flexi%20(Short%20Lease/99-Year%20Lease)&ViewOption=A&dteBallot=201711&projName='),(201711,'Sengkang','Anchorvale Village  /  Fernvale Glades','3-Room (income ceiling $6000)','2018-03-04 12:45:23',207,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Sengkang&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=3-Room%20(income%20ceiling%20$6,000)&ViewOption=A&dteBallot=201711&projName='),(201711,'Sengkang','Fernvale Glades','4-Room','2018-03-04 12:45:23',390,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Sengkang&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=4-Room&ViewOption=A&dteBallot=201711&projName='),(201711,'Sengkang','Fernvale Glades','5-Room/3Gen','2018-03-04 12:45:23',273,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Sengkang&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=5-Room/3Gen&ViewOption=A&dteBallot=201711&projName='),(201708,'Sengkang','Rivervale Shores','2-Room Flexi (Short Lease/99-Year Lease)','2018-03-04 12:45:23',1074,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Sengkang&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=2-Room%20Flexi%20(Short%20Lease/99-Year%20Lease)&ViewOption=A&dteBallot=201708&projName='),(201708,'Sengkang','Rivervale Shores','3-Room (income ceiling $6000)','2018-03-04 12:45:23',174,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Sengkang&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=3-Room%20(income%20ceiling%20$6,000)&ViewOption=A&dteBallot=201708&projName='),(201708,'Sengkang','Rivervale Shores','4-Room','2018-03-04 12:45:24',678,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Sengkang&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=4-Room&ViewOption=A&dteBallot=201708&projName='),(201708,'Sengkang','Rivervale Shores','5-Room','2018-03-04 12:45:24',574,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Sengkang&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=5-Room&ViewOption=A&dteBallot=201708&projName='),(201711,'Tampines','Tampines Greencourt','2-Room Flexi (Short Lease/99-Year Lease)','2018-03-04 12:45:23',192,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Tampines&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=2-Room%20Flexi%20(Short%20Lease/99-Year%20Lease)&ViewOption=A&dteBallot=201711&projName='),(201711,'Tampines','Tampines Greencourt','3-Room','2018-03-04 12:45:23',186,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Tampines&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=3-ROOM&ViewOption=A&dteBallot=201711&projName='),(201711,'Tampines','Tampines Greencourt','4-Room','2018-03-04 12:45:23',1228,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Tampines&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=4-Room&ViewOption=A&dteBallot=201711&projName='),(201711,'Tampines','Tampines Greencourt','5-Room','2018-03-04 12:45:23',586,'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Tampines&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=5-Room&ViewOption=A&dteBallot=201711&projName=');
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
  `last_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`idproject_hx_data`),
  KEY `fk_to_project_idx` (`project_name`,`room_type`),
  CONSTRAINT `fk_to_project` FOREIGN KEY (`project_name`, `room_type`) REFERENCES `project` (`project_name`, `room_type`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_hx_data`
--

LOCK TABLES `project_hx_data` WRITE;
/*!40000 ALTER TABLE `project_hx_data` DISABLE KEYS */;
INSERT INTO `project_hx_data` VALUES (1,'Eunos Court','4-Room',170,107,122,44,'2018-03-04 12:45:22'),(2,'Northshore Edge','4-Room',170,37,146,23,'2018-03-04 12:45:22'),(3,'Northshore Edge','5-Room',173,43,144,23,'2018-03-04 12:45:23'),(4,'Anchorvale Village  /  Fernvale Glades','2-Room Flexi (Short Lease/99-Year Lease)',636,142,535,79,'2018-03-04 12:45:23'),(5,'Anchorvale Village  /  Fernvale Glades','3-Room (income ceiling $6000)',205,46,174,26,'2018-03-04 12:45:23'),(6,'Fernvale Glades','4-Room',390,88,330,51,'2018-03-04 12:45:23'),(7,'Fernvale Glades','5-Room/3Gen',271,59,229,33,'2018-03-04 12:45:23'),(8,'Tampines Greencourt','2-Room Flexi (Short Lease/99-Year Lease)',164,35,141,24,'2018-03-04 12:45:23'),(9,'Tampines Greencourt','3-Room',150,30,137,18,'2018-03-04 12:45:23'),(10,'Tampines Greencourt','4-Room',1171,269,990,147,'2018-03-04 12:45:23'),(11,'Tampines Greencourt','5-Room',538,125,453,72,'2018-03-04 12:45:23'),(12,'West Scape  @  Bukit Batok','4-Room',9,0,9,9,'2018-03-04 12:45:23'),(13,'West Scape  @  Bukit Batok','5-Room',11,2,11,9,'2018-03-04 12:45:23'),(14,'Sky Vista  @  Bukit Batok  /  West Scape  @  Bukit Batok','2-Room Flexi (Short Lease/99-Year Lease)',221,55,201,50,'2018-03-04 12:45:23'),(15,'Sky Vista  @  Bukit Batok  /  West Scape  @  Bukit Batok','3-Room (income ceiling $6000)',113,20,107,21,'2018-03-04 12:45:23'),(16,'Rivervale Shores','2-Room Flexi (Short Lease/99-Year Lease)',673,187,571,109,'2018-03-04 12:45:23'),(17,'Rivervale Shores','3-Room (income ceiling $6000)',49,0,49,9,'2018-03-04 12:45:24'),(18,'Rivervale Shores','4-Room',331,80,299,64,'2018-03-04 12:45:24'),(19,'Rivervale Shores','5-Room',299,93,257,51,'2018-03-04 12:45:24');
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

-- Dump completed on 2018-03-04 12:50:19
