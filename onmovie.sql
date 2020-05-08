-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 08, 2020 at 01:40 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `onmovie`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `email` varchar(40) NOT NULL,
  `password` varchar(29) NOT NULL,
  `type` varchar(12) NOT NULL,
  `mobile` bigint(12) NOT NULL,
  `otp` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`email`, `password`, `type`, `mobile`, `otp`) VALUES
('a12@gmail.com', 'admin', 'Admin', 9876543456, 'None'),
('a@gmail.com', '123', 'Super-Admin', 1234567899, NULL),
('annn@gmail.com', 'admin', 'Admin', 7340761885, 'None'),
('aroraakshit544@gmail.com', '123', 'Super-Admin', 2147483647, NULL),
('batejurago@mailinator.com', 'Pa$$w0rd!', 'Super-Admin', 1448532130, NULL),
('c@gmail.com', '12345', 'Admin', 7340761885, NULL),
('celaqoge@mailinator.net', 'Pa$$w0rd!', 'Super-Admin', 7185254961, NULL),
('f@gmail.com', '12345', 'Admin', 7340761885, NULL),
('fypekac@mailinator.net', 'Pa$$w0rd!', 'Super-Admin', 9846685143, NULL),
('guco@mailinator.net', 'Pa$$w0rd!', 'Super-Admin', 5118596882, NULL),
('gugi@mailinator.net', 'Pa$$w0rd!', 'Super-Admin', 18671865761, NULL),
('h@gmail.com', '12345', 'Admin', 7340761885, NULL),
('hesex@mailinator.com', 'Pa$$w0rd!', 'Super-Admin', 16016466291, NULL),
('hoxabubi@mailinator.net', 'Pa$$w0rd!', 'Super-Admin', 1297687989, NULL),
('kudunote@mailinator.com', 'Pa$$w0rd!', 'Super-Admin', 1968405583, NULL),
('lapafaferi@mailinator.net', 'Pa$$w0rd!', 'Admin', 5375198622, NULL),
('pa@gmal.com', '123', 'Admin', 7340761885, NULL),
('recyf@mailinator.com', 'Pa$$w0rd!', 'Super-Admin', 16094991838, NULL),
('terubamewa@mailinator.net', 'Pa$$w0rd!', 'Admin', 3049911789, NULL),
('zyban@mailinator.com', 'Pa$$w0rd!', 'Super-Admin', 1136074877, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `billid` int(11) NOT NULL,
  `datetime` datetime NOT NULL,
  `email` varchar(100) NOT NULL,
  `total` float NOT NULL,
  `status` varchar(100) NOT NULL,
  `mobile` varchar(12) NOT NULL,
  `person1name` varchar(100) DEFAULT NULL,
  `person1image` text DEFAULT NULL,
  `person2name` varchar(100) DEFAULT NULL,
  `person2image` text DEFAULT NULL,
  `person3name` varchar(100) DEFAULT NULL,
  `person3image` text DEFAULT NULL,
  `person4name` varchar(100) DEFAULT NULL,
  `person4image` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`billid`, `datetime`, `email`, `total`, `status`, `mobile`, `person1name`, `person1image`, `person2name`, `person2image`, `person3name`, `person3image`, `person4name`, `person4image`) VALUES
