from collections import Counter
import re
import pandas as pd


def _tokens(value):
    return [x.strip() for x in str(value).split(";") if x.strip()]


def _normalize(text):
    text = str(text).lower().strip()
    replacements = {
        "á": "a", "à": "a", "ã": "a", "â": "a",
        "é": "e", "ê": "e",
        "í": "i",
        "ó": "o", "ô": "o", "õ": "o",
        "ú": "u", "ç": "c",
    }
    return "".join(replacements.get(char, char) for char in text)


def technology_frequency(df, area=None):
    data = df if not area else df[df["area"].apply(lambda x: _normalize(area) in _normalize(x))]
    counter = Counter()
    for value in data["tecnologias"]:
        counter.update(_tokens(value))
    total = len(data)
    if total == 0:
        return []
    return [
        {"tecnologia": k, "vagas": v, "percentual": round(v / total * 100, 1)}
        for k, v in counter.most_common()
    ]


def _find_match(question, values):
    """Find a dataset value mentioned in the question, accepting common variants."""
    q = _normalize(question)
    aliases = {
        "Remoto": ["remoto", "remota", "remotos", "remotas"],
        "Híbrido": ["hibrido", "hibrida", "hibridos", "hibridas"],
        "Presencial": ["presencial", "presenciais"],
        "Estágio": ["estagio", "estagio(s)", "estagiario", "estagiaria"],
        "Júnior": ["junior", "juniores", "jr"],
        "Pleno": ["pleno", "plena"],
        "Sênior": ["senior", "seniores", "sr"],
    }
    for value in values:
        candidates = [value] + aliases.get(value, [])
        if any(_normalize(candidate) in q for candidate in candidates):
            return value
    return None


def _find_technology(question, df):
    q = _normalize(question)
    known = sorted({t for x in df["tecnologias"] for t in _tokens(x)}, key=len, reverse=True)
    for tech in known:
        if _normalize(tech) in q:
            return tech
    return None


def _find_area(question, df):
    q = _normalize(question)
    # More specific areas first so "ciencia de dados" is not mistaken for "dados".
    areas = sorted(df["area"].unique(), key=lambda x: len(str(x)), reverse=True)
    for area in areas:
        if _normalize(area) in q:
            return area
    return None


def filter_jobs(df, technology=None, area=None, level=None, modality=None):
    data = df.copy()
    if technology:
        tech_norm = _normalize(technology)
        data = data[data["tecnologias"].apply(
            lambda value: any(_normalize(token) == tech_norm for token in _tokens(value))
        )]
    if area:
        area_norm = _normalize(area)
        data = data[data["area"].apply(lambda value: _normalize(value) == area_norm)]
    if level:
        level_norm = _normalize(level)
        data = data[data["nivel"].apply(lambda value: _normalize(value) == level_norm)]
    if modality:
        modality_norm = _normalize(modality)
        data = data[data["modalidade"].apply(lambda value: _normalize(value) == modality_norm)]
    return data


def average_salary(df, technology=None, area=None, level=None, modality=None):
    data = filter_jobs(df, technology, area, level, modality)
    return None if data.empty else float(data["salario"].mean())


def modality_frequency(df):
    return df["modalidade"].value_counts().to_dict()


def _format_salary(value):
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def _format_job(row):
    return (
        f"- {row['cargo']} | {row['empresa']} | {row['area']} | "
        f"{row['nivel']} | {row['modalidade']} | {_format_salary(row['salario'])} | "
        f"{row['tecnologias']}"
    )


