from flask import Flask, render_template, request, jsonify, abort
import os
import base64

app = Flask(__name__)

# Directory where scrolls are stored
SCROLLS_DIR = os.curdir + "/scrolls"

# List of available scrolls to be shown on the homepage
AVAILABLE_SCROLLS = {"Scroll of ra":"scroll_of_ra.txt","Book of the dead":"book_of_the_dead.txt","Curse of amenhotep":"curse_of_amenhotep.txt","Prophecy of osiris":"prophecy_of_osiris.txt","Ancient map":"ancient_map.txt"}

@app.route('/')
def index():
    # Show a list of available scrolls
    return render_template('index.html', scrolls=AVAILABLE_SCROLLS)

@app.route('/scrolls')
def get_scroll():
    file = request.args.get("file")
    # Construct the path to the scroll file (this is where the LFI occurs)
    scroll_path = os.path.join(SCROLLS_DIR, file)
    # Check if the requested scroll exists
    if os.path.exists(scroll_path):
        with open(scroll_path, 'rb') as f:
            content = f.read()
        # Return the content as JSON for the JavaScript to handle
        return jsonify({'content': base64.b64encode(content).decode()})
    else:
        abort(404, description="This scroll does not exist in the Pharaoh's archive.")

# Custom 404 error page for when the scroll is not found
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=False,port=1337)
