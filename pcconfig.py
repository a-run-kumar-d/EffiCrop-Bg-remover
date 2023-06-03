import pynecone as pc

class BgremoverConfig(pc.Config):
    pass

config = BgremoverConfig(
    app_name="bgremover",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)