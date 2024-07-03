from .hylora import HyLoRa
from .hylora import Prompt



def hylora():
    net = HyLoRa(inp_channels=31,
                 dim=96,
                 window_sizes=[16,32,32] ,        
                 depths=[6,6,6],         
                 num_heads=[6,6,6],
                 split_sizes=[1,2,4],
                 mlp_ratio=2,
                 weight_factor=0.1,
                 memory_blocks=128,
                 down_rank=4)     
    net.use_2dconv = True     
    net.bandwise = False          
    return net

def hyplora_16_rank():
    net = HyLoRa(inp_channels=31,
                 dim = 96,
                 window_sizes=[16,32,32] ,        
                 depths=[6,6,6],         
                 num_heads=[6,6,6],
                 split_sizes=[1,2,4],
                 mlp_ratio=2,
                 weight_factor=0.1,
                 memory_blocks=128,
                 down_rank=16)     
    net.use_2dconv = True     
    net.bandwise = False          
    return net


def hyplora_32_rank():
    net = HyLoRa(inp_channels=31,
                 dim = 96,
                 window_sizes=[16,32,32] ,        
                 depths=[6,6,6],         
                 num_heads=[6,6,6],
                 split_sizes=[1,2,4],
                 mlp_ratio=2,
                 weight_factor=0.1,
                 memory_blocks=128,
                 down_rank=32)     
    net.use_2dconv = True     
    net.bandwise = False          
    return net

def hyplora_210():
    net = HyLoRa(inp_channels=210,
                 dim = 96,
                 window_sizes=[16,32,32] ,        
                 depths=[6,6,6],         
                 num_heads=[6,6,6],
                 split_sizes=[1,2,4],
                 mlp_ratio=2,
                 weight_factor=0.1,
                 memory_blocks=128,
                 down_rank=8)     
    net.use_2dconv = True     
    net.bandwise = False          
    return net
