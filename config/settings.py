"""
Crypto Asset Analytics Pipeline - Configuration
Centralized settings for all modules
"""

# =============================================================================
# SYMBOLS & DATA
# =============================================================================
DEFAULT_SYMBOLS = ["BTC-USD", "ETH-USD"]
PERIOD = "3mo"           # Data history: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, max
INTERVAL = "1d"          # Data interval: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo

# =============================================================================
# TECHNICAL INDICATORS
# =============================================================================
# Moving Averages
SMA_SHORT = 20           # Short-term SMA period
SMA_LONG = 50            # Long-term SMA period
EMA_PERIOD = 12          # EMA period

# RSI (Relative Strength Index)
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70      # Overbought threshold
RSI_OVERSOLD = 30        # Oversold threshold

# Volatility
VOLATILITY_WINDOW = 20   # Rolling window for volatility calculation

# =============================================================================
# SIGNAL THRESHOLDS
# =============================================================================
CONFIDENCE_HIGH = 75     # High confidence threshold (%)
CONFIDENCE_MEDIUM = 50   # Medium confidence threshold (%)

# =============================================================================
# OUTPUT SETTINGS
# =============================================================================
DATA_OUTPUT_DIR = "data"
CSV_FILENAME_FORMAT = "{symbol}_{date}_analysis.csv"
SHOW_EMOJIS = True       # Enable emoji in console output

# =============================================================================
# EXPERT PERSONA
# =============================================================================
EXPERT_NAME = "🤖 Crypto Expert"
EXPERT_TAGLINE = "Never Sleeps - Always Analyzing"
