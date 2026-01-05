# -*- coding: utf-8 -*-
"""
Crypto Data Fetcher Module
Handles fetching OHLCV data from Yahoo Finance API

Part of the "Expert that Never Sleeps" system
"""

import sys
import io

# Fix Windows console encoding for emojis
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import yfinance as yf
import pandas as pd
from datetime import datetime
from typing import Optional

import sys
sys.path.insert(0, '.')
from config import settings


class CryptoDataFetcher:
    """
    Fetches and validates cryptocurrency market data.
    
    Usage:
        fetcher = CryptoDataFetcher("BTC-USD")
        df = fetcher.fetch_ohlcv("3mo")
        price = fetcher.get_latest_price()
    """
    
    def __init__(self, symbol: str):
        """
        Initialize the data fetcher.
        
        Args:
            symbol: Cryptocurrency symbol (e.g., "BTC-USD", "ETH-USD")
        """
        self.symbol = symbol.upper()
        self.ticker = yf.Ticker(self.symbol)
        self._data: Optional[pd.DataFrame] = None
        
    def fetch_ohlcv(self, period: str = None, interval: str = None) -> pd.DataFrame:
        """
        Fetch OHLCV (Open, High, Low, Close, Volume) data.
        
        Args:
            period: Data period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, max)
            interval: Data interval (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo)
            
        Returns:
            DataFrame with OHLCV columns and datetime index
        """
        period = period or settings.PERIOD
        interval = interval or settings.INTERVAL
        
        print(f"📥 Fetching {self.symbol} data (period: {period}, interval: {interval})...")
        
        try:
            df = self.ticker.history(period=period, interval=interval)
            
            if df.empty:
                raise ValueError(f"No data returned for {self.symbol}")
            
            # Validate and clean data
            df = self._validate_data(df)
            self._data = df
            
            print(f"✅ Retrieved {len(df)} records for {self.symbol}")
            return df
            
        except Exception as e:
            print(f"❌ Error fetching data for {self.symbol}: {e}")
            raise
    
    def _validate_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Validate and clean the fetched data.
        
        Args:
            df: Raw DataFrame from yfinance
            
        Returns:
            Cleaned DataFrame
        """
        # Required columns for OHLCV
        required_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
        
        # Check for required columns
        missing = [col for col in required_cols if col not in df.columns]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")
        
        # Keep only OHLCV columns
        df = df[required_cols].copy()
        
        # Remove rows with NaN values
        initial_len = len(df)
        df = df.dropna()
        
        if len(df) < initial_len:
            removed = initial_len - len(df)
            print(f"⚠️  Removed {removed} rows with missing values")
        
        # Ensure numeric types
        for col in required_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        return df
    
    def get_latest_price(self) -> float:
        """
        Get the most recent closing price.
        
        Returns:
            Latest close price as float
        """
        if self._data is None:
            self.fetch_ohlcv()
        
        return float(self._data['Close'].iloc[-1])
    
    def get_price_change(self) -> dict:
        """
        Calculate price change statistics.
        
        Returns:
            Dict with change amount and percentage
        """
        if self._data is None:
            self.fetch_ohlcv()
        
        current = self._data['Close'].iloc[-1]
        previous = self._data['Close'].iloc[-2]
        
        change = current - previous
        change_pct = (change / previous) * 100
        
        return {
            "current_price": round(current, 2),
            "previous_price": round(previous, 2),
            "change": round(change, 2),
            "change_percent": round(change_pct, 2),
            "direction": "📈" if change >= 0 else "📉"
        }
    
    def get_data_summary(self) -> dict:
        """
        Get a summary of the fetched data.
        
        Returns:
            Dict with data statistics
        """
        if self._data is None:
            self.fetch_ohlcv()
        
        df = self._data
        
        return {
            "symbol": self.symbol,
            "records": len(df),
            "start_date": df.index[0].strftime('%Y-%m-%d'),
            "end_date": df.index[-1].strftime('%Y-%m-%d'),
            "latest_close": round(df['Close'].iloc[-1], 2),
            "highest_high": round(df['High'].max(), 2),
            "lowest_low": round(df['Low'].min(), 2),
            "avg_volume": round(df['Volume'].mean(), 0)
        }


# Quick test when run directly
if __name__ == "__main__":
    print("=" * 60)
    print("🧪 Testing CryptoDataFetcher")
    print("=" * 60)
    
    # Test with Bitcoin
    fetcher = CryptoDataFetcher("BTC-USD")
    df = fetcher.fetch_ohlcv("1mo")
    
    print("\n📊 Data Summary:")
    summary = fetcher.get_data_summary()
    for key, value in summary.items():
        print(f"   {key}: {value}")
    
    print("\n💰 Price Change:")
    change = fetcher.get_price_change()
    for key, value in change.items():
        print(f"   {key}: {value}")
    
    print("\n✅ Test complete!")
