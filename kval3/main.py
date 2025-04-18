import sqlite3
db = sqlite3.connect("carV2.db")
cursor = db.cursor()
s = """

-- Структура таблицы `booking`
--

CREATE TABLE `booking` (
  `id_booking` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `id_user` int(11) NOT NULL,
  `id_car` int(11) NOT NULL,
  `id_status` int(11) NOT NULL,
  `booking_date` date NOT NULL,
  `status_comment` text  DEFAULT NULL
);

--
-- Дамп данных таблицы `booking`
--

INSERT INTO `booking` (`id_booking`, `id_user`, `id_car`, `id_status`, `booking_date`, `status_comment`) VALUES
(1, 1, 1, 2, '2025-01-25', NULL),
(2, 1, 2, 1, '2025-02-01', NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `car`
--

CREATE TABLE `car` (
  `id_car` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `brand` varchar(50)  NOT NULL,
  `model` varchar(50) NOT NULL,
  `year` int(4) NOT NULL,
  `registration_number` varchar(10)  NOT NULL
);

--
-- Дамп данных таблицы `car`
--

INSERT INTO `car` (`id_car`, `brand`, `model`, `year`, `registration_number`) VALUES
(1, 'Toyota', 'Camry', 2023, 'A123BC777'),
(2, 'BMW', 'X5', 2024, 'B456DE777'),
(3, 'Mercedes', 'E-Class', 2023, 'C789FG777');

-- --------------------------------------------------------
--
-- Структура таблицы `status`
--

CREATE TABLE `status` (
  `id_status` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `code` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL
);

--
-- Дамп данных таблицы `status`
--

INSERT INTO `status` (`id_status`, `code`, `name`) VALUES
(1, 'new', 'Новая'),
(2, 'confirmed', 'Подтверждено'),
(3, 'rejected', 'Отклонено');

-- --------------------------------------------------------

--
-- Структура таблицы `user`
--

CREATE TABLE `user` (
  `id_user` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name` varchar(50) NOT NULL,
  `surname` varchar(50)  NOT NULL,
  `patronymic` varchar(50)  NOT NULL,
  `phone` varchar(17)  NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50)  NOT NULL,
  `drivers_license` varchar(20) NOT NULL
) ;

--
-- Дамп данных таблицы `user`
--

INSERT INTO `user` (`id_user`, `name`, `surname`, `patronymic`, `phone`, `email`, `password`, `drivers_license`) VALUES
(1, 'Иван', 'Петров', 'Сергеевич', '+7(999)-999-99-99', 'user@mail.ru', '123456', '7777123456'),
(2, 'Админ', 'Админов', 'Админович', '+7(888)-888-88-88', 'car', 'carforme', '9999888777');

--
"""
cursor.executescript(s)
db.commit()
db.close()