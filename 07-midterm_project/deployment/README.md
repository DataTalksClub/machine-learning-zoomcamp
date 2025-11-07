## Without Docker 
To run the model
`uv run prediction.py`

To run new prediction
`uv run input.py`

To free port
`lsof -i :Port`
`kill -9 PID`

## With Docker
1. Build
`docker build -t bacteria-predictor .`
2. Run
`docker run --rm -p 9696:9696 bacteria-predictor`
`python input.py`

