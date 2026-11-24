import os

def config():
    cfg={"bootstrap.servers":os.environ["KAFKA_BOOTSTRAP_SERVERS"],
         "security.protocol":"SASL_SSL",
         "sasl.mechanism":os.environ.get("KAFKA_SASL_MECHANISM","SCRAM-SHA-256"),
         "sasl.username":os.environ["KAFKA_USERNAME"],
         "sasl.password":os.environ["KAFKA_PASSWORD"],
         "ssl.endpoint.identification.algorithm":"https"}
    if os.environ.get("KAFKA_SSL_CA_LOCATION"):
        cfg["ssl.ca.location"]=os.environ["KAFKA_SSL_CA_LOCATION"]
    return cfg
