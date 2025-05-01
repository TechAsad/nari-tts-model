import torch
import torch.nn as nn

class RMSNorm(nn.Module):
    """Root Mean Square Layer Normalization.
    
    Based on RMSNorm paper: https://arxiv.org/abs/1910.07467
    """
    def __init__(self, dim: int, eps: float = 1e-6, dtype: torch.dtype = torch.float32):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim, dtype=dtype))

    def _norm(self, x: torch.Tensor) -> torch.Tensor:
        return x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        output = self._norm(x.float()).to(x.dtype)
        return output * self.weight
