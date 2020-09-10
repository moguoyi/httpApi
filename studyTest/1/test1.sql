USE test;
INSERT INTO `users` (
    `UID`,
    `USERNAME`,
    `PASSWORD`,
    `ROLE`,
    `CREATE_TIME`
) SELECT
    `id`,
    `username`,
    `password`,
    `level`,
    `create_time`
FROM
    tbl_users;

create table mo(id string,name string);