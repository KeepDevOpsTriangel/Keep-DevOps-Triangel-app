CREATE TABLE IF NOT EXISTS `state` (
  `id` int NOT NULL AUTO_INCREMENT,
  `updated` timestamp NOT NULL DEFAULT (now()) ON UPDATE CURRENT_TIMESTAMP,
  `state` int DEFAULT '0',
  `note` varchar(150) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 2 DEFAULT CHARSET = utf8mb3 COLLATE = utf8mb3_spanish_ci;
INSERT INTO `state` (`id`, `updated`, `state`, `note`)
VALUES (1, '2024-01-17 17:04:55', 0, 'MANTENIMIENTO');
CREATE TABLE IF NOT EXISTS `options` (
  `id` int NOT NULL AUTO_INCREMENT,
  `updated` timestamp NOT NULL DEFAULT (now()) ON UPDATE CURRENT_TIMESTAMP,
  `opt` varchar(20) COLLATE utf8mb3_spanish_ci NOT NULL,
  `text` varchar(255) COLLATE utf8mb3_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 5 DEFAULT CHARSET = utf8mb3 COLLATE = utf8mb3_spanish_ci;
INSERT INTO `options` (`id`, `updated`, `opt`, `text`)
VALUES (
    1,
    '2024-01-17 17:05:15',
    'Que soy?',
    'Soy un asistente virtual basado en IA'
  ),
  (
    2,
    '2024-01-17 17:05:25',
    'Donde estoy?',
    'Vivo en un cloud donde se despliegan todos mis recursos'
  ),
  (
    3,
    '2024-01-17 17:05:34',
    'Que hago?',
    'Resuelvo las dudas que me preguntas basandome en mis conocimientos adquiridos'
  ),
  (
    4,
    '2024-01-17 17:05:41',
    'Como funciono?',
    'Muy simple, preguntame y yo te respondo'
  );
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `updated` timestamp NOT NULL DEFAULT (now()) ON UPDATE CURRENT_TIMESTAMP,
  `first_name` varchar(150) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `chatid` varchar(20) COLLATE utf8mb3_spanish_ci NOT NULL,
  `username` varchar(150) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `authorized` int DEFAULT '1',
  `pending` int DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb3 COLLATE = utf8mb3_spanish_ci;
INSERT INTO `users`
VALUES (
    1,
    '2024-01-22 09:12:36',
    'RAFAEL',
    '409645379',
    'RAFAELTORICES',
    1,
    0
  ),
  (
    2,
    '2024-01-22 11:08:06',
    'RAFAEL',
    '590541179',
    'RafaelTor',
    1,
    0
  ),
  (
    3,
    '2024-01-18 10:41:41',
    'yul',
    '310763395',
    'Yuldi8',
    1,
    0
  ),
  (
    4,
    '2024-01-18 12:23:23',
    'albertito',
    '1328819893',
    'atunconpann',
    1,
    0
  ),
  (
    5,
    '2024-01-22 09:01:41',
    'jeff',
    '1240875922',
    'Jeeffs',
    1,
    0
  );
-- Volcando estructura para tabla devops.mensajes
CREATE TABLE IF NOT EXISTS `messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `updated` timestamp NOT NULL DEFAULT (now()) ON UPDATE CURRENT_TIMESTAMP,
  `first_name` varchar(150) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `chatid` varchar(20) COLLATE utf8mb3_spanish_ci NOT NULL,
  `username` varchar(150) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `message` text COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb3 COLLATE = utf8mb3_spanish_ci;
CREATE TABLE IF NOT EXISTS `context` (
  `id` int NOT NULL AUTO_INCREMENT,
  `updated` timestamp NOT NULL DEFAULT (now()) ON UPDATE CURRENT_TIMESTAMP,
  `context` text COLLATE utf8mb3_spanish_ci,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb3 COLLATE = utf8mb3_spanish_ci;
INSERT INTO `context` (`id`, `updated`, `context`)
VALUES (
    1,
    '2024-01-18 12:23:23',
    'Eres un asistente virtual sobre servicios IT de informatica llamado TriangleApp que responde a preguntas que esten solo y exlusivamente relacionadas con servicios IT de informatica.Las respuestas que da son lo mas cortas,
    precisas y resumidas posible.'
  );