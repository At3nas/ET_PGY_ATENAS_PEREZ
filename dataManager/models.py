# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CategoriaProducto(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'categoria_producto'


class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    fecha_compra = models.DateField()
    porc_dcto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'compra'


class Despacho(models.Model):
    id_despacho = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=50)
    valor_envio = models.IntegerField()
    fecha_entrega = models.DateField()
    id_compra = models.ForeignKey(Compra, models.DO_NOTHING, db_column='id_compra')

    class Meta:
        managed = False
        db_table = 'despacho'


class DetalleCompra(models.Model):
    id_compra = models.OneToOneField(Compra, models.DO_NOTHING, db_column='id_compra', primary_key=True)  # The composite primary key (id_compra, id_producto) found, that is not supported. The first column is selected.
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    cant_producto = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_compra'
        unique_together = (('id_compra', 'id_producto'),)


class EstadoDespacho(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    descripcion_estado = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'estado_despacho'


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=40)
    stock = models.IntegerField()
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    id_categoria = models.ForeignKey(CategoriaProducto, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Suscriptor(models.Model):
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    fecha_inicio_susc = models.DateField()
    fecha_fin_susc = models.DateField()

    class Meta:
        managed = False
        db_table = 'suscriptor'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'usuario'
