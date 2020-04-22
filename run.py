# handle application running

from app import app

if __name__ == '__main__':
    # app.run(debug = True)//debug=True being handled by the subclass in config.py now
    app.run()