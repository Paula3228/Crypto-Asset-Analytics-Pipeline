# 📈 Crypto Asset Analytics Pipeline

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat&logo=python)
![Finance](https://img.shields.io/badge/Domain-Financial%20Engineering-green?style=flat&logo=cashapp)
![Pipeline](https://img.shields.io/badge/Architecture-ETL%20Pipeline-orange?style=flat)
![Status](https://img.shields.io/badge/Status-Active%20Development-yellow)

**Automated ETL pipeline designed to bridge the gap between Financial Engineering and MLOps.**
This system ingests real-time cryptocurrency market data, calculates advanced technical indicators and risk metrics (Volatility, Log Returns), and monitors market anomalies for algorithmic trading purposes.

---

## 🚀 Key Features

* **Automated Data Ingestion:** Fetches real-time OHLCV (Open, High, Low, Close, Volume) data from reliable financial APIs (Yahoo Finance/Binance).
* **Financial Engineering Core:** Custom implementation of technical indicators:
    * **SMA/EMA:** Trend identification.
    * **Log Returns:** For accurate statistical analysis and volatility modeling.
    * **Volatility (Rolling Std Dev):** Dynamic risk assessment.
* **Scalable Architecture:** Modular design separating extraction, transformation, and logic, ready for cloud deployment (AWS/Render).

---

## 🏗️ Arquitectura del Sistema (Premium Dark Theme)

```mermaid
graph TD
    %% Estilos de la Paleta Dark
    classDef ingestion fill:#161b22,stroke:#238636,stroke-width:2px,color:#fff;
    classDef engine fill:#161b22,stroke:#1f6feb,stroke-width:2px,color:#fff,stroke-dasharray: 5 5;
    classDef output fill:#161b22,stroke:#8957e5,stroke-width:2px,color:#fff;
    classDef box fill:#0d1117,stroke:#30363d,color:#8b949e,font-weight:bold;

    subgraph INGESTION ["📥 CAPA DE INGESTIÓN"]
        A1[Yahoo Finance API]:::ingestion --> B[Data Ingestion Module]:::ingestion
        A2[Binance WebSocket]:::ingestion -.-> B
    end

    subgraph QUANT ["⚙️ NÚCLEO CUANTITATIVO"]
        B --> C{Financial Engine}:::engine
        C --> D[Log Returns & Volatility]:::engine
        C --> E[SMA / EMA / RSI]:::engine
        C --> F[Feature Store / Clean Data]:::engine
    end

    subgraph LOADING ["📤 CAPA DE SALIDA"]
        F --> G[Real-time Dashboard JS]:::output
        F --> H[Anomaly Alert System]:::output
        F --> I[ML Training Ready]:::output
    end

    class INGESTION,QUANT,LOADING box;
