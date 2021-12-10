-- create Database user_login_details;
-- USE user_login_details;

-- CREATE TABLE `user_account` (
-- 	`id` int NOT NULL AUTO_INCREMENT,
--   	`username` varchar(50) NOT NULL,
--   	`password` varchar(50) NOT NULL,
--   	`email` varchar(60) NOT NULL,
--     PRIMARY KEY (`id`)
-- ) 

INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES (1, 'TestUsername', 'TestPassword', 'testemail@test.com');
