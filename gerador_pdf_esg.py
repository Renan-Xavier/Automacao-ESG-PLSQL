from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(w=190, h=10, text='Atividades de Automacao ESG - Eficiencia Energetica', new_x='LMARGIN', new_y='NEXT', align='C')
pdf.ln(10)

pdf.set_font('Helvetica', 'B', 12)
pdf.cell(w=190, h=10, text='Tema: Eficiencia Energetica e Sustentabilidade', new_x='LMARGIN', new_y='NEXT')
pdf.ln(5)

activities = [
    ('1. Geracao de Alerta de Consumo Excessivo', 'Motivo: Quando um equipamento ultrapassa o limite toleravel de consumo, e essencial emitir um alerta imediato. Essa automacao evita o desperdicio de energia, reduzindo custos e a pegada de carbono sem necessidade de monitoramento humano.'),
    ('2. Atualizacao Automatica de Status do Equipamento', 'Motivo: Saber quais equipamentos estao ligados em tempo real e fundamental. A automacao atualiza o status (Ativo/Inativo) baseando-se nas leituras dos sensores IoT, mantendo um mapa predial fiel a realidade.'),
    ('3. Resolucao Automatica de Alertas', 'Motivo: Para evitar a fadiga de alarmes, se o consumo do equipamento voltar aos limites normais, o sistema fecha o alerta ativo automaticamente. Isso otimiza o tempo da equipe de manutencao.'),
    ('4. Acumulo Consolidado do Consumo de Energia', 'Motivo: Calcular o consumo total no banco em tempo de relatorio exige processamento. Automatizar a soma da energia a cada leitura permite ter o consumo consolidado instantaneo para dashboards e relatorios ESG.')
]

for title, desc in activities:
    pdf.set_font('Helvetica', 'B', 11)
    pdf.multi_cell(w=190, h=8, text=title)
    pdf.set_font('Helvetica', '', 11)
    pdf.multi_cell(w=190, h=6, text=desc)
    pdf.ln(5)

pdf.output('c:/Users/rsrx1/OneDrive/Desktop/ADS FIAP/NP/atividades_automacao_esg.pdf')
print('PDF gerado com sucesso!')
