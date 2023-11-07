import tekore as tk
def authorize():
 CLIENT_ID = "b4dad3bdf5144e6f8f408ec2f6f278a3"
 CLIENT_SECRET = "a1e9ff23036a4444abcf6067fd63c2ca"
 app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
 return tk.Spotify(app_token)