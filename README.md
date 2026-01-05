 # 🚀 DonCrypto: Asset Analytics Pipeline

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Finance](https://img.shields.io/badge/Domain-Financial%20Engineering-green?style=for-the-badge&logo=cashapp)
![Status](https://img.shields.io/badge/Status-Under%20Construction-orange?style=for-the-badge)

**DonCrypto** es una infraestructura de MLOps diseñada para cerrar la brecha entre el caos del mercado cripto y la precisión del análisis cuantitativo. A diferencia de herramientas de visualización estándar, este pipeline construye un **Feature Store** de grado institucional para la gestión de riesgo y el trading algorítmico.

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



