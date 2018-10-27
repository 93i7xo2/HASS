@echo off
set BATCH_NAME=create_cluster
start /B networkstatus
wait -t img -vlp click-HAIPMI-UT-04-01.png(TM(ccoeffnormed,0.95)) 60
@if %ERRORLEVEL%==0 (echo Success) else goto fail
mouseoperation click click-HAIPMI-UT-04-01.png(TM(ccoeffnormed,0.95))
@if %ERRORLEVEL%==0 (echo Success) else goto fail
wait -t img -vlp click-HAIPMI-UT-04-02.png(TM(ccoeffnormed,0.95)) 60
@if %ERRORLEVEL%==0 (echo Success) else goto fail
mouseoperation click click-HAIPMI-UT-04-02.png(TM(ccoeffnormed,0.95))
@if %ERRORLEVEL%==0 (echo Success) else goto fail
wait -t img -vlp click-HAIPMI-UT-04-03.png(TM(ccoeffnormed,0.95)) 60
@if %ERRORLEVEL%==0 (echo Success) else goto fail
mouseoperation click click-HAIPMI-UT-04-03.png(TM(ccoeffnormed,0.95))
@if %ERRORLEVEL%==0 (echo Success) else goto fail
send "C:\Users\Shinta\Documents\SEPProject\create_cluster\evt\001.evt.tmp" 
wait -t img -vlp click-HAIPMI-UT-04-04.png(TM(ccoeffnormed,0.95)) 60
@if %ERRORLEVEL%==0 (echo Success) else goto fail
mouseoperation click click-HAIPMI-UT-04-04.png(TM(ccoeffnormed,0.95))
@if %ERRORLEVEL%==0 (echo Success) else goto fail
wait -t img -vlp assert-HAIPMI-UT-04-03.png(TM(ccoeffnormed,0.95)) 180
@if %ERRORLEVEL%==0 (echo Success) else goto fail
assert -t bgimg -vlp assert-HAIPMI-UT-04-03.png(TM(ccoeffnormed,0.95)) -a n:1:t
@if %ERRORLEVEL%==0 (echo Success) else goto fail
wait -t img -vlp clickHome.png(TM(ccoeffnormed,0.95)) 60
@if %ERRORLEVEL%==0 (echo Success) else goto fail
mouseoperation click clickHome.png(TM(ccoeffnormed,0.95))
@if %ERRORLEVEL%==0 (echo Success) else goto fail
wait -t img -vlp home.PNG(TM(ccoeffnormed,0.95)) 60
@if %ERRORLEVEL%==0 (echo Success) else goto fail
:end
@taskkill /f /im networkstatus.exe
echo END_TEST_CASE
goto :eof
:fail
echo Fail
goto end
