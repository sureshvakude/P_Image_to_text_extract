import torch

def check_cuda_cudnn():
    cuda_available = torch.cuda.is_available()
    cudnn_available = torch.backends.cudnn.is_available()

    if cuda_available:
        print("CUDA is available.")
        if cudnn_available:
            print("cuDNN is available.")
        else:
            print("cuDNN is not available. Check if cuDNN is properly installed.")
    else:
        print("CUDA is not available. Make sure you have installed CUDA Toolkit.")

if __name__ == "__main__":
    check_cuda_cudnn()