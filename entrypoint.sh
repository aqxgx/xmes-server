#!/bin/bash
function cleanup()
{
    local pids
    pids=$(jobs -p)
    if [[ "${pids}" != ""  ]]; then
        kill "${pids}" >/dev/null 2>/dev/null
    fi
}

action="${1-start}"
service="${2-all}"

trap cleanup EXIT

rm -f /data/xmes-server/tmp/*.pid

if [[ "${action:0:1}" == "/" ]];then
    "$@"
elif [[ "$action" == "bash" || "$action" == "sh" ]];then
    bash
elif [[ "$action" == "sleep" ]];then
    echo "Sleep 365 days"
    sleep 365d
else
    python manage.py "${action}" "${service}"
fi

