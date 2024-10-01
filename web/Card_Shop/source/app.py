from flask import Flask, render_template, request, redirect, make_response, abort
import sqlite3
import os
import secrets
app = Flask(__name__)

# Path to the SQLite database file
DB_PATH = f'card_shop_{secrets.token_hex(4)}.db'
secret_token = secrets.token_hex(10)

# Database connection
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database if it doesn't exist
def init_db():
    if not os.path.exists(DB_PATH):
        #print("Initializing database...")
        conn = get_db_connection()
        with conn:
            conn.executescript(f'''
            -- Create a SQLite database for the card shop
            CREATE TABLE users1234567890No (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                token TEXT NOT NULL,
                is_admin INTEGER DEFAULT 0
            );

            -- Insert sample data
            INSERT INTO users1234567890No (username, token, is_admin) VALUES ('guest', 'guest_token', 0);
            INSERT INTO users1234567890No (username, token, is_admin) VALUES ('admin', '{secret_token}', 1);

            -- Create a table for storing Yu-Gi-Oh cards
            CREATE TABLE cards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                image_url TEXT NOT NULL
            );

            -- Insert Yu-Gi-Oh cards into the cards table
            INSERT INTO cards (name, price, image_url) VALUES
            ('Blue-Eyes White Dragon', 50.00, '/static/images/Blue-Eyes-White-Dragon.jpg'),
            ('Dark Magician', 30.00, '/static/images/dark_magician.jpg'),
            ('Red-Eyes Black Dragon', 45.00, '/static/images/red_eyes_black_dragon.jpg'),
            ('Exodia the Forbidden One', 100.00, '/static/images/Exodia-the-Forbidden-CardF.jpg'),
            ('Slifer the Sky Dragon', 70.00, '/static/images/slifer_the_sky_dragon.jpg'),
            ('Obelisk the Tormentor', 80.00, '/static/images/obelisk.jpg'),
            ('The Winged Dragon of Ra', 90.00, '/static/images/Winged-Dragon-of-Ra.jpg'),
            ('Summoned Skull', 35.00, '/static/images/Summoned-Skull.jpg'),
            ('Kuriboh', 10.00, '/static/images/Kuriboh.jpg');

            -- Insert hidden cards with specific IDs (10 and 200)
            INSERT INTO cards (id, name, price, image_url) VALUES (10, 'Advance Draw', 1000.00, '/static/images/5533.jpg');
            INSERT INTO cards (id, name, price, image_url) VALUES (200, 'Secret Database Card', 9999.99, '/static/images/hidden_card2.webp');
            ''')
        conn.close()



# Block SQLMap requests based on User-Agent
@app.before_request
def block_sqlmap():
    user_agent = request.headers.get('User-Agent')
    if user_agent and 'sqlmap' in user_agent.lower():
        abort(403)

@app.route('/')
def index():
    # Generate a default token for the guest when they visit
    token = request.cookies.get('token')
    if not token:
        # Set a default token for the guest
        token = "guest_token"
        resp = make_response(redirect('/shop'))
        resp.set_cookie('token', token)
        return resp
    return redirect('/shop')

@app.route('/shop')
def shop():
    try:
        token = request.cookies.get('token')
        conn = get_db_connection()

        # Vulnerable to Blind SQLi
        query = "SELECT * FROM users1234567890No WHERE token = '{}'".format(token)
        result = conn.execute(query).fetchone()

        # Retrieve all cards from the database except hidden ones
        cards_query = "SELECT * FROM cards WHERE id NOT IN (10, 200)"
        cards = conn.execute(cards_query).fetchall()

        conn.close()

        # Blind SQLi feedback: Show welcome message based on the query result
        if result:
            welcome_message = f"Welcome, {result['username']}!"
        else:
            welcome_message = ""
    except sqlite3.OperationalError as e:
        abort(500)
        # welcome_message = ""
        # return render_template('shop.html', welcome_message=welcome_message, cards=cards)
    except Exception as e:
        abort(500)

    return render_template('shop.html', welcome_message=welcome_message, cards=cards)

@app.route('/card/<int:card_id>', methods=['GET'])
def card_detail(card_id):
    conn = get_db_connection()
    query = "SELECT * FROM cards WHERE id = ?"
    card = conn.execute(query, (card_id,)).fetchone()
    conn.close()

    if not card:
        return "Card not found", 404

    # Special description for card with ID 200
    description = ""
    if card_id == 200:
        description = '''
            CREATE TABLE users1234567890No (
                id INTEGER PRIMARY KEY AUTOINCREMENT,\n
                username TEXT NOT NULL,\n
                token TEXT NOT NULL,\n
                is_admin INTEGER DEFAULT 0\n
            );\n

            INSERT INTO users1234567890No (username, token, is_admin) VALUES ('guest', 'guest_token', 0);\n
            INSERT INTO users1234567890No (username, token, is_admin) VALUES ('admin', 'REDACTED', 1);'''

    # Pass the description to the template
    return render_template('card_detail.html', card=card, description=description)


@app.route('/admin')
def admin():
    token = request.cookies.get('token')
    conn = get_db_connection()

    # Only allow access to the admin page if the token matches 'admin_token'
    query = "SELECT * FROM users1234567890No WHERE token = ?"
    result = conn.execute(query, (token,)).fetchone()

    conn.close()

    # Only allow access if the token is 'admin_token'
    if result and result['token'] == f'{secret_token}':
        return render_template('admin.html', username=result['username'],Flag=os.environ.get('FLAG',"PlaygroundsCTF{FAKE_FLAG}"))
    else:
        return "Access Denied!", 403

if __name__ == "__main__":
    init_db()  # Initialize the database if it doesn't exist
    app.run(host="0.0.0.0",debug=False, port=1337)
        
