import hvac

client = hvac.Client(url="http://vault-server:8200", token="your-token")
secret = client.secrets.kv.read_secret_version(path="my-secret")

print(secret["data"]["data"])
