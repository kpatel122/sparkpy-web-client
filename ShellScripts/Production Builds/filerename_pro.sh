#!/bin/bash

DEV_SOURCE=../sparkpy-web-client/index.html
DEV_DESTINATION=../sparkpy-web-client/index-dev.html
PRO_SOURCE=../sparkpy-web-client/index-pro.html
PRO_DESTINATION=../sparkpy-web-client/index.html
if test -f "$DEV_SOURCE"; then
    echo "$PRO_SOURCE exists."
    mv $DEV_SOURCE $DEV_DESTINATION #index.html -> index-dev.html
    mv $PRO_SOURCE $PRO_DESTINATION #index-pro.html -> index.html

fi
