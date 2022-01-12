-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 12, 2022 at 06:55 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `best_hotels`
--

CREATE TABLE `best_hotels` (
  `id` bigint(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `location` varchar(255) NOT NULL,
  `neighborhoodName` varchar(255) DEFAULT NULL,
  `price` varchar(255) NOT NULL,
  `stars` varchar(255) DEFAULT NULL,
  `score` varchar(255) DEFAULT NULL,
  `amenities` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `hotel_deals`
--

CREATE TABLE `hotel_deals` (
  `id` bigint(255) NOT NULL,
  `place` varchar(255) NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `location` varchar(255) NOT NULL,
  `price` varchar(255) NOT NULL,
  `stars` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `landmark_hotels`
--

CREATE TABLE `landmark_hotels` (
  `id` bigint(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `location` varchar(255) NOT NULL,
  `landmark` varchar(255) NOT NULL,
  `neighborhoodName` varchar(255) DEFAULT NULL,
  `price` varchar(255) NOT NULL,
  `stars` varchar(255) DEFAULT NULL,
  `score` varchar(255) DEFAULT NULL,
  `amenities` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `best_hotels`
--
ALTER TABLE `best_hotels`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hotel_deals`
--
ALTER TABLE `hotel_deals`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `landmark_hotels`
--
ALTER TABLE `landmark_hotels`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `best_hotels`
--
ALTER TABLE `best_hotels`
  MODIFY `id` bigint(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `hotel_deals`
--
ALTER TABLE `hotel_deals`
  MODIFY `id` bigint(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `landmark_hotels`
--
ALTER TABLE `landmark_hotels`
  MODIFY `id` bigint(255) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
