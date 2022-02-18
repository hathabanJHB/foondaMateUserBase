from flask import Flask, json

#user base test data
userBaseData = {
           "01-01-2022":300,
           "02-01-2022":500,
           "03-01-2022":700,
           "04-01-2022":1300,
           "05-01-2022":2000,
           "06-01-2022":3000,
           "15-01-2022":90000
           }

api = Flask(__name__)

@api.route('/test', methods=['GET'])
def get_companies():
  return json.dumps(userBaseData)

if __name__ == '__main__':
    api.run()