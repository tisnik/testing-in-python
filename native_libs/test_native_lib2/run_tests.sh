#!/bin/bash -ex

export NOVENV=1
function prepare_venv() {
    virtualenv -p python3 venv && source venv/bin/activate && python3 `which pip3` install -r requirements.txt
}

[ "$NOVENV" == "1" ] || prepare_venv || exit 1

PYTHONDONTWRITEBYTECODE=1 LD_LIBRARY_PATH=lib python3 "`which behave`" --tags=-skip -D dump_errors=true @feature_list.txt $@

