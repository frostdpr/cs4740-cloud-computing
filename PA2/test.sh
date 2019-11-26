#!/bin/bash
tmpoutput=`echo -e 5 6 | go run add.go`
CORRECT=0
f1=`echo $tmpoutput | grep -q '11'`
if [ $? = 0 ]; then
    let CORRECT=CORRECT+1
fi
tmpoutput=`echo -e 15  8 | go run add.go`
f1=`echo $tmpoutput | grep -q '23'`
if [ $? = 0 ]; then
    let CORRECT=CORRECT+1
fi
exit $CORRECT
