import grpc
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..\generative_code"))
import calculator_pb2
import calculator_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.AddRequest(a=10, b=20))
    print("Result:", response.result)

if __name__ == '__main__':
    run()