-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 23-Abr-2022 às 20:48
-- Versão do servidor: 10.4.22-MariaDB
-- versão do PHP: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `terraria`
--
CREATE DATABASE IF NOT EXISTS `terraria` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `terraria`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `sections`
--

CREATE TABLE `sections` (
  `id` varchar(5) NOT NULL,
  `header` varchar(30) NOT NULL,
  `section` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `weapons`
--

CREATE TABLE `weapons` (
  `id` int(11) NOT NULL,
  `identifier` varchar(5) NOT NULL,
  `name` varchar(50) NOT NULL,
  `damage` int(10) UNSIGNED NOT NULL,
  `knockback` int(10) UNSIGNED NOT NULL DEFAULT 0,
  `usetime` int(10) UNSIGNED NOT NULL,
  `rarity` enum('-1','0','1','2','3','4','5','6','7','8','9','10','11','12') NOT NULL DEFAULT '0',
  `sell` int(10) UNSIGNED NOT NULL DEFAULT 0,
  `hardmode` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `sections`
--
ALTER TABLE `sections`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `weapons`
--
ALTER TABLE `weapons`
  ADD PRIMARY KEY (`id`),
  ADD KEY `identifier` (`identifier`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `weapons`
--
ALTER TABLE `weapons`
  ADD CONSTRAINT `weapons_ibfk_1` FOREIGN KEY (`identifier`) REFERENCES `sections` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
