from fastapi.testclient import TestClient

from src.clientes.api import _clientes, app

cliente = TestClient(app)


def setup_function():
    _clientes.clear()


def test_cria_e_consulta_cliente():
    resposta = cliente.post("/clientes", json={"nome": "Ana", "cpf": "52998224725"})
    assert resposta.status_code == 201
    assert cliente.get("/clientes/52998224725").json()["nome"] == "Ana"


def test_cpf_duplicado_retorna_409():
    corpo = {"nome": "Ana", "cpf": "52998224725"}
    cliente.post("/clientes", json=corpo)
    assert cliente.post("/clientes", json=corpo).status_code == 409


def test_cliente_inexistente_retorna_404():
    assert cliente.get("/clientes/00000000000").status_code == 404
