create table request(
        id integer PRIMARY key,
        firstName VARCHAR(50) not null,
        email VARCHAR(50) unique not null,
        messages VARCHAR(750) not null,
        phone string VARCHAR(50) not null unique
        )




insert into request (firstName, email,messages,phone)
values ('Avaz', 'avaz.aliyev.1997@gmail.com', 'Issue',05075015); 

select * from request




