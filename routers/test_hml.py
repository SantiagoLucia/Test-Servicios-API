from fastapi import APIRouter
from servicios.consultaDocumento import *
from servicios.consultaCuitCuil import *
from servicios.consultaUsuario import *
from servicios.ffcc import *
from servicios.consultaTipoDocumento import *
from servicios.generarTareaGEDO import *
from servicios.generacionDocumentos import *
from servicios.consultaExpediente import *
from servicios.consultaEstadoPaseExpediente import *
from servicios.tratas import *
from servicios.generacionExpediente import *
from servicios.bloqueoExpediente import *
from servicios.documentosTrabajo import *
from servicios.documentosOficiales import *
from servicios.generacionPaseExpediente import *
from servicios.expedientesAsociados import *
from servicios.tramitacionConjunta import *
from servicios.consultarNumero import *
from servicios.datosHistoricos import *
from servicios.consultaRegistro import *
from datetime import datetime
import base64
from config import URL_TOKEN_HML, AUTH_HML, URL_SERVICIO_HML


url_token = URL_TOKEN_HML
auth = AUTH_HML
url_servicio = URL_SERVICIO_HML


router = APIRouter()


def test_buscarDetallePorNumero(num):        
    url = url_servicio+'consultaDocumento?wsdl'
    request = {
        'request': {
        'assignee': True,
        'numeroDocumento': num,
        'usuarioConsulta': 'USERT',
        }
    }
    servicio = ConsultaDocumento(url, url_token, auth)
    try:
        respuesta = servicio.buscarDetallePorNumero(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaDocumento','metodo':'buscarDetallePorNumero','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaDocumento','metodo':'buscarDetallePorNumero','codigo':codigo,'error':e,'fecha':dt}


def test_buscarDocumentoEnExpedientess(num):        
    url = url_servicio+'consultaDocumento?wsdl'
    request = {
        'request': {
        'numeroDocumento': num,
        }
    }
    servicio = ConsultaDocumento(url, url_token, auth)
    try:
        respuesta = servicio.buscarDocumentoEnExpedientes(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaDocumento','metodo':'buscarDocumentoEnExpedientes','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaDocumento','metodo':'buscarDocumentoEnExpedientes','codigo':codigo,'error':e,'fecha':dt}


def test_buscarDocumentoPublicablePorNumero(num):        
    url = url_servicio+'consultaDocumento?wsdl'
    request = {
        'request': {
        'assignee': True,
        'numeroDocumento': num,
        'usuarioConsulta': 'USERT',
        }
    }
    servicio = ConsultaDocumento(url, url_token, auth)
    try:
        respuesta = servicio.buscarDocumentoPublicablePorNumero(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaDocumento','metodo':'buscarDocumentoPublicablePorNumero','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaDocumento','metodo':'buscarDocumentoPublicablePorNumero','codigo':codigo,'error':e,'fecha':dt}


def test_buscarNumeroGDEBA(id):        
    url = url_servicio+'consultaDocumento?wsdl'
    request = {
        'request': {
        'id': id,
        }
    }
    servicio = ConsultaDocumento(url, url_token, auth)
    try:
        respuesta = servicio.buscarNumeroGDEBA(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaDocumento','metodo':'buscarNumeroGDEBA','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaDocumento','metodo':'buscarNumeroGDEBA','codigo':codigo,'error':e,'fecha':dt}


def test_buscarPDFPorNumero(num):        
    url = url_servicio+'consultaDocumento?wsdl'
    request = {
        'request': {
        'assignee': True,
        'numeroDocumento': num,
        'usuarioConsulta': 'USERT',
        }
    }
    servicio = ConsultaDocumento(url, url_token, auth)
    try:
        respuesta = servicio.buscarPDFPorNumero(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaDocumento','metodo':'buscarPDFPorNumero','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaDocumento','metodo':'buscarPDFPorNumero','codigo':codigo,'error':e,'fecha':dt}


def test_buscarPorNumero(num):
    url = url_servicio+'consultaDocumento?wsdl'
    request = {
        'request': {
        'assignee': True,
        'numeroDocumento': num,
        'usuarioConsulta': 'USERT',
        }
    }
    servicio = ConsultaDocumento(url, url_token, auth)
    try:
        respuesta = servicio.buscarPorNumero(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaDocumento','metodo':'buscarPorNumero','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaDocumento','metodo':'buscarPorNumero','codigo':codigo,'error':e,'fecha':dt}


def test_buscarPorCuitCuil(cuil):
    url = url_servicio+'consultaCuitCuil?wsdl'
    request = {'consultaCuitCuilRequest': cuil}
    servicio = ConsultaCuitCuil(url, url_token, auth)
    try:
        respuesta = servicio.buscarPorCuitCuil(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaCuitCuil','metodo':'buscarPorCuitCuil','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaCuitCuil','metodo':'buscarPorCuitCuil','codigo':codigo,'error':e,'fecha':dt}


def test_buscarPorUsuario(usuario):
    url = url_servicio+'consultaUsuario?wsdl'
    request = {'usuario': usuario}
    servicio = ConsultaUsuario(url, url_token, auth)
    try:
        respuesta = servicio.buscarPorUsuario(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaUsuario','metodo':'buscarPorUsuario','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaUsuario','metodo':'buscarPorUsuario','codigo':codigo,'error':e,'fecha':dt}


def test_buscarPorNombre(nombre):
    url = url_servicio+'FFCC?wsdl'
    request = {'nombreFormulario': nombre}
    servicio = FFCC(url, url_token, auth)
    try:
        respuesta = servicio.buscarPorNombre(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'FFCC','metodo':'buscarPorNombre','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'FFCC','metodo':'buscarPorNombre','codigo':codigo,'error':e,'fecha':dt}


def test_consultarTipoDocumento(acronimo):
    url = url_servicio+'consultaTipoDocumento?wsdl'
    request = {'acronimo': acronimo}
    servicio = ConsultaTipoDocumento(url, url_token, auth)
    try:
        respuesta = servicio.consultarTipoDocumento(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaTipoDocumento','metodo':'consultarTipoDocumento','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaTipoDocumento','metodo':'consultarTipoDocumento','codigo':codigo,'error':e,'fecha':dt}


def test_generarTareaGEDO():
    url = url_servicio+'generarTareaGEDO?wsdl'
    
    request = {
        'request': {
            'acronimoTipoDocumento': 'TESTL',
            'data': bytes('Documento de prueba. Carece de motivación administrativa.','utf-8'),
            'tarea': 'Firmar Documento',
            'usuarioEmisor': 'USERT',
            'usuarioFirmante': {
                'entry': {
                    'key': 1,
                    'value': 'USERT',
                }                
            },
            'usuarioReceptor': 'USERT',
            'referencia': 'Documento de prueba. Carece de motivación administrativa.',
            'suscribirseAlDocumento': True,
            'enviarCorreoReceptor': False,
            'listaUsuariosDestinatariosExternos': {
                'entry': {
                    'key': '',
                    'value': '',
                }
            },
            'metaDatos': {
                'entry': {
                    'key': '',
                    'value': '',
                }                
            },
            'recibirAvisoFirma': False
        }
    }
    
    servicio = GenerarTareaGEDO(url, url_token, auth)
    try:
        respuesta = servicio.generarTareaGEDO(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'generarTareaGEDO','metodo':'generarTareaGEDO','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'generarTareaGEDO','metodo':'generarTareaGEDO','codigo':codigo,'error':e,'fecha':dt}


def test_generarDocumento():
    url = url_servicio+'generacionDocumentos?wsdl'
    
    request = {
        'request': {
            'acronimoTipoDocumento': 'TESTL',
            'data': bytes('Documento de prueba. Carece de motivación administrativa.','utf-8'),
            'usuario': 'USERT',
            'referencia': 'Documento de prueba. Carece de motivación administrativa.',
            'listaUsuariosDestinatariosExternos': {
                'entry': {
                    'key': '',
                    'value': '',
                }
            },
            'metaDatos': {
                'entry': {
                    'key': '',
                    'value': '',
                }                
            },
        }
    }
    
    servicio = GeneracionDocumentos(url, url_token, auth)
    try:
        respuesta = servicio.generarDocumento(request)
        codigo, contenido, tiempo = respuesta
        d = xmltodict.parse(contenido)
        resp_numero = d['soap:Envelope']['soap:Body']['iop:generarDocumentoResponse']['return']['numero']        
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'generacionDocumentos','metodo':'generarDocumento','codigo':codigo,'tiempo':tiempo,'fecha':dt, 'numero': resp_numero}
    except Exception as e:
        return {'servicio':'generacionDocumentos','metodo':'generarDocumento','codigo':codigo,'error':e,'fecha':dt}


def test_generarDocumentoUsuarioExterno():
    url = url_servicio+'generacionDocumentos?wsdl'
    
    request = {
        'request': {
            'acronimoTipoDocumento': 'TESTL',
            'data': bytes('Documento de prueba. Carece de motivación administrativa.','utf-8'),
            'usuario': 'USERT',
            'referencia': 'Documento de prueba. Carece de motivación administrativa.',
            'nombreYApellido': 'Usuario Test',
            'cargo': 'Analista',
            'reparticion': 'TESTGDEBA',
            'listaUsuariosDestinatariosExternos': {
                'entry': {
                    'key': '',
                    'value': '',
                }
            },
            'metaDatos': {
                'entry': {
                    'key': '',
                    'value': '',
                }                
            },
        }
    }
    
    servicio = GeneracionDocumentos(url, url_token, auth)
    try:
        respuesta = servicio.generarDocumentoUsuarioExterno(request)
        codigo, contenido, tiempo = respuesta
        d = xmltodict.parse(contenido)
        resp_numero = d['soap:Envelope']['soap:Body']['iop:generarDocumentoUsuarioExternoResponse']['return']['numero']        
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'generacionDocumentos','metodo':'generarDocumentoUsuarioExterno','codigo':codigo,'tiempo':tiempo,'fecha':dt, 'numero': resp_numero}
    except Exception as e:
        return {'servicio':'generacionDocumentos','metodo':'generarDocumentoUsuarioExterno','codigo':codigo,'error':e,'fecha':dt}


def test_consultarCaratulaVariablePorNumeroExpedienteUsuario(numero):
    url = url_servicio+'consultaExpediente?wsdl'
    
    request = {
        'numeroExpediente': numero,
        'usuario': 'USERT',
    }
    
    servicio = ConsultaExpediente(url, url_token, auth)
    try:
        respuesta = servicio.consultarCaratulaVariablePorNumeroExpedienteUsuario(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaExpediente','metodo':'consultarCaratulaVariablePorNumeroExpedienteUsuario','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaExpediente','metodo':'consultarCaratulaVariablePorNumeroExpedienteUsuario','codigo':codigo,'error':e,'fecha':dt}


def test_buscarCaratulaPorNumeroExpediente(numero):
    url = url_servicio+'consultaExpediente?wsdl'
    
    request = {
        'request': {
            'numeroExpediente': numero,
        }
    }

    servicio = ConsultaExpediente(url, url_token, auth)
    try:
        respuesta = servicio.buscarCaratulaPorNumeroExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaExpediente','metodo':'buscarCaratulaPorNumeroExpediente','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaExpediente','metodo':'buscarCaratulaPorNumeroExpediente','codigo':codigo,'error':e,'fecha':dt}


def test_consultarIdFCPorNumeroExpediente(numero):
    url = url_servicio+'consultaExpediente?wsdl'
    
    request = {
        'numeroExpediente': numero,
    }

    servicio = ConsultaExpediente(url, url_token, auth)
    try:
        respuesta = servicio.consultarIdFCPorNumeroExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaExpediente','metodo':'consultarIdFCPorNumeroExpediente','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaExpediente','metodo':'consultarIdFCPorNumeroExpediente','codigo':codigo,'error':e,'fecha':dt}


def test_buscarHistorialPasesExpediente(numero):
    url = url_servicio+'consultaExpediente?wsdl'
    
    request = {
        'numeroExpediente': numero,
    }

    servicio = ConsultaExpediente(url, url_token, auth)
    try:
        respuesta = servicio.buscarHistorialPasesExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaExpediente','metodo':'buscarHistorialPasesExpediente','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaExpediente','metodo':'buscarHistorialPasesExpediente','codigo':codigo,'error':e,'fecha':dt}


def test_buscarExpedientesPorSistemaOrigenUsuario(usuario):
    url = url_servicio+'consultaExpediente?wsdl'
    
    request = {
        'usuario': usuario,
    }

    servicio = ConsultaExpediente(url, url_token, auth)
    try:
        respuesta = servicio.buscarExpedientesPorSistemaOrigenUsuario(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaExpediente','metodo':'buscarExpedientesPorSistemaOrigenUsuario','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaExpediente','metodo':'buscarExpedientesPorSistemaOrigenUsuario','codigo':codigo,'error':e,'fecha':dt}


def test_buscarExpedientePorIdSistemaExterno(id):
    url = url_servicio+'consultaExpediente?wsdl'
    
    request = {
        'idSistemaExterno': id,
    }

    servicio = ConsultaExpediente(url, url_token, auth)
    try:
        respuesta = servicio.buscarExpedientePorIdSistemaExterno(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaExpediente','metodo':'buscarExpedientePorIdSistemaExterno','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaExpediente','metodo':'buscarExpedientePorIdSistemaExterno','codigo':codigo,'error':e,'fecha':dt}


def test_buscarExpediente(numero):
    url = url_servicio+'consultaExpediente?wsdl'
    
    request = {
        'numeroExpediente': numero,
    }

    servicio = ConsultaExpediente(url, url_token, auth)
    try:
        respuesta = servicio.buscarExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaExpediente','metodo':'buscarExpediente','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaExpediente','metodo':'buscarExpediente','codigo':codigo,'error':e,'fecha':dt}


def test_consultarExpedienteDetallado(numero):
    url = url_servicio+'consultaExpediente?wsdl'
    
    request = {
        'numeroExpediente': numero,
    }

    servicio = ConsultaExpediente(url, url_token, auth)
    try:
        respuesta = servicio.consultarExpedienteDetallado(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaExpediente','metodo':'consultarExpedienteDetallado','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaExpediente','metodo':'consultarExpedienteDetallado','codigo':codigo,'error':e,'fecha':dt}


def test_buscarCodigoCaratulaPorNumeroExpediente(numero):
    url = url_servicio+'consultaExpediente?wsdl'
    
    request = {
        'numeroExpediente': numero,
    }

    servicio = ConsultaExpediente(url, url_token, auth)
    try:
        respuesta = servicio.buscarCodigoCaratulaPorNumeroExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaExpediente','metodo':'buscarCodigoCaratulaPorNumeroExpediente','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaExpediente','metodo':'buscarCodigoCaratulaPorNumeroExpediente','codigo':codigo,'error':e,'fecha':dt}


def test_buscarDatosExpedienteVariable(numero):
    url = url_servicio+'consultaExpediente?wsdl'
    
    request = {
        'numeroExpediente': numero,
        'usuario': 'USERT',
    }

    servicio = ConsultaExpediente(url, url_token, auth)
    try:
        respuesta = servicio.buscarDatosExpedienteVariable(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaExpediente','metodo':'buscarDatosExpedienteVariable','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaExpediente','metodo':'buscarDatosExpedienteVariable','codigo':codigo,'error':e,'fecha':dt}


def test_validarExpediente(numero):
    url = url_servicio+'consultaExpediente?wsdl'
    
    request = {
        'numeroExpediente': numero,
    }

    servicio = ConsultaExpediente(url, url_token, auth)
    try:
        respuesta = servicio.validarExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaExpediente','metodo':'validarExpediente','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaExpediente','metodo':'validarExpediente','codigo':codigo,'error':e,'fecha':dt}


def test_consultarExpedientesPorSistemaOrigenReparticion(reparticion):
    url = url_servicio+'consultaExpediente?wsdl'
    
    request = {
        'reparticion': reparticion,
    }

    servicio = ConsultaExpediente(url, url_token, auth)
    try:
        respuesta = servicio.consultarExpedientesPorSistemaOrigenReparticion(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaExpediente','metodo':'consultarExpedientesPorSistemaOrigenReparticion','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaExpediente','metodo':'consultarExpedientesPorSistemaOrigenReparticion','codigo':codigo,'error':e,'fecha':dt}


def test_buscarDatosExpedientePorCodigosTrata():
    url = url_servicio+'consultaExpediente?wsdl'
    
    request = {
        'codigosTrata': 'TEST0001',
        'estadoDestino': 'Iniciación',
        'usuario': 'USERT',
    }

    servicio = ConsultaExpediente(url, url_token, auth)
    try:
        respuesta = servicio.buscarDatosExpedientePorCodigosTrata(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaExpediente','metodo':'buscarDatosExpedientePorCodigosTrata','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaExpediente','metodo':'buscarDatosExpedientePorCodigosTrata','codigo':codigo,'error':e,'fecha':dt}


def test_buscarExpedientesPorSistemaOrigenLibreUsuario():
    url = url_servicio+'consultaExpediente?wsdl'
    
    request = {
        'usuario': 'USERT',
        'sistemaOrigen': 'EE',
    }

    servicio = ConsultaExpediente(url, url_token, auth)
    try:
        respuesta = servicio.buscarExpedientesPorSistemaOrigenLibreUsuario(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaExpediente','metodo':'buscarExpedientesPorSistemaOrigenLibreUsuario','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaExpediente','metodo':'buscarExpedientesPorSistemaOrigenLibreUsuario','codigo':codigo,'error':e,'fecha':dt}


def test_consultarExpedientesPorSistemaOrigenLibreReparticion():
    url = url_servicio+'consultaExpediente?wsdl'
    
    request = {
        'reparticion': 'TESTGDEBA',
        'sistemaOrigen': 'EE',
    }

    servicio = ConsultaExpediente(url, url_token, auth)
    try:
        respuesta = servicio.consultarExpedientesPorSistemaOrigenLibreReparticion(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaExpediente','metodo':'consultarExpedientesPorSistemaOrigenLibreReparticion','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaExpediente','metodo':'consultarExpedientesPorSistemaOrigenLibreReparticion','codigo':codigo,'error':e,'fecha':dt}


def test_consultaEstadoActualExpediente(numero):
    url = url_servicio+'consultaEstadoPaseExpediente?wsdl'
    request = {'numeroExpediente': numero}
    servicio = ConsultaEstadoPaseExpediente(url, url_token, auth)
    try:
        respuesta = servicio.consultaEstadoActualExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaEstadoPaseExpediente','metodo':'consultaEstadoActualExpediente','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaEstadoPaseExpediente','metodo':'consultaEstadoActualExpediente','codigo':codigo,'error':e,'fecha':dt}


def test_consultaEstadosPaseExpedientePosibles(numero):
    url = url_servicio+'consultaEstadoPaseExpediente?wsdl'
    request = {'numeroExpediente': numero}
    servicio = ConsultaEstadoPaseExpediente(url, url_token, auth)
    try:
        respuesta = servicio.consultaEstadosPaseExpedientePosibles(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaEstadoPaseExpediente','metodo':'consultaEstadosPaseExpedientePosibles','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaEstadoPaseExpediente','metodo':'consultaEstadosPaseExpedientePosibles','codigo':codigo,'error':e,'fecha':dt}


def test_esEstadoPaseExpedienteValido(numero):
    url = url_servicio+'consultaEstadoPaseExpediente?wsdl'
    request = {
        'numeroExpediente': numero,
        'estadoDestino': 'Tramitación',
        }
    servicio = ConsultaEstadoPaseExpediente(url, url_token, auth)
    try:
        respuesta = servicio.esEstadoPaseExpedienteValido(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaEstadoPaseExpediente','metodo':'esEstadoPaseExpedienteValido','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaEstadoPaseExpediente','metodo':'esEstadoPaseExpedienteValido','codigo':codigo,'error':e,'fecha':dt}


def test_buscarTratasPorCodigo():
    url = url_servicio+'tratas?wsdl'
    request = {'codigoTrata': 'TEST0001'}
    servicio = Tratas(url, url_token, auth)
    try:
        respuesta = servicio.buscarTratasPorCodigo(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'tratas','metodo':'buscarTratasPorCodigo','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'tratas','metodo':'buscarTratasPorCodigo','codigo':codigo,'error':e,'fecha':dt}


def test_generarCaratulaExpediente():
    url = url_servicio+'generacionExpediente?wsdl'
    
    request = {
        'request': {
            'motivo': 'Expediente de prueba. Carece de motivación administrativa.',
            'codigoTrata': 'TEST0001',
            'descripcion': 'Expediente de prueba. Carece de motivación administrativa.',
            'usuario': 'USERT',
            'interno': True,
            'empresa': False,
            'externo': False,
            'persona': True,
            'tieneCuitCuil': False,
        }
    }
    
    servicio = GeneracionExpediente(url, url_token, auth)
    try:
        respuesta = servicio.generarCaratulaExpediente(request)
        codigo, contenido, tiempo = respuesta
        d = xmltodict.parse(contenido)
        resp_numero = d['soap:Envelope']['soap:Body']['iop:generarCaratulaExpedienteResponse']['return']        
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'generacionExpediente','metodo':'generarCaratulaExpediente','codigo':codigo,'tiempo':tiempo,'fecha':dt, 'numero':resp_numero}
    except Exception as e:
        return {'servicio':'generacionExpediente','metodo':'generarCaratulaExpediente','codigo':codigo,'error':e,'fecha':dt}


def test_bloquearExpediente(numero):
    url = url_servicio+'bloqueoExpediente?wsdl'
    request = {'numeroExpediente': numero}
    servicio = BloqueoExpediente(url, url_token, auth)
    try:
        respuesta = servicio.bloquearExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'bloqueoExpediente','metodo':'bloquearExpediente','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'bloqueoExpediente','metodo':'bloquearExpediente','codigo':codigo,'error':e,'fecha':dt}


def test_estaExpedienteBloqueado(numero):
    url = url_servicio+'bloqueoExpediente?wsdl'
    request = {'numeroExpediente': numero}
    servicio = BloqueoExpediente(url, url_token, auth)
    try:
        respuesta = servicio.estaExpedienteBloqueado(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'bloqueoExpediente','metodo':'estaExpedienteBloqueado','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'bloqueoExpediente','metodo':'estaExpedienteBloqueado','codigo':codigo,'error':e,'fecha':dt}


def test_desbloquearExpediente(numero):
    url = url_servicio+'bloqueoExpediente?wsdl'
    request = {'numeroExpediente': numero}
    servicio = BloqueoExpediente(url, url_token, auth)
    try:
        respuesta = servicio.desbloquearExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'bloqueoExpediente','metodo':'desbloquearExpediente','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'bloqueoExpediente','metodo':'desbloquearExpediente','codigo':codigo,'error':e,'fecha':dt}


def test_adjuntarDocumentosTrabajo(expediente):
    url = url_servicio+'documentosTrabajo?wsdl'

    with open('./static/archivo_trabajo.pdf', 'rb') as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read())

    request = {
        'usuario': 'USERT',
        'numeroExpediente': expediente,
        'documentosTrabajo': {
            'dataArchivo': encoded_string,
            'nombreArchivo': 'archivo_trabajo.pdf',
            'tipoDocumentoTrabajo': 'Otros',
        }
    }
    
    servicio = DocumentosTrabajo(url, url_token, auth)
    try:
        respuesta = servicio.adjuntarDocumentosTrabajo(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'documentosTrabajo','metodo':'adjuntarDocumentosTrabajo','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'documentosTrabajo','metodo':'adjuntarDocumentosTrabajo','codigo':codigo,'error':e,'fecha':dt}


def test_buscarArchivoTrabajo(expediente):
    url = url_servicio+'documentosTrabajo?wsdl'

    request = {
        'usuario': 'USERT',
        'numeroExpediente': expediente,
        'nombre': 'archivo_trabajo.pdf',
        }
    
    servicio = DocumentosTrabajo(url, url_token, auth)
    try:
        respuesta = servicio.buscarArchivoTrabajo(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'documentosTrabajo','metodo':'buscarArchivoTrabajo','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'documentosTrabajo','metodo':'buscarArchivoTrabajo','codigo':codigo,'error':e,'fecha':dt}


def test_desadjuntarDocumentosTrabajo(expediente):
    url = url_servicio+'documentosTrabajo?wsdl'

    request = {
        'usuario': 'USERT',
        'numeroExpediente': expediente,
        'documentosTrabajo': 'archivo_trabajo.pdf',
        }
    
    servicio = DocumentosTrabajo(url, url_token, auth)
    try:
        respuesta = servicio.desadjuntarDocumentosTrabajo(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'documentosTrabajo','metodo':'desadjuntarDocumentosTrabajo','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'documentosTrabajo','metodo':'desadjuntarDocumentosTrabajo','codigo':codigo,'error':e,'fecha':dt}


def test_vincularDocumentosOficiales(expediente, documento):
    url = url_servicio+'documentosOficiales?wsdl'
    
    request = {
        'request': {
            'usuario': 'USERT',
            'numeroExpediente': expediente,
            'documentosOficiales': documento,
        }
    
    }
    
    servicio = DocumentosOficiales(url, url_token, auth)
    try:
        respuesta = servicio.vincularDocumentosOficiales(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'documentosOficiales','metodo':'vincularDocumentosOficiales','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'documentosOficiales','metodo':'vincularDocumentosOficiales','codigo':codigo,'error':e,'fecha':dt}


def test_desvincularDocumentosOficiales(expediente, documento):
    url = url_servicio+'documentosOficiales?wsdl'
    
    request = {
        'request': {
            'usuario': 'USERT',
            'numeroExpediente': expediente,
            'documentosOficiales': documento,
        }
    }
    
    servicio = DocumentosOficiales(url, url_token, auth)
    try:
        respuesta = servicio.desvincularDocumentosOficiales(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'documentosOficiales','metodo':'desvincularDocumentosOficiales','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'documentosOficiales','metodo':'desvincularDocumentosOficiales','codigo':codigo,'error':e,'fecha':dt}


def test_vincularDocumentosOficialesConNumeroEspecial(expediente, documento):
    url = url_servicio+'documentosOficiales?wsdl'
    
    request = {
        'request': {
            'usuario': 'USERT',
            'numeroExpediente': expediente,
            'documentosOficiales': {
                'documento': documento,
            }
        }    
    }
    
    servicio = DocumentosOficiales(url, url_token, auth)
    try:
        respuesta = servicio.vincularDocumentosOficialesConNumeroEspecial(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'documentosOficiales','metodo':'vincularDocumentosOficialesConNumeroEspecial','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'documentosOficiales','metodo':'vincularDocumentosOficialesConNumeroEspecial','codigo':codigo,'error':e,'fecha':dt}


def test_desvincularDocumentosOficialesConNumeroEspecial(expediente, documento):
    url = url_servicio+'documentosOficiales?wsdl'
    
    request = {
        'request': {
            'usuario': 'USERT',
            'numeroExpediente': expediente,
            'documentosOficiales': {
                'documento': documento,
            }
        }    
    }
    
    servicio = DocumentosOficiales(url, url_token, auth)
    try:
        respuesta = servicio.desvincularDocumentosOficialesConNumeroEspecial(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'documentosOficiales','metodo':'desvincularDocumentosOficialesConNumeroEspecial','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'documentosOficiales','metodo':'desvincularDocumentosOficialesConNumeroEspecial','codigo':codigo,'error':e,'fecha':dt}


def test_eliminarDocumentosOficialesNoDefinitivos(expediente, documento):
    url = url_servicio+'documentosOficiales?wsdl'
    
    test_vincularDocumentosOficiales(expediente, documento)

    request = {
        'request': {
            'usuario': 'USERT',
            'numeroExpediente': expediente,
        }    
    }
    
    servicio = DocumentosOficiales(url, url_token, auth)
    try:
        respuesta = servicio.eliminarDocumentosOficialesNoDefinitivos(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'documentosOficiales','metodo':'eliminarDocumentosOficialesNoDefinitivos','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'documentosOficiales','metodo':'eliminarDocumentosOficialesNoDefinitivos','codigo':codigo,'error':e,'fecha':dt}


def test_hacerDefinitivosDocumentosOficiales(expediente, documento):
    url = url_servicio+'documentosOficiales?wsdl'

    request = {
        'request': {
            'usuario': 'USERT',
            'numeroExpediente': expediente,
        }    
    }
    
    servicio = DocumentosOficiales(url, url_token, auth)
    try:
        respuesta = servicio.hacerDefinitivosDocumentosOficiales(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'documentosOficiales','metodo':'hacerDefinitivosDocumentosOficiales','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'documentosOficiales','metodo':'hacerDefinitivosDocumentosOficiales','codigo':codigo,'error':e,'fecha':dt}


def test_generarPaseExpedienteSinDocumento(expediente, documento):
    url = url_servicio+'generacionPaseExpediente?wsdl'

    request = {
        'datosPase': {
            'numeroExpediente': expediente,
            'esMesaDestino': False,
            'esReparticionDestino': False,
            'esSectorDestino': False,
            'esUsuarioDestino': True,
            'estadoSeleccionado': 'Tramitación',
            'motivoPase': 'Expediente de prueba. Carece de motivación administrativa.',
            'usuarioDestino': 'USERT',
            'usuarioOrigen': 'USERT',
        },
        'numeroGDEBAPase': documento,
    }
    
    servicio = GeneracionPaseExpediente(url, url_token, auth)
    try:
        respuesta = servicio.generarPaseExpedienteSinDocumento(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'generacionPaseExpediente','metodo':'generarPaseExpedienteSinDocumento','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'generacionPaseExpediente','metodo':'generarPaseExpedienteSinDocumento','codigo':codigo,'error':e,'fecha':dt}


def test_generarPaseExpediente(expediente):
    url = url_servicio+'generacionPaseExpediente?wsdl'

    request = {
        'datosPase': {
            'numeroExpediente': expediente,
            'esMesaDestino': False,
            'esReparticionDestino': False,
            'esSectorDestino': False,
            'esUsuarioDestino': True,
            'estadoSeleccionado': 'Tramitación',
            'motivoPase': 'Expediente de prueba. Carece de motivación administrativa.',
            'usuarioDestino': 'USERT',
            'usuarioOrigen': 'USERT',
        }
    }
    
    servicio = GeneracionPaseExpediente(url, url_token, auth)
    try:
        respuesta = servicio.generarPaseExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'generacionPaseExpediente','metodo':'generarPaseExpediente','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'generacionPaseExpediente','metodo':'generarPaseExpediente','codigo':codigo,'error':e,'fecha':dt}


def test_generarPaseExpedienteConDesbloqueo(expediente):
    url = url_servicio+'generacionPaseExpediente?wsdl'

    request = {
        'datosPase': {
            'numeroExpediente': expediente,
            'esMesaDestino': False,
            'esReparticionDestino': False,
            'esSectorDestino': False,
            'esUsuarioDestino': True,
            'estadoSeleccionado': 'Tramitación',
            'motivoPase': 'Expediente de prueba. Carece de motivación administrativa.',
            'usuarioDestino': 'USERT',
            'usuarioOrigen': 'USERT',
        }
    }
    
    servicio = GeneracionPaseExpediente(url, url_token, auth)
    try:
        respuesta = servicio.generarPaseExpedienteConDesbloqueo(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'generacionPaseExpediente','metodo':'generarPaseExpedienteConDesbloqueo','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'generacionPaseExpediente','metodo':'generarPaseExpedienteConDesbloqueo','codigo':codigo,'error':e,'fecha':dt}


def test_generarPaseExpedienteConBloqueo(expediente):
    url = url_servicio+'generacionPaseExpediente?wsdl'

    request = {
        'datosPase': {
            'numeroExpediente': expediente,
            'esMesaDestino': False,
            'esReparticionDestino': False,
            'esSectorDestino': False,
            'esUsuarioDestino': True,
            'estadoSeleccionado': 'Tramitación',
            'motivoPase': 'Expediente de prueba. Carece de motivación administrativa.',
            'usuarioDestino': 'USERT',
            'usuarioOrigen': 'USERT',
        }
    }
    
    servicio = GeneracionPaseExpediente(url, url_token, auth)
    try:
        respuesta = servicio.generarPaseExpedienteConBloqueo(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'generacionPaseExpediente','metodo':'generarPaseExpedienteConBloqueo','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'generacionPaseExpediente','metodo':'generarPaseExpedienteConBloqueo','codigo':codigo,'error':e,'fecha':dt}


def test_asociarExpediente(expediente1, expediente2):
    url = url_servicio+'expedientesAsociados?wsdl'
    
    request = {
        'usuario': 'USERT',
        'numeroExpediente': expediente1,
        'numeroExpedienteAsociado': expediente2,
    }
    
    servicio = ExpedientesAsociados(url, url_token, auth)
    try:
        respuesta = servicio.asociarExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'expedientesAsociados','metodo':'asociarExpediente','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'expedientesAsociados','metodo':'asociarExpediente','codigo':codigo,'error':e,'fecha':dt}


def test_desasociarExpediente(expediente1, expediente2):
    url = url_servicio+'expedientesAsociados?wsdl'
    
    request = {
        'usuario': 'USERT',
        'numeroExpediente': expediente1,
        'numeroExpedienteDesasociado': expediente2,
    }
    
    servicio = ExpedientesAsociados(url, url_token, auth)
    try:
        respuesta = servicio.desasociarExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'expedientesAsociados','metodo':'desasociarExpediente','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'expedientesAsociados','metodo':'desasociarExpediente','codigo':codigo,'error':e,'fecha':dt}


def test_vincularTramitacionConjunta(expediente1, expediente2):
    url = url_servicio+'tramitacionConjunta?wsdl'
    
    request = {
        'usuario': 'USERT',
        'numeroExpedientePadre': expediente1,
        'expedientesHijo': expediente2,
    }
    
    servicio = TramitacionConjunta(url, url_token, auth)
    try:
        respuesta = servicio.vincularTramitacionConjunta(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'tramitacionConjunta','metodo':'vincularTramitacionConjunta','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'tramitacionConjunta','metodo':'vincularTramitacionConjunta','codigo':codigo,'error':e,'fecha':dt}


def test_desvincularTramitacionConjunta(expediente1):
    url = url_servicio+'tramitacionConjunta?wsdl'
    
    request = {
        'usuario': 'USERT',
        'numeroExpedientePadre': expediente1,
    }
    
    servicio = TramitacionConjunta(url, url_token, auth)
    try:
        respuesta = servicio.desvincularTramitacionConjunta(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'tramitacionConjunta','metodo':'desvincularTramitacionConjunta','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'tramitacionConjunta','metodo':'desvincularTramitacionConjunta','codigo':codigo,'error':e,'fecha':dt}


def test_consultarNumero():
    url = url_servicio+'consultarNumero?wsdl'
    
    request = {
        'anio': 2022,
        'numero': 1,
    }
    
    servicio = ConsultarNumero(url, url_token, auth)
    try:
        respuesta = servicio.consultarNumero(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultarNumero','metodo':'consultarNumero','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultarNumero','metodo':'consultarNumero','codigo':codigo,'error':e,'fecha':dt}


def test_datosHistoricos():
    url = url_servicio+'datosHistoricos?wsdl'
    
    request = {
        'request': {
            'numeroRLM': 'RL-2021-32086080-GDEBA-DLMJYDHGP',
            'usuario': 'USERT',
            #'fecha': '',
        }
    }
    
    servicio = DatosHistoricos(url, url_token, auth)
    try:
        respuesta = servicio.datosHistoricos(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'datosHistoricos','metodo':'datosHistoricos','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'datosHistoricos','metodo':'datosHistoricos','codigo':codigo,'error':e,'fecha':dt}


def test_consultarRegistroPorCUIT():
    url = url_servicio+'consultaRegistro?wsdl'
    
    request = {
        'arg0': {
            'codigoTipoRegistro': 'RLSOC0001',
            'cuit': '30900532128',
        }
    }
    
    servicio = ConsultaRegistro(url, url_token, auth)
    try:
        respuesta = servicio.consultarRegistroPorCUIT(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaRegistro','metodo':'consultarRegistroPorCUIT','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaRegistro','metodo':'consultarRegistroPorCUIT','codigo':codigo,'error':e,'fecha':dt}


def test_consultarRegistroPorNumero():
    url = url_servicio+'consultaRegistro?wsdl'
    
    request = {
        'arg0': {
            'anio': 2021,
            'numero': 23213,
        }
    }
    
    servicio = ConsultaRegistro(url, url_token, auth)
    try:
        respuesta = servicio.consultarRegistroPorNumero(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaRegistro','metodo':'consultarRegistroPorNumero','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaRegistro','metodo':'consultarRegistroPorNumero','codigo':codigo,'error':e,'fecha':dt}


def test_listarRegistroPublico():
    url = url_servicio+'consultaRegistro?wsdl'
    
    request = {
        'arg0': {
            'idTipoRegistro': 11316,
        }
    }
    
    servicio = ConsultaRegistro(url, url_token, auth)
    try:
        respuesta = servicio.listarRegistroPublico(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaRegistro','metodo':'listarRegistroPublico','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaRegistro','metodo':'listarRegistroPublico','codigo':codigo,'error':e,'fecha':dt}


def test_listarTodosLosRegistrosPublicos():
    url = url_servicio+'consultaRegistro?wsdl'
    
    request = {}
    
    servicio = ConsultaRegistro(url, url_token, auth)
    try:
        respuesta = servicio.listarTodosLosRegistrosPublicos(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'servicio':'consultaRegistro','metodo':'listarTodosLosRegistrosPublicos','codigo':codigo,'tiempo':tiempo,'fecha':dt}
    except Exception as e:
        return {'servicio':'consultaRegistro','metodo':'listarTodosLosRegistrosPublicos','codigo':codigo,'error':e,'fecha':dt}



def ejecutar_test_hml(res):
    res.append(test_buscarDetallePorNumero('IF-2021-00138435-GDEBA-TESTGDEBA'))
    res.append(test_buscarDocumentoEnExpedientess('IF-2021-00138435-GDEBA-TESTGDEBA'))
    res.append(test_buscarDocumentoPublicablePorNumero('IF-2021-00138435-GDEBA-TESTGDEBA'))
    res.append(test_buscarNumeroGDEBA('procesoGEDO.439390192'))
    res.append(test_buscarPDFPorNumero('IF-2021-00138435-GDEBA-TESTGDEBA'))
    res.append(test_buscarPorNumero('IF-2021-00138435-GDEBA-TESTGDEBA'))
    res.append(test_buscarPorCuitCuil('20367180162'))
    res.append(test_buscarPorUsuario('SPRIVITERA'))
    res.append(test_buscarPorNombre('FFCC_Nota solicitud trata'))
    res.append(test_generarTareaGEDO())
    generar_doc_resp = test_generarDocumento()
    res.append(generar_doc_resp)
    documento = generar_doc_resp['numero']
    res.append(test_generarDocumentoUsuarioExterno())
    res.append(test_consultarCaratulaVariablePorNumeroExpedienteUsuario('EX-2020-00018982- -GDEBA-DDIMJGM'))
    res.append(test_buscarCaratulaPorNumeroExpediente('EX-2020-00018982- -GDEBA-DDIMJGM'))
    res.append(test_consultarIdFCPorNumeroExpediente('EX-2020-00018982- -GDEBA-DDIMJGM'))
    res.append(test_buscarHistorialPasesExpediente('EX-2020-00018982- -GDEBA-DDIMJGM'))
    res.append(test_buscarExpedientesPorSistemaOrigenUsuario('USERT'))
    res.append(test_buscarExpedientePorIdSistemaExterno(0))
    res.append(test_buscarExpediente('EX-2020-00018982- -GDEBA-DDIMJGM'))
    res.append(test_consultarExpedienteDetallado('EX-2020-00018982- -GDEBA-DDIMJGM'))
    res.append(test_buscarCodigoCaratulaPorNumeroExpediente('EX-2022-00190675- -GDEBA-TESTGDEBA'))
    res.append(test_buscarDatosExpedienteVariable('EX-2020-00018982- -GDEBA-DDIMJGM'))
    res.append(test_validarExpediente('EX-2020-00018982- -GDEBA-DDIMJGM'))
    res.append(test_consultarExpedientesPorSistemaOrigenReparticion('TESTGDEBA'))
    res.append(test_buscarDatosExpedientePorCodigosTrata())
    res.append(test_buscarExpedientesPorSistemaOrigenLibreUsuario())
    res.append(test_consultarExpedientesPorSistemaOrigenLibreReparticion())
    res.append(test_consultaEstadoActualExpediente('EX-2020-00018982- -GDEBA-DDIMJGM'))
    res.append(test_consultaEstadosPaseExpedientePosibles('EX-2020-00018982- -GDEBA-DDIMJGM'))
    res.append(test_esEstadoPaseExpedienteValido('EX-2020-00018982- -GDEBA-DDIMJGM'))
    res.append(test_buscarTratasPorCodigo())
    generar_carat_resp = test_generarCaratulaExpediente()
    res.append(generar_carat_resp)
    expediente1 = generar_carat_resp['numero']
    expediente2 = test_generarCaratulaExpediente()['numero']
    res.append(test_bloquearExpediente(expediente1))
    res.append(test_estaExpedienteBloqueado(expediente1))
    res.append(test_desbloquearExpediente(expediente1))
    res.append(test_bloquearExpediente(expediente1))
    res.append(test_bloquearExpediente(expediente2))
    res.append(test_adjuntarDocumentosTrabajo(expediente1))
    res.append(test_buscarArchivoTrabajo(expediente1))
    res.append(test_desadjuntarDocumentosTrabajo(expediente1))    
    res.append(test_vincularDocumentosOficiales(expediente1, documento))
    res.append(test_desvincularDocumentosOficiales(expediente1, documento))
    res.append(test_vincularDocumentosOficialesConNumeroEspecial(expediente1, 'DIFST-2021-1-GDEBA-TESTGDEBA'))
    res.append(test_desvincularDocumentosOficialesConNumeroEspecial(expediente1, 'DIFST-2021-1-GDEBA-TESTGDEBA'))
    res.append(test_eliminarDocumentosOficialesNoDefinitivos(expediente1, documento))
    res.append(test_vincularDocumentosOficiales(expediente1, documento))
    res.append(test_hacerDefinitivosDocumentosOficiales(expediente1, documento))
    res.append(test_generarPaseExpedienteSinDocumento(expediente2, documento))
    res.append(test_generarPaseExpediente(expediente1))
    res.append(test_generarPaseExpediente(expediente2))
    res.append(test_generarPaseExpedienteConBloqueo(expediente1))
    res.append(test_generarPaseExpedienteConDesbloqueo(expediente1))
    res.append(test_asociarExpediente(expediente2, expediente1))
    res.append(test_desasociarExpediente(expediente2, expediente1))
    res.append(test_bloquearExpediente(expediente1))
    res.append(test_vincularTramitacionConjunta(expediente2, expediente1))
    res.append(test_desvincularTramitacionConjunta(expediente2))
    res.append(test_consultarNumero())
    res.append(test_datosHistoricos())
    res.append(test_consultarRegistroPorCUIT())
    res.append(test_consultarRegistroPorNumero())
    res.append(test_listarRegistroPublico())
    res.append(test_listarTodosLosRegistrosPublicos())


@router.get('/test_servicios/test_hml', tags=['test_hml'])
def test_hml():
    resultado = []
    ejecutar_test_hml(resultado)
    return {'test_hml': resultado}