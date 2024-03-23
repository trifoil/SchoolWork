-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Client: localhost
-- Généré le: Lun 22 Janvier 2018 à 15:23
-- Version du serveur: 5.6.12-log
-- Version de PHP: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `vikings`
--
CREATE DATABASE IF NOT EXISTS `vikings` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `vikings`;

-- --------------------------------------------------------

--
-- Structure de la table `chefs`
--

CREATE TABLE IF NOT EXISTS `chefs` (
  `id_chef` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `titre` varchar(255) NOT NULL,
  `icone` varchar(32) NOT NULL,
  PRIMARY KEY (`id_chef`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

--
-- Contenu de la table `chefs`
--

INSERT INTO `chefs` (`id_chef`, `nom`, `titre`, `icone`) VALUES
(1, 'Ingvar', 'l''intrépide', 'duel'),
(2, 'Rudolf', 'le borgne', 'corne'),
(3, 'Alrik', 'double-hache', 'hache2'),
(4, 'Drifa', 'l''égorgeuse', 'valkirie'),
(5, 'Rorik', 'panse-de-fer', 'jambon'),
(6, 'Munrod', 'le serpent', 'lances');

-- --------------------------------------------------------

--
-- Structure de la table `pillages`
--

CREATE TABLE IF NOT EXISTS `pillages` (
  `id_pillage` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `annee` int(10) unsigned NOT NULL,
  `saison` tinyint(255) unsigned NOT NULL,
  `lieu` varchar(255) NOT NULL,
  `id_chef` int(10) unsigned NOT NULL,
  `icone` varchar(32) NOT NULL,
  `drakkars` int(10) unsigned NOT NULL,
  `naufrages` int(10) unsigned NOT NULL,
  `butin` int(10) unsigned NOT NULL COMMENT '(estimation en pièces d''or)',
  `esclaves` int(10) unsigned NOT NULL,
  `vikings` int(10) unsigned NOT NULL,
  `pertes` int(10) unsigned NOT NULL,
  `météo` varchar(255) NOT NULL,
  `commentaire` text NOT NULL,
  PRIMARY KEY (`id_pillage`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=26 ;

--
-- Contenu de la table `pillages`
--

INSERT INTO `pillages` (`id_pillage`, `annee`, `saison`, `lieu`, `id_chef`, `icone`, `drakkars`, `naufrages`, `butin`, `esclaves`, `vikings`, `pertes`, `météo`, `commentaire`) VALUES
(1, 812, 2, 'Novgorod', 1, '', 4, 0, 12000, 18, 62, 8, 'pluie', 'Mycket guld. Mycket alkohol. Många kvinnor. Trevlig kamp, vi slog dem väl. Nästa gång, tänka på att lämna några levande.'),
(2, 813, 2, 'York', 1, 'tour', 3, 0, 0, 0, 51, 6, 'nuages', 'Staden är för mycket befäst. Vi går norrut.'),
(3, 813, 2, 'Écosse', 1, '', 3, 0, 600, 12, 45, 0, 'pluie', 'Inte mycket guld. Men vi har kunnat hämnas våra fallna män i York genom att kasta skottens blod.'),
(4, 813, 3, 'Gaule', 3, 'biere', 2, 0, 0, 0, 28, 0, 'pluie', 'Vi promenerade i regnet i flera dagar. Det finns bara träsken. Slutligen bjudde goda bönder oss att äta vildsvin vid elden. Vi berättade inte för dem att vi var vikingar. Vi drack mycket öl, då lämnade vi med drickarna.'),
(5, 814, 0, 'Côtes Est de la Baltique', 1, '', 2, 0, 300, 4, 31, 1, 'neige', 'Denna vinterexpedition var inte en bra idé. Vi borde ha stannat varmt med våra kvinnor.'),
(6, 814, 1, 'Bretagne', 1, '', 5, 0, 3500, 12, 74, 0, 'pluie', 'Slavarna var inte tillräckligt starka. Hälften av det kastades överbord på vägen tillbaka.'),
(7, 814, 1, 'Normandie', 1, '', 5, 0, 1000, 6, 74, 0, 'soleil', 'Mycket mat. Många alkoholhaltiga drycker. Inte mycket guld.'),
(8, 814, 1, 'Bretagne', 1, '', 5, 0, 200, 3, 74, 1, 'soleil', 'På vägen tillbaka gick vi tillbaka till Bretagne eftersom Ulf hade förlorat sin fars öxa. Han berättade för det för dagar. Ulf hittade äntligen sin yxa, men det övergavs i Bretagne, så han uppblåste oss.'),
(9, 814, 3, 'Écosse', 5, '', 3, 0, 800, 9, 53, 2, 'nuages', 'Dessa män är fortfarande svaga. Utan sina stenmurar vet de inte hur man ska slåss. Om Thor kunde bryta ner sina väggar skulle vi ta större städer och rikare lojaler!'),
(10, 815, 1, 'York', 1, 'tour', 6, 0, 9000, 22, 83, 14, 'soleil', 'Jag är Ingvar Jarl och ingen fästning kan motstå mig!'),
(11, 815, 2, 'Normandie', 1, '', 5, 0, 2400, 16, 75, 3, 'soleil', 'Odin bevittnar vikarnas mod!'),
(12, 815, 3, 'Shetland', 1, '', 3, 2, 200, 0, 52, 27, 'nuages', 'Förbannad storm! Vi förlorade 2 drakkars. Det var omöjligt att ta tillbaka slavar eftersom den sista långskikten var för upptagen. Denna öfolk kommer länge komma ihåg vår ilska!'),
(13, 816, 1, 'Novgorod', 1, '', 4, 0, 5500, 16, 61, 7, 'soleil', 'Utan Gotlands kust kom vi över en ormslang längre än två drakkars. Den mäktiga varelsen tittade på vart och ett av våra fartyg och försvann i djupet.'),
(14, 816, 2, 'Amérique du Nord', 2, 'drakkar', 2, 1, 50, 0, 28, 4, 'soleil', 'Det var verkligen inte Skottland. Männen träffades var vilda och klädda med endast djurskinn. De hade inte guld men deras land var enormt och rik på mat. Vid återkomsten bröt en storm ett av våra skepp och flera män försvann till sjöss.'),
(15, 817, 1, 'Angleterre', 1, '', 3, 0, 3200, 10, 51, 5, 'nuages', 'England är ett rikt land om du vet var du ska leta efter skatterna. Engelska soldater är små och långsamma. Deras rustning är för tung. Endast deras kavalleri är en verklig fara för vikingarna.'),
(16, 817, 1, 'Normandie', 1, '', 3, 0, 1400, 15, 46, 2, 'soleil', 'Män törstig för blod och plundring. Byarna i Normandie var inte så rika men lätta att plundra.'),
(17, 817, 2, 'Irlande', 4, '', 2, 0, 2400, 6, 32, 2, 'nuages', 'Drifa Slayer har samlat en expedition för att resa västerut. Irlands plundring var lätt och fruktbart. Irländare kommer ihåg Drifa'),
(18, 818, 2, 'Angleterre', 1, '', 3, 0, 4600, 3, 54, 8, 'pluie', 'Regnet rensar blodet. Men de döda stiger inte upp.'),
(19, 818, 3, 'Irlande', 4, '', 2, 2, 0, 0, 35, 35, 'pluie', 'De kom aldrig tillbaka. Jag sa till honom att irländarna var för farliga att gå tillbaka så snabbt.'),
(20, 819, 1, 'Bretagne', 1, '', 4, 0, 3200, 6, 74, 2, 'nuages', 'Vi gick tillbaka till var vi lämnade Ulf 5 år sedan. Han var inte längre där. Vi plundrade tre Bretonska byar genom att söka efter det.'),
(21, 819, 1, 'York', 1, '', 4, 1, 300, 2, 72, 22, 'nuages', 'Lean booty men minnesvärd kamp. Gudarna kommer ihåg det. Män också.'),
(22, 819, 1, 'Gaule', 1, '', 3, 0, 1000, 8, 50, 0, 'pluie', 'Fartygen var för upptagna. Vi var tvungna att dricka 3 fat öl och ge upp 10 slavar innan vi gick tillbaka till havet.'),
(23, 819, 3, 'Côtes Est de la Baltique', 3, '', 1, 0, 300, 1, 19, 12, 'pluie', 'Pillage var lätt. Inte mycket guld men mycket mat och verktyg. Vid återvändande störde ryttare i rustning och beväpnade med pilhuvud oss. Tolv av oss dog och några av krigslagen var kvar.'),
(24, 820, 2, 'Irlande', 1, 'mjolnir', 5, 0, 3000, 12, 80, 15, 'soleil', 'Jag såg den molnformade hammaren i himlen. Thor skickade ett tecken. Blod kallar blod. hädanefter hämnas våra döda.'),
(25, 819, 2, 'Nord', 6, 'drakkar', 1, 0, 0, 0, 8, 1, 'nuages', 'I åratal önskade Munrod en expedition norr om Vikinglandet. Ingvar ville inte ha det och skickade Munrod med en enda drakar och 7 män att besöka norr. De såg renar, valar och valor. Efter den sista frusna marken ville Munrod fortsätta längre norrut. Hans män kastade honom överbord och återvände.');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
