from clined import create_app
import os

app = create_app()

if __name__ == '__main__':
    if not os.path.exists('clined/uploads'):
        os.makedirs('clined/uploads/audio')
        os.makedirs('clined/uploads/video')
        os.makedirs('clined/uploads/transcripts')
    app.run(debug=True)
