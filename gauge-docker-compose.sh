#!/bin/bash



available_envi=("staging")

if [[ "${available_envi[*]}" =~ "${GAUGE_ENVI}" ]]; then
    if [[ $GAUGE_TABLE_ROW == '' ]]; then
        gauge run --env "${GAUGE_ENVI}" --verbose $GAUGE_SPEC
    else
        gauge run --env "${GAUGE_ENVI}" --verbose $GAUGE_SPEC --table-rows "${GAUGE_TABLE_ROW}"
    fi
else
    echo $GAUGE_ENVI environment is not available.
fi
