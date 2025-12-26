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

## 🏗️ Architecture

```mermaid
graph LR
    A[Yahoo Finance API] -->|Raw Data| B(Data Ingestion Module)
    B -->|Cleaned DataFrame| C{Financial Processor}
    C -->|Calculates| D[SMA & Trend Indicators]
    C -->|Calculates| E[Volatility & Risk Metrics]
    D & E -->|Processed Data| F[Alert System / Database]
