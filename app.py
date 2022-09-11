from flask import Flask, render_template
from rates import dict_final, btc_values, eth_values, bnb_values, eur_values
from rates import atom_values, bch_values, luna_values, link_values, sol_values, usdt_values, keys_dict, dictionary, coin_list
from request_valores import price 
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', price=price,
                        dict_final=dict_final, btc_values=btc_values, eth_values=eth_values, bnb_values=bnb_values,
                        eur_values=eur_values, atom_values=atom_values, bch_values=bch_values, luna_values=luna_values,
                        link_values=link_values, usdt_values=usdt_values, sol_values=sol_values, keys_dict=keys_dict)

@app.route('/api/v1/resources/cripto/all', methods=['GET'])
def api_all():
    return render_template('api_data.html' , dict_final=dict_final, dictionary=dictionary, coin_list=coin_list)


if __name__ == "__main__":
    app.run(debug=True)
