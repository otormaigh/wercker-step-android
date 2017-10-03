#!/bin/sh
if [ ! "${ANDROID_DEPLOY_NOTIFY_WEBHOOK_URL}" ]; then
    fail "No webhook url has been set, skipping this step."
fi

pip install -r "$WERCKER_STEP_ROOT/requirements.txt"
python "$WERCKER_STEP_ROOT/run.py"
