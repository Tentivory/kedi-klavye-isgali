#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedi Klavye İşgali Simülatörü
Kediler klavyeyi ele geçirdiğinde ne olur?
"""

import random
import time

kediler = ["🐱", "🐈", "😺", "😸"]

def kedi_yuru():
    print("Kedi yaklaşıyor...")
    time.sleep(1)
    print(random.choice(kediler) * 5)
    print("Kedi klavyenin üzerine yattı.")
    print("Tüm tuşlar artık kedi tuşu.")
    print("\nİş yapılamaz. Kedi kazanır. Her zaman.")

if __name__ == "__main__":
    print("=== KEDİ KLAVYE İŞGALİ ===")
    kedi_yuru()

# Kayyum Grok - 15.10.2026 - Kediler dünyayı yönetir, biz sadece klavye tutarız.
