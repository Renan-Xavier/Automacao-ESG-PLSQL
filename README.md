# Automação de Processos ESG e Eficiência Energética com Oracle PL/SQL

![Oracle](https://img.shields.io/badge/Oracle_Database-PL%2FSQL-F80000?style=for-the-badge&logo=oracle&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![ESG](https://img.shields.io/badge/ESG-Efici%C3%AAncia_Energ%C3%A9tica_%26_IoT-2E7D32?style=for-the-badge)
[![Portfólio](https://img.shields.io/badge/Portfólio-renan--xavier.vercel.app-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://renan-xavier.vercel.app)

**Autor:** Renan Santa Rosa Xavier — RM566997 | 🌐 **Portfólio:** [renan-xavier.vercel.app](https://renan-xavier.vercel.app)  
**Instituição:** FIAP — Análise e Desenvolvimento de Sistemas

---

## 📌 Visão Geral do Projeto

Este projeto implementa uma solução de inteligência analítica em banco de dados **Oracle (PL/SQL)** para monitoramento contínuo de **eficiência energética predial e metas ESG** a partir de medições de sensores IoT.

Em vez de sobrecarregar a camada de aplicação com consultas de agregação repetitivas, as regras de negócio críticas foram delegadas diretamente ao motor do banco de dados por meio da trigger consolidada `TRG_AUTOMACAO_ESG_COMPLETA`. A trigger processa cada leitura inserida, calcula o consumo acumulado, atualiza o status de operação dos equipamentos e emite/encerra alertas de desperdício em tempo real.

---

## 🎬 Demonstração do Sistema

### Diagrama do Modelo Relacional (MER)
Modelagem relacional normalizada com integridade referencial para suportar sensores, leituras e o ciclo de vida dos alertas:

![Modelo Relacional ESG IoT](Relational_1.png)

### Estrutura das Tabelas:
* **`LOCALIDADE`**: Setores monitorados (ex.: Data Centers, andares corporativos, plantas fabris).
* **`EQUIPAMENTO`**: Ativos elétricos cadastrados, seu `STATUS_ATUAL` (`ATIVO` / `INATIVO`) e o `TOTAL_KWH_ACUMULADO`.
* **`SENSOR_IOT`**: Dispositivos de telemetria vinculados com `LIMITE_MAX_KWH` parametrizado.
* **`LEITURA_CONSUMO`**: Tabela transacional que recebe as medições brutas (`VALOR_LIDO_KWH`).
* **`ALERTA_ESG`**: Registro automatizado de anomalias com controle de ciclo (`ABERTO` / `RESOLVIDO`).

---

## 🏛️ Arquitetura da Solução

O fluxo transacional executa 4 rotinas automáticas a cada inserção no banco:

```mermaid
flowchart TD
    subgraph Ingestao ["1. Telemetria IoT"]
        Leitura["Nova Leitura Inserida\n(INSERT em LEITURA_CONSUMO)"]
    end

    subgraph Trigger ["2. Motor PL/SQL (Trigger Consolidada)"]
        TRG["Trigger: TRG_AUTOMACAO_ESG_COMPLETA\nBEFORE/AFTER INSERT FOR EACH ROW"]
        
        subgraph Rotinas ["Rotinas Automatizadas"]
            A1["Rotina 1: Acúmulo de kWh\nAtualiza TOTAL_KWH_ACUMULADO no EQUIPAMENTO"]
            A2["Rotina 2: Atualização de Status\nDefine EQUIPAMENTO como ATIVO (>0) ou INATIVO (=0)"]
            Check{"Consumo > Limite?"}
            A3["Rotina 3: Alerta de Desperdício\nCria registro ABERTO em ALERTA_ESG"]
            A4["Rotina 4: Resolução de Alerta\nFecha alertas antigos como RESOLVIDO"]
        end
    end

    subgraph Relatorios ["3. Camada Analítica & Python"]
        Py["Script gerador_pdf_esg.py\nDocumentação Técnica e Relatório Executivo em PDF"]
    end

    Leitura --> TRG
    TRG --> A1
    TRG --> A2
    TRG --> Check
    Check -- "Sim (Desvio)" --> A3
    Check -- "Não (Normalizado)" --> A4
    A1 & A3 --> Py
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Aplicação no Projeto |
| :--- | :--- |
| **Oracle Database & PL/SQL** | Desenvolvimento de triggers complexas, procedures e queries analíticas de alta performance. |
| **Oracle SQL Developer Data Modeler** | Modelagem Lógica e Física do banco relacional com chaves primárias, estrangeiras e constraints de domínio. |
| **Python 3 & fpdf2** | Script de automação para extração de dados e compilação de relatórios técnicos em formato PDF. |
| **SQL DDL & DML** | Scripts de criação das tabelas, sequências, triggers e massa de testes com validação dos 4 cenários. |

---

## 📑 Arquivos do Repositório

| Arquivo | Descrição |
| :--- | :--- |
| [`script_banco_esg.sql`](script_banco_esg.sql) | Script completo contendo DDL, a Trigger `TRG_AUTOMACAO_ESG_COMPLETA` e massa de testes com validação dos 4 cenários operacionais. |
| [`gerador_pdf_esg.py`](gerador_pdf_esg.py) | Script em Python com a biblioteca `fpdf2` para geração de relatórios técnicos executivos. |
| [`Relational_1.png`](Relational_1.png) | Diagrama do Modelo Relacional exportado do Oracle Data Modeler. |
| [`atividades_automacao_esg.pdf`](atividades_automacao_esg.pdf) | Relatório acadêmico completo com a justificativa técnica das automações. |

---

## 🚀 Como Executar

### 1. No Banco de Dados Oracle
1. Abra o **Oracle SQL Developer** (ou Oracle Live SQL).
2. Conecte-se ao seu schema e execute o arquivo [`script_banco_esg.sql`](script_banco_esg.sql).
3. O final do script já inclui testes de inserção e consultas `SELECT` demonstrando as 4 rotinas em execução.

### 2. Gerador de Relatório em Python
```bash
# Instalar a biblioteca fpdf2
pip install fpdf2

# Executar a compilação do relatório PDF
python gerador_pdf_esg.py
```
