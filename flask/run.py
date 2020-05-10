from ytopod import create_app, socketio

app = create_app()

if __name__ == "__main__":
    app.run()
    socketio.run()