(12, '2020-03-23 08:25:18', 'syco@mailinator.net', 1200, 'unsubscribe', '6948128972', 'Leo Rios', '336000022.jpg', 'Grady Potter', '290000016.jpg', 'Sierra Ray', '669000017.jpg', 'Medge Rivas', '16000188.jpg'),
(13, '2020-03-23 08:38:38', 'pusa@mailinator.net', 1000, 'subscribe', '6599624042', 'Winifred Long', '819000008.jpg', 'Lila David', '876000001.jpg', NULL, NULL, NULL, NULL),
(14, '2020-03-23 09:09:42', 'pusa@mailinator.net', 1000, 'subscribe', '6599624042', 'Brenna Jarvis', '901000604.jpg', 'Chase Knowles', '607000438.jpg', NULL, NULL, NULL, NULL),
(15, '2020-04-22 10:07:08', 'syco@mailinator.net', 1200, 'unsubscribe', '6948128972', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(16, '2020-04-22 11:09:37', 'wizyqyrumi@mailinator.com', 600, 'unsubscribe', '7589496215', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(17, '2020-04-22 11:12:26', 'wizyqyrumi@mailinator.com', 600, 'unsubscribe', '7589496215', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(18, '2020-04-23 03:26:37', 'joxa@mailinator.net', 1200, 'subscribe', '1379185734', 'Libby Mason', '9033.0_92532.jpg', 'Amaya Dillard', '4672.9_115834.jpg', 'Lawrence Rose', '7552.1_68291.jpg', 'Willow Sweet', '2131.9_270846.jpg'),
(19, '2020-04-23 03:34:40', 'hikitibi@mailinator.com', 600, 'unsubscribe', '4916326013', 'Kendall Cooley', '761.9_96870.jpg', NULL, NULL, NULL, NULL, NULL, NULL),
(20, '2020-05-08 11:24:56', 'ravikantgautamjazz@gmail.com', 600, 'subscribe', '6280276218', 'Ravi', '4412.9_93300.jpg', NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `catname` varchar(100) NOT NULL,
  `description` text NOT NULL,
  `photo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`catname`, `description`, `photo`) VALUES
('Movies', 'Nihil quia amet ass', '686insta1176.jpg'),
('Tv Shows', 'Expedita atque illum', '829insta1099.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `clientregistration`
--

CREATE TABLE `clientregistration` (
  `email` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `type` varchar(200) DEFAULT NULL,
  `mobile` varchar(12) NOT NULL,
  `otp` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `clientregistration`
--

INSERT INTO `clientregistration` (`email`, `name`, `password`, `type`, `mobile`, `otp`) VALUES
('hikitibi@mailinator.com', 'Joy Chapman', 'Pa$$w0rd!', 'unsubscribe', '4916326013', NULL),
('joxa@mailinator.net', 'Sasha Cline', 'Pa$$w0rd!', 'subscribe', '1379185734', NULL),
('pusa@mailinator.net', 'Ulla Landry', 'hello', 'subscribe', '6599624042', 'None'),
('ravikantgautamjazz@gmail.com', 'Ravi', 'ravi', 'subscribe', '6280276218', 'None'),
('syco@mailinator.net', 'Kasimir Berry', 'Pa$$w0rd!', 'unsubscribe', '6948128972', ''),
('wizyqyrumi@mailinator.com', 'Shellie Sutton', 'Pa$$w0rd!', 'unsubscribe', '7589496215', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `episodes`
--

CREATE TABLE `episodes` (
  `eid` int(11) NOT NULL,
  `vid` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` text NOT NULL,
  `videopath` text NOT NULL,
  `photo` text NOT NULL,
  `cast` text NOT NULL,
  `rating` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `episodes`
--

INSERT INTO `episodes` (`eid`, `vid`, `name`, `description`, `videopath`, `photo`, `cast`, `rating`) VALUES
(24, 30, 'Jack Shaffer', 'Nisi do consequatur? Officia dolor cupidatat non delectus, sed nemo deleniti mollitia dolores irure .', '886Nebula - 33154.mp4', '487insta155.jpg', 'Natalie Carney / Kapoor Wazir', 2),
(25, 30, 'Stacey Fuentes', 'Mollitia quis dolor dolores eiusmod sed pariatur. Sapiente unde ex repellendus. Dolor atque consequa.', '714Rabbit - 31604.mp4', '816insta595.jpg', 'Malin Akerman', 6),
(26, 29, 'Wyatt Espinoza', 'Et beatae culpa, culpa aliquid officiis beatae ducimus, unde voluptate mollit tempor iusto ut facili.', '642Nebula - 33154.mp4', '316insta957.jpg', 'Danny Denzongpa', 1),
(27, 25, 'Wang Hicks', 'Velit, illum, quisquam qui enim fugiat aut officia sed vitae sunt, ipsum explicabo. Est consequatur .', '652Yellow - 27803.mp4', '484insta712.jpg', 'Jake Gyllenhaal', 1),
(28, 25, 'Kirsten Leblanc', 'Elit, dolores nemo aut et et esse sed ratione molestias doloribus in qui quos rerum minima ea ea mol.', '213Child - 33631.mp4', '596insta1072.jpg', 'Hassan Shehreyar Yasin', 9),
(29, 29, 'Caleb Stevens', 'Placeat, explicabo. Id deserunt labore minima sint, ullamco elit, temporibus atque beatae corrupti, .', '331Beautiful - 33599.mp4', '967insta1556.jpg', 'Lara Stone', 6),
(30, 30, 'Odette Duke', 'Qui qui aspernatur ut facilis sint pariatur. Autem a qui maxime voluptatem voluptatem quis veritatis.', '496Sea - 24216.mp4', '702insta1471.jpg', 'Darsheel Safary', 1),
(31, 32, 'Brent Rosario', 'Ut quo ea eligendi porro error sed repudiandae qui dicta quo laborum adipisci consequatur? Quas dolo.', '72Forest - 17844.mp4', '274insta1334.jpg', 'Frankie Dettori', 7),
(32, 29, 'Nasim Terrell', 'Esse tempor nostrum laborum. Alias recusandae. Iste esse, esse, perspiciatis, molestias ducimus, ea .', '176Cliff - 22619.mp4', '474insta1490.jpg', 'KVIEW ALL', 7),
(33, 30, 'Kristen West', 'Exercitationem obcaecati sunt cupidatat lorem pariatur? Fuga. Vero voluptates doloribus sapiente aut.', '607Welcome - 24829.mp4', '888insta1635.jpg', 'Cash Warren,', 9),
(34, 29, 'Nelle Carrillo', 'Eveniet, dolores ratione ut fugiat, atque consectetur duis quos duis necessitatibus ex quis quia cup.', '726Nebula - 33154.mp4', '822insta1610.jpg', 'Wayne Rooney', 10),
(35, 29, 'Nelle Carrillo', 'Eveniet, dolores ratione ut fugiat, atque consectetur duis quos duis necessitatibus ex quis quia cup.', '688Nebula - 33154.mp4', '557insta660.jpg', 'Wayne Rooney', 10),
(37, 25, 'Carson Alston', 'Mollitia rerum dolore iure consequatur? Deserunt dolorum omnis anim quis enim debitis consequatur, d.', '893Welcome - 24829.mp4', '60insta491.jpg', 'Kanye West', 4),
(38, 30, 'Gemma Salas', 'Iste officia Nam ea expedita in nulla dolor rerum enim provident, sint, id dicta dolor in adipisicin.', '32Beautiful - 33599.mp4', '503insta234.jpg', 'Z', 3),
(40, 25, 'Levi Rush', 'Quo odio deserunt sunt quaerat debitis quo reprehenderit eiusmod consequat. Repellendus. Est quis di.', '656Nature - 29529.mp4', '493insta2817.jpg', 'Harper Seven Beckham', 10);

-- --------------------------------------------------------

--
-- Table structure for table `genre`
--

CREATE TABLE `genre` (
  `genreid` int(11) NOT NULL,
  `genre` varchar(50) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `genre`
--

INSERT INTO `genre` (`genreid`, `genre`, `description`) VALUES
(5, 'comedy', 'this contaims all sort of movie s'),
(6, 'romantic', 'contain all '),
(7, 'horror', 'contain all sort of videos '),
(9, 'action', 'hh'),
(11, 'Documentary', 'This contains the biography of legends'),
(13, 'Action & Adventure', 'Aliquid magnam in au'),
(16, 'Anime', 'Et laudantium hic d'),
(17, 'Children & Family', 'Dolorum odit dolore '),
(18, 'Classic', 'In aliqua Et aliqua'),
(19, 'Dramas', 'Accusamus incidunt '),
(20, 'Music', 'Dolore aut debitis a'),
(21, 'Romantic', 'Enim consequatur qua'),
(22, 'Sci-fi & Fantasy', 'Nulla nesciunt dolo'),
(23, 'Sports', 'Et possimus consequ'),
(24, 'Thrillers', 'Corrupti consequat'),
(27, 'Crime', 'Consequatur fugiat n');

-- --------------------------------------------------------

--
-- Table structure for table `rating`
--

CREATE TABLE `rating` (
  `ratingid` int(11) NOT NULL,
  `rating` float NOT NULL,
  `reviews` varchar(500) NOT NULL,
  `eid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `videos`
--

CREATE TABLE `videos` (
  `vid` int(11) NOT NULL,
  `title` varchar(60) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `catname` varchar(20) NOT NULL,
  `genreid` int(11) NOT NULL,
  `photo` varchar(50) NOT NULL,
  `movievideopath` varchar(700) DEFAULT NULL,
  `moviecast` varchar(500) DEFAULT NULL,
  `rating` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `videos`
--

INSERT INTO `videos` (`vid`, `title`, `description`, `catname`, `genreid`, `photo`, `movievideopath`, `moviecast`, `rating`) VALUES
(24, 'Salome', 'Incididunt sed ea recusandae. Rerum molestiae pariatur. Incididunt duis est quaerat tenetur dicta re.', 'Tv Shows', 6, '553insta8.jpg', '953Forest - 17844.mp4', 'Natalie Imbruglia', 3),
(25, 'Kauas pilvet karkaavat', 'Labore tempora amet, rerum temporibus minima qui ut lorem soluta quis pariatur. Quaerat cum ullam de.', 'Tv Shows', 20, '606insta151.jpg', '38Rabbit - 31604.mp4', 'Olivia Wilde', 3),
(26, 'Lone Star', 'Distinctio. Exercitation aliquip enim eum sed delectus, nostrud quaerat quis esse, voluptates tempor.', 'Movies', 23, '191insta191.jpg', '596Sea - 24216.mp4', 'Lata Mangeshkar', 10),
(27, 'Gadjo Dilo', 'Laboris fugit, veniam, minima nostrud vitae Nam mollitia harum ut maxime enim odit voluptatem, at co.', 'Movies', 27, '978insta5.jpg', '963United States - 33888.mp4', 'Carmen Electra', 9),
(28, 'The Velvet Vampire', 'Quasi ut minus facere consequat. Id, non magni laborum ut commodo ut labore ut quia dolor cillum Nam.', 'Movies', 24, '393insta208.jpg', '695Nebula - 33154.mp4', 'Hassan Shehreyar Yasin', 5),
(29, 'El barrendero', 'Eos consequuntur ab exercitation qui est earum repudiandae deserunt asperiores sunt, quia maxime et .', 'Tv Shows', 7, '752insta183.jpg', '530Sea - 24216.mp4', 'Z', 1),
(30, 'Beynelmilel', 'Odio rerum excepteur alias minus consequatur debitis eum deserunt aute aut molestias eligendi ullam .', 'Tv Shows', 11, '356insta357.jpg', '673Nature - 29529.mp4', 'Patrick Dempsey', 9),
(31, 'The Mad Miss Manton', 'Veniam, doloribus dolor saepe sit, rem rerum autem facilis ea accusantium similique sint doloremque .', 'Movies', 7, '992insta529.jpg', '989Rabbit - 31604.mp4', 'Adele', 6),
(32, 'Los girasoles ciegos', 'Rerum dolor necessitatibus repellendus. Eveniet, doloribus nesciunt, sed a ut repudiandae nisi asper.', 'Tv Shows', 9, '919insta134.jpg', '932Yellow - 27803.mp4', 'Kamal Haasan', 4),
(33, 'Warm Summer Rain', 'Earum ipsa, commodi ullamco impedit, sed illo minima officia excepteur eos dolore unde nemo pariatur.', 'Movies', 16, '956insta185.jpg', '419Cliff - 22619.mp4', 'Xavier Samuel', 2),
(34, 'Running Wild', 'Consectetur modi eius non ad architecto doloremque sed qui est consequat. Est, sit autem dolor ullam.', 'Tv Shows', 24, '967insta640.jpg', '609Sea - 24216.mp4', 'Cash Warren,', 9),
(35, 'A Phantasy', 'Est delectus, at ut aperiam cum proident, totam omnis nisi voluptate quia officiis eu eveniet, culpa.', 'Tv Shows', 11, '665insta767.jpg', '403Forest - 17844.mp4', 'Benji Madden', 7),
(36, 'Excess Baggage', 'Hic eiusmod sit, neque fuga. Ducimus, eu sit, quod neque nostrum ea porro voluptatem. Soluta sunt vo.', 'Movies', 17, '3insta16156.jpg', '339United States - 33888.mp4', 'Casey Affleck', 7),
(37, 'Fantastic Mr. Fox', 'Est aut sed ducimus, et veritatis aperiam rerum repudiandae incididunt in quo sed quis vel aliqua. P.', 'Movies', 16, '170insta700.jpg', '147Welcome - 24829.mp4', 'Zach Galifianakis', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`billid`),
  ADD KEY `email` (`email`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`catname`);

--
-- Indexes for table `clientregistration`
--
ALTER TABLE `clientregistration`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `episodes`
--
ALTER TABLE `episodes`
  ADD PRIMARY KEY (`eid`),
  ADD KEY `vid` (`vid`);

--
-- Indexes for table `genre`
--
ALTER TABLE `genre`
  ADD PRIMARY KEY (`genreid`);

--
-- Indexes for table `rating`
--
ALTER TABLE `rating`
  ADD PRIMARY KEY (`ratingid`);

--
-- Indexes for table `videos`
--
ALTER TABLE `videos`
  ADD PRIMARY KEY (`vid`),
  ADD KEY `catname` (`catname`),
  ADD KEY `genrename` (`genreid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bill`
--
ALTER TABLE `bill`
  MODIFY `billid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `episodes`
--
ALTER TABLE `episodes`
  MODIFY `eid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `genre`
--
ALTER TABLE `genre`
  MODIFY `genreid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `rating`
--
ALTER TABLE `rating`
  MODIFY `ratingid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `videos`
--
ALTER TABLE `videos`
  MODIFY `vid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bill`
--
ALTER TABLE `bill`
  ADD CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`email`) REFERENCES `clientregistration` (`email`);

--
-- Constraints for table `episodes`
--
ALTER TABLE `episodes`
  ADD CONSTRAINT `episodes_ibfk_1` FOREIGN KEY (`vid`) REFERENCES `videos` (`vid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `videos`
--
ALTER TABLE `videos`
  ADD CONSTRAINT `videos_ibfk_1` FOREIGN KEY (`catname`) REFERENCES `category` (`catname`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `videos_ibfk_2` FOREIGN KEY (`genreid`) REFERENCES `genre` (`genreid`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
