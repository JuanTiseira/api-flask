from sqlalchemy import CheckConstraint, Column, Date, ForeignKey, Integer, LargeBinary, Numeric, String, Table, Text, Time, text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry
from database import db
Base = declarative_base()
metadata = Base.metadata

class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
    def __str__(self):
        return f'<User {self.email}>'
        
class Token(db.Model):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    token = Column(String)
    
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token
    
    def __str__(self):
        return f'<Token {self.token}>'

class CalidadEdilicia(Base):
    __tablename__ = 'calidad_edilicia'

    id = Column(Integer, primary_key=True, server_default=text("nextval('calidad_edilicia_id_seq'::regclass)"))
    descripcion = Column(String(50))


class CalidadZonaUrbana(Base):
    __tablename__ = 'calidad_zona_urbana'

    id = Column(Integer, primary_key=True, server_default=text("nextval('calidad_zona_urbana_id_seq'::regclass)"))
    descripcion = Column(String(50))


class CaracteristicaZona(Base):
    __tablename__ = 'caracteristica_zona'

    id = Column(Integer, primary_key=True, server_default=text("nextval('caracteristica_zona_id_seq'::regclass)"))
    descripcion = Column(String(50))


class Categoria(db.Model):
    
    def __init__(self, user: dict):
        """
        Initialize a User by passing in a dictionary.
        :param user: A dictionary with fields matching the User fields
        """
        self.id = user.get("id")
        self.codigo = user.get("codigo")
        self.descripcion = user.get("descripcion")
        
    __tablename__ = 'categoria'

    id = Column(Integer, primary_key=True, server_default=text("nextval('categoria_id_seq'::regclass)"))
    codigo = Column(String(50))
    descripcion = Column(String(50))
    
    def __str__(self):
        """
        String representation of a user.  This representation is meant to be human readable.
        :return: The user in string form.
        """
        return (
            f"categoria: [id: {self.id}, codigo: {self.codigo}, descripcion: {self.descripcion}"
        )
        
    # def __repr__(self):
    #     """
    #     String representation of a user.  This representation is meant to be machine readable.
    #     :return: The user in string form.
    #     """
    #     return f"<User {self.descripcion}>"

class DatosEntorno(Base):
    __tablename__ = 'datos_entorno'

    id = Column(Integer, primary_key=True, server_default=text("nextval('datos_entorno_id_seq'::regclass)"))
    descripcion = Column(String(50))


class EstadoConservacion(Base):
    __tablename__ = 'estado_conservacion'

    id = Column(Integer, primary_key=True, server_default=text("nextval('estado_conservacion_id_seq'::regclass)"))
    descripcion = Column(String(50))


t_geography_columns = Table(
    'geography_columns', metadata,
    Column('f_table_catalog', String),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geography_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', Text)
)


t_geometry_columns = Table(
    'geometry_columns', metadata,
    Column('f_table_catalog', String(256)),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geometry_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', String(30))
)


class Imagen(Base):
    
    def __init__(self, imagen: dict):
    
        self.id = imagen.get("id")
        self.ruta_frente = imagen.get("ruta_frente")
        self.ruta_informe = imagen.get("ruta_informe")    
        self.imagen_frente = imagen.get("imagen_frente")
        self.imagen_aviso = imagen.get("imagen_aviso")
    
    
    __tablename__ = 'imagen'

    id = Column(Integer, primary_key=True, server_default=text("nextval('imagen_id_seq'::regclass)"))
    ruta_frente = Column(String(254))
    ruta_informe = Column(String(254))
    imagen_frente = Column(LargeBinary)
    imagen_aviso = Column(LargeBinary)


class Operador(Base):
    __tablename__ = 'operador'

    id = Column(Integer, primary_key=True, server_default=text("nextval('operador_id_seq'::regclass)"))
    nombre = Column(String(50))
    dependencia = Column(String(50))
    apellido = Column(String(50))
    dni = Column(Integer)
    telefono = Column(Integer)
    email = Column(String(70))


class RelevamientoCsv(Base):
    __tablename__ = 'relevamiento_csv'

    cca = Column(String(20), primary_key=True)
    categoria = Column(String(15))
    superficie = Column(Numeric(10, 2))
    coord_xx = Column(Numeric(15, 13))
    coord_yy = Column(Numeric(15, 13))
    sector = Column(String(50))
    foto = Column(String(254))
    cal_edilic = Column(String(50))
    tipo = Column(String(50))
    estado_con = Column(String(50))
    terminaciones = Column(String(50))
    antiguedad = Column(Integer)
    niveles = Column(Integer)
    carac_zona = Column(String(50))
    datos_ent = Column(String(50))
    car_zon_urb = Column(String(50))
    observaciones = Column(Text)
    operador = Column(String(50))
    fecha = Column(Date)
    hora = Column(Time)
    informe = Column(String(15))
    aviso = Column(String(254))


class SpatialRefSy(Base):
    __tablename__ = 'spatial_ref_sys'
    __table_args__ = (
        CheckConstraint('(srid > 0) AND (srid <= 998999)'),
    )

    srid = Column(Integer, primary_key=True)
    auth_name = Column(String(256))
    auth_srid = Column(Integer)
    srtext = Column(String(2048))
    proj4text = Column(String(2048))


