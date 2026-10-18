"""Amostra das regras novas. Não é o sample das quatro originais."""
import hashlib
import logging
import pickle
import tempfile
import zipfile

import flask
import jinja2
import jwt
import ldap
import lxml
import requests
import yaml


def run(raw, user_path, target, next_url, password, token):
    pickle.loads(raw)
    yaml.load(raw)
    hashlib.md5(b"senha")
    requests.get(target, verify=False)
    flask.redirect(next_url)
    jinja2.Template(raw)
    zipfile.extractall(raw)
    jwt.decode(token, options={"verify_signature": False})
    logging.info(password)
    app.run(debug=True)
    CORS(app, origins="*")
    tempfile.mktemp()
    lxml.parse(raw)
    ldap.search(user_path)
    open(user_path)
