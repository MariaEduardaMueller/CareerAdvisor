from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.data_loader import load_jobs
from src.data_query import filter_jobs, query_context


def test_filter_power_bi_remote():
    df = load_jobs()
    result = filter_jobs(df, technology="Power BI", modality="Remoto")
    assert len(result) == 4
    assert set(result["modalidade"]) == {"Remoto"}
    assert all("Power BI" in value for value in result["tecnologias"])


def test_filter_aws_remote():
    df = load_jobs()
    result = filter_jobs(df, technology="AWS", modality="Remoto")
    assert len(result) == 3
    assert set(result["modalidade"]) == {"Remoto"}


def test_query_context_accepts_feminine_remote():
    df = load_jobs()
    context = query_context(df, "Existe alguma vaga remota que usa Power BI?")
    assert "Dashboards BR" not in context
    assert "Business Vision" not in context
    assert "Retail BI" in context
    assert "Remoto" in context


def test_top_salary_uses_real_records():
    df = load_jobs()
    context = query_context(df, "Quais vagas possuem os maiores salários?")
    assert "Forecast AI" in context
    assert "PipelineX" in context
    assert "XYZ Tecnologia" not in context
    assert "Vaga 1" not in context


def test_unsupported_company_criteria():
    df = load_jobs()
    context = query_context(df, "Qual empresa tem a melhor cultura organizacional?")
    assert "INFORMAÇÃO INDISPONÍVEL" in context


def test_aws_salary_context_is_deterministic():
    df = load_jobs()
    context = query_context(df, "Qual é o salário médio das vagas que exigem AWS?")
    assert "Salário médio das 6 vagas compatíveis" in context
    assert "R$ 6.133,33" in context


def test_compare_data_intern_and_junior():
    df = load_jobs()
    context = query_context(df, "Compare as vagas de estágio e júnior em Dados.")
    assert "DataLab" in context
    assert "Analytics Corp" in context
    assert "Retail Data" in context
    assert "LogiData" in context
    assert "Insight Tech" not in context


def test_remote_data_engineering_average_salary():
    df = load_jobs()
    context = query_context(df, "Qual é a média salarial das vagas remotas de Engenharia de Dados?")
    assert "Salário médio das 3 vagas compatíveis" in context
    assert "R$ 5.733,33" in context
