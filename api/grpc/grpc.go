package grpc

import (
	"context"
	"log"
	"net"

	pb "github.com/hkm15022001/Supply-Chain-Event-Management/pb"
	"google.golang.org/grpc"
)

// Implement your gRPC service here
type grpcServerStruct struct {
	pb.UnimplementedCalculatorServer
}

// mustEmbedUnimplementedCalculatorServer implements pb.CalculatorServer.
func (*grpcServerStruct) mustEmbedUnimplementedCalculatorServer() {

}

func (s *grpcServerStruct) Add(ctx context.Context, req *pb.AddRequest) (*pb.AddResponse, error) {
	result := req.A + req.B
	return &pb.AddResponse{Result: result}, nil
}

// grpc server
func RunServer() {
	log.Println("Starting gRPC server...")

	grpcServer := grpc.NewServer()
	pb.RegisterCalculatorServer(grpcServer, &grpcServerStruct{})

	// Listen on port 50052
	lis, err := net.Listen("tcp", "localhost:50052")
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}

	log.Println("gRPC server is starting...")
	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}

	log.Println("Listening on port 50052")
}
func main() {
	RunServer()
}
