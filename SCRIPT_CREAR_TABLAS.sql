--------------------------------------------------------
-- ELIMINAR TABLAS --
--------------------------------------------------------
DROP TABLE USUARIO CASCADE CONSTRAINTS;
DROP TABLE SUSCRIPTOR CASCADE CONSTRAINTS;
DROP TABLE CATEGORIA_PRODUCTO CASCADE CONSTRAINTS;
DROP TABLE PRODUCTO CASCADE CONSTRAINTS;
DROP TABLE DETALLE_COMPRA CASCADE CONSTRAINTS;
DROP TABLE COMPRA CASCADE CONSTRAINTS;
DROP TABLE ESTADO_DESPACHO CASCADE CONSTRAINTS;
DROP TABLE DESPACHO CASCADE CONSTRAINTS;


--------------------------------------------------------
-- TABLA | USUARIO --
--------------------------------------------------------
CREATE TABLE USUARIO (
    id_usuario NUMBER(5) GENERATED ALWAYS AS IDENTITY
    START WITH 1
    INCREMENT BY 1,
    nombre VARCHAR2(50) NOT NULL,
    apellido VARCHAR2(50) NOT NULL,
    email VARCHAR2(50) NOT NULL,
    clave VARCHAR2(50) NOT NULL,
    
    -- PRIMARY KEY | ID_USUARIO --
    CONSTRAINT PK_USUARIO PRIMARY KEY (id_usuario)
);


--------------------------------------------------------
-- TABLA | SUSCRIPTOR --
--------------------------------------------------------
CREATE TABLE SUSCRIPTOR (
    id_usuario NUMBER(5) PRIMARY KEY,
    fecha_inicio_susc DATE NOT NULL,
    fecha_fin_susc DATE NOT NULL,
   
    -- FOREIGN KEY | ID_USUARIO --
    CONSTRAINT FK_SUSCRIPTOR_USUARIO FOREIGN KEY (id_usuario)
    REFERENCES USUARIO (id_usuario)
);


--------------------------------------------------------
-- TABLA | CATEGORIA_PRODUCTO --
--------------------------------------------------------
CREATE TABLE CATEGORIA_PRODUCTO (
    id_categoria NUMBER(3),
    nombre_categoria VARCHAR2(40) NOT NULL,
    
    -- PRIMARY KEY | ID_CATEG_PROD --
    CONSTRAINT PK_CATEGORIA_PRODUCTO PRIMARY KEY (id_categoria)
);


--------------------------------------------------------
-- TABLA | PRODUCTO --
--------------------------------------------------------
CREATE TABLE PRODUCTO (
    id_producto NUMBER(5) GENERATED ALWAYS AS IDENTITY
    START WITH 1
    INCREMENT BY 1,
    nombre_producto VARCHAR2(40) NOT NULL,
    stock NUMBER(3) NOT NULL,
    precio NUMBER(6) NOT NULL,
    descripcion VARCHAR2(150),
    id_categoria NUMBER(5),
    
    -- PRIMARY KEY | ID_PRODUCTO --
    CONSTRAINT PK_PRODUCTO PRIMARY KEY (id_producto),
    
    -- FOREIGN KEY | ID_CATEG_PROD --
    CONSTRAINT FK_PRODUCTO_CATEGORIA FOREIGN KEY (id_categoria)
    REFERENCES CATEGORIA_PRODUCTO(id_categoria)
);


--------------------------------------------------------
-- TABLA | DETALLE_COMPRA --
--------------------------------------------------------
CREATE TABLE DETALLE_COMPRA (
    id_compra NUMBER(5),
    id_producto NUMBER(5),
    cant_producto NUMBER(3) NOT NULL,
    total NUMBER(6) NOT NULL,
    
    -- PRIMARY KEY | ID_COMPRA / ID_PRODUCTO --
    CONSTRAINT PK_DETALLE_COMPRA PRIMARY KEY (id_compra, id_producto)  
);

ALTER TABLE DETALLE_COMPRA 
	ADD CONSTRAINT FK_DETCOMPRA_PRODUCTO FOREIGN KEY (id_producto)
	  REFERENCES PRODUCTO (id_producto);


--------------------------------------------------------      
-- TABLA | COMPRA --
--------------------------------------------------------
CREATE TABLE COMPRA (
    id_compra NUMBER(5) GENERATED ALWAYS AS IDENTITY
    START WITH 1
    INCREMENT BY 1,
    id_usuario NUMBER(5) NOT NULL,
    fecha_compra DATE NOT NULL,
    porc_dcto NUMBER(10, 2),
    total NUMBER(6) NOT NULL,
    
    -- PRIMARY KEY | ID_COMPRA --
    CONSTRAINT PK_COMPRA PRIMARY KEY (id_compra),
    
    -- FOREIGN KEY | ID_USUARIO --
    CONSTRAINT FK_COMPRA_USUARIO FOREIGN KEY (id_usuario)
    REFERENCES USUARIO(id_usuario)
);

ALTER TABLE DETALLE_COMPRA 
	ADD CONSTRAINT FK_DETCOMPRA_COMPRA FOREIGN KEY (id_compra)
	  REFERENCES COMPRA (id_compra);


--------------------------------------------------------      
-- TABLA | ESTADO_DESPACHO --
--------------------------------------------------------
CREATE TABLE ESTADO_DESPACHO(
    id_estado NUMBER(2),
    descripcion_estado VARCHAR2(40) NOT NULL,
    
    -- PRIMARY KEY | ID_ESTADO --
    CONSTRAINT PK_ESTADO_DESPACHO PRIMARY KEY (id_estado)
);


--------------------------------------------------------      
-- TABLA | DESPACHO --
--------------------------------------------------------
CREATE TABLE DESPACHO(
    id_despacho NUMBER(5) GENERATED ALWAYS AS IDENTITY
    START WITH 1
    INCREMENT BY 1,
    direccion VARCHAR2(50) NOT NULL,
    valor_envio NUMBER(4) NOT NULL,
    fecha_entrega DATE NOT NULL,
    id_compra NUMBER(5) NOT NULL,
    
    -- PRIMARY KEY | ID_DESPACHO --
    CONSTRAINT PK_DESPACHO PRIMARY KEY (id_despacho),
    
    -- FOREIGN KEY | ID_COMPRA --
    CONSTRAINT FK_DESPACHO_COMPRA FOREIGN KEY (id_compra)
    REFERENCES COMPRA(id_compra)
);