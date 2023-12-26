-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Client: localhost
-- Généré le: Mer 09 Janvier 2019 à 12:27
-- Version du serveur: 5.6.12-log
-- Version de PHP: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `dragons`
--
CREATE DATABASE IF NOT EXISTS `dragons` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `dragons`;

-- --------------------------------------------------------

--
-- Structure de la table `especes`
--

CREATE TABLE IF NOT EXISTS `especes` (
  `id_espece` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `espece` varchar(32) NOT NULL,
  PRIMARY KEY (`id_espece`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=18 ;

--
-- Contenu de la table `especes`
--

INSERT INTO `especes` (`id_espece`, `espece`) VALUES
(1, 'Dragon rouge'),
(2, 'Dragon noir'),
(3, 'Dragon vert'),
(4, 'Dragon d''or'),
(5, 'Dragon des profondeurs'),
(6, 'Hydre'),
(7, 'Dragon de bronze'),
(8, 'Dragon oriental'),
(9, 'Cauchemar oriental'),
(10, 'Dragon vert à 3 têtes'),
(11, 'Dragon souterrain'),
(12, 'Dragon des mers'),
(13, 'Dragon bleu à 4 têtes'),
(14, 'Dragon des abysses'),
(15, 'Dragon-rat'),
(16, 'Dragon cornu'),
(17, 'Dragon infernal');

-- --------------------------------------------------------

--
-- Structure de la table `observations`
--

CREATE TABLE IF NOT EXISTS `observations` (
  `id_observation` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id_espece` int(10) unsigned NOT NULL DEFAULT '0',
  `nombre` int(10) unsigned NOT NULL DEFAULT '1',
  `annee` int(11) NOT NULL,
  `saison` tinyint(3) unsigned NOT NULL,
  `nuit` tinyint(1) NOT NULL DEFAULT '0',
  `commentaire` text NOT NULL,
  PRIMARY KEY (`id_observation`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=35 ;

--
-- Contenu de la table `observations`
--

INSERT INTO `observations` (`id_observation`, `id_espece`, `nombre`, `annee`, `saison`, `nuit`, `commentaire`) VALUES
(1, 3, 1, 2012, 1, 0, ''),
(2, 14, 2, 2012, 2, 0, 'Observés au large'),
(3, 16, 1, 2012, 3, 1, 'Observé dans le ciel, volant vers le sud'),
(4, 4, 1, 2013, 1, 0, ''),
(5, 8, 1, 2013, 2, 0, ''),
(6, 8, 1, 2013, 2, 0, 'Sans doute le même que 6 jours auparavant'),
(7, 15, 3, 2013, 2, 1, ''),
(8, 12, 2, 2013, 3, 0, 'Au moins 2, peut-être 3'),
(9, 1, 1, 2013, 3, 0, 'Pas observé personnellement, mais observation certifiée par plusieurs personnes de confiance'),
(10, 13, 1, 2013, 4, 0, ''),
(11, 11, 1, 2014, 1, 0, 'Observation rapportée par les mineurs d''Ankor'),
(12, 3, 1, 2014, 1, 0, 'Le même qu''en 412 : il est revenu'),
(13, 8, 1, 2014, 3, 0, ''),
(14, 15, 2, 2014, 4, 0, ''),
(15, 15, 4, 2014, 4, 0, ''),
(16, 4, 1, 2015, 1, 0, 'A la tombée de la nuit'),
(17, 6, 1, 2015, 1, 1, ''),
(18, 17, 1, 2015, 3, 0, ''),
(19, 14, 1, 2015, 4, 0, ''),
(20, 7, 1, 2015, 4, 0, ''),
(21, 10, 1, 2016, 1, 0, ''),
(22, 3, 3, 2016, 1, 0, ''),
(23, 15, 3, 2016, 2, 1, ''),
(24, 13, 1, 2016, 4, 0, 'J''ai même compté 5 têtes'),
(25, 1, 1, 2016, 4, 0, ''),
(26, 7, 1, 2017, 3, 1, 'Difficile à dire de nuit, mais sans doute un dragon de bronze'),
(27, 9, 1, 2017, 2, 0, ''),
(28, 12, 1, 2017, 4, 0, ''),
(29, 3, 1, 2018, 1, 0, ''),
(30, 16, 2, 2018, 1, 0, ''),
(31, 14, 1, 2018, 2, 0, ''),
(32, 9, 1, 2018, 3, 0, ''),
(33, 6, 3, 2018, 4, 0, ''),
(34, 2, 1, 2018, 4, 0, '');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
