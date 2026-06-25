import time

def log_system_metrics(duration_seconds=10, interval=2):
    log_file = "system_observational_logs.txt"
    print(f"=== Starting Observational Logger: Writing to {log_file} ===")
    
    with open(log_file, "w") as f:
        f.write("Timestamp,CPU_Simulated_Usage,Memory_Simulated_Usage\n")
        
        elapsed = 0
        while elapsed < duration_seconds:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            simulated_cpu = 15.4 + (elapsed * 1.2) 
            simulated_mem = 42.1
            
            log_line = f"{timestamp},{simulated_cpu}%,{simulated_mem}%\n"
            f.write(log_line)
            print(f"Observed Frame: {log_line.strip()}")
            
            time.sleep(interval)
            elapsed += interval
            
    print(f"=== Logging complete. Structural data saved successfully. ===")

if __name__ == "__main__":
    log_system_metrics()
