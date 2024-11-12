
from flask import Flask, request, jsonify
from .tasks import send_notification_task

app = Flask(__name__)

@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    user_id = data.get('user_id')
    message = data.get('message')
    
    if not user_id or not message:
        return jsonify({'error': 'User ID and message are not requested'}), 400
    
    send_notification_task.apply_async(args=[user_id, message])
    return jsonify({'message': 'Notification is being sent'}), 202

@app.route('/get_notification/<int:user_id>', methods=['GET'])
def get_notification(user_id):
    notification = [
        {'user_id': user_id, 'message': 'Your order has been shipped.'},
        {'user_id': user_id, 'message': 'Payment received successfully'},
        ]
    return jsonify(notification)
if __name__ == '__main__':
    app.run(debug=True)