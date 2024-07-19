import tkinter as tk
import os
import subprocess
from time import sleep

####################################################################################
#[1] Setting Up application
####################################################################################
#-> Declaring the pairs to be traded
pair_list = ["BTCUSDT"]#, "ETHUSDT"]


#-> Declaring time intervals
time_intervals = ["5m"]
config_ti = ["1m", "5m", "15m", "1h", "4h", "1d"] # Time intervals for creating program files 

#-> Declaring Limit for Historical Data Gathered
limit = 1000

#-> Declaring levels for Orderbook
levels = 10

#-> DECARING INTERVALS OF INTEREST
#SMA Intervals
sma_intervals = [20, 50, 100] + [15, 45, 90]
ema_intervals = sma_intervals
wf_intervals = [3]
rsi_intervals = [6, 12]
wfc_intervals = [100, 90]



#TRADING ENVIRONMENT (flag)
#     [0] LIVE TRADING
#     [1] DEMO TRADING
flag = 1

from sys import path

"""TRADING PAIR LIST"""
#pair_list = ["BTCUSDT", "ETHUSDT"]

path.append("0-Run")
from Setup import start_1, start_2, start_3, start_4, start_5

#[1.1] Creates folders for data storage
####################################################################################
start_1(pair_list)
start_2(pair_list)
start_3(pair_list)
start_4(pair_list)
start_5(pair_list)

#[1.2] Creates python files for data gathering and analysis
####################################################################################
from config_files.Data_Gathering_file_C import create_data_gathering

#Create programs for data Gathering
create_data_gathering(pair_list, config_ti, limit, levels)


####################################################################################
#[2] Data Gathering
####################################################################################
def gathering_data_file_list1(): #COMPLETE
    # Running historical klines programs
    run_historical_klines = []
    for n in range(len(pair_list)):
        for i in range(len(time_intervals)):
            program_name = f"1-DataGathering/Programs/{pair_list[n]}/Historical_Klines/Data_Gathering_Binance_Historical_{pair_list[n]}_interval={time_intervals[i]}.py"
            run_historical_klines.append(program_name)

    gathering_data_programs_list = run_historical_klines
    return gathering_data_programs_list

def gathering_data_file_list2(): #COMPLETE
    # Running live klines programs
    run_live_klines = []
    for n in range(len(pair_list)):
        for i in range(len(time_intervals)):
            program_name = f"1-DataGathering/Programs/{pair_list[n]}/Live_Data/Data_Gathering_Binance_Live_{pair_list[n]}_interval={time_intervals[i]}.py"
            run_live_klines.append(program_name)

    gathering_data_programs_list = run_live_klines
    return gathering_data_programs_list

def gathering_data_file_list3(): #PENDING TESTS
    #Running Orderbook
    run_orderbooks = []
    for n in range(len(pair_list)):
        program_name = f"1-DataGathering/Programs/{pair_list[n]}/Live_Data/Data_Gathering_Binance_{pair_list[n]}_Orderbook.py"
        run_orderbooks.append(program_name)

    gathering_data_programs_list = run_orderbooks
    return gathering_data_programs_list

####################################################################################
#[3] Processing Data into from Market Information
####################################################################################

