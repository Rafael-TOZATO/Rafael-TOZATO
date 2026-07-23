def validar_requisitos_qa(projeto, cobertura_testes):
    print(f"Iniciando auditoria para o projeto: {projeto}")
    if cobertura_testes >= 80:
        return "Status: Aprovado. Cobertura de testes adequada."
    else:
        return "Status: Pendente. Aumentar a cobertura de testes."

if __name__ == "__main__":
    resultado = validar_requisitos_qa("Governança 4.0", 85)
    print(resultado)
  
