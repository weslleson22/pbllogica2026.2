# Dados hipotéticos de um estudante

matricula_ativa = True
renda_aprovada = True
frequencia_adequada = True
documentacao_completa = True

# Regra lógica de elegibilidade

elegivel = (
    matricula_ativa
    and renda_aprovada
    and frequencia_adequada
    and documentacao_completa
)

# Avaliação da condição

if elegivel:
    print("Estudante elegível")
else:
    print("Estudante não elegível")