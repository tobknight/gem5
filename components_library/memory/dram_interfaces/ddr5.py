# All rights reserved.
#
# The license below extends only to copyright in the software and shall
# not be construed as granting a license to any other intellectual
# property including but not limited to intellectual property relating
# to a hardware implementation of the functionality of the software
# licensed hereunder.  You may use the software subject to the license
# terms below provided that you ensure that this notice is replicated
# unmodified and in its entirety in all distributions of the software,
# modified or unmodified, in source code or in binary form.
#
# Copyright (c) 2021 Dunzhi Zhou, Projjal Gupta & Raina Waryani
# Copyright (c) 2021 University of Florida
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Interfaces for DDR5 memories

These memory "interfaces" contain the timing,energy,etc parameters for each
memory type and are usually based on datasheets for the memory devices.

You can use these interfaces in the MemCtrl object as the `dram` timing
interface.
"""

from m5.objects import DRAMInterface

class DDR5_4800_16x4(DRAMInterface):
    """
    A single DDR5-4800 x64 (x32 times 2) channel (1 command and address bus),
    with timings based on a DDR5-4800 16 Gbit datasheet (Micron MT60B1G16)
    in an 16x8 configuration. # PLEASE UPDATE
    Total channel capacity is 32GiB
    16 devices/rank * 2 ranks/channel * 1GiB/device = 32GiB/channel
    """

    # size of device
    device_size = "1GiB" #updated ( Based on Mouser site
    # listing of above ram stick)

    # 16x8 configuration, 16 devices each with a 8 bit interface
    # (mouser website)
    device_bus_width = 8 #updated

    # DDR5 is a BL16 device
    burst_length = 16 #updated

    # Each device has a page (row buffer) size of 1 kilobyte (2K columns x4)
    device_rowbuffer_size = "1KiB" #updated

    # 16x4 configuration, so 16 devices
    devices_per_rank = 16

    # Dual rank device
    ranks_per_channel = 2 #updated

    # DDR5 has 4 (x16) or 8 (x4 and x8) bank groups
    # Set to 8 for x4 case
    # 8 Groups of 4 banks = 32 banks
    bank_groups_per_rank = 8 #updated

    # DDR5 has 32 banks(x4,x8) and 16 banks(x16) (4 or 8 bank groups in all
    # configurations). Currently we do not capture the additional
    # constraints incurred by the bank groups
    banks_per_rank = 32 #updated

    # override the default buffer sizes and go for something larger to
    # accommodate the larger bank count
    write_buffer_size = 128
    read_buffer_size = 64 # 2 32bit busses per channel

    # 40 CL, 4800MHz
    tCK = "0.416ns" #updated

    # tBURST is equivalent to the CAS-to-CAS delay (tCCD)
    # With bank group architectures, tBURST represents the CAS-to-CAS
    # delay for bursts to different bank groups (tCCD_S) max(8nCK,3.333ns)
    tBURST = "3.333ns" #updated

    # @2400 data rate, tCCD_L is 6 CK
    # CAS-to-CAS delay for bursts to the same bank group
    # tBURST is equivalent to tCCD_S; no explicit parameter required
    # for CAS-to-CAS delay for bursts to different bank groups max(8nCK,5ns)
    tCCD_L = "5ns" #updated

    # DDR5-4800 40-39-39 ( Speed Grade -48B )
    tRCD = "16ns" #updated
    tCL = "16.6ns" #updated
    tRP = "16ns" #updated
    tRAS = "32ns" #updated

    # RRD_S (different bank group) for 512B page is 8CK
    tRRD = "3.328ns" #updated

    # RRD_L (same bank group) for 1B page is MAX(8 CK, 5ns)
    tRRD_L = "5ns" #updated

    # tFAW for 1kB page is max(32nCK,13.333ns))
    tXAW = "13.333ns" #updated
    activation_limit = 4 #updated
    # tRFC is 295ns in document
    tRFC = "295ns" #updated

    tWR = "30ns" #updated

    # Here using the average of WTR_S and WTR_L (4 ck from diagram,
    # need to update)
    tWTR = "6.25ns" #updated

    # max(12nCK, 7.5ns)
    tRTP = "7.5ns" #updated

    # Default same rank rd-to-wr bus turnaround to
    # 2 CK + tDQS may add (0.5) = 2.5 nCk,
    # @2400 MHz = 1 ns
    tRTW = "1ns" #updated

    # Default different rank bus delay to 2 CK, @2400 MHz = 0.832 ns
    tCS = "0.832ns" #updated

    # <=85C, half for >85C
    tREFI = "3.9us" #updated

    # active powerdown and precharge powerdown exit time max(7.5ns, 8nCK)
    tXP = "7.5ns" #updated

    # self refresh exit time
    # same a trfc1
    tXS = "295ns" #updated

    # Current values from datasheet
    IDD0 = "103mA" #updated
    IDD02 = "8mA" #updated
    IDD2N = "92mA" #updated
    IDD3N = "142mA" #updated
    IDD3N2 = "7mA" #updated
    IDD4W = "349mA" #updated
    IDD4R = "377mA" #updated
    IDD5 = "277mA" #updated
    IDD3P1 = "140mA" #updated
    IDD2P1 = "88mA" #updated
    IDD6 = "102mA" #updated
    VDD = "1.1V" #updated ( Supply Voltage )
    VDD2 = "1.8V" #updated( Vpp : Auxiliary supply for wordline boost)
