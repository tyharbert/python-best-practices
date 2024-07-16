from typing import List, Dict, Any
import psutil

def get_process_data() -> List[Dict[str, Any]]:
    """
    Retrieve a list of dictionaries containing process information.
    """
    process_data = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        try:
            process_info = proc.info
            process_data.append(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process_data