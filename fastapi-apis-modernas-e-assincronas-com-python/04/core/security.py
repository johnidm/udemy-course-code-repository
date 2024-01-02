from passlib.context import CryptContext


cripto = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verificar_senha(senha: str, hash_senha: str) -> bool:
    return cripto.verify(senha, hash_senha)    


def gerar_hash_senha(senha: str) -> str:
    return cripto.hash(senha)