def data_processing_file_lists():
    # Running ATR programs
    run_atr_programs = []
    for n in range(len(pair_list)):
        for i in range(len(time_intervals)):
            program_name = f"2-DataProcessing/Programs/{pair_list[n]}/Average_True_Range_{pair_list[n]}interval={time_intervals[i]}.py"
            run_atr_programs.append(program_name)

    #Running GARCH programs
    run_GARCH_programs = []
    for n in range(len(pair_list)):
        for i in range(len(time_intervals)):
            program_name = f"2-DataProcessing/Programs/{pair_list[n]}/GARCH_Model_{pair_list[n]}interval={time_intervals[i]}.py"
            run_GARCH_programs.append(program_name)

    #Running Mean Reversion programs
    run_mr_programs = []
    for n in range(len(pair_list)):
        for i in range(len(time_intervals)): 
            program_name = f"2-DataProcessing/Programs/{pair_list[n]}/Mean_Reversion_{pair_list[n]}interval={time_intervals[i]}.py"
            run_mr_programs.append(program_name)
    
    #Running SMA programs
    run_SMA_programs = []
    for n in range(len(pair_list)):
        for i in range(len(time_intervals)): 
            for l in range(len(sma_intervals)):
                program_name = f"2-DataProcessing/Programs/{pair_list[n]}/Simple_Moving_Average_{pair_list[n]}interval={time_intervals[i]}tick={sma_intervals[l]}.py"
                run_SMA_programs.append(program_name)

    #Running EMA programs
    run_EMA_programs = []
    for n in range(len(pair_list)):
        for i in range(len(time_intervals)): 
            for l in range(len(ema_intervals)):
                program_name = f"2-DataProcessing/Programs/{pair_list[n]}/Exponential_Moving_Average_{pair_list[n]}interval={time_intervals[i]}tick={ema_intervals[l]}.py"
                run_EMA_programs.append(program_name)

    #Running WF programs
    run_WF_programs = []
    for n in range(len(pair_list)):
        for i in range(len(time_intervals)): 
            for l in range(len(wf_intervals)):
                program_name = f"2-DataProcessing/Programs/{pair_list[n]}/Williams_Fractals_{pair_list[n]}interval={time_intervals[i]}tick={wf_intervals[l]}.py"
                run_WF_programs.append(program_name)

    #Running RSI programs
    run_RSI_programs = []
    for n in range(len(pair_list)):
        for i in range(len(time_intervals)): 
            for l in range(len(rsi_intervals)):
                program_name = f"2-DataProcessing/Programs/{pair_list[n]}/Relative_Strength_Indicator_{pair_list[n]}interval={time_intervals[i]}tick={rsi_intervals[l]}.py"
                run_RSI_programs.append(program_name) 
    
    #Running WFC programs 
    run_WFC_programs = []
    for n in range(len(pair_list)):
        for i in range(len(time_intervals)): 
            for l in range(len(rsi_intervals)):
                program_name = f"2-DataProcessing/Programs/{pair_list[n]}/Williams_Fractal_Cap_{pair_list[n]}interval={time_intervals[i]}tick={wfc_intervals[l]}.py"
                run_WFC_programs.append(program_name)  


    # Running Delete Empty Files programs
    run_File_Monitoring = []
    sections_monitored = 2
    for i in range(sections_monitored):
        program_name = f"Misc/Programs/FIle_Monitoring/File_Monitoring_{i+1}.py"
        run_File_Monitoring.append(program_name)
    
    """program_list = (run_atr_programs + run_GARCH_programs + run_mr_programs + run_SMA_programs + run_EMA_programs + run_WF_programs 
                    + run_RSI_programs + run_WFC_programs)"""
    
    program_list = (run_SMA_programs + run_EMA_programs + run_WF_programs 
                    + run_RSI_programs + run_WFC_programs + run_File_Monitoring)
    
    return program_list

####################################################################################
#[4] Get Account Balances
####################################################################################

def demo_account_Balance_list(): # Creates Demo account balances for relevant pairs
    #Running Demo_balance programs 
    run_demo_balance_programs = []
    # Splitting the pair
    for i in range(len(pair_list)):
        if "USDT" in pair_list[i]:
            pair1 = pair_list[i].replace("USDT","")
            pair2 = "USDT"
            symbol_list = [pair1, pair2]
            for p in range(len(symbol_list)): 
                program_name = F"3-AccountBalance/Programs/{symbol_list[p]}/Paper_Trading_Account_Create_{symbol_list[p]}.py"
                run_demo_balance_programs.append(program_name)
    return run_demo_balance_programs            

""" Gets live account balances for relevant pairs """
def live_account_Balance_list(): # WIP
    pass


if flag == 1: # Demo
    account_balance_program = demo_account_Balance_list()
elif flag == 0: # Live
    account_balance_program = live_account_Balance_list()
else:
    pass

####################################################################################
#[5] Programs to monitor live trades
####################################################################################