def query_context(df, question):
    """Create deterministic evidence for the LLM from the user's question.

    Python/Pandas performs all filtering, counting, sorting and averages.
    The LLM should only verbalize the resulting context.
    """
    q = _normalize(question)
    parts = []

    area = _find_area(question, df)
    level = _find_match(question, df["nivel"].unique())
    modality = _find_match(question, df["modalidade"].unique())
    tech = _find_technology(question, df)

    # Comparison questions may mention more than one level. Keep the area/technology
    # filters deterministic and include all explicitly mentioned levels.
    comparison_levels = []
    if "compare" in q or "diferenca" in q or "diferencas" in q:
        for candidate in df["nivel"].unique():
            aliases = {
                "Estágio": ["estagio", "estagiario", "estagiaria"],
                "Júnior": ["junior", "juniores", "jr"],
                "Pleno": ["pleno", "plena"],
                "Sênior": ["senior", "seniores", "sr"],
            }.get(candidate, [candidate])
            if any(_normalize(alias) in q for alias in aliases):
                comparison_levels.append(candidate)

    filtered = filter_jobs(df, tech, area, None if comparison_levels else level, modality)
    if comparison_levels:
        filtered = filtered[filtered["nivel"].isin(comparison_levels)]

    asks_technology = any(k in q for k in ["tecnologia", "tecnologias", "skill", "ferramenta"])
    asks_salary = any(k in q for k in ["salario", "salarial", "remuneracao", "ganha", "paga"])
    asks_count = any(k in q for k in ["quantas", "quantidade", "numero de", "existem", "quantas vagas"])
    asks_modality = any(k in q for k in ["modalidade", "remoto", "remota", "hibrido", "hibrida", "presencial"])
    asks_top_salary = any(k in q for k in ["maiores salarios", "maior salario", "salarios mais altos", "melhores salarios"])

    # Explicitly identify unsupported qualitative questions. This prevents the LLM
    # from trying to answer them from unrelated columns.
    unsupported_topics = [
        "cultura organizacional", "cultura da empresa", "plano de carreira",
        "plano de promocao", "taxa de promocao", "promocao dos funcionarios",
        "beneficios", "beneficio", "vale refeicao", "vale alimentacao",
        "ferias", "clima organizacional", "satisfacao dos funcionarios",
    ]
    if any(topic in q for topic in unsupported_topics):
        parts.append("INFORMAÇÃO INDISPONÍVEL: a base não contém dados sobre esse critério.")
        parts.append("Não é permitido inferir ou comparar empresas com base em salário, cargo ou tecnologia.")
        return "\n".join(parts)

    if asks_top_salary:
        top = df.sort_values("salario", ascending=False).head(5)
        parts.append("TOP 5 SALÁRIOS DA BASE (calculado pelo Python; não é ranking de empresas):")
        parts.extend(_format_job(row) for _, row in top.iterrows())
        return "\n".join(parts)

    if asks_technology:
        freq = technology_frequency(df, area)
        scope = f"na área '{area}'" if area else "em toda a base"
        parts.append(f"Frequência de tecnologias {scope} (calculada pelo Python):")
        parts.extend(
            f"- {x['tecnologia']}: {x['vagas']} vagas ({x['percentual']}%)"
            for x in freq[:10]
        )

    if asks_salary:
        if filtered.empty:
            parts.append("Não existem vagas na base para o filtro solicitado.")
        else:
            avg = float(filtered["salario"].mean())
            parts.append(f"Salário médio das {len(filtered)} vagas compatíveis: {_format_salary(avg)}")

    if asks_count:
        parts.append(f"Quantidade de vagas compatíveis: {len(filtered)}")

    if asks_modality and not asks_count:
        if modality:
            parts.append(f"Filtro de modalidade aplicado: {modality}.")
        else:
            parts.append(f"Distribuição por modalidade na base: {modality_frequency(df)}")

    # Show matching records whenever the question contains a concrete filter.
    if tech or area or level or modality or comparison_levels:
        if filtered.empty:
            parts.append("Nenhuma vaga da base corresponde a todos os filtros informados.")
        else:
            parts.append(f"Vagas compatíveis: {len(filtered)}")
            parts.extend(_format_job(row) for _, row in filtered.head(8).iterrows())

    if not parts:
        parts.append(
            f"Dataset: {len(df)} vagas. Áreas: {', '.join(sorted(df['area'].unique()))}. "
            f"Níveis: {', '.join(sorted(df['nivel'].unique()))}."
        )

    return "\n".join(parts)
