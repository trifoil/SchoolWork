-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Client: localhost
-- Généré le: Lun 07 Janvier 2019 à 12:15
-- Version du serveur: 5.6.12-log
-- Version de PHP: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `rohan`
--
CREATE DATABASE IF NOT EXISTS `rohan` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `rohan`;

-- --------------------------------------------------------

--
-- Structure de la table `commandants`
--

CREATE TABLE IF NOT EXISTS `commandants` (
  `id_commandant` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `commandant` varchar(255) NOT NULL,
  `mort` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_commandant`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=9 ;

--
-- Contenu de la table `commandants`
--

INSERT INTO `commandants` (`id_commandant`, `commandant`, `mort`) VALUES
(1, 'Erkenbrand', 0),
(2, 'Éomer', 0),
(3, 'Grimbold', 0),
(4, 'Gamlin', 0),
(5, 'Théoden', 0),
(6, 'Théodred', 1),
(7, 'Helm', 1),
(8, 'Eorl le jeune', 1);

-- --------------------------------------------------------

--
-- Structure de la table `renforts`
--

CREATE TABLE IF NOT EXISTS `renforts` (
  `id_renfort` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `clan` varchar(255) NOT NULL,
  `cavaliers` int(11) NOT NULL,
  `couleur_banniere` varchar(16) NOT NULL,
  `id_commandant` int(10) unsigned NOT NULL,
  `estimation` int(11) NOT NULL,
  PRIMARY KEY (`id_renfort`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=15 ;

--
-- Contenu de la table `renforts`
--

INSERT INTO `renforts` (`id_renfort`, `clan`, `cavaliers`, `couleur_banniere`, `id_commandant`, `estimation`) VALUES
(1, 'Cohorte d''Edoras', 1600, '#006600', 5, 2000),
(2, 'Cohorte de la Marche Est', 1500, '#006600', 2, 1500),
(3, 'Cohorte Ouest', 1200, '#336600', 3, 1500),
(4, 'Ouestfolde', 500, '#990000', 1, 1000),
(5, 'Fenmarche', 300, '#cc9900', 2, 500),
(6, 'Snowbourn', 0, '#666699', 1, 200),
(7, 'Cavaliers du Thrihyrne', 100, '#6666cc', 3, 300),
(8, 'Cavaliers de l''Ouest Emnet', 200, '#996600', 2, 250),
(9, 'Cavaliers de l''Est Emnet', 900, '#006600', 4, 1000),
(10, 'Amon Hen', 80, '#444444', 3, 100),
(11, 'Cavaliers du Célébrant', 40, '#226600', 4, 0),
(12, 'Lances écarlates', 60, '#990000', 3, 20),
(13, 'Capes noires', 30, '#111111', 2, 10),
(14, 'Estfolde', 400, '#006600', 3, 300);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
