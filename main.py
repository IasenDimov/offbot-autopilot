# ============================================================
# PROJECT NAME: OffBot - Auto-Pinterest Engine
# AUTHOR: Ясен
# ARCHIVE TAG: OffBot - Ясен
# DESCRIPTION: 100% Autonomous Affiliate Traffic Generator
# VERSION: 1.0.0 (Full Release)
# ============================================================

import requests
import json
import os
import random
import datetime

class PinterestBot:
    def __init__(self):
        # Тези данни се извличат сигурно от настройките на GitHub, а не се пишат тук
        self.access_token = os.getenv('PINTEREST_TOKEN')
        self.board_id = os.getenv('PINTEREST_BOARD_ID')
        self.affiliate_id = os.getenv('AMAZON_AFFILIATE_ID')
        self.api_url = "https://api.pinterest.com/v5/pins"

    def get_trending_products(self):
        """
        Списък с продукти за автоматизирано публикуване. 
        В бъдеще тук може да се добави API на Amazon за динамично извличане.
        """
        product_database = [
            {
                "title": "Minimalist Smart LED Desk Lamp 2026",
                "description": "Upgrade your workspace with this AI-integrated smart lamp. Perfect for deep work sessions. #smarthome #interiordesign #productivity",
                "image": "https://images.unsplash.com/photo-1534073828943-f801091bb18c",
                "url": f"https://www.amazon.com/dp/B08WLS9BPN?tag={self.affiliate_id}"
            },
            {
                "title": "Portable Ergonomic Laptop Stand",
                "description": "Work from anywhere with comfort. Lightweight, foldable, and durable. A must-have for digital nomads. #digitalnomad #remotework #gadgets",
                "image": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf",
                "url": f"https://www.amazon.com/dp/B086PR9L8K?tag={self.affiliate_id}"
            },
            {
                "title": "Ultrawide Curved Monitor for Professionals",
                "description": "Boost your productivity with a 49-inch immersive display. Ideal for coding and creative work. #setup #tech #gaming",
                "image": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf",
                "url": f"https://www.amazon.com/dp/B07L9GL7T8?tag={self.affiliate_id}"
            }
        ]
        return random.choice(product_database)

    def create_pin(self):
        """Изпраща заявка към Pinterest API за създаване на нов Пин."""
        product = self.get_trending_products()
        
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "title": product["title"],
            "description": product["description"],
            "link": product["url"],
            "board_id": self.board_id,
            "media_source": {
                "source_type": "image_url",
                "url": product["image"]
            }
        }

        print(f"[*] Опит за публикуване на: {product['title']}")
        
        try:
            response = requests.post(self.api_url, headers=headers, data=json.dumps(payload))
            if response.status_code == 201:
                print(f"[✔] Успешно публикувано в Pinterest!")
                return True
            else:
                print(f"[✘] Грешка при публикуване: {response.status_code}")
                print(response.text)
                return False
        except Exception as e:
            print(f"[✘] Критична грешка: {str(e)}")
            return False

if __name__ == "__main__":
    print(f"--- OffBot Autonomous Cycle Started: {datetime.datetime.now()} ---")
    bot = PinterestBot()
    bot.create_pin()
    print(f"--- Cycle Finished ---")
