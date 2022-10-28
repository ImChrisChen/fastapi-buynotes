CREATE DATABASE IF NOT EXISTS buy_notes;

-- 帐单类型表
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS account_type;
SET FOREIGN_KEY_CHECKS = 1;
CREATE TABLE account_type
(
    `id`           INT(10)     NOT NULL AUTO_INCREMENT,
    `amount_type`  varchar(10) NOT NULL COMMENT '金额类型(收入/支出,1/0)',
    `type_zh_name` VARCHAR(50) NOT NULL COMMENT '类型名称-zh',
    `type_en_name` VARCHAR(50) COMMENT ' 类型名称—en',
    `created_at`   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at`   TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;


-- 帐单记录表
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS account_note;
SET FOREIGN_KEY_CHECKS = 1;
CREATE TABLE account_note
(
    `id`         INT(10)     NOT NULL AUTO_INCREMENT,
    `remark`     VARCHAR(50) NOT NULL COMMENT '备注',
    `amount`     INT(10)     NOT NULL COMMENT '金额',
    `type_id`    INT(10)     NOT NULL COMMENT '消费/收入类型(消费和支出会读取不同的typeid)',
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    CONSTRAINT FK_AccountNote_AccountType FOREIGN KEY (`type_id`) REFERENCES account_type (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;


-- 预算表
DROP TABLE IF EXISTS budget;
CREATE TABLE budget
(
    `id`           int(10)     NOT NULL AUTO_INCREMENT,
    `zh_name`      varchar(50) NOT NULL COMMENT '饮食预算表-zh',
    `en_name`      varchar(50) DEFAULT '' COMMENT '饮食预算表-en',
    `date_type_zh` varchar(50) NOT NULL COMMENT '时间预算范围(年,月,周,日)',
    `date_type_en` varchar(50) NOT NULL COMMENT '时间预算范围(year,month,week,day)',
    `created_at`   TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,
    `updated_at`   TIMESTAMP   DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
);

INSERT INTO account_type(amount_type, type_zh_name, type_en_name)
VALUES ('0', '餐饮', 'food');
INSERT INTO account_type(amount_type, type_zh_name, type_en_name)
VALUES ('0', '交通', 'traffic');
INSERT INTO account_type(amount_type, type_zh_name, type_en_name)
VALUES ('0', '日用品', 'daily necessity')