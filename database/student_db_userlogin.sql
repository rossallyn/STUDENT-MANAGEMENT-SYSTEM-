-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: student_db
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `userlogin`
--

DROP TABLE IF EXISTS `userlogin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userlogin` (
  `userid` int DEFAULT NULL,
  `name` text,
  `email` text,
  `username` text,
  `password` text,
  `register_date` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userlogin`
--

LOCK TABLES `userlogin` WRITE;
/*!40000 ALTER TABLE `userlogin` DISABLE KEYS */;
INSERT INTO `userlogin` VALUES (1,'Zia Abella','abellazia17@gmail.com','ziamaea','$5$rounds=535000$gVKy7uUhSTUx2rAZ$QVwXodHAQQiv6EkK.B/v5rHLde2SC19oaJmZoqu7DL7','2020-11-04 13:14:14'),(3,'Kezzia Abella','abellazia17@gmail.com','ziamaeaa','$5$rounds=535000$gVKy7uUhSTUx2rAZ$QVwXodHAQQiv6EkK.B/v5rHLde2SC19oaJmZoqu7DL7','2020-11-04 19:47:24'),(4,'MMMMMMMMMMMMMM','SSSSSSSSSSSSSSSS','WHATDASHIT','$5$rounds=535000$PrbrFgO54lUvYLXs$HoV93JsRyiNOOcgn59A.n4vhyisOJFDrGE6uVuGKJ2/','2020-11-13 13:54:29'),(5,'Jannessa','jannessa@gmail.com','jannessa_123','$5$rounds=535000$m7fvehkMyey.Gh9k$G5b8N6QhC10dbdPzJydxf3Qf/nqzhJzI0JueO2RZ3w/','2021-10-06 20:16:34'),(NULL,'Rosalyn','rosalync667@gmail.com','rossallyn','$5$rounds=535000$5A3nKT91eIeybbQD$//USd5cLt1XwqmZ6.ThaFN0gYFKcsIArvQpm3zFuKT3',NULL),(NULL,'Rosalyn','rosallyn@gmail.com','zozoqwe','$5$rounds=535000$Y1mXbHci7i8ZhZwO$O3PGEWm1N6Znc4Ld9qt/R8FztZsF6YytAQjHalAUec.',NULL),(NULL,'Kikianna','kiki@gmail.com','rosalyn123','$5$rounds=535000$omeCdqdiRR5aEHtC$YqFp4mCrISsuKjGFrcv3kEjcaye3TEwhaUjaz98MUt3',NULL);
/*!40000 ALTER TABLE `userlogin` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-31 11:32:49
