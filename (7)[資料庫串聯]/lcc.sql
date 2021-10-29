-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- 主機： localhost
-- 產生時間： 
-- 伺服器版本： 8.0.17
-- PHP 版本： 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `lcc`
--

-- --------------------------------------------------------

--
-- 資料表結構 `kind`
--

CREATE TABLE `kind` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `kind`
--

INSERT INTO `kind` (`id`, `name`) VALUES
(1, '手機'),
(2, '電視'),
(3, '食品');

-- --------------------------------------------------------

--
-- 資料表結構 `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `shop` varchar(15) NOT NULL,
  `name` varchar(100) NOT NULL,
  `price` int(11) NOT NULL,
  `photo_url` varchar(200) NOT NULL,
  `link` varchar(200) NOT NULL,
  `mount` int(11) NOT NULL,
  `create_date` date NOT NULL,
  `product_type` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `product`
--

INSERT INTO `product` (`id`, `shop`, `name`, `price`, `photo_url`, `link`, `mount`, `create_date`, `product_type`) VALUES
(31, 'Yahoo', 'Apple iPhone 13 256G 6.1吋智慧型手機', 29400, 'https://s.yimg.com/zp/MerchandiseImages/ca76480d7a-Gd-9685151.jpg', 'https://tw.buy.yahoo.com/gdsale/Apple-iPhone-13-256G-6-1吋智慧型手機-9685151.html', 0, '0000-00-00', 1),
(32, 'Yahoo', '2020 Apple iPhone 12 128G 6.1吋智慧型手機', 24500, 'https://s.yimg.com/zp/MerchandiseImages/6B05CC323D-SP-9028553.jpg', 'https://tw.buy.yahoo.com/gdsale/2020-Apple-iPhone-12-128G-6-1吋智慧型手機-9218365.html', 0, '0000-00-00', 1),
(33, 'Yahoo', 'Apple iPhone 13 mini 128G 5.4吋智慧型手機', 22900, 'https://s.yimg.com/zp/MerchandiseImages/390D50C611-SP-10375706.jpg', 'https://tw.buy.yahoo.com/gdsale/Apple-iPhone-13-mini-128G-5-4吋智慧型手機-9686616.html', 0, '0000-00-00', 1),
(34, 'Yahoo', 'Apple iPhone 11 64G 6.1吋智慧型手機', 16500, 'https://s.yimg.com/zp/MerchandiseImages/7dbe3bf824-Gd-9525429.jpg', 'https://tw.buy.yahoo.com/gdsale/Apple-iPhone-11-64G-6-1吋智-9525429.html', 0, '0000-00-00', 1),
(35, 'Yahoo', 'Apple iPhone 12 Pro 256G 6.1吋智慧型手機', 37400, 'https://s.yimg.com/zp/MerchandiseImages/205CCCE65E-SP-9490550.jpg', 'https://tw.buy.yahoo.com/gdsale/Apple-iPhone-12-Pro-256G-6-1吋智慧型手機-9383405.html', 0, '0000-00-00', 1),
(36, 'Yahoo', 'Apple iPhone 13 512G 6.1吋智慧型手機', 36400, 'https://s.yimg.com/zp/MerchandiseImages/ca76480d7a-Gd-9685149.jpg', 'https://tw.buy.yahoo.com/gdsale/Apple-iPhone-13-512G-6-1吋智慧型手機-9685149.html', 0, '0000-00-00', 1),
(37, 'Yahoo', 'Apple iPhone 13 128G MINI 5.4吋智慧型手機', 22900, 'https://s.yimg.com/zp/MerchandiseImages/3041AF5452-SP-10374417.jpg', 'https://tw.buy.yahoo.com/gdsale/Apple-iPhone-13-128G-MINI-5-4吋智慧型手機-9687210.html', 0, '0000-00-00', 1),
(38, 'Yahoo', 'Apple iPhone 12 Pro Max 128G 6.7吋智慧型手機', 37900, 'https://s.yimg.com/zp/MerchandiseImages/205CCCE65E-SP-9375435.jpg', 'https://tw.buy.yahoo.com/gdsale/Apple-iPhone-12-Pro-Max-128G-6-7吋智慧型手機-9341958.html', 0, '0000-00-00', 1),
(39, 'Yahoo', 'Apple iPhone 13 256G 6.1吋智慧型手機', 29400, 'https://s.yimg.com/zp/MerchandiseImages/3041AF5452-SP-10374220.jpg', 'https://tw.buy.yahoo.com/gdsale/Apple-iPhone-13-256G-6-1吋智慧型手機-9687220.html', 0, '0000-00-00', 1),
(40, 'Yahoo', 'Apple iPhone 13 mini 128G 5G手機', 22900, 'https://s.yimg.com/zp/MerchandiseImages/1F7ACA1678-SP-10376053.jpg', 'https://tw.buy.yahoo.com/gdsale/Apple-iPhone-13-mini-128G-5G手機-9687299.html', 0, '0000-00-00', 1),
(41, 'Yahoo', 'Apple iPhone 12 128G 6.1吋智慧型手機', 24500, 'https://s.yimg.com/zp/MerchandiseImages/E69C47DC52-SP-9007246.jpg', 'https://tw.buy.yahoo.com/gdsale/Apple-iPhone-12-128G-6-1吋智慧型手機-9330891.html', 0, '0000-00-00', 1),
(42, 'Yahoo', 'Apple iPhone 12 Pro Max 256G 6.7吋智慧型手機', 41400, 'https://s.yimg.com/zp/MerchandiseImages/205CCCE65E-SP-9375474.jpg', 'https://tw.buy.yahoo.com/gdsale/Apple-iPhone-12-Pro-Max-256G-6-7吋智慧型手機-9341957.html', 0, '0000-00-00', 1),
(43, 'Yahoo', 'Apple iPhone 13 256G', 29400, 'https://s.yimg.com/zp/MerchandiseImages/4FE60E80A2-SP-10392018.jpg', 'https://tw.buy.yahoo.com/gdsale/Apple-iPhone-13-256G-9692015.html', 0, '0000-00-00', 1),
(44, 'Yahoo', 'Apple iPhone 13 mini 512G 5.4吋 智慧型手機', 33400, 'https://s.yimg.com/zp/MerchandiseImages/ca76480d7a-Gd-9685203.jpg', 'https://tw.buy.yahoo.com/gdsale/Apple-iPhone-13-mini-512G-5-4吋-智慧型手機-9685203.html', 0, '0000-00-00', 1),
(45, 'Yahoo', 'Apple iPhone 13 256G 組合', 30400, 'https://s.yimg.com/zp/MerchandiseImages/4FE60E80A2-SP-10393916.jpg', 'https://tw.buy.yahoo.com/gdsale/Apple-iPhone-13-256G-組合-9692501.html', 0, '0000-00-00', 1);

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `kind`
--
ALTER TABLE `kind`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `kind`
--
ALTER TABLE `kind`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
