# Install Instructions

1. Create python virtual environment
2. `pip install -r requirements.txt`
3. Copy secret_settings.py.sample as secret_settings.py in the conf folder
4. Enter a django secret key.
5. Launch Redis using `docker run -p 6379:6379 -d redis:5`
