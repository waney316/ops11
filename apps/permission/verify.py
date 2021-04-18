import os
from pathlib import Path

import casbin

from .adapter import DjangoAdapter
from .models import CasbinRule

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent


def verify_permission(username, uri, method):
    # username, path, method
    adapter = DjangoAdapter(CasbinRule)
    model_conf_file = os.path.join(BASE_DIR, "config", "keymatch_model.conf")
    e = casbin.Enforcer(model_conf_file, adapter=adapter)
    # e = casbin.Enforcer("path/to/model.conf", "path/to/policy.csv")
    return e.enforce(username, uri, method)  # e.enforce(username, uri, method)