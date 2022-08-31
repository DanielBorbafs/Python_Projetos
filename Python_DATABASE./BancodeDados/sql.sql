create table colaboradores (
matricula int not null auto_increment,
nome varchar(30) not null,
nascimento date not null,
cpf varchar(11) not null,
rg varchar(8) not null,
nacionalidade varchar(20) default 'Brasil',
estado varchar(30) not null,
bairro varchar(30),
rua_avenida varchar(30),
numero varchar(5),
cep varchar(8),
primary key (matricula)
)default charset = utf8mb4;
