#!/usr/bin/env python3
"""
Crypto Asset Analytics Pipeline
🤖 El experto que nunca duerme

Entry point for the cryptocurrency analysis system.
"""

import argparse
import sys
from datetime import datetime

# Add project root to path for imports
sys.path.insert(0, '.')

from config import settings


def print_banner():
    """Display the application banner."""
    banner = f"""
╔══════════════════════════════════════════════════════════════╗
║  {settings.EXPERT_NAME}                                      ║
║  {settings.EXPERT_TAGLINE}                         ║
╠══════════════════════════════════════════════════════════════╣
║  Version: 0.1.0 MVP                                          ║
║  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                              ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Crypto Asset Analytics Pipeline - Trend Guidance System"
    )
    parser.add_argument(
        "--symbol", "-s",
        type=str,
        default="BTC-USD",
        help="Cryptocurrency symbol to analyze (default: BTC-USD)"
    )
    parser.add_argument(
        "--period", "-p",
        type=str,
        default=settings.PERIOD,
        help=f"Historical data period (default: {settings.PERIOD})"
    )
    parser.add_argument(
        "--export", "-e",
        action="store_true",
        help="Export analysis results to CSV"
    )
    parser.add_argument(
        "--all", "-a",
        action="store_true",
        help="Analyze all default symbols"
    )
    return parser.parse_args()


def main():
    """Main entry point."""
    args = parse_args()
    print_banner()
    
    # Get symbols to analyze
    symbols = settings.DEFAULT_SYMBOLS if args.all else [args.symbol]
    
    print(f"📊 Analyzing: {', '.join(symbols)}")
    print(f"📅 Period: {args.period}")
    print("-" * 60)
    
    # TODO: Phase 2 - Data Ingestion
    # TODO: Phase 3 - Financial Processing  
    # TODO: Phase 4 - Trend Analysis
    # TODO: Phase 5 - Alerts & Output
    
    print("\n✅ Phase 1 Complete - Structure Ready!")
    print("🔜 Next: Implement Data Ingestion Module (Phase 2)")


if __name__ == "__main__":
    main()
