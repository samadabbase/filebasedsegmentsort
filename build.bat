@echo off
setlocal

REM Build Docker Image
docker build -t sortinalgorithm/consumers .

REM Run Docker Container
docker run sortinalgorithm/consumers

endlocal