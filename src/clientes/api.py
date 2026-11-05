"""API de cadastro de clientes. Projeto fictício, sem dado real."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
_clientes: dict[str, dict] = {}


class NovoCliente(BaseModel):
    nome: str
    cpf: str


@app.post("/clientes", status_code=201)
def criar_cliente(cliente: NovoCliente) -> dict:
    if cliente.cpf in _clientes:
        raise HTTPException(status_code=409, detail="CPF já cadastrado")
    _clientes[cliente.cpf] = {"nome": cliente.nome, "cpf": cliente.cpf}
    return _clientes[cliente.cpf]


@app.get("/clientes/{cpf}")
def obter_cliente(cpf: str) -> dict:
    if cpf not in _clientes:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return _clientes[cpf]
