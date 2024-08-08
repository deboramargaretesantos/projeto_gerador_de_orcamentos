#Importando biblioteca FPDF (Free PDF) para gerar arquivos PDF;

from fpdf import FPDF

#Recebendo dados do usuário e guardar as informações digitadas em variáveis;

projeto = input("Digite o nome do projeto: ")
horas_estimadas = input("quantidade de horas estimada para execução do projeto: ")
valor_hora = input("Informe o valor da hora trabalhada: R$  ")
prazo = input("Informe o prazo estimado para conclusão do projeto: ")

#Calculando valor total do projeto e armazenando o resultado em uma variável;

valor_total = int(horas_estimadas) * int(valor_hora)

#Gerando o PDF vazio do orçamento do projeto e armazenando em uma variável;
#Adicionando uma página ao PDF gerado;
#Definindo a fonte que será utilizada;

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

#Incluindo e posicionando o template no PDF;

pdf.image("template.png", x=0, y=0)

#Incluindo texto fixo, resumo, no orçamento;
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

#Salvando o arquico PDF criado.
pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!")