class Terminacione(Base):
    __tablename__ = 'terminaciones'

    id = Column(Integer, primary_key=True, server_default=text("nextval('terminaciones_id_seq'::regclass)"))
    descripcion = Column(String(50))


class Tipo(Base):
    __tablename__ = 'tipo'

    id = Column(Integer, primary_key=True, server_default=text("nextval('tipo_id_seq'::regclass)"))
    descripcion = Column(String(80))


class Operativo(Base):
    __tablename__ = 'operativo'

    id = Column(Integer, primary_key=True)
    fecha = Column(Date)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)
    operador_id = Column(ForeignKey('operador.id'))

    operador = relationship('Operador')


class Sector(Base):
    __tablename__ = 'sector'

    id = Column(Integer, primary_key=True, server_default=text("nextval('sector_id_seq'::regclass)"))
    descripcion = Column(String(15))
    caracteristica_zona_id = Column(ForeignKey('caracteristica_zona.id'))
    datos_entorno_id = Column(ForeignKey('datos_entorno.id'))
    calidad_zona_urbana_id = Column(ForeignKey('calidad_zona_urbana.id'))

    calidad_zona_urbana = relationship('CalidadZonaUrbana')
    caracteristica_zona = relationship('CaracteristicaZona')
    datos_entorno = relationship('DatosEntorno')


class Informe(Base):
    __tablename__ = 'informe'

    id = Column(Integer, primary_key=True, server_default=text("nextval('informe_id_seq'::regclass)"))
    numero_de_informe = Column(String(15))
    fecha = Column(Date)
    hora = Column(Time)
    imagen_id = Column(ForeignKey('imagen.id'))
    operativo_id = Column(ForeignKey('operativo.id'))
    operador_id = Column(ForeignKey('operador.id'))
    observaciones = Column(Text)

    imagen = relationship('Imagen')
    operador = relationship('Operador')
    operativo = relationship('Operativo')


class Parcela(Base):
    
    def __init__(self, parcela: dict):
        """
        Initialize a User by passing in a dictionary.
        :param user: A dictionary with fields matching the User fields
        """
        self.id_gis = user.get("id_gis")
        self.sector_id = user.get("sector_id")
        self.coordenadasxx = user.get("coordenadasxx")
        self.coordenadasyy = user.get("coordenadasyy")
        self.geom = user.get("geom")
        self.categoria_id = user.get("categoria_id")
        self.calidad_edilicia_id = user.get("calidad_edilicia_id")
        self.tipo_id = user.get("tipo_id")
        self.estado_conservacion_id = user.get("estado_conservacion_id")
        self.terminacion_id = user.get("terminacion_id")
        self.antiguedad = user.get("antiguedad")
        self.informe_id = user.get("informe_id")
        self.niveles = user.get("niveles")
        self.superficie = user.get("superficie")
        self.valor_economico = user.get("valor_economico")
        self.superficie_ajustada = user.get("superficie_ajustada")
        self.coeficiente_ajuste = user.get("coeficiente_ajuste")
        self.estado_revaluo = user.get("estado_revaluo")
        self.observaciones = user.get("observaciones")
        self.observaciones = user.get("observaciones")
        self.partida = user.get("partida")
        
    __tablename__ = 'parcela'

    id_gis = Column(String(20), primary_key=True)
    sector_id = Column(ForeignKey('sector.id'))
    coordenadasxx = Column(Numeric(15, 13))
    coordenadasyy = Column(Numeric(15, 13))
    geom = Column(Geometry())
    categoria_id = Column(ForeignKey('categoria.id'))
    calidad_edilicia_id = Column(Integer)
    tipo_id = Column(ForeignKey('tipo.id'))
    estado_conservacion_id = Column(ForeignKey('estado_conservacion.id'))
    terminacion_id = Column(ForeignKey('terminaciones.id'))
    antiguedad = Column(Integer)
    informe_id = Column(ForeignKey('informe.id'))
    niveles = Column(Integer)
    superficie = Column(Numeric(10, 2))
    valor_economico = Column(Numeric(10, 2))
    superficie_ajustada = Column(Numeric(10, 2))
    coeficiente_ajuste = Column(Numeric(10, 2))
    estado_revaluo = Column(String(20))
    observaciones = Column(Text)
    partida = Column(String(7))

    categoria = relationship('Categoria')
    estado_conservacion = relationship('EstadoConservacion')
    informe = relationship('Informe')
    sector = relationship('Sector')
    terminacion = relationship('Terminacione')
    tipo = relationship('Tipo')
    
    
    def __str__(self):
        """
        String representation of a user.  This representation is meant to be human readable.
        :return: The user in string form.
        """
        return (
            f"parcela: [id: {self.id_gis}, sector_id: {self.sector_id}, coordenadasxx: {self.coordenadasxx}",
            f"coordenadasyy : {self.coordenadasyy}, geom: {self.geom}, "
        )
