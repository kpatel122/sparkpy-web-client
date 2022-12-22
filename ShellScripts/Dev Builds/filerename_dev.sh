#!/bin/bash

DEV_SOURCE=../sparkpy-web-client/index-dev.html
DEV_DESTINATION=../sparkpy-web-client/index.html
PRO_SOURCE=../sparkpy-web-client/index.html
PRO_DESTINATION=../sparkpy-web-client/index-pro.html
if test -f "$DEV_SOURCE"; then
    echo "$DEV_SOURCE exists."
    mv $PRO_SOURCE $PRO_DESTINATION #index.html -> #index-pro.html
    mv $DEV_SOURCE $DEV_DESTINATION #index-dev.html -> #index.html
fi




