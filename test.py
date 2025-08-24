from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    crypto_data = fetch_crypto_data()
    market_data = {
        'total_coins': len(crypto_data),
        'market_cap': sum(coin.get('market_cap', 0) for coin in crypto_data),
        'volume': sum(coin.get('total_volume', 0) for coin in crypto_data),
        'sentiment': 'Bearish'  # Replace with dynamic logic if available
    }
    return jsonify({
        'coins': crypto_data,
        'market': market_data
    })

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return [
            {
                'name': coin['name'],
                'price': coin['current_price'],
                'change': coin['price_change_percentage_24h'],
                'market_cap': coin['market_cap'],
                'total_volume': coin['total_volume']
            }
            for coin in response.json()
        ]
    except Exception as e:
        print(f"Error fetching crypto data: {e}")
        return []

@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return empty response to avoid 404 for favicon

if __name__ == "__main__":
    app.run(debug=True)