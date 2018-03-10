'''Front end micro service to the crwaler app.
'''
from app import app_obj

if __name__ == '__main__':
    app_obj.run(debug=True, host='0.0.0.0')
