--------------------------------------------------------
-- ELIMINAR TABLAS --
--------------------------------------------------------
DROP TABLE usuario CASCADE CONSTRAINTS;

DROP TABLE suscriptor CASCADE CONSTRAINTS;

DROP TABLE categoria_producto CASCADE CONSTRAINTS;

DROP TABLE descuento_producto CASCADE CONSTRAINTS;

DROP TABLE producto CASCADE CONSTRAINTS;

DROP TABLE detalle_compra CASCADE CONSTRAINTS;

DROP TABLE compra CASCADE CONSTRAINTS;

DROP TABLE estado_despacho CASCADE CONSTRAINTS;

DROP TABLE despacho CASCADE CONSTRAINTS;


--------------------------------------------------------
-- TABLA | USUARIO --
--------------------------------------------------------
CREATE TABLE usuario (
    id_usuario NUMBER(5)
        GENERATED ALWAYS AS IDENTITY START WITH 1 INCREMENT BY 1,
    nombre     VARCHAR2(50) NOT NULL,
    apellido   VARCHAR2(50) NOT NULL,
    email      VARCHAR2(50) NOT NULL,
    clave      VARCHAR2(50) NOT NULL,
    
    -- PRIMARY KEY | ID_USUARIO --
    CONSTRAINT pk_usuario PRIMARY KEY ( id_usuario )
);


--------------------------------------------------------
-- TABLA | SUSCRIPTOR --
--------------------------------------------------------
CREATE TABLE suscriptor (
    id_usuario        NUMBER(5) PRIMARY KEY,
    fecha_inicio_susc DATE NOT NULL,
    fecha_fin_susc    DATE NOT NULL,
   
    -- FOREIGN KEY | ID_USUARIO --
    CONSTRAINT fk_suscriptor_usuario FOREIGN KEY ( id_usuario )
        REFERENCES usuario ( id_usuario )
);


--------------------------------------------------------
-- TABLA | CATEGORIA_PRODUCTO --
--------------------------------------------------------
CREATE TABLE categoria_producto (
    id_categoria     NUMBER(3),
    nombre_categoria VARCHAR2(40) NOT NULL,
    
    -- PRIMARY KEY | ID_CATEG_PROD --
    CONSTRAINT pk_categoria_producto PRIMARY KEY ( id_categoria )
);


--------------------------------------------------------
-- TABLA | DESCUENTO_PRODUCTO --
--------------------------------------------------------
CREATE TABLE descuento_producto (
    id_dcto   NUMBER(4)
        GENERATED ALWAYS AS IDENTITY START WITH 1 INCREMENT BY 1,
    porc_dcto NUMBER(10, 2),
    
    -- PRIMARY KEY | ID_DCTO --
    CONSTRAINT pk_dcto_producto PRIMARY KEY ( id_dcto )
);


--------------------------------------------------------
-- TABLA | PRODUCTO --
--------------------------------------------------------
CREATE TABLE producto (
    id_producto     NUMBER(5)
        GENERATED ALWAYS AS IDENTITY START WITH 1 INCREMENT BY 1,
    nombre_producto VARCHAR2(40) NOT NULL,
    stock           NUMBER(3) NOT NULL,
    precio          NUMBER(6) NOT NULL,
    descripcion     VARCHAR2(150),
    imagen          BLOB,
    id_categoria    NUMBER(5) NOT NULL,
    id_dcto         NUMBER(5),
    
    -- PRIMARY KEY | ID_PRODUCTO --
    CONSTRAINT pk_producto PRIMARY KEY ( id_producto ),
    
    -- FOREIGN KEY | ID_CATEG_PROD --
    CONSTRAINT fk_producto_categoria FOREIGN KEY ( id_categoria )
        REFERENCES categoria_producto ( id_categoria ),
    
    -- FOREIGN KEY | ID_DCTO --
    CONSTRAINT fk_producto_descuento FOREIGN KEY ( id_dcto )
        REFERENCES descuento_producto ( id_dcto )
);


--------------------------------------------------------
-- TABLA | DETALLE_COMPRA --
--------------------------------------------------------
CREATE TABLE detalle_compra (
    id_compra     NUMBER(5),
    id_producto   NUMBER(5),
    cant_producto NUMBER(3) NOT NULL,
    total         NUMBER(6) NOT NULL,
    
    -- PRIMARY KEY | ID_COMPRA / ID_PRODUCTO --
    CONSTRAINT pk_detalle_compra PRIMARY KEY ( id_compra,
                                               id_producto )
);

ALTER TABLE detalle_compra
    ADD CONSTRAINT fk_detcompra_producto FOREIGN KEY ( id_producto )
        REFERENCES producto ( id_producto );


--------------------------------------------------------      
-- TABLA | COMPRA --
--------------------------------------------------------
CREATE TABLE compra (
    id_compra    NUMBER(5)
        GENERATED ALWAYS AS IDENTITY START WITH 1 INCREMENT BY 1,
    id_usuario   NUMBER(5) NOT NULL,
    fecha_compra DATE NOT NULL,
    total        NUMBER(6) NOT NULL,
    
    -- PRIMARY KEY | ID_COMPRA --
    CONSTRAINT pk_compra PRIMARY KEY ( id_compra ),
    
    -- FOREIGN KEY | ID_USUARIO --
    CONSTRAINT fk_compra_usuario FOREIGN KEY ( id_usuario )
        REFERENCES usuario ( id_usuario )
);

ALTER TABLE detalle_compra
    ADD CONSTRAINT fk_detcompra_compra FOREIGN KEY ( id_compra )
        REFERENCES compra ( id_compra );


--------------------------------------------------------      
-- TABLA | ESTADO_DESPACHO --
--------------------------------------------------------
CREATE TABLE estado_despacho (
    id_estado          NUMBER(2),
    descripcion_estado VARCHAR2(40) NOT NULL,
    
    -- PRIMARY KEY | ID_ESTADO --
    CONSTRAINT pk_estado_despacho PRIMARY KEY ( id_estado )
);


--------------------------------------------------------      
-- TABLA | DESPACHO --
--------------------------------------------------------
CREATE TABLE despacho (
    id_despacho   NUMBER(5)
        GENERATED ALWAYS AS IDENTITY START WITH 1 INCREMENT BY 1,
    direccion     VARCHAR2(50) NOT NULL,
    valor_envio   NUMBER(4) NOT NULL,
    fecha_entrega DATE NOT NULL,
    id_compra     NUMBER(5) NOT NULL,
    
    -- PRIMARY KEY | ID_DESPACHO --
    CONSTRAINT pk_despacho PRIMARY KEY ( id_despacho ),
    
    -- FOREIGN KEY | ID_COMPRA --
    CONSTRAINT fk_despacho_compra FOREIGN KEY ( id_compra )
        REFERENCES compra ( id_compra )
);