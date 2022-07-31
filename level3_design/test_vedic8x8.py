import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_multiplier(dut):
    """Test for multiplication"""
    for i in range(10):
       A = random.randint(0,255)
       B = random.randint(0,255)
       dut.a.value = A
       dut.b.value = B
       await Timer(2, units='ns')
    
       dut.log.info(f'a={A} b={B} model={A*B} DUT={int(dut.p.value)}')
       assert dut.p.value == A*B, "Randomised test failed with: a={A} and a={B} and product p!={P}"#.format(
       #A=s, B=dut.inp12.value, S=dut.sel.value,M=dut.out.value,E=dut.inp12.value)      

@cocotb.test()
async def test_multiplier1(dut):
    """Test for multiplication"""
    
    A = 0x04
    B = 0x04
    dut.a.value = A
    dut.b.value = B
    await Timer(2, units='ns')
    
    dut.log.info(f'a={A} b={B} model={A*B} DUT={int(dut.m.value)}')
    assert dut.A.m.value == 0  , "Randomised test failed with: a={A} and b={B} and product p!={P}".format(
    A=dut.a.value, B=dut.b.value, P=A*B)      