def live_trade_monitoring_file_lists():
    # Running asset precision monitoring programs
    run_asset_precision = []
    for n in range(len(pair_list)): 
        program_name = f"5-Trade_Monitoring/Programs/{pair_list[n]}/asset_precision_{pair_list[n]}.py"
        run_asset_precision.append(program_name)
    
    # Running Hourling Interest rate monitoring programs
    run_HIR = []
    for n in range(len(pair_list)): 
        program_name = f"5-Trade_Monitoring/Programs/{pair_list[n]}/Hourly_Interest_Rate_{pair_list[n]}.py"
        run_HIR.append(program_name)

    program_list = run_asset_precision + run_HIR

    return program_list


####################################################################################
#[6] Programs for Strategies to place orders
####################################################################################
def strategy_file_list():
    # Running asset strategy 2 programs
    run_strategy_2 = []
    for n in range(len(pair_list)): 
        for p in range(len(time_intervals)):
            program_name = f"4-Strategies/Programs/{pair_list[n]}/Strategy_2_{pair_list[n]}interval={time_intervals[p]}.py"
            run_strategy_2.append(program_name)
    

    program_list = run_strategy_2

    return program_list

####################################################################################
# [7] Programs for Orderbook Monitoring
####################################################################################
def orderbook_monitoring_file_lists():
    # Running orderbook monitoring programs
    run_orderbook_monitoring = []
    for n in range(len(pair_list)):
        for i in range(len(time_intervals)):
            program_name = f"5-Trade_Monitoring/Programs/{pair_list[n]}/Orderbook_Monitoring_{pair_list[n]}_Interval={time_intervals[i]}.py"
            run_orderbook_monitoring.append(program_name)



    program_list = run_orderbook_monitoring

    return program_list

####################################################################################
#[8] lists of all programs to be run
####################################################################################

# 1. Account Balance Gathering + {Trade system startup}
account_balance_programs = account_balance_program


# 2. Raw Data Gathering
gathering_data_programs_1 = gathering_data_file_list1() 
gathering_data_programs_2 = gathering_data_file_list2()
gathering_data_programs_3 = gathering_data_file_list3()
raw_data_lists = gathering_data_programs_1 + gathering_data_programs_2 + gathering_data_programs_3
# 3. Processed Data Gathering
processed_data_program = data_processing_file_lists()

# 4. Trade monitoring
trade_monitoring_programs = live_trade_monitoring_file_lists()

# 5. Strategies
strategy_programs = strategy_file_list()

# 6. Orderbook Monitoring
orderbook_monitoring_programs = orderbook_monitoring_file_lists()

gathering_data_programs_list = account_balance_programs + raw_data_lists + processed_data_program + trade_monitoring_programs + strategy_programs + orderbook_monitoring_programs




"""ALL PROGRAMS TO BE RUN"""
programs = gathering_data_programs_list #+ processing_data_programs_list

#UI INTERFACE

# Create a function to run the programs
def run_programs():
    environment = ".venv\Scripts\python.exe" # For virtual environment #"python" - > Defaullt
    for program in programs:
        # Run the program using the subprocess module
        proc = subprocess.Popen([environment, program])
        print(proc)
        # Store the process in a list
        processes.append(proc)
        # Update the list of running files
        running_files.set("\n".join([proc.args[1] for proc in processes]))
        
        sleep(1) #Waits 0.5 second between starting every program
        

# Create a function to terminate the programs
def terminate_programs():
    for proc in processes:
        # Terminate the process
        print(proc)
        proc.terminate()
    # Clear the list of running files
    running_files.set("")

# Create a list to store the running processes
processes = []

# Create the GUI
root = tk.Tk()
root.title("Python Program Runner")

# Create a label to display the running files
running_files = tk.StringVar()
running_files_label = tk.Label(root, textvariable=running_files)
running_files_label.pack()

# Create the "Run Programs" button
run_button = tk.Button(root, text="Run Programs", command=run_programs)
run_button.pack()

# Create the "Terminate Programs" button
terminate_button = tk.Button(root, text="Terminate Programs", command=terminate_programs)
terminate_button.pack()

# Start the GUI event loop
root.mainloop()







