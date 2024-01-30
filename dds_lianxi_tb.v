`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2022/08/09 22:02:03
// Design Name: 
// Module Name: dds_lianxi_tb
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module dds_lianxi_tb(

    );
	
	reg clk_50mhz;
	
	initial begin 
		clk_50mhz = 1'b0;
	end 
	
	always #10 clk_50mhz = ~clk_50mhz;
	
	dds_lianxi dds_lianxi(

	. clk_50mhz(clk_50mhz)
    );
	
	
	
	
	
	
	
	
	
	
	
endmodule
