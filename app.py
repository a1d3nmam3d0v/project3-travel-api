from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route("/")
def home_page():
    user_query = request.args 
    city = request.args.get('city')
    results = get_results(city)  # replace with your code
    # let's pretend that results is a dictionary, {'restaurant': 'Pizza', 'videoID': '12345', 'exchangeRate': 123.45}
    # yours is probably more complex
    return render_template("travel.html", {'results': results})


@app.route('/save')
def bookmark(methods=['POST']):  # only respond to POST requests. 
    save_form_data = request.form  # a dictionary so you can say requests.form.get('the key you want')
    bookmark_module.save(save_form_data) # or you'll need to restructure in whatever way this function expects data
    return redirect('/bookmarks')  # or show a success page or go back to the home page or whatever 


@app.route('/bookmarks')
def show_bookmarks():
    all_bookmarks = bookmark_module.get_all()  # show user all bookmarks 
    return render_template('bookmarks.html', {'bookmarks': all_bookmarks})


